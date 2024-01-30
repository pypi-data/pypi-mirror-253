import aspose.page
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class PdfDevice(aspose.page.Device):
    '''Class incapsulating image composing device.'''
    
    @overload
    def __init__(self, stream: io.BytesIO):
        '''Creates the new instance.
        
        :param stream: The output stream containing PDF.'''
        ...
    
    @overload
    def __init__(self, stream: io.BytesIO, page_size: aspose.pydrawing.Size):
        '''Creates the new instance with specified media size.
        
        :param stream: The output stream containing PDF.
        :param page_size: The size of the device output media.'''
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

class PdfEncryptionDetails:
    '''Contains details for a pdf encryption.'''
    
    def __init__(self, user_password: str, owner_password: str, permissions: int, encryption_algorithm: aspose.page.xps.presentation.pdf.PdfEncryptionAlgorithm):
        '''Initializes a new instance of the  class.
        
        :param user_password: The user password.
        :param owner_password: The owner password.
        :param permissions: The permissions.
        :param encryption_algorithm: The encryption algorithm.'''
        ...
    
    @property
    def user_password(self) -> str:
        '''Gets or sets the User password.
        
        Opening the document with the correct user password (or opening a document
        that does not have a user password) allows additional operations to be
        performed according to the user access permissions specified in the document’s
        encryption dictionary.'''
        ...
    
    @user_password.setter
    def user_password(self, value: str):
        ...
    
    @property
    def owner_password(self) -> str:
        '''Gets or sets the Owner password.
        
        Opening the document with the correct owner password (assuming it is not the
        same as the user password) allows full (owner) access to the document. This
        unlimited access includes the ability to change the document’s passwords and
        access permissions.'''
        ...
    
    @owner_password.setter
    def owner_password(self, value: str):
        ...
    
    @property
    def permissions(self) -> int:
        '''Gets or sets the permissions.'''
        ...
    
    @permissions.setter
    def permissions(self, value: int):
        ...
    
    @property
    def encryption_algorithm(self) -> aspose.page.xps.presentation.pdf.PdfEncryptionAlgorithm:
        '''Gets or sets the encryption mode.'''
        ...
    
    @encryption_algorithm.setter
    def encryption_algorithm(self, value: aspose.page.xps.presentation.pdf.PdfEncryptionAlgorithm):
        ...
    
    ...

class PdfSaveOptions(aspose.page.SaveOptions):
    '''Class for XPS-as-PDF saving options.'''
    
    def __init__(self):
        '''Creates new instance of options.'''
        ...
    
    @property
    def page_numbers(self) -> list[int]:
        '''Gets/sets the array of numbers of pages to convert.'''
        ...
    
    @page_numbers.setter
    def page_numbers(self, value: list[int]):
        ...
    
    @property
    def outline_tree_height(self) -> int:
        '''Specifies the height of the document outline tree to save.
        0 - the outline tree will not be converted,
        1 - only the first level outline items will be converted,
        ans so on.
        Default is 10.'''
        ...
    
    @outline_tree_height.setter
    def outline_tree_height(self, value: int):
        ...
    
    @property
    def outline_tree_expansion_level(self) -> int:
        '''Specifies up to what level the document outline should be expanded when the PDF file is opened in a viewer.
        1 - only the first level outline items are shown,
        2 - only the first and second level outline items are shown,
        and so on.
        Default is 1.'''
        ...
    
    @outline_tree_expansion_level.setter
    def outline_tree_expansion_level(self, value: int):
        ...
    
    @property
    def text_compression(self) -> aspose.page.xps.presentation.pdf.PdfTextCompression:
        '''Specifies compression type to be used for all content streams except images.
        Default is :attr:`PdfTextCompression.FLATE`.'''
        ...
    
    @text_compression.setter
    def text_compression(self, value: aspose.page.xps.presentation.pdf.PdfTextCompression):
        ...
    
    @property
    def image_compression(self) -> aspose.page.xps.presentation.pdf.PdfImageCompression:
        '''Specifies compression type to be used for all images in the document.
        Default is :attr:`PdfImageCompression.AUTO`.'''
        ...
    
    @image_compression.setter
    def image_compression(self, value: aspose.page.xps.presentation.pdf.PdfImageCompression):
        ...
    
    @property
    def encryption_details(self) -> aspose.page.xps.presentation.pdf.PdfEncryptionDetails:
        '''Gets or sets a encryption details. If not set, then no encryption will be performed.'''
        ...
    
    @encryption_details.setter
    def encryption_details(self, value: aspose.page.xps.presentation.pdf.PdfEncryptionDetails):
        ...
    
    ...

class PdfEncryptionAlgorithm:
    '''Encryption mode enum. Describe using algorithm and key length.
    This enum is extended in order to be able to further increase functionality.
    This enum implements "Base-to-Core" pattern.'''
    
    RC4_40: int
    RC4_128: int

class PdfImageCompression:
    '''Specifies the type of compression applied to images in the PDF file.'''
    
    AUTO: int
    NONE: int
    RLE: int
    FLATE: int
    LZW_BASELINE_PREDICTOR: int
    LZW_OPTIMIZED_PREDICTOR: int
    JPEG: int

class PdfTextCompression:
    '''Specifies a type of compression applied to all contents in the PDF file except images.'''
    
    NONE: int
    RLE: int
    LZW: int
    FLATE: int

