from aspose.page import eps
from aspose.page import font
from aspose.page import plugins
from aspose.page import xps
import aspose.page
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

class BuildVersionInfo:
    '''This class provides information about current product build.'''
    
    def __init__(self):
        ...
    
    ASSEMBLY_VERSION: str
    
    PRODUCT: str
    
    FILE_VERSION: str
    
    ...

class Device:
    '''This class encapsulates rendering of document to abstract device.
    Rendering of the document is performed page by page.'''
    
    @overload
    def rotate(self, theta: float) -> None:
        '''Rotate the current transformation matrix. Calls writeTransform(Transform).
        Rotating with a positive angle theta rotates points on the positive x axis
        toward the positive y axis.
        
        :param theta: Angle in radians over which to rotate.'''
        ...
    
    @overload
    def rotate(self, theta: float, x: float, y: float) -> None:
        '''Rotate the current transformation matrix around a point.
        
        :param theta: An angle of rotation in radians.
        :param x: X coordinate of point.
        :param y: Y coordinate of point.'''
        ...
    
    @overload
    def draw_polyline(self, x_points: list[int], y_points: list[int], n_points: int) -> None:
        '''Draws a polyline.
        
        :param x_points: X coordinates of points.
        :param y_points: Y coordinate of points.
        :param n_points: The number of points.'''
        ...
    
    @overload
    def draw_polyline(self, x_points: list[float], y_points: list[float], n_points: int) -> None:
        '''Draws a polyline.
        
        :param x_points: X coordinates of points.
        :param y_points: Y coordinate of points.
        :param n_points: The number of points.'''
        ...
    
    @overload
    def draw_polygon(self, x_points: list[int], y_points: list[int], n_points: int) -> None:
        '''Draws a polygon.
        
        :param x_points: X coordinates of points.
        :param y_points: Y coordinate of points.
        :param n_points: The number of points.'''
        ...
    
    @overload
    def draw_polygon(self, x_points: list[float], y_points: list[float], n_points: int) -> None:
        '''Draws a poligone.
        
        :param x_points: X coordinates of points.
        :param y_points: Y coordinate of points.
        :param n_points: The number of points.'''
        ...
    
    @overload
    def fill_polygon(self, x_points: list[int], y_points: list[int], n_points: int) -> None:
        '''Fills a poligone.
        
        :param x_points: X coordinates of points.
        :param y_points: Y coordinate of points.
        :param n_points: The number of points.'''
        ...
    
    @overload
    def fill_polygon(self, x_points: list[float], y_points: list[float], n_points: int) -> None:
        '''Fills a poligone.
        
        :param x_points: X coordinates of points.
        :param y_points: Y coordinate of points.
        :param n_points: The number of points.'''
        ...
    
    def re_new(self) -> None:
        '''Reset device to initial state for whole document. Used for reseting output stream.'''
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
        '''Gets a value of margin property.
        
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
    
    def scale(self, x: float, y: float) -> None:
        '''Scales the current transformation matrix. Calls writeTransform(Transform).
        
        :param x: A scale in X axis.
        :param y: A scale in Y axis.'''
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
    
    def draw(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Draws a path.
        
        :param path: A path to be drawn.'''
        ...
    
    def fill(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Fills a path.
        
        :param path: A path to be filled.'''
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
    
    def draw_arc(self, x: float, y: float, width: float, height: float, start_angle: float, arc_angle: float) -> None:
        '''Draws an arc.
        
        :param x: X coordinate of center of the arc.
        :param y: Y coordinate of center of the arc.
        :param width: A width of circumscribed rectangle.
        :param height: A height of circumscribed rectangle.
        :param start_angle: A start angle of the arc.
        :param arc_angle: An angle of the arc.'''
        ...
    
    def draw_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        '''Draws a line segment.
        
        :param x1: X coordinate of the beginning of segment.
        :param y1: Y coordinate of the beginning of segment.
        :param x2: X coordinate of the end of segment.
        :param y2: Y coordinate of the end of segment.'''
        ...
    
    def draw_oval(self, x: float, y: float, width: float, height: float) -> None:
        '''Draws an oval.
        
        :param x: X coordinate of center of the oval.
        :param y: Y coordinate of center of the oval.
        :param width: A width of circumscribed rectangle.
        :param height: A height of circumscribed rectangle.'''
        ...
    
    def draw_rect(self, x: float, y: float, width: float, height: float) -> None:
        '''Draws a rectangle.
        
        :param x: X coordinate of upper left corner of the rectangle.
        :param y: Y coordinate of upper left corner of the rectangle.
        :param width: A width of the rectangle.
        :param height: A height of the rectangle.'''
        ...
    
    def draw_round_rect(self, x: float, y: float, width: float, height: float, arc_width: float, arc_height: float) -> None:
        '''Draws a round rectangle.
        
        :param x: X coordinate of upper left corner of the rectangle.
        :param y: Y coordinate of upper left corner of the rectangle.
        :param width: A width of the rectangle.
        :param height: A height of the rectangle.
        :param arc_width: A width of circumscribed rectangle of the arc that rounds an angle of the rectangle.
        :param arc_height: A height of circumscribed rectangle of the arc that rounds an angle of the rectangle.'''
        ...
    
    def fill_arc(self, x: float, y: float, width: float, height: float, start_angle: float, arc_angle: float) -> None:
        '''Fills an arc.
        
        :param x: X coordinate of center of the arc.
        :param y: Y coordinate of center of the arc.
        :param width: A width of circumscribed rectangle.
        :param height: A height of circumscribed rectangle.
        :param start_angle: A start angle of the arc.
        :param arc_angle: An angle of the arc.'''
        ...
    
    def fill_oval(self, x: float, y: float, width: float, height: float) -> None:
        '''Fills an oval.
        
        :param x: X coordinate of center of the oval.
        :param y: Y coordinate of center of the oval.
        :param width: A width of circumscribed rectangle.
        :param height: A height of circumscribed rectangle.'''
        ...
    
    def fill_rect(self, x: float, y: float, width: float, height: float) -> None:
        '''Fills a rectangle.
        
        :param x: X coordinate of upper left corner of the rectangle.
        :param y: Y coordinate of upper left corner of the rectangle.
        :param width: A width of the rectangle.
        :param height: A height of the rectangle.'''
        ...
    
    def fill_round_rect(self, x: float, y: float, width: float, height: float, arc_width: float, arc_height: float) -> None:
        '''Fills a round rectangle.
        
        :param x: X coordinate of upper left corner of the rectangle.
        :param y: Y coordinate of upper left corner of the rectangle.
        :param width: A width of the rectangle.
        :param height: A height of the rectangle.
        :param arc_width: A width of circumscribed rectangle of the arc that rounds an angle of the rectangle.
        :param arc_height: A height of circumscribed rectangle of the arc that rounds an angle of the rectangle.'''
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
        '''Returns or specifies current background of the page.'''
        ...
    
    @background.setter
    def background(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def opacity(self) -> float:
        '''Returns or specifies current opacity.'''
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
    def opacity_mask(self) -> aspose.pydrawing.Brush:
        '''Returns or specifies current opacity mask.'''
        ...
    
    @opacity_mask.setter
    def opacity_mask(self, value: aspose.pydrawing.Brush):
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
    
    version: str
    
    ...

class Document:
    '''A superclass for all encapsulated documents.'''
    
    def save(self, device: aspose.page.Device, options: aspose.page.SaveOptions) -> None:
        '''Saves this document to a device.
        
        :param device: An output device.
        :param options: Contains flags that specify output of errors thrown during conversion.'''
        ...
    
    ...

class ExternalFontCache:
    '''Use this class to obtain font encapsulation in a form that is accepted by :class:`Device`.'''
    
    def __init__(self):
        ...
    
    @staticmethod
    def fetch_dr_font(self, family_name: str, size_points: float, style: aspose.pydrawing.FontStyle) -> aspose.page.font.DrFont:
        '''Fetches :class:`aspose.page.font.DrFont` by font family name, size and style.
        
        :param family_name: Font family name.
        :param size_points: Font size in points (one point is 1/72 of inch).
        :param style: Font style.
        :returns: Returns DrFont'''
        ...
    
    @staticmethod
    def create_font_by_family_name(self, family_name: str, size: float, style: aspose.pydrawing.FontStyle) -> aspose.pydrawing.Font:
        '''Creates  by font family name, style and size.
        
        :param family_name: Font family name.
        :param size: Font size in points (one point is 1/72 of inch).
        :param style: Font style.
        :returns: Returns Font object.'''
        ...
    
    ...

class GraphicsFactory:
    '''This class statically creates common graphics objects.'''
    
    def __init__(self):
        ...
    
    @staticmethod
    def create_pen_by_color(self, color: aspose.pydrawing.Color) -> aspose.pydrawing.Pen:
        '''Creates a pen by color.
        
        :param color: The pen color.'''
        ...
    
    @staticmethod
    def create_pen_by_color_and_width(self, color: aspose.pydrawing.Color, width: float) -> aspose.pydrawing.Pen:
        ...
    
    @staticmethod
    def create_pen_by_brush(self, brush: aspose.pydrawing.Brush) -> aspose.pydrawing.Pen:
        '''Creates a pen by brush.
        
        :param brush: The pen brush.'''
        ...
    
    @staticmethod
    def create_pen_by_brush_and_width(self, brush: aspose.pydrawing.Brush, width: float) -> aspose.pydrawing.Pen:
        '''Creates a pen by brush and width.
        
        :param brush: The pen brush.
        :param width: The Pen width.'''
        ...
    
    @staticmethod
    def create_linear_gradient_brush_by_points(self, start: aspose.pydrawing.PointF, end: aspose.pydrawing.PointF, start_color: aspose.pydrawing.Color, end_color: aspose.pydrawing.Color) -> aspose.pydrawing.Drawing2D.LinearGradientBrush:
        '''Creates a linear gradient brush by points.
        
        :param start: The start point of the gradient.
        :param end: The end point of the gradient.
        :param start_color: The start color of the gradient.
        :param end_color: The end color of the gradient.'''
        ...
    
    @staticmethod
    def create_linear_gradient_brush_by_rect_and_mode(self, rect: aspose.pydrawing.RectangleF, start_color: aspose.pydrawing.Color, end_color: aspose.pydrawing.Color, mode: aspose.pydrawing.Drawing2D.LinearGradientMode) -> aspose.pydrawing.Drawing2D.LinearGradientBrush:
        '''Creates a linear gradient brush by rectangle and LinearGradientMode.
        
        :param rect: The bounding rectangle of the gradient.
        :param start_color: The start color of the gradient.
        :param end_color: The end color of the gradient.
        :param mode: The linear gradient mode.'''
        ...
    
    @staticmethod
    def create_linear_gradient_brush_by_rect_and_angle(self, rect: aspose.pydrawing.RectangleF, start_color: aspose.pydrawing.Color, end_color: aspose.pydrawing.Color, angle: float) -> aspose.pydrawing.Drawing2D.LinearGradientBrush:
        '''Creates a linear gradient brush by rectangle and an angle of rotation.
        
        :param rect: The bounding rectangle of the gradient.
        :param start_color: The start color of the gradient.
        :param end_color: The end color of the gradient.
        :param angle: The angle of the rotation of the gradient.'''
        ...
    
    @staticmethod
    def create_path_gradient_brush_by_points(self, points: list[aspose.pydrawing.PointF], wrap_mode: aspose.pydrawing.Drawing2D.WrapMode) -> aspose.pydrawing.Drawing2D.PathGradientBrush:
        '''Creates a path gradient brush by points and WrapMode.
        
        :param points: The points of the gradient.
        :param wrap_mode: The wrap mode of the gradient.'''
        ...
    
    @staticmethod
    def create_path_gradient_brush_by_path(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> aspose.pydrawing.Drawing2D.PathGradientBrush:
        '''Creates a path gradient brush by an object of GraphicsPath and WrapMode.
        
        :param path: The path of the gradient.'''
        ...
    
    @staticmethod
    def create_hatch_brush_by_style_and_color(self, style: aspose.pydrawing.Drawing2D.HatchStyle, color: aspose.pydrawing.Color) -> aspose.pydrawing.Drawing2D.HatchBrush:
        '''Creates a hatch brush by hatch style and a color.
        
        :param style: The hatch style.
        :param color: The foreground color of the brush.'''
        ...
    
    @staticmethod
    def create_hatch_brush_by_style_and_colors(self, style: aspose.pydrawing.Drawing2D.HatchStyle, fore_color: aspose.pydrawing.Color, back_color: aspose.pydrawing.Color) -> aspose.pydrawing.Drawing2D.HatchBrush:
        '''Creates a hatch brush by hatch style and two colors.
        
        :param style: The hatch style.
        :param fore_color: The foreground color of the brush.
        :param back_color: The background color of the brush.'''
        ...
    
    ...

class IGlyph:
    '''This interface give access to main parameters of glyphs.'''
    
    @property
    def advance_width(self) -> float:
        '''Returns advanced width of the glyph.'''
        ...
    
    @property
    def char_code(self) -> str:
        '''Returns char code of the glyph.'''
        ...
    
    @property
    def left_side_bearing(self) -> float:
        '''Returns left side bearing of the glyph.'''
        ...
    
    ...

class IMultiPageDevice:
    '''This interface contains methods for manipulating multi-paged device.'''
    
    @overload
    def open_page(self, title: str) -> bool:
        '''Makes necessary preparation of the device before page rendering.
        
        :param title: The page title.
        :returns: True if page is from requested range, otherwise false.
                  Used in devices that can render specified array of page numbers.'''
        ...
    
    @overload
    def open_page(self, width: float, height: float) -> bool:
        '''Makes necessary preparation of the device before each page rendering.
        
        :param width: A width of the page.
        :param height: A height of the page.
        :returns: Returns true if opened page has a number that falls in a range of selected page numbers and false otherwise.'''
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
    def current_page_number(self) -> int:
        '''Current page number.'''
        ...
    
    ...

class IStreamable:
    '''This interface is used for dervices that renders document to a stream.'''
    
    @property
    def output_stream(self) -> io.BytesIO:
        '''Gets or specifies an output stream.'''
        ...
    
    @output_stream.setter
    def output_stream(self, value: io.BytesIO):
        ...
    
    ...

class ITrFont:
    '''This interface gives access to main parameters of font.'''
    
    def get_char_width(self, char_value: str) -> float:
        '''Returns a width of character.
        
        :param char_value: Character.
        :returns: A width of character.'''
        ...
    
    def get_outline(self, char_value: str, x: float, y: float) -> aspose.pydrawing.Drawing2D.GraphicsPath:
        '''Returns an outline of glyph in specified location.
        
        :param char_value: Character.
        :param x: X coordinate of the character location.
        :param y: Y coordinate of the character location.
        :returns: An outline of glyph.'''
        ...
    
    @property
    def encoding(self) -> list[str]:
        '''Returns enbcoding array.'''
        ...
    
    @property
    def encoding_table(self) -> str:
        '''Returns the name of the encoding.'''
        ...
    
    @property
    def fid(self) -> int:
        '''Returns font identificator.'''
        ...
    
    @property
    def font_name(self) -> str:
        '''Returns font name.'''
        ...
    
    @property
    def font_type(self) -> int:
        '''Returns a type of font in Adobe classification.'''
        ...
    
    @property
    def native_font(self) -> aspose.pydrawing.Font:
        '''Returns System.Drawing.Font corresponding to this font.'''
        ...
    
    @property
    def size(self) -> float:
        '''Returns font size.'''
        ...
    
    @property
    def style(self) -> aspose.pydrawing.FontStyle:
        '''Returns font style.'''
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        '''Returns font transform.'''
        ...
    
    ...

class License:
    '''Provides methods to license the component.'''
    
    def __init__(self):
        '''Initializes a new instance of this class.'''
        ...
    
    @overload
    def set_license(self, license_name: str) -> None:
        '''Licenses the component.
        
        Tries to find the license in the following locations:
        
        1. Explicit path.'''
        ...
    
    @overload
    def set_license(self, stream: io.BytesIO) -> None:
        '''Licenses the component.
        
        :param stream: A stream that contains the license.
        
        Use this method to load a license from a stream.'''
        ...
    
    @property
    def embedded(self) -> bool:
        '''License number was added as embedded resource.'''
        ...
    
    @embedded.setter
    def embedded(self, value: bool):
        ...
    
    ...

class Margins:
    '''This class encapsulates top, left, bottom and right margins.'''
    
    def __init__(self, top: int, left: int, bottom: int, right: int):
        '''Initializes an instance of Margin class.
        
        :param top: Top margin.
        :param left: Left margin.
        :param bottom: Bottom margin.
        :param right: Right margin.'''
        ...
    
    def set(self, top: int, left: int, bottom: int, right: int) -> None:
        '''Specifies margins values.
        
        :param top: Top margin.
        :param left: Left margin.
        :param bottom: Bottom margin.
        :param right: Right margin.'''
        ...
    
    @property
    def top(self) -> int:
        '''Top margin.'''
        ...
    
    @top.setter
    def top(self, value: int):
        ...
    
    @property
    def left(self) -> int:
        '''Left margin.'''
        ...
    
    @left.setter
    def left(self, value: int):
        ...
    
    @property
    def bottom(self) -> int:
        '''Bottom margin.'''
        ...
    
    @bottom.setter
    def bottom(self, value: int):
        ...
    
    @property
    def right(self) -> int:
        '''Right margin.'''
        ...
    
    @right.setter
    def right(self, value: int):
        ...
    
    ...

class Metered:
    '''Provides methods to set metered key.'''
    
    def __init__(self):
        '''Initializes a new instance of this class.'''
        ...
    
    def set_metered_key(self, public_key: str, private_key: str) -> None:
        '''Sets metered public and private key.
        If you purchase metered license, when start application, this API should be called, normally, this is enough.
        However, if always fail to upload consumption data and exceed 24 hours, the license will be set to evaluation status,
        to avoid such case, you should regularly check the license status, if it is evaluation status, call this API again.
        
        :param public_key: public key
        :param private_key: private key'''
        ...
    
    @staticmethod
    def get_consumption_quantity(self) -> decimal.Decimal:
        '''Gets consumption file size
        
        :returns: consumption quantity'''
        ...
    
    @staticmethod
    def get_consumption_credit(self) -> decimal.Decimal:
        '''Gets consumption credit
        
        :returns: consumption quantity'''
        ...
    
    ...

class SaveOptions:
    '''This class contains options necessary for managing conversion process.'''
    
    @property
    def supress_errors(self) -> bool:
        '''Specifies whether errors must be suppressed or not.
        If true suppressed errors are added to  list.
        If false the first error will terminate the program.'''
        ...
    
    @supress_errors.setter
    def supress_errors(self, value: bool):
        ...
    
    @property
    def debug(self) -> bool:
        '''Specifies whether debug information must be printed to standard output stream or not.'''
        ...
    
    @debug.setter
    def debug(self, value: bool):
        ...
    
    @property
    def additional_fonts_folders(self) -> list[str]:
        '''Specifies additional folders where converter should find fonts for input document.
        Default folder are standard fonts folder where OS finds fonts for internal needs.'''
        ...
    
    @additional_fonts_folders.setter
    def additional_fonts_folders(self, value: list[str]):
        ...
    
    @property
    def jpeg_quality_level(self) -> int:
        '''The Quality category specifies the level of compression for an image.
        Available values are 0 to 100.
        The lower the number specified, the higher the compression and therefore the lower the quality of the image.
        0 value results in lowest quality image, while 100 results in highest.'''
        ...
    
    @jpeg_quality_level.setter
    def jpeg_quality_level(self, value: int):
        ...
    
    ...

class UserProperties:
    '''Special property class which allows typed properties to be set and
    returned. It also allows the hookup of two default property objects
    to be searched if this property object does not contain the property.'''
    
    def __init__(self):
        '''Initializes an empty instance of UserProperties class.'''
        ...
    
    @overload
    def set_property(self, key: str, value: str) -> object:
        '''Sets string property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: list[str]) -> object:
        '''Sets string array property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: aspose.pydrawing.Color) -> object:
        '''Sets color property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: aspose.pydrawing.Rectangle) -> object:
        '''Sets rectangle property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: aspose.page.Margins) -> object:
        '''Sets margins property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: aspose.pydrawing.Size) -> object:
        '''Sets size property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: int) -> object:
        '''Sets integer property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: float) -> object:
        '''Sets double property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: float) -> object:
        '''Sets float property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def set_property(self, key: str, value: bool) -> object:
        '''Sets boolean property value.
        
        :param key: The name of property.
        :param value: The value of property.
        :returns: A property.'''
        ...
    
    @overload
    def get_property(self, key: str) -> str:
        '''Gets string property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property(self, key: str, defValue: str) -> str:
        '''Gets string property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_string_array(self, key: str) -> list[str]:
        '''Gets string array property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_string_array(self, key: str, defValue: list[str]) -> list[str]:
        '''Gets string array property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_color(self, key: str) -> aspose.pydrawing.Color:
        '''Gets color property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_color(self, key: str, defValue: aspose.pydrawing.Color) -> aspose.pydrawing.Color:
        '''Gets color property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_rectangle(self, key: str) -> aspose.pydrawing.RectangleF:
        '''Gets rectangle property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_rectangle(self, key: str, defValue: aspose.pydrawing.RectangleF) -> aspose.pydrawing.RectangleF:
        '''Gets rectangle property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_margins(self, key: str) -> aspose.page.Margins:
        '''Gets margins property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_margins(self, key: str, defValue: aspose.page.Margins) -> aspose.page.Margins:
        '''Gets margins property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_size(self, key: str) -> aspose.pydrawing.Size:
        '''Gets size property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_size(self, key: str, defValue: aspose.pydrawing.Size) -> aspose.pydrawing.Size:
        '''Gets size property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_int(self, key: str) -> int:
        '''Gets integer property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_int(self, key: str, defValue: int) -> int:
        '''Gets integer property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_double(self, key: str) -> float:
        '''Gets double property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_double(self, key: str, defValue: float) -> float:
        '''Gets double property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_float(self, key: str) -> float:
        '''Gets float property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def get_property_float(self, key: str, defValue: float) -> float:
        '''Gets float property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    @overload
    def is_property(self, key: str) -> bool:
        '''Gets boolean property value.
        
        :param key: The name of property.
        :returns: Property value.'''
        ...
    
    @overload
    def is_property(self, key: str, defValue: bool) -> bool:
        '''Gets boolean property value. If requested property is absent, returns provided default value.
        
        :param key: The name of property.
        :param defValue: Default value of property.
        :returns: Property value.'''
        ...
    
    def property_names(self) -> Iterable[str]:
        '''Returns properties names.
        
        :returns: Enumerator of properties names.'''
        ...
    
    def print_properties(self) -> None:
        ...
    
    ...

class TextRenderingMode:
    '''This enum contains possible values for text rendering mode.'''
    
    FILL: int
    STROKE: int
    FILL_AND_STROKE: int
    NO: int

class Units:
    '''This enum contains possible values for size units.'''
    
    POINTS: int
    INCHES: int
    MILLIMETERS: int
    CENTIMETERS: int
    PERCENTS: int

