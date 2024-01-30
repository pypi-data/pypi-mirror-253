"""This module is not intended to be called explicitly"""

from aspose.pydrawing import imaging
from aspose.pydrawing import drawing2d

from typing import Any

def get_pyinstaller_hook_dirs() -> Any:
  """Function required by PyInstaller. Returns paths to module 
  PyInstaller hooks. Not intended to be called explicitly."""
...


class Bitmap(aspose.pydrawing.Image):
    '''Encapsulates a GDI+ bitmap, which consists of the pixel data for a graphics image and its attributes. A :class:`Bitmap` is an object used to work with images defined by pixel data.'''

    @overload
    def __init__(self, filename: str):
        '''Initializes a new instance of the :class:`Bitmap` class from the specified file.

        :param filename: The bitmap file name and path.
        :raises System.IO.FileNotFoundException: The specified file is not found.'''
        ...

    @overload
    def __init__(self, filename: str, use_icm: bool):
        '''Initializes a new instance of the :class:`Bitmap` class from the specified file.

        :param filename: The name of the bitmap file.
        :param use_icm: to use color correction for this :class:`Bitmap`; otherwise, .'''
        ...

    @overload
    def __init__(self, width: int, height: int):
        '''Initializes a new instance of the :class:`Bitmap` class with the specified size.

        :param width: The width, in pixels, of the new :class:`Bitmap`.
        :param height: The height, in pixels, of the new :class:`Bitmap`.
        :raises System.Exception: The operation failed.'''
        ...

    @overload
    def __init__(self, width: int, height: int, format: aspose.pydrawing.Imaging.PixelFormat):
        '''Initializes a new instance of the :class:`Bitmap` class with the specified size and format.

        :param width: The width, in pixels, of the new :class:`Bitmap`.
        :param height: The height, in pixels, of the new :class:`Bitmap`.
        :param format: The pixel format for the new :class:`Bitmap`. This must specify a value that begins with ``Format``.
        :raises System.ArgumentException: A :class:`aspose.pydrawing.imaging.PixelFormat` value is specified whose name does not start with Format. For example, specifying :attr:`aspose.pydrawing.imaging.PixelFormat.GDI` will cause an , but :attr:`aspose.pydrawing.imaging.PixelFormat.FORMAT_48BPP_RGB` will not.'''
        ...

    @overload
    def __init__(self, original: aspose.pydrawing.Image):
        '''Initializes a new instance of the :class:`Bitmap` class from the specified existing image.

        :param original: The :class:`Image` from which to create the new :class:`Bitmap`.'''
        ...

    @overload
    def __init__(self, original: aspose.pydrawing.Image, new_size):
        '''Initializes a new instance of the :class:`Bitmap` class from the specified existing image, scaled to the specified size.

        :param original: The :class:`Image` from which to create the new :class:`Bitmap`.
        :param new_size: The  structure that represent the size of the new :class:`Bitmap`.
        :raises System.Exception: The operation failed.'''
        ...

    @overload
    def __init__(self, original: aspose.pydrawing.Image, width: int, height: int):
        '''Initializes a new instance of the :class:`Bitmap` class from the specified existing image, scaled to the specified size.

        :param original: The :class:`Image` from which to create the new :class:`Bitmap`.
        :param width: The width, in pixels, of the new :class:`Bitmap`.
        :param height: The height, in pixels, of the new :class:`Bitmap`.
        :raises System.Exception: The operation failed.'''
        ...

    @overload
    def __init__(self, type, resource: str):
        '''Initializes a new instance of the :class:`Bitmap` class from a specified resource.

        :param type: The class used to extract the resource.
        :param resource: The name of the resource.'''
        ...

    @overload
    def clone(self, rect, format: aspose.pydrawing.Imaging.PixelFormat) -> aspose.pydrawing.Bitmap:
        '''Creates a copy of the section of this :class:`Bitmap` defined with a specified :class:`aspose.pydrawing.imaging.PixelFormat` enumeration.

        :param rect: Defines the portion of this :class:`Bitmap` to copy.
        :param format: Specifies the :class:`aspose.pydrawing.imaging.PixelFormat` enumeration for the destination :class:`Bitmap`.
        :returns: The :class:`Bitmap` that this method creates.

        :raises System.OutOfMemoryException: is outside of the source bitmap bounds.
        :raises System.ArgumentException: The height or width of  is 0.'''
        ...

    @overload
    def clone(self, rect, format: aspose.pydrawing.Imaging.PixelFormat) -> aspose.pydrawing.Bitmap:
        '''Creates a copy of the section of this :class:`Bitmap` defined by  structure and with a specified :class:`aspose.pydrawing.imaging.PixelFormat` enumeration.

        :param rect: Defines the portion of this :class:`Bitmap` to copy. Coordinates are relative to this :class:`Bitmap`.
        :param format: The pixel format for the new :class:`Bitmap`. This must specify a value that begins with ``Format``.
        :returns: The new :class:`Bitmap` that this method creates.

        :raises System.OutOfMemoryException: is outside of the source bitmap bounds.
        :raises System.ArgumentException: The height or width of  is 0.
                                          -or-
                                          A:class:`aspose.pydrawing.imaging.PixelFormat` value is specified whose name does not start with Format. For example, specifying :attr:`aspose.pydrawing.imaging.PixelFormat.GDI` will cause an , but :attr:`aspose.pydrawing.imaging.PixelFormat.FORMAT_48BPP_RGB` will not.'''
        ...

    @overload
    def make_transparent(self) -> None:
        '''Makes the default transparent color transparent for this :class:`Bitmap`.

        :raises System.InvalidOperationException: The image format of the :class:`Bitmap` is an icon format.
        :raises System.Exception: The operation failed.'''
        ...

    @overload
    def make_transparent(self, transparent_color) -> None:
        '''Makes the specified color transparent for this :class:`Bitmap`.

        :param transparent_color: The  structure that represents the color to make transparent.
        :raises System.InvalidOperationException: The image format of the :class:`Bitmap` is an icon format.
        :raises System.Exception: The operation failed.'''
        ...

    def set_resolution(self, x_dpi: float, y_dpi: float) -> None:
        '''Sets the resolution for this :class:`Bitmap`.

        :param x_dpi: The horizontal resolution, in dots per inch, of the :class:`Bitmap`.
        :param y_dpi: The vertical resolution, in dots per inch, of the :class:`Bitmap`.
        :raises System.Exception: The operation failed.'''
        ...

    ...


class Image:
    '''An abstract base class that provides functionality for the :class:`Bitmap` and :class:`aspose.pydrawing.imaging.Metafile` descended classes.'''

    @overload
    @staticmethod
    def from_file(self, filename: str) -> aspose.pydrawing.Image:
        '''Creates an :class:`Image` from the specified file.

        :param filename: A string that contains the name of the file from which to create the :class:`Image`.
        :returns: The :class:`Image` this method creates.

        :raises System.OutOfMemoryException: The file does not have a valid image format.
                                             -or-
                                             GDI+ does not support the pixel format of the file.
        :raises System.IO.FileNotFoundException: The specified file does not exist.
        :raises System.ArgumentException: is a.'''
        ...

    @overload
    def save(self, filename: str) -> None:
        '''Saves this :class:`Image` to the specified file or stream.

        :param filename: A string that contains the name of the file to which to save this :class:`Image`.
        :raises System.ArgumentNullException: is
        :raises System.Runtime.InteropServices.ExternalException: The image was saved with the wrong image format.
                                                                  -or-
                                                                  The image was saved to the same file it was created from.'''
        ...

    @overload
    def save(self, filename: str, format: aspose.pydrawing.Imaging.ImageFormat) -> None:
        '''Saves this :class:`Image` to the specified file in the specified format.

        :param filename: A string that contains the name of the file to which to save this :class:`Image`.
        :param format: The :class:`aspose.pydrawing.imaging.ImageFormat` for this :class:`Image`.
        :raises System.ArgumentNullException: or is
        :raises System.Runtime.InteropServices.ExternalException: The image was saved with the wrong image format.
                                                                  -or-
                                                                  The image was saved to the same file it was created from.'''
        ...

    def rotate_flip(self, rotate_flip_type: aspose.pydrawing.RotateFlipType) -> None:
        '''Rotates, flips, or rotates and flips the :class:`Image`.

        :param rotate_flip_type: A :class:`RotateFlipType` member that specifies the type of rotation and flip to apply to the image.'''
        ...

    def clone(self) -> object:
        '''Creates an exact copy of this :class:`Image`.

        :returns: The :class:`Image` this method creates, cast as an object.'''
        ...

    @property
    def size(self) -> None:
        '''Gets the width and height, in pixels, of this image.

        :returns: A  structure that represents the width and height, in pixels, of this image.'''
        ...

    @property
    def width(self) -> int:
        '''Gets the width, in pixels, of this :class:`Image`.

        :returns: The width, in pixels, of this :class:`Image`.'''
        ...

    @property
    def height(self) -> int:
        '''Gets the height, in pixels, of this :class:`Image`.

        :returns: The height, in pixels, of this :class:`Image`.'''
        ...

    @property
    def horizontal_resolution(self) -> float:
        '''Gets the horizontal resolution, in pixels per inch, of this :class:`Image`.

        :returns: The horizontal resolution, in pixels per inch, of this :class:`Image`.'''
        ...

    @property
    def vertical_resolution(self) -> float:
        '''Gets the vertical resolution, in pixels per inch, of this :class:`Image`.

        :returns: The vertical resolution, in pixels per inch, of this :class:`Image`.'''
        ...

    @property
    def flags(self) -> int:
        '''Gets attribute flags for the pixel data of this :class:`Image`.

        :returns: The integer representing a bitwise combination of :class:`aspose.pydrawing.imaging.ImageFlags` for this :class:`Image`.'''
        ...

    @property
    def raw_format(self) -> aspose.pydrawing.Imaging.ImageFormat:
        '''Gets the file format of this :class:`Image`.

        :returns: The :class:`aspose.pydrawing.imaging.ImageFormat` that represents the file format of this :class:`Image`.'''
        ...

    @property
    def pixel_format(self) -> aspose.pydrawing.Imaging.PixelFormat:
        '''Gets the pixel format for this :class:`Image`.

        :returns: A :class:`aspose.pydrawing.imaging.PixelFormat` that represents the pixel format for this :class:`Image`.'''
        ...
    ...


