import aspose.page
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class PsDevice(aspose.page.Device):
    '''Class incapsulating PostScript composing device.'''
    
    def __init__(self, stream: io.BytesIO):
        '''Creates the new instance.
        
        :param stream: The output stream containing PostScript.'''
        ...
    
    @overload
    def rotate(self, theta: float) -> None:
        '''Applies a clockwise rotation about the origin to the current transformation matrix.
        
        :param theta: The angle of the rotation, in radians.'''
        ...
    
    @overload
    def open_page(self, title: str) -> bool:
        '''Starts a new page with the specifies title.
        
        :param title: The title.
        :returns: ``True`` if started page is to be output (it's number is contained in PageNumbers save options).
                  ``False``, otherwise.'''
        ...
    
    @overload
    def open_page(self, width: float, height: float) -> bool:
        '''Starts a new page with the specified width and height.
        
        :param width: The width of the page.
        :param height: The height of the page.
        :returns: ``True`` if started page is to be output (it's number is contained in PageNumbers save options).
                  ``False``, otherwise.'''
        ...
    
    @overload
    def set_hyperlink_target(self, target_uri: str) -> None:
        '''Sets the hyperlink with an external URI as its target.
        
        :param target_uri: The target external URI.'''
        ...
    
    @overload
    def set_hyperlink_target(self, target_page_number: int) -> None:
        '''Sets the hyperlink with a page number as its target.
        
        :param target_page_number: The target page number.'''
        ...
    
    @overload
    def add_outline(self, outline_level: int, description: str) -> None:
        '''Adds an outline item with the last object as its target.
        
        :param outline_level: The outline level.
        :param description: The item description.'''
        ...
    
    @overload
    def add_outline(self, origin: aspose.pydrawing.PointF, outline_level: int, description: str) -> None:
        '''Adds an outline item with the origin point as its target.
        
        :param origin: The target origin.
        :param outline_level: The outline level.
        :param description: The item description.'''
        ...
    
    def re_new(self) -> None:
        '''Sets the devices to the initial state.'''
        ...
    
    def create(self) -> aspose.page.Device:
        '''Creates a new instance of the device based on this device instance.
        Writes this device graphics state, i.e. creates  instance(s)
        with corresponding RenderTransform and Clip properties.
        
        :returns: The new device instance.'''
        ...
    
    def set_transform(self, transform: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Sets the current transformation matrix.
        
        :param transform: The new transformation matrix.'''
        ...
    
    def get_transform(self) -> aspose.pydrawing.Drawing2D.Matrix:
        '''Returns the current transformation matrix.
        
        :returns: The current transformation matrix.'''
        ...
    
    def transform(self, transform: aspose.pydrawing.Drawing2D.Matrix) -> None:
        '''Multiplies the current transformation matrix by the specified .
        
        :param transform: The matrix by which the current transformation matrix is to be multiplied.'''
        ...
    
    def translate(self, x: float, y: float) -> None:
        '''Applies the specified translation vector to the current transformation matrix.
        
        :param x: The x offset.
        :param y: The y offset.'''
        ...
    
    def scale(self, x: float, y: float) -> None:
        '''Applies the specified scale vector to the current transformation matrix.
        
        :param x: The x scale factor.
        :param y: The y scale factor.'''
        ...
    
    def shear(self, shx: float, shy: float) -> None:
        '''Applies the specified shear vector to the current transformation matrix.
        
        :param shx: The x shear factor.
        :param shy: The y shear factor.'''
        ...
    
    def set_clip(self, clip_path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Adds the specified path to the current clip path.
        
        :param clip_path: The clip path to be added.'''
        ...
    
    def draw(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Draws the specified path.
        
        :param path: The path to draw.'''
        ...
    
    def fill(self, path: aspose.pydrawing.Drawing2D.GraphicsPath) -> None:
        '''Fills the specified path.
        
        :param path: The path to fill.'''
        ...
    
    def draw_string(self, str: str, x: float, y: float) -> None:
        '''Draws a string at the specified position.
        
        :param str: The text to be drawn.
        :param x: The x-coordinate of the string position.
        :param y: The y-coordinate of the string position.'''
        ...
    
    def start_document(self) -> None:
        '''Starts the document.'''
        ...
    
    def end_document(self) -> None:
        '''Accomplishes the document.'''
        ...
    
    def dispose(self) -> None:
        '''Disposes this device instance. Finalizes this device instance graphics state,
        i.e. switches APS composing context to the  of the level higher then this
        device's graphics state .'''
        ...
    
    def reset(self) -> None:
        '''Resets the device.'''
        ...
    
    def init_page_numbers(self) -> None:
        '''Initializes numbers of pages to output.'''
        ...
    
    def close_page(self) -> None:
        '''Accomplishes the page.'''
        ...
    
    def update_page_parameters(self, device: aspose.page.IMultiPageDevice) -> None:
        '''Updates the current page parameters.
        
        :param device: The multipage device.'''
        ...
    
    def open_partition(self) -> None:
        '''Starts a new document partition.'''
        ...
    
    def close_partition(self) -> None:
        '''Accomplished the document partition.'''
        ...
    
    @property
    def size(self) -> aspose.pydrawing.Size:
        '''Gets/sets the device media size.'''
        ...
    
    @size.setter
    def size(self, value: aspose.pydrawing.Size):
        ...
    
    @property
    def background(self) -> aspose.pydrawing.Color:
        '''Gets/sets the background color.'''
        ...
    
    @background.setter
    def background(self, value: aspose.pydrawing.Color):
        ...
    
    @property
    def opacity(self) -> float:
        '''Gets/sets the opacity.'''
        ...
    
    @opacity.setter
    def opacity(self, value: float):
        ...
    
    @property
    def stroke(self) -> aspose.pydrawing.Pen:
        '''Gets/sets the stroke for drawing paths.'''
        ...
    
    @stroke.setter
    def stroke(self, value: aspose.pydrawing.Pen):
        ...
    
    @property
    def paint(self) -> aspose.pydrawing.Brush:
        '''Gets/sets the brush for filling paths.'''
        ...
    
    @paint.setter
    def paint(self, value: aspose.pydrawing.Brush):
        ...
    
    @property
    def opacity_mask(self) -> aspose.pydrawing.Brush:
        '''Gets/sets the brush for opacity mask. The mask applies over Paint or Strike.'''
        ...
    
    @opacity_mask.setter
    def opacity_mask(self, value: aspose.pydrawing.Brush):
        ...
    
    @property
    def current_page_number(self) -> int:
        '''Returns the absolute number of the current page withint the document.'''
        ...
    
    @property
    def current_relative_page_number(self) -> int:
        '''Returns the number of the current page within the current partititon.'''
        ...
    
    ...

