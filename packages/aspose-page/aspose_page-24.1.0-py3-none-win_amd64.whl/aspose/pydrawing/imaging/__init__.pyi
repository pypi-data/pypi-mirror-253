"""This module is not intended to be called explicitly"""
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

from typing import Any

def get_pyinstaller_hook_dirs() -> Any:
  """Function required by PyInstaller. Returns paths to module 
  PyInstaller hooks. Not intended to be called explicitly."""
...


class ImageFormat:
    '''Specifies the file format of the image. Not inheritable.'''

    def __init__(self, guid: uuid.UUID):
        '''Initializes a new instance of the :class:`ImageFormat` class by using the specified  structure.

        :param guid: The  structure that specifies a particular image format.'''
        ...

    @property
    def guid(self) -> uuid.UUID:
        '''Gets a  structure that represents this :class:`ImageFormat` object.

        :returns: A  structure that represents this :class:`ImageFormat` object.'''
        ...

    bmp: aspose.pydrawing.imaging.ImageFormat

    emf: aspose.pydrawing.imaging.ImageFormat

    wmf: aspose.pydrawing.imaging.ImageFormat

    jpeg: aspose.pydrawing.imaging.ImageFormat

    png: aspose.pydrawing.imaging.ImageFormat

    tiff: aspose.pydrawing.imaging.ImageFormat

    ...


class PixelFormat:
    '''Specifies the format of the color data for each pixel in the image.'''

    INDEXED: int
    GDI: int
    ALPHA: int
    P_ALPHA: int
    EXTENDED: int
    CANONICAL: int
    UNDEFINED: int
    DONT_CARE: int
    FORMAT_1BPP_INDEXED: int
    FORMAT_4BPP_INDEXED: int
    FORMAT_8BPP_INDEXED: int
    FORMAT_16BPP_GRAY_SCALE: int
    FORMAT_16BPP_RGB_555: int
    FORMAT_16BPP_RGB_565: int
    FORMAT_16BPP_ARGB_1555: int
    FORMAT_24BPP_RGB: int
    FORMAT_32BPP_RGB: int
    FORMAT_32BPP_ARGB: int
    FORMAT_32BPP_P_ARGB: int
    FORMAT_48BPP_RGB: int
    FORMAT_64BPP_ARGB: int
    FORMAT_64BPP_P_ARGB: int
    MAX: int