class KnownColor:
    '''Known system colors (enumeration).'''
    ACTIVE_BORDER: KnownColor
    ACTIVE_CAPTION: KnownColor
    ACTIVE_CAPTION_TEXT: KnownColor
    ALICE_BLUE: KnownColor
    ANTIQUE_WHITE: KnownColor
    APP_WORKSPACE: KnownColor
    AQUA: KnownColor
    AQUAMARINE: KnownColor
    AZURE: KnownColor
    BEIGE: KnownColor
    BISQUE: KnownColor
    BLACK: KnownColor
    BLANCHED_ALMOND: KnownColor
    BLUE: KnownColor
    BLUE_VIOLET: KnownColor
    BROWN: KnownColor
    BURLY_WOOD: KnownColor
    BUTTON_FACE: KnownColor
    BUTTON_HIGHLIGHT: KnownColor
    BUTTON_SHADOW: KnownColor
    CADET_BLUE: KnownColor
    CHARTREUSE: KnownColor
    CHOCOLATE: KnownColor
    CONTROL: KnownColor
    CONTROL_DARK: KnownColor
    CONTROL_DARK_DARK: KnownColor
    CONTROL_LIGHT: KnownColor
    CONTROL_LIGHT_LIGHT: KnownColor
    CONTROL_TEXT: KnownColor
    CORAL: KnownColor
    CORNFLOWER_BLUE: KnownColor
    CORNSILK: KnownColor
    CRIMSON: KnownColor
    CYAN: KnownColor
    DARK_BLUE: KnownColor
    DARK_CYAN: KnownColor
    DARK_GOLDENROD: KnownColor
    DARK_GRAY: KnownColor
    DARK_GREEN: KnownColor
    DARK_KHAKI: KnownColor
    DARK_MAGENTA: KnownColor
    DARK_OLIVE_GREEN: KnownColor
    DARK_ORANGE: KnownColor
    DARK_ORCHID: KnownColor
    DARK_RED: KnownColor
    DARK_SALMON: KnownColor
    DARK_SEA_GREEN: KnownColor
    DARK_SLATE_BLUE: KnownColor
    DARK_SLATE_GRAY: KnownColor
    DARK_TURQUOISE: KnownColor
    DARK_VIOLET: KnownColor
    DEEP_PINK: KnownColor
    DEEP_SKY_BLUE: KnownColor
    DESKTOP: KnownColor
    DIM_GRAY: KnownColor
    DODGER_BLUE: KnownColor
    FIREBRICK: KnownColor
    FLORAL_WHITE: KnownColor
    FOREST_GREEN: KnownColor
    FUCHSIA: KnownColor
    GAINSBORO: KnownColor
    GHOST_WHITE: KnownColor
    GOLD: KnownColor
    GOLDENROD: KnownColor
    GRADIENT_ACTIVE_CAPTION: KnownColor
    GRADIENT_INACTIVE_CAPTION: KnownColor
    GRAY: KnownColor
    GRAY_TEXT: KnownColor
    GREEN: KnownColor
    GREEN_YELLOW: KnownColor
    HIGHLIGHT: KnownColor
    HIGHLIGHT_TEXT: KnownColor
    HONEYDEW: KnownColor
    HOT_PINK: KnownColor
    HOT_TRACK: KnownColor
    INACTIVE_BORDER: KnownColor
    INACTIVE_CAPTION: KnownColor
    INACTIVE_CAPTION_TEXT: KnownColor
    INDIAN_RED: KnownColor
    INDIGO: KnownColor
    INFO: KnownColor
    INFO_TEXT: KnownColor
    IVORY: KnownColor
    KHAKI: KnownColor
    LAVENDER: KnownColor
    LAVENDER_BLUSH: KnownColor
    LAWN_GREEN: KnownColor
    LEMON_CHIFFON: KnownColor
    LIGHT_BLUE: KnownColor
    LIGHT_CORAL: KnownColor
    LIGHT_CYAN: KnownColor
    LIGHT_GOLDENROD_YELLOW: KnownColor
    LIGHT_GRAY: KnownColor
    LIGHT_GREEN: KnownColor
    LIGHT_PINK: KnownColor
    LIGHT_SALMON: KnownColor
    LIGHT_SEA_GREEN: KnownColor
    LIGHT_SKY_BLUE: KnownColor
    LIGHT_SLATE_GRAY: KnownColor
    LIGHT_STEEL_BLUE: KnownColor
    LIGHT_YELLOW: KnownColor
    LIME: KnownColor
    LIME_GREEN: KnownColor
    LINEN: KnownColor
    MAGENTA: KnownColor
    MAROON: KnownColor
    MEDIUM_AQUAMARINE: KnownColor
    MEDIUM_BLUE: KnownColor
    MEDIUM_ORCHID: KnownColor
    MEDIUM_PURPLE: KnownColor
    MEDIUM_SEA_GREEN: KnownColor
    MEDIUM_SLATE_BLUE: KnownColor
    MEDIUM_SPRING_GREEN: KnownColor
    MEDIUM_TURQUOISE: KnownColor
    MEDIUM_VIOLET_RED: KnownColor
    MENU: KnownColor
    MENU_BAR: KnownColor
    MENU_HIGHLIGHT: KnownColor
    MENU_TEXT: KnownColor
    MIDNIGHT_BLUE: KnownColor
    MINT_CREAM: KnownColor
    MISTY_ROSE: KnownColor
    MOCCASIN: KnownColor
    NAVAJO_WHITE: KnownColor
    NAVY: KnownColor
    OLD_LACE: KnownColor
    OLIVE: KnownColor
    OLIVE_DRAB: KnownColor
    ORANGE: KnownColor
    ORANGE_RED: KnownColor
    ORCHID: KnownColor
    PALE_GOLDENROD: KnownColor
    PALE_GREEN: KnownColor
    PALE_TURQUOISE: KnownColor
    PALE_VIOLET_RED: KnownColor
    PAPAYA_WHIP: KnownColor
    PEACH_PUFF: KnownColor
    PERU: KnownColor
    PINK: KnownColor
    PLUM: KnownColor
    POWDER_BLUE: KnownColor
    PURPLE: KnownColor
    REBECCA_PURPLE: KnownColor
    RED: KnownColor
    ROSY_BROWN: KnownColor
    ROYAL_BLUE: KnownColor
    SADDLE_BROWN: KnownColor
    SALMON: KnownColor
    SANDY_BROWN: KnownColor
    SCROLL_BAR: KnownColor
    SEA_GREEN: KnownColor
    SEA_SHELL: KnownColor
    SIENNA: KnownColor
    SILVER: KnownColor
    SKY_BLUE: KnownColor
    SLATE_BLUE: KnownColor
    SLATE_GRAY: KnownColor
    SNOW: KnownColor
    SPRING_GREEN: KnownColor
    STEEL_BLUE: KnownColor
    TAN: KnownColor
    TEAL: KnownColor
    THISTLE: KnownColor
    TOMATO: KnownColor
    TRANSPARENT: KnownColor
    TURQUOISE: KnownColor
    VIOLET: KnownColor
    WHEAT: KnownColor
    WHITE: KnownColor
    WHITE_SMOKE: KnownColor
    WINDOW: KnownColor
    WINDOW_FRAME: KnownColor
    WINDOW_TEXT: KnownColor
    YELLOW: KnownColor
    YELLOW_GREEN: KnownColor


