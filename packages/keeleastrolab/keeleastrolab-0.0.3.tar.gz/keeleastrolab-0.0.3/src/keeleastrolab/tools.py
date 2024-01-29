# -*- coding: utf-8 -*-
"""
tools
=====

 Functions related to analysing data from from a digital camera.

"""

import rawpy
from rawpy import LibRawTooBigError
import exifread
import errno
import os
import csv
import numpy as np

from astropy.wcs import WCS
from astropy.visualization.wcsaxes import WCSAxes
import matplotlib.pyplot as plt
import matplotlib
from astropy.io import fits

__all__ = [ 'read_raw','pixel_size_from_exif','inspect_image']

def read_raw(file, channel='G'):
    """
    Read image data for one colour and EXIF information from a raw file.

    If there two channels corresponding to the selected colour (typically for
    'G') then the two image data values are summed.
    
    Return image data as a numpy array, an EXIF tags dictionary.

    :param file: full path to file containing raw image data.

    :returns: image_data, exif_info

    :Example:

     >>> from keeleastrolab import tools
     >>> green_image, exif_info = tools.read_raw('IMG_0001.CR2')
     >>> blue_image, _ = tools.read_raw('IMG_0001.CR2',channel='B')
    
    """

    try:
        with rawpy.imread(file) as raw:
            raw_image = raw.raw_image_visible
            raw_colors = raw.raw_colors_visible
            color_desc = raw.color_desc.decode()
            if channel not in color_desc:
                msg = f'No such colour {channel} in raw image file {file}'
                raise ValueError(msg)
            new_shape = [s//2 for s in raw_image.shape]
            image_data  = np.zeros(new_shape)
            for i,c in enumerate(color_desc):
                if c == channel:
                    image_data += raw_image[raw_colors == i].reshape(new_shape)
    except LibRawTooBigError:
        raise FileNotFoundError(
                errno.ENOENT, os.strerror(errno.ENOENT), file)

    with open(file,'rb') as fp:
        exif_info = exifread.process_file(fp, details=False)

    return image_data, exif_info



def list_camera_database(return_dict=False):
    """
    Print sensor size and resolution data for all cameras in the database.

    Sensor sizes are width x height in mm.

    Set return_dict=True to return the database as a python dictionary,
    otherwise the results are returned as a string.

    Each value in the returned dictionary if return_dict=True is itself a
    dictionary with the following keys: Make, Model, SensorWidth,
    SensorHeight, ImageWidth, ImageLength

    :param return_dict: return database as a dictionary if True.

    :returns: database as a string or a python dictionary.

    :Example:

     >>> from keeleastrolab import tools
     >>> print(tools.list_camera_to_database())

    """
    package_root = os.path.abspath(os.path.dirname(__file__))
    database_path = os.path.join(package_root, 'camera_database.csv')
    with open (database_path) as csvfile:
        reader = csv.DictReader(csvfile)
        if return_dict:
            r = {}
            for row in reader:
                key = f'{row["Make"]}_{row["Model"]}'.replace(' ','_')
                r[key] = row
            return r
        else:
            t = "Make                Model                "
            t += "Width  Height XResolution YResolution\n"
            for row in reader:
                t += f'{row["Make"]:19.19} {row["Model"]:18.18} '
                t += f'{row["Width"]:>7} {row["Height"]:>7} '
                t += f'{row["XResolution"]:>11} {row["YResolution"]:>11}\n'
            return t

def inspect_image(fitsfile, pmin=90, pmax=99.9, cmap='Greens', 
                  swap_axes = None, figsize=(9,6)):
    class myWCSAxes(WCSAxes):
        def _display_world_coords(self, x, y):
            if not self._drawn:
                return ""
            pixel = np.array([x, y])
            coords = self._all_coords[self._display_coords_index]
            world = coords._transform.transform(np.array([pixel]))[0]
            rastr = f"{world[0]/15:02.0f}h {60*(world[0]/15 % 1):02.0f}m"
            destr = f"{world[1]:+02.0f}° {60*(world[1] % 1):02.0f}'"
            return f"{rastr}, {destr} ({x:6.1f}, {y:6.1f})"
    def format_cursor_data(self,data):
        return f': {data:6.0f}'
    matplotlib.artist.Artist.format_cursor_data=format_cursor_data

    fig = plt.figure(figsize=(9,6))
    data,hdr = fits.getdata(fitsfile,header=True)
    wcs = WCS(hdr)
    if wcs.has_celestial:
        ax = myWCSAxes(fig, [0.1,0.1,0.8,0.8], wcs=wcs)
        img = ax.imshow(data,
            vmin=np.percentile(data,pmin),
            vmax=np.percentile(data,pmax),
            origin='lower',cmap=cmap)
        lon = ax.coords[0]
        lat = ax.coords[1]
        if swap_axes is None:
            pc = wcs.pixel_scale_matrix
            _swap_axes = np.hypot(pc[0,0],pc[1,1]) < np.hypot(pc[1,0],pc[0,1])
        else:
            _swap_axes = swap_axes
        if _swap_axes:
            lon.set_ticks_position('lr')
            lon.set_ticklabel_position('lr')
            lat.set_ticks_position('tb')
            lat.set_ticklabel_position('tb')
            ax.set_xlabel('Dec')
            ax.set_ylabel('RA')
        else:
            lat.set_ticks_position('lr')
            lat.set_ticklabel_position('lr')
            lon.set_ticks_position('tb')
            lon.set_ticklabel_position('tb')
            ax.set_xlabel('RA')
            ax.set_ylabel('Dec')
        ax.grid()
        fig.tight_layout()
        fig.add_axes(ax);  # axes have to be explicitly added to the figure
    else:
        plt.imshow(data,
                vmin=np.percentile(data,pmin),
                vmax=np.percentile(data,pmax),
                origin='lower',cmap=cmap)
        plt.xlabel('Column')
        plt.ylabel('Row')
        fig.tight_layout()
    return fig
