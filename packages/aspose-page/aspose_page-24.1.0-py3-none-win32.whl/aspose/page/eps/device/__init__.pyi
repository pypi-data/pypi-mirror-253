import aspose.page
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class ImageDevice(aspose.page.Device):
    '''This class encapsulates rendering of document to image.'''
    
    @overload
    def __init__(self):
        '''Initializes new instance of :class:`ImageDevice`.'''
        ...
    
    @overload
    def __init__(self, size: aspose.pydrawing.Size):
        '''Initializes new instance of :class:`ImageDevice` with specified size of a page.
        
        :param size: Page size.'''
        ...
    
    @overload
    def __init__(self, image_format: aspose.pydrawing.Imaging.ImageFormat):
        '''Initializes new instance of :class:`ImageDevice` with specified image format.
        
        :param image_format: Format of the image.'''
        ...
    
    @overload
    def __init__(self, size: aspose.pydrawing.Size, image_format: aspose.pydrawing.Imaging.ImageFormat):
        '''Initializes new instance of :class:`ImageDevice` with specified size of a page and image format.
        
        :param size: Page size.
        :param image_format: Format of the image.'''
        ...
    
    @overload
    def rotate(self, theta: float) -> None:
        '''Rotate the current transformation matrix over the Z-axis. Calls writeTransform(Transform).
        Rotating with a positive angle theta rotates points on the positive x axis
        toward the positive y axis.
        
        :param theta: Angle in radians over which to rotate.'''
        ...
    
    @overload
    def open_page(self, title: str) -> bool:
        '''Makes necessary preparation of the device before page rendering.
        
        :param title: The page title.
        :returns: Always true.'''
        ...
    
    @overload
    def open_page(self, width: float, height: float) -> bool:
        '''Makes necessary preparation of the device before each page rendering.
        
        :param width: A width of the page.
        :param height: A height of the page.
        :returns: Always true.'''
        ...
    
    def re_new(self) -> None:
        '''Reset device to initial state for whole document.'''
        ...
    
    def get_property(self, key: str) -> str:
        '''Gets a value of string property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def get_property_color(self, key: str) -> aspose.pydrawing.Color:
        '''Gets a value of color property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def get_property_rectangle(self, key: str) -> aspose.pydrawing.RectangleF:
        '''Gets a value of rectangle property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def get_property_margins(self, key: str) -> aspose.page.Margins:
        '''Gets a value of margins property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def get_property_size(self, key: str) -> aspose.pydrawing.Size:
        '''Gets a value of size property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def get_property_int(self, key: str) -> int:
        '''Gets a value of integer property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def get_property_double(self, key: str) -> float:
        '''Gets a value of double property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def is_property(self, key: str) -> bool:
        '''Gets a value of boolean property.
        
        :param key: The name of property.
        :returns: The property value.'''
        ...
    
    def create(self) -> aspose.page.Device:
        '''Creates a copy of this device.
        
        :returns: Copy of this device.'''
        ...
    
    def set_transform(self, transform: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Specifies current transform.
        
        :param transform: A transform.'''
        ...
    
    def get_transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        '''Gets the current transform.
        
        :returns: Current transform.'''
        ...
    
    def transform(self, transform: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Transforms the current transformation matrix. Calls writeTransform(Transform).
        
        :param transform: Transform to be applied.'''
        ...
    
    def translate(self, x: float, y: float) -> None:
        '''Translates the current transformation matrix. Calls writeTransform(Transform).
        
        :param x: Translation in X axis.
        :param y: Translation in Y axis.'''
        ...
    
    def scale(self, sx: float, sy: float) -> None:
        '''Scales the current transformation matrix. Calls writeTransform(Transform).
        
        :param sx: A scale in X axis.
        :param sy: A scale in Y axis.'''
        ...
    
    def shear(self, shx: float, shy: float) -> None:
        '''Shears the current transformation matrix. Calls writeTransform(Transform).
        
        :param shx: A shear in X axis.
        :param shy: A shear in Y axis.'''
        ...
    
    def init_clip(self) -> None:
        '''Initializes a clip of the device.'''
        ...
    
    def set_clip(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Clips shape.
        
        :param path: Path that is used for clipping.'''
        ...
    
    def draw(self, s: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Draws a path.
        
        :param s: A path to be drawn.'''
        ...
    
    def fill(self, s: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Fills a path.
        
        :param s: A path to be filled.'''
        ...
    
    def draw_string(self, str: str, x: float, y: float) -> None:
        '''Draws a string at given point.
        
        :param str: A string to be drawn.
        :param x: X coordinate of point.
        :param y: Y coordinate of point.'''
        ...
    
    def draw_image(self, image: aspose.pydrawing.Bitmap, transform: aspose.pydrawing.Drawing2D.Matrix, bkg: aspose.pydrawing.Color) -> None:
        '''Draws an image with assigned transform and background.
        
        :param image: An image to be drawn.
        :param transform: A transform.
        :param bkg: A background color.'''
        ...
    
    def start_document(self) -> None:
        '''Makes necessary preparation of device before start rendering of document.'''
        ...
    
    def end_document(self) -> None:
        '''Makes necessary preparation of device after the document has been rendered.'''
        ...
    
    def dispose(self) -> None:
        '''Disposes the device.'''
        ...
    
    def reset(self) -> None:
        '''Reset the device to initial state for a page.'''
        ...
    
    def write_comment(self, comment: str) -> None:
        '''Writes a comment.
        
        :param comment: A comment to be written.'''
        ...
    
    def init_page_numbers(self) -> None:
        '''Initializes numbers of pages to output.'''
        ...
    
    def close_page(self) -> None:
        '''Makes necessary preparation of the device after page has been rendered.'''
        ...
    
    def update_page_parameters(self, device: aspose.page.IMultiPageDevice) -> None:
        '''Updates page parameters from other multi-paged device.
        
        :param device: Another instance of the same device.'''
        ...
    
    @property
    def creator(self) -> str:
        '''Returns or specifies creator of resulting device output.'''
        ...
    
    @creator.setter
    def creator(self, value: str):
        ...
    
    @property
    def size(self) -> aspose.pydrawing.Size:
        '''Returns or specifies a size of the page.'''
        ...
    
    @size.setter
    def size(self, value: aspose.pydrawing.Size):
        ...
    
    @property
    def is_direct_rgb(self) -> bool:
        '''Indicates whether device uses direct RGB mode, that is RGB.
        
        :returns: True if direct RGB mode and false otherwise, that is BGR.'''
        ...
    
    @property
    def background(self) -> aspose.pydrawing.Color:
        '''Indicates whether device uses direct RGB mode, that is RGB.
        
        :returns: True if direct RGB mode and false otherwise, that is BGR.'''
        ...
    
    @background.setter
    def background(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def opacity(self) -> float:
        '''Returns or specifies current background of the page.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    @property
    def stroke(self) -> aspose.pydrawing.Pen:
        '''Returns or specifies current stroke.'''
        ...
    
    @stroke.setter
    def stroke(self, value: aspose.pydrawing.Pen):
        ...
    
    @property
    def paint(self) -> aspose.pydrawing.Brush:
        '''Returns or specifies current paint.'''
        ...
    
    @paint.setter
    def paint(self, value: aspose.pydrawing.Brush):
        ...
    
    @property
    def char_tm(self) -> aspose.pydrawing.Drawing2D.Matrix:
        '''Returns or specifies current characters transform.'''
        ...
    
    @char_tm.setter
    def char_tm(self, value: aspose.pydrawing.Drawing2D.Matrix):
        ...
    
    @property
    def text_rendering_mode(self) -> aspose.page.TextRenderingMode:
        '''Returns or specifies current text rendering mode.'''
        ...
    
    @text_rendering_mode.setter
    def text_rendering_mode(self, value: aspose.page.TextRenderingMode):
        ...
    
    @property
    def text_stroke_width(self) -> float:
        '''Returns or specifies current text stroke width.'''
        ...
    
    @text_stroke_width.setter
    def text_stroke_width(self, value: float):
        ...
    
    @property
    def format(self) -> aspose.pydrawing.Imaging.ImageFormat:
        '''Image format.'''
        ...
    
    @property
    def current_page_number(self) -> int:
        '''Current page number.'''
        ...
    
    @property
    def images_bytes(self) -> list[bytes]:
        '''Returns resulting images in bytes, one byte array for one page.'''
        ...
    
    TRANSPARENT: str
    
    BACKGROUND: str
    
    BACKGROUND_COLOR: str
    
    PAGE_SIZE: str
    
    PAGE_MARGINS: str
    
    ORIENTATION: str
    
    FIT_TO_PAGE: str
    
    EMBED_FONTS: str
    
    EMIT_WARNINGS: str
    
    EMIT_ERRORS: str
    
    PRODUCER: str
    
    ...

class ImageSaveOptions(aspose.page.SaveOptions):
    '''This class contains options necessary for managing image saving process.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`ImageSaveOptions` class with default values
        for flags  (true) and  (false).'''
        ...
    
    @overload
    def __init__(self, supress_errors: bool):
        '''Initializes a new instance of the :class:`ImageSaveOptions` with
        default value for flag  (false).
        
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @property
    def resolution(self) -> float:
        '''Gets/sets the image resolution.'''
        ...
    
    @resolution.setter
    def resolution(self, value: float):
        ...
    
    @property
    def smoothing_mode(self) -> aspose.pydrawing.Drawing2D.SmoothingMode:
        '''Gets/sets the smoothing mode for rendering image.'''
        ...
    
    @smoothing_mode.setter
    def smoothing_mode(self, value: aspose.pydrawing.Drawing2D.SmoothingMode):
        ...
    
    ...

class PdfDevice(aspose.page.Device):
    '''This class encapsulates rendering of document to PDF.'''
    
    @overload
    def __init__(self, ros: io.BytesIO):
        '''Initializes new instance of :class:`PdfDevice` with output stream.
        
        :param ros: Output stream.'''
        ...
    
    @overload
    def __init__(self, ros: io.BytesIO, size: aspose.pydrawing.Size):
        '''Initializes new instance of :class:`PdfDevice` with output stream and specified size of a page.
        
        :param ros: Output stream.
        :param size: Page size.'''
        ...
    
    @overload
    def rotate(self, theta: float) -> None:
        '''Rotate the current transform over the Z-axis. Calls writeTransform(Transform).
        Rotating with a positive angle theta rotates points on the positive x axis
        toward the positive y axis.
        
        :param theta: radians over which to rotate'''
        ...
    
    @overload
    def open_page(self, title: str) -> bool:
        '''Makes necessary preparation of the device before page rendering.
        
        :param title: The page title.
        :returns: Always true.'''
        ...
    
    @overload
    def open_page(self, width: float, height: float) -> bool:
        '''Makes necessary preparation of the device before each page rendering.
        
        :param width: A width of the page.
        :param height: A height of the page.
        :returns: Always true.'''
        ...
    
    def re_new(self) -> None:
        '''Reset device to initial state for whole document. Used for reseting output stream.'''
        ...
    
    def create(self) -> aspose.page.Device:
        '''Creates a copy of this device.
        
        :returns: Copy of this device.'''
        ...
    
    def set_transform(self, transform: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Specifies the current transform. Since most output formats do not
        implement this functionality, the inverse transform of the
        currentTransform is calculated and multiplied by the
        transform to be set.The result is then forwarded by a call
        to writeTransform(Transform).
        
        :param transform: Transform to be applied.'''
        ...
    
    def get_transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        '''Gets current transform.
        
        :returns: Current transform'''
        ...
    
    def transform(self, transform: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Transforms the current transformation matrix. Calls writeTransform(Transform)
        
        :param transform: Transform to be applied.'''
        ...
    
    def translate(self, x: float, y: float) -> None:
        '''Translates the current transformation matrix. Calls writeTransform(Transform).
        
        :param x: Translation in X axis.
        :param y: Translation in Y axis.'''
        ...
    
    def scale(self, sx: float, sy: float) -> None:
        '''Scales the current transformation matrix. Calls writeTransform(Transform).
        
        :param sx: A scale in X axis.
        :param sy: A scale in Y axis.'''
        ...
    
    def shear(self, shx: float, shy: float) -> None:
        '''Shears the current transformation matrix. Calls writeTransform(Transform).
        
        :param shx: A shear in X axis.
        :param shy: A shear in Y axis.'''
        ...
    
    def init_clip(self) -> None:
        '''Initializes clip of the device.'''
        ...
    
    def set_clip(self, clip_path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Specifies the clip of the device.
        
        :param clip_path: A clipping path.'''
        ...
    
    def draw(self, s: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Draws a path.
        
        :param s: A path to be drawn.'''
        ...
    
    def fill(self, s: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Fills a path.
        
        :param s: A path to be filled.'''
        ...
    
    def draw_string(self, str: str, x: float, y: float) -> None:
        '''Draws a string at given point.
        
        :param str: A string to be drawn.
        :param x: X coordinate of point.
        :param y: Y coordinate of point.'''
        ...
    
    def draw_image(self, image: aspose.pydrawing.Bitmap, transform: aspose.pydrawing.Drawing2D.Matrix, bkg: aspose.pydrawing.Color) -> None:
        '''Draws an image with assigned transform and background.
        
        :param image: An image to be drawn.
        :param transform: A transform.
        :param bkg: A background color.'''
        ...
    
    def start_document(self) -> None:
        '''Makes necessary preparation of device before start rendering of document.'''
        ...
    
    def end_document(self) -> None:
        '''Makes necessary preparation of device after the document has been rendered.'''
        ...
    
    def dispose(self) -> None:
        '''Disposes the graphics context. If on creation restoreOnDispose was true,
        writeGraphicsRestore() will be called.'''
        ...
    
    def reset(self) -> None:
        '''If page device parameters will be set this method allows to return writing stream back the begining of page.'''
        ...
    
    def write_comment(self, comment: str) -> None:
        '''Writes a comment.
        
        :param comment: A comment to be written.'''
        ...
    
    def init_page_numbers(self) -> None:
        '''Initializes numbers of pages to output.'''
        ...
    
    def close_page(self) -> None:
        '''Makes necessary preparation of the device after page has been rendered.'''
        ...
    
    def update_page_parameters(self, device: aspose.page.IMultiPageDevice) -> None:
        '''Updates page parameters from other multi-paged device.
        
        :param device: Another instance of the same device.'''
        ...
    
    @property
    def stroke(self) -> aspose.pydrawing.Pen:
        '''Returns or specifies current stroke.'''
        ...
    
    @stroke.setter
    def stroke(self, value: aspose.pydrawing.Pen):
        ...
    
    @property
    def paint(self) -> aspose.pydrawing.Brush:
        '''Returns or specifies current paint.'''
        ...
    
    @paint.setter
    def paint(self, value: aspose.pydrawing.Brush):
        ...
    
    version: str
    
    @property
    def current_page_number(self) -> int:
        '''Current page number.'''
        ...
    
    @property
    def output_stream(self) -> io.BytesIO:
        '''Specifies or returns an output stream.'''
        ...
    
    @output_stream.setter
    def output_stream(self, value: io.BytesIO):
        ...
    
    VERSION: str
    
    VERSION5: str
    
    TRANSPARENT: str
    
    BACKGROUND: str
    
    BACKGROUND_COLOR: str
    
    PAGE_SIZE: str
    
    PAGE_MARGINS: str
    
    ORIENTATION: str
    
    FIT_TO_PAGE: str
    
    EMBED_FONTS: str
    
    EMBED_FONTS_AS: str
    
    COMPRESS: str
    
    WRITE_IMAGES_AS: str
    
    AUTHOR: str
    
    TITLE: str
    
    SUBJECT: str
    
    KEYWORDS: str
    
    EMIT_WARNINGS: str
    
    EMIT_ERRORS: str
    
    ...

class PdfSaveOptions(aspose.page.SaveOptions):
    '''This class contains input and output streams and other options necessary for managing conversion process.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PdfSaveOptions` class with default values
        for flags  (true) and  (false).'''
        ...
    
    @overload
    def __init__(self, supress_errors: bool):
        '''Initializes a new instance of the :class:`PdfSaveOptions` class with default values for flag  (false).
        
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    ...

class PsSaveOptions(aspose.page.SaveOptions):
    '''This class contains options necessary for managing process of converting document to PostScript (PS) or Encapsulated PostScript (EPS) file.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PsSaveOptions` class with default values
        for flags  (true) and  (false).'''
        ...
    
    @overload
    def __init__(self, supress_errors: bool):
        '''Initializes a new instance of the :class:`PsSaveOptions` class with default values for flag  (false).
        
        :param supress_errors: Specifies whether errors must be suppressed or not.
                               If true suppressed errors are added to  list.'''
        ...
    
    @property
    def page_size(self) -> aspose.pydrawing.Size:
        '''The size of the page.'''
        ...
    
    @page_size.setter
    def page_size(self, value: aspose.pydrawing.Size):
        ...
    
    @property
    def margins(self) -> aspose.page.Margins:
        '''The margins of the page.'''
        ...
    
    @margins.setter
    def margins(self, value: aspose.page.Margins):
        ...
    
    @property
    def background_color(self) -> aspose.pydrawing.Color:
        '''The background color.'''
        ...
    
    @background_color.setter
    def background_color(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def transparent(self) -> bool:
        '''Indicates if background is transparent.'''
        ...
    
    @transparent.setter
    def transparent(self, value: bool):
        ...
    
    @property
    def embed_fonts(self) -> bool:
        '''Indicates whether to embed used fonts in PS document.'''
        ...
    
    @embed_fonts.setter
    def embed_fonts(self, value: bool):
        ...
    
    @property
    def embed_fonts_as(self) -> str:
        '''A type of font in which to embed fonts in PS document.'''
        ...
    
    @embed_fonts_as.setter
    def embed_fonts_as(self, value: str):
        ...
    
    ...