class Color:
    '''Represents an ARGB color.'''
    
    @property
    def a(self) -> int:
        '''Gets the alpha component value.'''
        ...

    @property
    def r(self) -> int:
        '''Gets the red component value.'''
        ...

    @property
    def g(self) -> int:
        '''Gets the green component value.'''
        ...

    @property
    def b(self) -> int:
        '''Gets the blue component value.'''
        ...

    @property
    def name(self) -> str:
        '''Gets the name of this Color.'''
        ...

    @property
    def is_empty(self) -> bool:
        '''Returns True if this is uninitialized color.'''
        ...

    @property
    def is_known_color(self) -> bool:
        '''Returns True if this is a predefined color.'''
        ...

    @property
    def is_named_color(self) -> bool:
        '''Returns True if this is a named color.'''
        ...

    @property
    def is_system_color(self) -> bool:
        '''Returns True if this is a system color.'''
        ...

    empty: Color

    alice_blue: Color
    antique_white: Color
    aqua: Color
    aquamarine: Color
    azure: Color
    beige: Color
    bisque: Color
    black: Color
    blanched_almond: Color
    blue: Color
    blue_violet: Color
    brown: Color
    burly_wood: Color
    cadet_blue: Color
    chartreuse: Color
    chocolate: Color
    coral: Color
    cornflower_blue: Color
    cornsilk: Color
    crimson: Color
    cyan: Color
    dark_blue: Color
    dark_cyan: Color
    dark_goldenrod: Color
    dark_gray: Color
    dark_green: Color
    dark_khaki: Color
    dark_magenta: Color
    dark_olive_green: Color
    dark_orange: Color
    dark_orchid: Color
    dark_red: Color
    dark_salmon: Color
    dark_sea_green: Color
    dark_slate_blue: Color
    dark_slate_gray: Color
    dark_turquoise: Color
    dark_violet: Color
    deep_pink: Color
    deep_sky_blue: Color
    dim_gray: Color
    dodger_blue: Color
    firebrick: Color
    floral_white: Color
    forest_green: Color
    fuchsia: Color
    gainsboro: Color
    ghost_white: Color
    gold: Color
    goldenrod: Color
    gray: Color
    green: Color
    green_yellow: Color
    honeydew: Color
    hot_pink: Color
    indian_red: Color
    indigo: Color
    ivory: Color
    khaki: Color
    lavender: Color
    lavender_blush: Color
    lawn_green: Color
    lemon_chiffon: Color
    light_blue: Color
    light_coral: Color
    light_cyan: Color
    light_goldenrod_yellow: Color
    light_gray: Color
    light_green: Color
    light_pink: Color
    light_salmon: Color
    light_sea_green: Color
    light_sky_blue: Color
    light_slate_gray: Color
    light_steel_blue: Color
    light_yellow: Color
    lime: Color
    lime_green: Color
    linen: Color
    magenta: Color
    maroon: Color
    medium_aquamarine: Color
    medium_blue: Color
    medium_orchid: Color
    medium_purple: Color
    medium_sea_green: Color
    medium_slate_blue: Color
    medium_spring_green: Color
    medium_turquoise: Color
    medium_violet_red: Color
    midnight_blue: Color
    mint_cream: Color
    misty_rose: Color
    moccasin: Color
    navajo_white: Color
    navy: Color
    old_lace: Color
    olive: Color
    olive_drab: Color
    orange: Color
    orange_red: Color
    orchid: Color
    pale_goldenrod: Color
    pale_green: Color
    pale_turquoise: Color
    pale_violet_red: Color
    papaya_whip: Color
    peach_puff: Color
    peru: Color
    pink: Color
    plum: Color
    powderblue: Color
    purple: Color
    rebecca_purple: Color
    red: Color
    rosy_brown: Color
    royal_blue: Color
    saddle_brown: Color
    salmon: Color
    sandy_brown: Color
    sea_green: Color
    sea_shell: Color
    sienna: Color
    silver: Color
    sky_blue: Color
    slate_blue: Color
    slate_gray: Color
    snow: Color
    spring_green: Color
    steel_blue: Color
    tan: Color
    teal: Color
    thistle: Color
    tomato: Color
    transparent: Color
    turquoise: Color
    violet: Color
    wheat: Color
    white: Color
    white_smoke: Color
    yellow: Color
    yellow_green: Color
    
    @overload
    @staticmethod
    def from_argb(value: int) -> Color:
        '''Creates a Color from a 32-bit ARGB value.'''
        ...

    @overload
    @staticmethod
    def from_argb(aplha: int, color: Color) -> Color:
        '''Creates a Color from the specified color with the new alpha value.'''
        ...

    @overload
    @staticmethod
    def from_argb(red: int, green: int, blue: int) -> Color:
        '''Creates a Color from the specified red, green, and blue components.'''
        ...

    @overload
    @staticmethod
    def from_argb(alpha: int, red: int, green: int, blue: int) -> Color:
        '''Creates a Color from the specified alpha, red, green, and blue components.'''
        ...

    @staticmethod
    def from_known_color(color: KnownColor) -> Color:
        '''Creates a Color from the specified predefined color.'''
        ...

    @staticmethod
    def from_name(name: str) -> Color:
        '''Creates a Color with the specified name.'''
        ...

    def get_brightness(self) -> float:
        '''Gets the HSL lightness value.'''
        ...

    def get_hue(self) -> float:
        '''Gets the HSL hue value.'''
        ...

    def get_saturation(self) -> float:
        '''Gets the HSL saturation value.'''
        ...

    def to_argb(self) -> int:
        '''Gets the ARGB value.'''

    def to_known_color(self) -> KnownColor:
        '''Gets the element of the KnownColor enumeration if the Color is created 
        from a predefined color; otherwise, returns 0.'''
        ...

    def to_string(self) -> str:
        '''Converts this Color to a string.'''
        ...


class PointF:
    '''Pair of x and y coordinates.'''

    def __init__(self, x: float, y: float):
        '''Initialize PointF with the specified coordinates.'''
        ...

    empty: PointF

    @property
    def is_empty(self) -> bool:
        '''Returns True if x and y are 0.'''
        ...

    @property
    def x(self) -> float:
        '''Gets x-coordinate.'''
        ...

    @x.setter
    def x(self, value: float):
        '''Sets x-coordinate.'''
        ...

    @property
    def y(self) -> float:
        '''Gets y-coordinate.'''
        ...

    @x.setter
    def y(self, value: float):
        '''Sets y-coordinate.'''
        ...

    @staticmethod
    def add(point: PointF, size: SizeF) -> PointF:
        '''Moves a point by a specified offset.'''
        ...

    @staticmethod
    def subtract(point: PointF, size: SizeF) -> PointF:
        '''Moves a point by the negative of a specified offset.'''
        ...

    def to_string(self) -> str:
        '''Converts this PointF to a string.'''
        ...


class SizeF:
    '''Pair of width and height values.'''

    @overload
    def __init__(self, point: PointF):
        '''Initialize SizeF from the specified PointF.'''
        ...

    @overload
    def __init__(self, width: float, height: float):
        '''Initialize SizeF from the specified width and height values.'''
        ...

    @overload
    def __init__(self, other: SizeF):
        '''Initialize SizeF from the existing SizeF.'''
        ...

    empty: SizeF

    @property
    def is_empty(self) -> bool:
        '''Returns True if width and height are 0.'''
        ...

    @property
    def height(self) -> float:
        '''Gets the height value.'''
        ...

    @height.setter
    def height(self, value: float):
        '''Sets the height value.'''
        ...

    @property
    def width(self) -> float:
        '''Gets the width value.'''
        ...

    @width.setter
    def width(self, value: float):
        '''Sets the width value.'''
        ...

    @staticmethod
    def add(a: SizeF, b: SizeF) -> SizeF:
        '''Adds the width and height of one SizeF to the width and height of another SizeF.'''
        ...

    @staticmethod
    def substract(a: SizeF, b: SizeF) -> SizeF:
        '''Substracts the width and height of one SizeF from the width and height of another SizeF.'''
        ...

    def to_point_f(self) -> PointF:
        '''Converts this SizeF to a PointF.'''
        ...

    def to_string(self) -> str:
        '''Converts this SizeF to a string.'''
        ...


class RectangleF:
    '''Stores location and size of a rectangle.'''

    @overload
    def __init__(self, location: PointF, size: SizeF):
        '''Initialize RectangleF from the specified location and size.'''
        ...

    @overload
    def __init__(self, x: float, y: float, width: float, height: float):
        '''Initialize RectangleF from the specified location and size.'''
        ...

    empty: RectangleF

    @property
    def is_empty(self) -> bool:
        '''Returns True if x, y, width and height are 0.'''
        ...

    @property
    def bottom(self) -> float:
        '''Gets the y-coordinate of the bottom edge.'''
        ...

    @property
    def height(self) -> float:
        '''Gets the height value.'''
        ...

    @height.setter
    def height(self, value: float):
        '''Sets the height value.'''
        ...

    @property
    def left(self) -> float:
        '''Gets the x-coordinate of the left edge.'''
        ...

    @property
    def location(self) -> PointF:
        '''Gets the coordinates of the upper-left corner.'''
        ...

    @location.setter
    def location(self, value: PointF):
        '''Sets the coordinates of the upper-left corner.'''
        ...

    @property
    def right(self) -> float:
        '''Gets the x-coordinate of the right edge.'''
        ...

    @property
    def size(self) -> SizeF:
        '''Gets the size.'''
        ...

    @size.setter
    def size(self, value: SizeF):
        '''Sets the size.'''
        ...

    @property
    def top(self) -> float:
        '''Gets the y-coordinate of the top edge.'''
        ...

    @property
    def width(self) -> float:
        '''Gets the width value.'''
        ...

    @width.setter
    def width(self, value: float):
        '''Sets the width value.'''
        ...

    @property
    def x(self) -> float:
        '''Gets the x-coordinate.'''
        ...

    @x.setter
    def x(self, value: float):
        '''Sets the x-coordinate.'''
        ...

    @property
    def y(self) -> float:
        '''Gets the y-coordinate.'''
        ...

    @y.setter
    def y(self, value: float):
        '''Sets the y-coordinate.'''
        ...

    @overload
    def contains(self, point: PointF) -> bool:
        '''Checks if the specified point is inside this rectangle.'''
        ...

    @overload
    def contains(self, rectangle: RectangleF) -> bool:
        '''Checks if the specified rectangle is entirely contained within this rectangle.'''
        ...

    @overload
    def contains(self, x: float, y: float) -> bool:
        '''Checks if the specified point is inside this rectangle.'''
        ...

    @staticmethod
    def from_ltrb(left: float, top: float, right: float, bottom: float) -> RectangleF:
        '''Creates RectangleF from the specified coordinates.'''
        ...

    @overload
    def inflate(self, x: float, y: float) -> RectangleF:
        '''Enlarges rectangle by the specified size.'''
        ...

    @overload
    def inflate(self, size: SizeF) -> RectangleF:
        '''Enlarges rectangle by the specified size.'''
        ...

    def intersect(self, rect: RectangleF):
        '''Intersects this rectangle with the specified rectangle.'''
        ...

    def intersects_with(self, rect: RectangleF) -> bool:
        '''Checks if this rectangle intersects with the specified rectangle.'''
        ...

    @overload
    def offset(self, pos: PointF):
        '''Moves the position of this rectangle by the specified offset.'''
        ...

    @overload
    def offset(self, x: float, y: float):
        '''Moves the position of this rectangle by the specified offset.'''
        ...

    def to_string(self) -> str:
        '''Converts this RectangleF to a string.'''
        ...

    @staticmethod
    def union(a: RectangleF, b: RectangleF) -> RectangleF:
        '''Creates rectangle than can contains both of the specified rectangles.'''
        ...


class Brushes:
    '''Brushes for all the standard colors. This class cannot be inherited.'''

    transparent: aspose.pydrawing.Brush

    alice_blue: aspose.pydrawing.Brush

    antique_white: aspose.pydrawing.Brush

    aqua: aspose.pydrawing.Brush

    aquamarine: aspose.pydrawing.Brush

    azure: aspose.pydrawing.Brush

    beige: aspose.pydrawing.Brush

    bisque: aspose.pydrawing.Brush

    black: aspose.pydrawing.Brush

    blanched_almond: aspose.pydrawing.Brush

    blue: aspose.pydrawing.Brush

    blue_violet: aspose.pydrawing.Brush

    brown: aspose.pydrawing.Brush

    burly_wood: aspose.pydrawing.Brush

    cadet_blue: aspose.pydrawing.Brush

    chartreuse: aspose.pydrawing.Brush

    chocolate: aspose.pydrawing.Brush

    coral: aspose.pydrawing.Brush

    cornflower_blue: aspose.pydrawing.Brush

    cornsilk: aspose.pydrawing.Brush

    crimson: aspose.pydrawing.Brush

    cyan: aspose.pydrawing.Brush

    dark_blue: aspose.pydrawing.Brush

    dark_cyan: aspose.pydrawing.Brush

    dark_goldenrod: aspose.pydrawing.Brush

    dark_gray: aspose.pydrawing.Brush

    dark_green: aspose.pydrawing.Brush

    dark_khaki: aspose.pydrawing.Brush

    dark_magenta: aspose.pydrawing.Brush

    dark_olive_green: aspose.pydrawing.Brush

    dark_orange: aspose.pydrawing.Brush

    dark_orchid: aspose.pydrawing.Brush

    dark_red: aspose.pydrawing.Brush

    dark_salmon: aspose.pydrawing.Brush

    dark_sea_green: aspose.pydrawing.Brush

    dark_slate_blue: aspose.pydrawing.Brush

    dark_slate_gray: aspose.pydrawing.Brush

    dark_turquoise: aspose.pydrawing.Brush

    dark_violet: aspose.pydrawing.Brush

    deep_pink: aspose.pydrawing.Brush

    deep_sky_blue: aspose.pydrawing.Brush

    dim_gray: aspose.pydrawing.Brush

    dodger_blue: aspose.pydrawing.Brush

    firebrick: aspose.pydrawing.Brush

    floral_white: aspose.pydrawing.Brush

    forest_green: aspose.pydrawing.Brush

    fuchsia: aspose.pydrawing.Brush

    gainsboro: aspose.pydrawing.Brush

    ghost_white: aspose.pydrawing.Brush

    gold: aspose.pydrawing.Brush

    goldenrod: aspose.pydrawing.Brush

    gray: aspose.pydrawing.Brush

    green: aspose.pydrawing.Brush

    green_yellow: aspose.pydrawing.Brush

    honeydew: aspose.pydrawing.Brush

    hot_pink: aspose.pydrawing.Brush

    indian_red: aspose.pydrawing.Brush

    indigo: aspose.pydrawing.Brush

    ivory: aspose.pydrawing.Brush

    khaki: aspose.pydrawing.Brush

    lavender: aspose.pydrawing.Brush

    lavender_blush: aspose.pydrawing.Brush

    lawn_green: aspose.pydrawing.Brush

    lemon_chiffon: aspose.pydrawing.Brush

    light_blue: aspose.pydrawing.Brush

    light_coral: aspose.pydrawing.Brush

    light_cyan: aspose.pydrawing.Brush

    light_goldenrod_yellow: aspose.pydrawing.Brush

    light_green: aspose.pydrawing.Brush

    light_gray: aspose.pydrawing.Brush

    light_pink: aspose.pydrawing.Brush

    light_salmon: aspose.pydrawing.Brush

    light_sea_green: aspose.pydrawing.Brush

    light_sky_blue: aspose.pydrawing.Brush

    light_slate_gray: aspose.pydrawing.Brush

    light_steel_blue: aspose.pydrawing.Brush

    light_yellow: aspose.pydrawing.Brush

    lime: aspose.pydrawing.Brush

    lime_green: aspose.pydrawing.Brush

    linen: aspose.pydrawing.Brush

    magenta: aspose.pydrawing.Brush

    maroon: aspose.pydrawing.Brush

    medium_aquamarine: aspose.pydrawing.Brush

    medium_blue: aspose.pydrawing.Brush

    medium_orchid: aspose.pydrawing.Brush

    medium_purple: aspose.pydrawing.Brush

    medium_sea_green: aspose.pydrawing.Brush

    medium_slate_blue: aspose.pydrawing.Brush

    medium_spring_green: aspose.pydrawing.Brush

    medium_turquoise: aspose.pydrawing.Brush

    medium_violet_red: aspose.pydrawing.Brush

    midnight_blue: aspose.pydrawing.Brush

    mint_cream: aspose.pydrawing.Brush

    misty_rose: aspose.pydrawing.Brush

    moccasin: aspose.pydrawing.Brush

    navajo_white: aspose.pydrawing.Brush

    navy: aspose.pydrawing.Brush

    old_lace: aspose.pydrawing.Brush

    olive: aspose.pydrawing.Brush

    olive_drab: aspose.pydrawing.Brush

    orange: aspose.pydrawing.Brush

    orange_red: aspose.pydrawing.Brush

    orchid: aspose.pydrawing.Brush

    pale_goldenrod: aspose.pydrawing.Brush

    pale_green: aspose.pydrawing.Brush

    pale_turquoise: aspose.pydrawing.Brush

    pale_violet_red: aspose.pydrawing.Brush

    papaya_whip: aspose.pydrawing.Brush

    peach_puff: aspose.pydrawing.Brush

    peru: aspose.pydrawing.Brush

    pink: aspose.pydrawing.Brush

    plum: aspose.pydrawing.Brush

    powder_blue: aspose.pydrawing.Brush

    purple: aspose.pydrawing.Brush

    red: aspose.pydrawing.Brush

    rosy_brown: aspose.pydrawing.Brush

    royal_blue: aspose.pydrawing.Brush

    saddle_brown: aspose.pydrawing.Brush

    salmon: aspose.pydrawing.Brush

    sandy_brown: aspose.pydrawing.Brush

    sea_green: aspose.pydrawing.Brush

    sea_shell: aspose.pydrawing.Brush

    sienna: aspose.pydrawing.Brush

    silver: aspose.pydrawing.Brush

    sky_blue: aspose.pydrawing.Brush

    slate_blue: aspose.pydrawing.Brush

    slate_gray: aspose.pydrawing.Brush

    snow: aspose.pydrawing.Brush

    spring_green: aspose.pydrawing.Brush

    steel_blue: aspose.pydrawing.Brush

    tan: aspose.pydrawing.Brush

    teal: aspose.pydrawing.Brush

    thistle: aspose.pydrawing.Brush

    tomato: aspose.pydrawing.Brush

    turquoise: aspose.pydrawing.Brush

    violet: aspose.pydrawing.Brush

    wheat: aspose.pydrawing.Brush

    white: aspose.pydrawing.Brush

    white_smoke: aspose.pydrawing.Brush

    yellow: aspose.pydrawing.Brush

    yellow_green: aspose.pydrawing.Brush

    ...


class Pen:
    '''Defines an object used to draw lines and curves. This class cannot be inherited.'''

    @overload
    def __init__(self, color):
        '''Initializes a new instance of the :class:`Pen` class with the specified color.

        :param color: A  structure that indicates the color of this :class:`Pen`.'''
        ...

    @overload
    def __init__(self, color, width: float):
        '''Initializes a new instance of the :class:`Pen` class with the specified  and :attr:`Pen.width` properties.

        :param color: A  structure that indicates the color of this :class:`Pen`.
        :param width: A value indicating the width of this :class:`Pen`.'''
        ...

    @overload
    def __init__(self, brush: aspose.pydrawing.Brush):
        '''Initializes a new instance of the :class:`Pen` class with the specified :class:`Brush`.

        :param brush: A :class:`Brush` that determines the fill properties of this :class:`Pen`.
        :raises System.ArgumentNullException: is.'''
        ...

    @overload
    def __init__(self, brush: aspose.pydrawing.Brush, width: float):
        '''Initializes a new instance of the :class:`Pen` class with the specified :class:`Brush` and :attr:`Pen.width`.

        :param brush: A :class:`Brush` that determines the characteristics of this :class:`Pen`.
        :param width: The width of the new :class:`Pen`.
        :raises System.ArgumentNullException: is.'''
        ...

    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Multiplies the transformation matrix for this :class:`Pen` by the specified :class:`aspose.pydrawing.drawing2d.Matrix`.

        :param matrix: The :class:`aspose.pydrawing.drawing2d.Matrix` object by which to multiply the transformation matrix.'''
        ...

    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix,
                           order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Multiplies the transformation matrix for this :class:`Pen` by the specified :class:`aspose.pydrawing.drawing2d.Matrix` in the specified order.

        :param matrix: The :class:`aspose.pydrawing.drawing2d.Matrix` by which to multiply the transformation matrix.
        :param order: The order in which to perform the multiplication operation.'''
        ...

    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        '''Translates the local geometric transformation by the specified dimensions. This method prepends the translation to the transformation.

        :param dx: The value of the translation in x.
        :param dy: The value of the translation in y.'''
        ...

    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Translates the local geometric transformation by the specified dimensions in the specified order.

        :param dx: The value of the translation in x.
        :param dy: The value of the translation in y.
        :param order: The order (prepend or append) in which to apply the translation.'''
        ...

    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        '''Scales the local geometric transformation by the specified factors. This method prepends the scaling matrix to the transformation.

        :param sx: The factor by which to scale the transformation in the x-axis direction.
        :param sy: The factor by which to scale the transformation in the y-axis direction.'''
        ...

    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Scales the local geometric transformation by the specified factors in the specified order.

        :param sx: The factor by which to scale the transformation in the x-axis direction.
        :param sy: The factor by which to scale the transformation in the y-axis direction.
        :param order: A :class:`aspose.pydrawing.drawing2d.MatrixOrder` that specifies whether to append or prepend the scaling matrix.'''
        ...

    @overload
    def rotate_transform(self, angle: float) -> None:
        '''Rotates the local geometric transformation by the specified angle. This method prepends the rotation to the transformation.

        :param angle: The angle of rotation.'''
        ...

    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Rotates the local geometric transformation by the specified angle in the specified order.

        :param angle: The angle of rotation.
        :param order: A :class:`aspose.pydrawing.drawing2d.MatrixOrder` that specifies whether to append or prepend the rotation matrix.'''
        ...

    def clone(self) -> object:
        '''Creates an exact copy of this :class:`Pen`.

        :returns: An  that can be cast to a :class:`Pen`.'''
        ...

    def set_line_cap(self, start_cap: aspose.pydrawing.Drawing2D.LineCap, end_cap: aspose.pydrawing.Drawing2D.LineCap,
                     dash_cap: aspose.pydrawing.Drawing2D.DashCap) -> None:
        '''Sets the values that determine the style of cap used to end lines drawn by this :class:`Pen`.

        :param start_cap: A :class:`aspose.pydrawing.drawing2d.LineCap` that represents the cap style to use at the beginning of lines drawn with this :class:`Pen`.
        :param end_cap: A :class:`aspose.pydrawing.drawing2d.LineCap` that represents the cap style to use at the end of lines drawn with this :class:`Pen`.
        :param dash_cap: A :class:`aspose.pydrawing.drawing2d.LineCap` that represents the cap style to use at the beginning or end of dashed lines drawn with this :class:`Pen`.'''
        ...

    def reset_transform(self) -> None:
        '''Resets the geometric transformation matrix for this :class:`Pen` to identity.'''
        ...

    @property
    def width(self) -> float:
        '''Gets or sets the width of this :class:`Pen`, in units of the :class:`Graphics` object used for drawing.

        :returns: The width of this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.width` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @width.setter
    def width(self, value: float):
        ...

    @property
    def start_cap(self) -> aspose.pydrawing.Drawing2D.LineCap:
        '''Gets or sets the cap style used at the beginning of lines drawn with this :class:`Pen`.

        :returns: One of the :class:`aspose.pydrawing.drawing2d.LineCap` values that represents the cap style used at the beginning of lines drawn with this :class:`Pen`.

        :raises System.ComponentModel.InvalidEnumArgumentException: The specified value is not a member of :class:`aspose.pydrawing.drawing2d.LineCap`.
        :raises System.ArgumentException: The :attr:`Pen.start_cap` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @start_cap.setter
    def start_cap(self, value: aspose.pydrawing.Drawing2D.LineCap):
        ...

    @property
    def end_cap(self) -> aspose.pydrawing.Drawing2D.LineCap:
        '''Gets or sets the cap style used at the end of lines drawn with this :class:`Pen`.

        :returns: One of the :class:`aspose.pydrawing.drawing2d.LineCap` values that represents the cap style used at the end of lines drawn with this :class:`Pen`.

        :raises System.ComponentModel.InvalidEnumArgumentException: The specified value is not a member of :class:`aspose.pydrawing.drawing2d.LineCap`.
        :raises System.ArgumentException: The :attr:`Pen.end_cap` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @end_cap.setter
    def end_cap(self, value: aspose.pydrawing.Drawing2D.LineCap):
        ...

    @property
    def dash_cap(self) -> aspose.pydrawing.Drawing2D.DashCap:
        '''Gets or sets the cap style used at the end of the dashes that make up dashed lines drawn with this :class:`Pen`.

        :returns: One of the :class:`aspose.pydrawing.drawing2d.DashCap` values that represents the cap style used at the beginning and end of the dashes that make up dashed lines drawn with this :class:`Pen`.

        :raises System.ComponentModel.InvalidEnumArgumentException: The specified value is not a member of :class:`aspose.pydrawing.drawing2d.DashCap`.
        :raises System.ArgumentException: The :attr:`Pen.dash_cap` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @dash_cap.setter
    def dash_cap(self, value: aspose.pydrawing.Drawing2D.DashCap):
        ...

    @property
    def line_join(self) -> aspose.pydrawing.Drawing2D.LineJoin:
        '''Gets or sets the join style for the ends of two consecutive lines drawn with this :class:`Pen`.

        :returns: A :class:`aspose.pydrawing.drawing2d.LineJoin` that represents the join style for the ends of two consecutive lines drawn with this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.line_join` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @line_join.setter
    def line_join(self, value: aspose.pydrawing.Drawing2D.LineJoin):
        ...

    @property
    def miter_limit(self) -> float:
        '''Gets or sets the limit of the thickness of the join on a mitered corner.

        :returns: The limit of the thickness of the join on a mitered corner.

        :raises System.ArgumentException: The :attr:`Pen.miter_limit` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @miter_limit.setter
    def miter_limit(self, value: float):
        ...

    @property
    def alignment(self) -> aspose.pydrawing.Drawing2D.PenAlignment:
        '''Gets or sets the alignment for this :class:`Pen`.

        :returns: A :class:`aspose.pydrawing.drawing2d.PenAlignment` that represents the alignment for this :class:`Pen`.

        :raises System.ComponentModel.InvalidEnumArgumentException: The specified value is not a member of :class:`aspose.pydrawing.drawing2d.PenAlignment`.
        :raises System.ArgumentException: The :attr:`Pen.alignment` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @alignment.setter
    def alignment(self, value: aspose.pydrawing.Drawing2D.PenAlignment):
        ...

    @property
    def transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        '''Gets or sets a copy of the geometric transformation for this :class:`Pen`.

        :returns: A copy of the :class:`aspose.pydrawing.drawing2d.Matrix` that represents the geometric transformation for this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.transform` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @transform.setter
    def transform(self, value: aspose.pydrawing.Drawing2D.Matrix):
        ...

    @property
    def pen_type(self) -> aspose.pydrawing.Drawing2D.PenType:
        '''Gets the style of lines drawn with this :class:`Pen`.

        :returns: A :class:`aspose.pydrawing.drawing2d.PenType` enumeration that specifies the style of lines drawn with this :class:`Pen`.'''
        ...

    @property
    def color(self) -> None:
        '''Gets or sets the color of this :class:`Pen`.

        :returns: A  structure that represents the color of this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.color` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @color.setter
    def color(self, value: None):
        ...

    @property
    def brush(self) -> aspose.pydrawing.Brush:
        '''Gets or sets the :class:`Brush` that determines attributes of this :class:`Pen`.

        :returns: A :class:`Brush` that determines attributes of this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.brush` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @brush.setter
    def brush(self, value: aspose.pydrawing.Brush):
        ...

    @property
    def dash_style(self) -> aspose.pydrawing.Drawing2D.DashStyle:
        '''Gets or sets the style used for dashed lines drawn with this :class:`Pen`.

        :returns: A :class:`aspose.pydrawing.drawing2d.DashStyle` that represents the style used for dashed lines drawn with this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.dash_style` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @dash_style.setter
    def dash_style(self, value: aspose.pydrawing.Drawing2D.DashStyle):
        ...

    @property
    def dash_offset(self) -> float:
        '''Gets or sets the distance from the start of a line to the beginning of a dash pattern.

        :returns: The distance from the start of a line to the beginning of a dash pattern.

        :raises System.ArgumentException: The :attr:`Pen.dash_offset` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @dash_offset.setter
    def dash_offset(self, value: float):
        ...

    @property
    def dash_pattern(self) -> list[float]:
        '''Gets or sets an array of custom dashes and spaces.

        :returns: An array of real numbers that specifies the lengths of alternating dashes and spaces in dashed lines.

        :raises System.ArgumentException: The :attr:`Pen.dash_pattern` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @dash_pattern.setter
    def dash_pattern(self, value: list[float]):
        ...

    @property
    def compound_array(self) -> list[float]:
        '''Gets or sets an array of values that specifies a compound pen. A compound pen draws a compound line made up of parallel lines and spaces.

        :returns: An array of real numbers that specifies the compound array. The elements in the array must be in increasing order, not less than 0, and not greater than 1.

        :raises System.ArgumentException: The :attr:`Pen.compound_array` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @compound_array.setter
    def compound_array(self, value: list[float]):
        ...

    @property
    def custom_start_cap(self) -> aspose.pydrawing.Drawing2D.CustomLineCap:
        '''Gets or sets a custom cap to use at the beginning of lines drawn with this :class:`Pen`.

        :returns: A :class:`aspose.pydrawing.drawing2d.CustomLineCap` that represents the cap used at the beginning of lines drawn with this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.custom_start_cap` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @custom_start_cap.setter
    def custom_start_cap(self, value: aspose.pydrawing.Drawing2D.CustomLineCap):
        ...

    @property
    def custom_end_cap(self) -> aspose.pydrawing.Drawing2D.CustomLineCap:
        '''Gets or sets a custom cap to use at the end of lines drawn with this :class:`Pen`.

        :returns: A :class:`aspose.pydrawing.drawing2d.CustomLineCap` that represents the cap used at the end of lines drawn with this :class:`Pen`.

        :raises System.ArgumentException: The :attr:`Pen.custom_end_cap` property is set on an immutable :class:`Pen`, such as those returned by the :class:`Pens` class.'''
        ...

    @custom_end_cap.setter
    def custom_end_cap(self, value: aspose.pydrawing.Drawing2D.CustomLineCap):
        ...

    ...


class Pens:
    '''Pens for all the standard colors. This class cannot be inherited.'''

    transparent: aspose.pydrawing.Pen

    alice_blue: aspose.pydrawing.Pen

    antique_white: aspose.pydrawing.Pen

    aqua: aspose.pydrawing.Pen

    aquamarine: aspose.pydrawing.Pen

    azure: aspose.pydrawing.Pen

    beige: aspose.pydrawing.Pen

    bisque: aspose.pydrawing.Pen

    black: aspose.pydrawing.Pen

    blanched_almond: aspose.pydrawing.Pen

    blue: aspose.pydrawing.Pen

    blue_violet: aspose.pydrawing.Pen

    brown: aspose.pydrawing.Pen

    burly_wood: aspose.pydrawing.Pen

    cadet_blue: aspose.pydrawing.Pen

    chartreuse: aspose.pydrawing.Pen

    chocolate: aspose.pydrawing.Pen

    coral: aspose.pydrawing.Pen

    cornflower_blue: aspose.pydrawing.Pen

    cornsilk: aspose.pydrawing.Pen

    crimson: aspose.pydrawing.Pen

    cyan: aspose.pydrawing.Pen

    dark_blue: aspose.pydrawing.Pen

    dark_cyan: aspose.pydrawing.Pen

    dark_goldenrod: aspose.pydrawing.Pen

    dark_gray: aspose.pydrawing.Pen

    dark_green: aspose.pydrawing.Pen

    dark_khaki: aspose.pydrawing.Pen

    dark_magenta: aspose.pydrawing.Pen

    dark_olive_green: aspose.pydrawing.Pen

    dark_orange: aspose.pydrawing.Pen

    dark_orchid: aspose.pydrawing.Pen

    dark_red: aspose.pydrawing.Pen

    dark_salmon: aspose.pydrawing.Pen

    dark_sea_green: aspose.pydrawing.Pen

    dark_slate_blue: aspose.pydrawing.Pen

    dark_slate_gray: aspose.pydrawing.Pen

    dark_turquoise: aspose.pydrawing.Pen

    dark_violet: aspose.pydrawing.Pen

    deep_pink: aspose.pydrawing.Pen

    deep_sky_blue: aspose.pydrawing.Pen

    dim_gray: aspose.pydrawing.Pen

    dodger_blue: aspose.pydrawing.Pen

    firebrick: aspose.pydrawing.Pen

    floral_white: aspose.pydrawing.Pen

    forest_green: aspose.pydrawing.Pen

    fuchsia: aspose.pydrawing.Pen

    gainsboro: aspose.pydrawing.Pen

    ghost_white: aspose.pydrawing.Pen

    gold: aspose.pydrawing.Pen

    goldenrod: aspose.pydrawing.Pen

    gray: aspose.pydrawing.Pen

    green: aspose.pydrawing.Pen

    green_yellow: aspose.pydrawing.Pen

    honeydew: aspose.pydrawing.Pen

    hot_pink: aspose.pydrawing.Pen

    indian_red: aspose.pydrawing.Pen

    indigo: aspose.pydrawing.Pen

    ivory: aspose.pydrawing.Pen

    khaki: aspose.pydrawing.Pen

    lavender: aspose.pydrawing.Pen

    lavender_blush: aspose.pydrawing.Pen

    lawn_green: aspose.pydrawing.Pen

    lemon_chiffon: aspose.pydrawing.Pen

    light_blue: aspose.pydrawing.Pen

    light_coral: aspose.pydrawing.Pen

    light_cyan: aspose.pydrawing.Pen

    light_goldenrod_yellow: aspose.pydrawing.Pen

    light_green: aspose.pydrawing.Pen

    light_gray: aspose.pydrawing.Pen

    light_pink: aspose.pydrawing.Pen

    light_salmon: aspose.pydrawing.Pen

    light_sea_green: aspose.pydrawing.Pen

    light_sky_blue: aspose.pydrawing.Pen

    light_slate_gray: aspose.pydrawing.Pen

    light_steel_blue: aspose.pydrawing.Pen

    light_yellow: aspose.pydrawing.Pen

    lime: aspose.pydrawing.Pen

    lime_green: aspose.pydrawing.Pen

    linen: aspose.pydrawing.Pen

    magenta: aspose.pydrawing.Pen

    maroon: aspose.pydrawing.Pen

    medium_aquamarine: aspose.pydrawing.Pen

    medium_blue: aspose.pydrawing.Pen

    medium_orchid: aspose.pydrawing.Pen

    medium_purple: aspose.pydrawing.Pen

    medium_sea_green: aspose.pydrawing.Pen

    medium_slate_blue: aspose.pydrawing.Pen

    medium_spring_green: aspose.pydrawing.Pen

    medium_turquoise: aspose.pydrawing.Pen

    medium_violet_red: aspose.pydrawing.Pen

    midnight_blue: aspose.pydrawing.Pen

    mint_cream: aspose.pydrawing.Pen

    misty_rose: aspose.pydrawing.Pen

    moccasin: aspose.pydrawing.Pen

    navajo_white: aspose.pydrawing.Pen

    navy: aspose.pydrawing.Pen

    old_lace: aspose.pydrawing.Pen

    olive: aspose.pydrawing.Pen

    olive_drab: aspose.pydrawing.Pen

    orange: aspose.pydrawing.Pen

    orange_red: aspose.pydrawing.Pen

    orchid: aspose.pydrawing.Pen

    pale_goldenrod: aspose.pydrawing.Pen

    pale_green: aspose.pydrawing.Pen

    pale_turquoise: aspose.pydrawing.Pen

    pale_violet_red: aspose.pydrawing.Pen

    papaya_whip: aspose.pydrawing.Pen

    peach_puff: aspose.pydrawing.Pen

    peru: aspose.pydrawing.Pen

    pink: aspose.pydrawing.Pen

    plum: aspose.pydrawing.Pen

    powder_blue: aspose.pydrawing.Pen

    purple: aspose.pydrawing.Pen

    red: aspose.pydrawing.Pen

    rosy_brown: aspose.pydrawing.Pen

    royal_blue: aspose.pydrawing.Pen

    saddle_brown: aspose.pydrawing.Pen

    salmon: aspose.pydrawing.Pen

    sandy_brown: aspose.pydrawing.Pen

    sea_green: aspose.pydrawing.Pen

    sea_shell: aspose.pydrawing.Pen

    sienna: aspose.pydrawing.Pen

    silver: aspose.pydrawing.Pen

    sky_blue: aspose.pydrawing.Pen

    slate_blue: aspose.pydrawing.Pen

    slate_gray: aspose.pydrawing.Pen

    snow: aspose.pydrawing.Pen

    spring_green: aspose.pydrawing.Pen

    steel_blue: aspose.pydrawing.Pen

    tan: aspose.pydrawing.Pen

    teal: aspose.pydrawing.Pen

    thistle: aspose.pydrawing.Pen

    tomato: aspose.pydrawing.Pen

    turquoise: aspose.pydrawing.Pen

    violet: aspose.pydrawing.Pen

    wheat: aspose.pydrawing.Pen

    white: aspose.pydrawing.Pen

    white_smoke: aspose.pydrawing.Pen

    yellow: aspose.pydrawing.Pen

    yellow_green: aspose.pydrawing.Pen

    ...


class FontStyle:
    '''Specifies style information applied to text.'''

    REGULAR: int
    BOLD: int
    ITALIC: int
    UNDERLINE: int
    STRIKEOUT: int

class Brush:
    '''Defines objects used to fill the interiors of graphical shapes such as rectangles, ellipses, pies, polygons, and paths.'''

    def clone(self) -> object:
        '''When overridden in a derived class, creates an exact copy of this :class:`Brush`.

        :returns: The new :class:`Brush` that this method creates.'''
        ...

    ...


class Font:
    '''Defines a particular format for text, including font face, size, and style attributes. This class cannot be inherited.'''

    @overload
    def __init__(self, prototype: aspose.pydrawing.Font, new_style: aspose.pydrawing.FontStyle):
        '''Initializes a new :class:`Font` that uses the specified existing :class:`Font` and :class:`FontStyle` enumeration.

        :param prototype: The existing :class:`Font` from which to create the new :class:`Font`.
        :param new_style: The :class:`FontStyle` to apply to the new :class:`Font`. Multiple values of the :class:`FontStyle` enumeration can be combined with the  operator.'''
        ...

    @overload
    def __init__(self, family_name: str, em_size: float, style: aspose.pydrawing.FontStyle):
        '''Initializes a new :class:`Font` using a specified size and style.

        :param family_name: A string representation of the :class:`FontFamily` for the new :class:`Font`.
        :param em_size: The em-size, in points, of the new font.
        :param style: The :class:`FontStyle` of the new font.
        :raises System.ArgumentException: is less than or equal to 0, evaluates to infinity, or is not a valid number.'''
        ...

    @overload
    def __init__(self, family_name: str, em_size: float):
        '''Initializes a new :class:`Font` using a specified size.

        :param family_name: A string representation of the :class:`FontFamily` for the new :class:`Font`.
        :param em_size: The em-size, in points, of the new font.
        :raises System.ArgumentException: is less than or equal to 0, evaluates to infinity or is not a valid number.'''
        ...

    @overload
    def get_height(self, dpi: float) -> float:
        '''Returns the height, in pixels, of this :class:`Font` when drawn to a device with the specified vertical resolution.

        :param dpi: The vertical resolution, in dots per inch, used to calculate the height of the font.
        :returns: The height, in pixels, of this :class:`Font`.'''
        ...

    @overload
    def get_height(self) -> float:
        '''Returns the line spacing, in pixels, of this font.

        :returns: The line spacing, in pixels, of this font.'''
        ...

    def clone(self) -> object:
        '''Creates an exact copy of this :class:`Font`.

        :returns: The :class:`Font` this method creates, cast as an .'''
        ...

    @property
    def size(self) -> float:
        '''Gets the em-size of this :class:`Font` measured in the units specified by the :attr:`Font.unit` property.

        :returns: The em-size of this :class:`Font`.'''
        ...

    @property
    def style(self) -> aspose.pydrawing.FontStyle:
        '''Gets style information for this :class:`Font`.

        :returns: A :class:`FontStyle` enumeration that contains style information for this :class:`Font`.'''
        ...

    @property
    def bold(self) -> bool:
        '''Gets a value that indicates whether this :class:`Font` is bold.

        :returns:  if this :class:`Font` is bold; otherwise, .'''
        ...

    @property
    def italic(self) -> bool:
        '''Gets a value that indicates whether this font has the italic style applied.

        :returns:  to indicate this font has the italic style applied; otherwise, .'''
        ...

    @property
    def strikeout(self) -> bool:
        '''Gets a value that indicates whether this :class:`Font` specifies a horizontal line through the font.

        :returns:  if this :class:`Font` has a horizontal line through it; otherwise, .'''
        ...

    @property
    def underline(self) -> bool:
        '''Gets a value that indicates whether this :class:`Font` is underlined.

        :returns:  if this :class:`Font` is underlined; otherwise, .'''
        ...

    @property
    def name(self) -> str:
        '''Gets the face name of this :class:`Font`.

        :returns: A string representation of the face name of this :class:`Font`.'''
        ...

    @property
    def original_font_name(self) -> str:
        '''Gets the name of the font originally specified.

        :returns: The string representing the name of the font originally specified.'''
        ...

    @property
    def system_font_name(self) -> str:
        '''Gets the name of the system font if the :attr:`Font.is_system_font` property returns .

        :returns: The name of the system font, if :attr:`Font.is_system_font` returns ; otherwise, an empty string ("").'''
        ...

    @property
    def is_system_font(self) -> bool:
        '''Gets a value indicating whether the font is a member of :class:`SystemFonts`.

        :returns:  if the font is a member of :class:`SystemFonts`; otherwise, . The default is .'''
        ...

    @property
    def height(self) -> int:
        '''Gets the line spacing of this font.

        :returns: The line spacing, in pixels, of this font.'''
        ...

    @property
    def size_in_points(self) -> float:
        '''Gets the em-size, in points, of this :class:`Font`.

        :returns: The em-size, in points, of this :class:`Font`.'''
        ...

    ...


class SolidBrush(aspose.pydrawing.Brush):
    '''Defines a brush of a single color. Brushes are used to fill graphics shapes, such as rectangles, ellipses, pies, polygons, and paths. This class cannot be inherited.'''

    def __init__(self, color):
        '''Initializes a new :class:`SolidBrush` object of the specified color.

        :param color: A  structure that represents the color of this brush.'''
        ...

    def clone(self) -> object:
        '''Creates an exact copy of this :class:`SolidBrush` object.

        :returns: The :class:`SolidBrush` object that this method creates.'''
        ...

    @property
    def color(self) -> None:
        '''Gets or sets the color of this :class:`SolidBrush` object.

        :returns: A  structure that represents the color of this brush.

        :raises System.ArgumentException: The :attr:`SolidBrush.color` property is set on an immutable :class:`SolidBrush`.'''
        ...

    @color.setter
    def color(self, value: None):
        ...

    ...


class TextureBrush(aspose.pydrawing.Brush):
    '''Each property of the :class:`TextureBrush` class is a :class:`Brush` object that uses an image to fill the interior of a shape. This class cannot be inherited.'''

    @overload
    def __init__(self, bitmap: aspose.pydrawing.Image):
        '''Initializes a new :class:`TextureBrush` object that uses the specified image.

        :param bitmap: The :class:`Image` object with which this :class:`TextureBrush` object fills interiors.'''
        ...

    @overload
    def __init__(self, image: aspose.pydrawing.Image, wrap_mode: aspose.pydrawing.Drawing2D.WrapMode):
        '''Initializes a new :class:`TextureBrush` object that uses the specified image and wrap mode.

        :param image: The :class:`Image` object with which this :class:`TextureBrush` object fills interiors.
        :param wrap_mode: A :class:`aspose.pydrawing.drawing2d.WrapMode` enumeration that specifies how this :class:`TextureBrush` object is tiled.'''
        ...

    @overload
    def __init__(self, image: aspose.pydrawing.Image, wrap_mode: aspose.pydrawing.Drawing2D.WrapMode, dst_rect):
        '''Initializes a new :class:`TextureBrush` object that uses the specified image, wrap mode, and bounding rectangle.

        :param image: The :class:`Image` object with which this :class:`TextureBrush` object fills interiors.
        :param wrap_mode: A :class:`aspose.pydrawing.drawing2d.WrapMode` enumeration that specifies how this :class:`TextureBrush` object is tiled.
        :param dst_rect: A  structure that represents the bounding rectangle for this :class:`TextureBrush` object.'''
        ...

    @overload
    def __init__(self, image: aspose.pydrawing.Image, wrap_mode: aspose.pydrawing.Drawing2D.WrapMode, dst_rect):
        '''Initializes a new :class:`TextureBrush` object that uses the specified image, wrap mode, and bounding rectangle.

        :param image: The :class:`Image` object with which this :class:`TextureBrush` object fills interiors.
        :param wrap_mode: A :class:`aspose.pydrawing.drawing2d.WrapMode` enumeration that specifies how this :class:`TextureBrush` object is tiled.
        :param dst_rect: A  structure that represents the bounding rectangle for this :class:`TextureBrush` object.'''
        ...

    @overload
    def __init__(self, image: aspose.pydrawing.Image, dst_rect):
        '''Initializes a new :class:`TextureBrush` object that uses the specified image and bounding rectangle.

        :param image: The :class:`Image` object with which this :class:`TextureBrush` object fills interiors.
        :param dst_rect: A  structure that represents the bounding rectangle for this :class:`TextureBrush` object.'''
        ...

    @overload
    def __init__(self, image: aspose.pydrawing.Image, dst_rect):
        '''Initializes a new :class:`TextureBrush` object that uses the specified image and bounding rectangle.

        :param image: The :class:`Image` object with which this :class:`TextureBrush` object fills interiors.
        :param dst_rect: A  structure that represents the bounding rectangle for this :class:`TextureBrush` object.'''
        ...

    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Multiplies the :class:`aspose.pydrawing.drawing2d.Matrix` object that represents the local geometric transformation of this :class:`TextureBrush` object by the specified :class:`aspose.pydrawing.drawing2d.Matrix` object by prepending the specified :class:`aspose.pydrawing.drawing2d.Matrix` object.

        :param matrix: The :class:`aspose.pydrawing.drawing2d.Matrix` object by which to multiply the geometric transformation.'''
        ...

    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.Drawing2D.Matrix,
                           order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Multiplies the :class:`aspose.pydrawing.drawing2d.Matrix` object that represents the local geometric transformation of this :class:`TextureBrush` object by the specified :class:`aspose.pydrawing.drawing2d.Matrix` object in the specified order.

        :param matrix: The :class:`aspose.pydrawing.drawing2d.Matrix` object by which to multiply the geometric transformation.
        :param order: A :class:`aspose.pydrawing.drawing2d.MatrixOrder` enumeration that specifies the order in which to multiply the two matrices.'''
        ...

    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        '''Translates the local geometric transformation of this :class:`TextureBrush` object by the specified dimensions. This method prepends the translation to the transformation.

        :param dx: The dimension by which to translate the transformation in the x direction.
        :param dy: The dimension by which to translate the transformation in the y direction.'''
        ...

    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Translates the local geometric transformation of this :class:`TextureBrush` object by the specified dimensions in the specified order.

        :param dx: The dimension by which to translate the transformation in the x direction.
        :param dy: The dimension by which to translate the transformation in the y direction.
        :param order: The order (prepend or append) in which to apply the translation.'''
        ...

    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        '''Scales the local geometric transformation of this :class:`TextureBrush` object by the specified amounts. This method prepends the scaling matrix to the transformation.

        :param sx: The amount by which to scale the transformation in the x direction.
        :param sy: The amount by which to scale the transformation in the y direction.'''
        ...

    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Scales the local geometric transformation of this :class:`TextureBrush` object by the specified amounts in the specified order.

        :param sx: The amount by which to scale the transformation in the x direction.
        :param sy: The amount by which to scale the transformation in the y direction.
        :param order: A :class:`aspose.pydrawing.drawing2d.MatrixOrder` enumeration that specifies whether to append or prepend the scaling matrix.'''
        ...

    @overload
    def rotate_transform(self, angle: float) -> None:
        '''Rotates the local geometric transformation of this :class:`TextureBrush` object by the specified amount. This method prepends the rotation to the transformation.

        :param angle: The angle of rotation.'''
        ...

    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.Drawing2D.MatrixOrder) -> None:
        '''Rotates the local geometric transformation of this :class:`TextureBrush` object by the specified amount in the specified order.

        :param angle: The angle of rotation.
        :param order: A :class:`aspose.pydrawing.drawing2d.MatrixOrder` enumeration that specifies whether to append or prepend the rotation matrix.'''
        ...

    def clone(self) -> object:
        '''Creates an exact copy of this :class:`TextureBrush` object.

        :returns: The :class:`TextureBrush` object this method creates, cast as an  object.'''
        ...

    def reset_transform(self) -> None:
        '''Resets the  property of this :class:`TextureBrush` object to identity.'''
        ...

    @property
    def transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        '''Gets or sets a copy of the :class:`aspose.pydrawing.drawing2d.Matrix` object that defines a local geometric transformation for the image associated with this :class:`TextureBrush` object.

        :returns: A copy of the :class:`aspose.pydrawing.drawing2d.Matrix` object that defines a geometric transformation that applies only to fills drawn by using this :class:`TextureBrush` object.'''
        ...

    @transform.setter
    def transform(self, value: aspose.pydrawing.Drawing2D.Matrix):
        ...

    @property
    def wrap_mode(self) -> aspose.pydrawing.Drawing2D.WrapMode:
        '''Gets or sets a :class:`aspose.pydrawing.drawing2d.WrapMode` enumeration that indicates the wrap mode for this :class:`TextureBrush` object.

        :returns: A :class:`aspose.pydrawing.drawing2d.WrapMode` enumeration that specifies how fills drawn by using this :class:`aspose.pydrawing.drawing2d.LinearGradientBrush` object are tiled.'''
        ...

    @wrap_mode.setter
    def wrap_mode(self, value: aspose.pydrawing.Drawing2D.WrapMode):
        ...

    @property
    def image(self) -> aspose.pydrawing.Image:
        '''Gets the :class:`Image` object associated with this :class:`TextureBrush` object.

        :returns: An :class:`Image` object that represents the image with which this :class:`TextureBrush` object fills shapes.'''
        ...

    ...
