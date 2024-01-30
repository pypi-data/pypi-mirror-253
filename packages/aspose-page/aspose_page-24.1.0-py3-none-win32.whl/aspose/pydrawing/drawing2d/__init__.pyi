import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class Blend:
    '''Defines a blend pattern for a :class:`LinearGradientBrush` object. This class cannot be inherited.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`Blend` class.'''
        ...
    
    @overload
    def __init__(self, count: int):
        '''Initializes a new instance of the :class:`Blend` class with the specified number of factors and positions.
        
        :param count: The number of elements in the :attr:`Blend.factors` and :attr:`Blend.positions` arrays.'''
        ...
    
    @property
    def factors(self) -> list[float]:
        '''Gets or sets an array of blend factors for the gradient.
        
        :returns: An array of blend factors that specify the percentages of the starting color and the ending color to be used at the corresponding position.'''
        ...
    
    @factors.setter
    def factors(self, value: list[float]):
        ...
    
    @property
    def positions(self) -> list[float]:
        '''Gets or sets an array of blend positions for the gradient.
        
        :returns: An array of blend positions that specify the percentages of distance along the gradient line.'''
        ...
    
    @positions.setter
    def positions(self, value: list[float]):
        ...
    
    ...

class ColorBlend:
    '''Defines arrays of colors and positions used for interpolating color blending in a multicolor gradient. This class cannot be inherited.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`ColorBlend` class.'''
        ...
    
    @overload
    def __init__(self, count: int):
        '''Initializes a new instance of the :class:`ColorBlend` class with the specified number of colors and positions.
        
        :param count: The number of colors and positions in this :class:`ColorBlend`.'''
        ...
    
    @property
    def colors(self) -> None:
        '''Gets or sets an array of colors that represents the colors to use at corresponding positions along a gradient.
        
        :returns: An array of  structures that represents the colors to use at corresponding positions along a gradient.'''
        ...
    
    @colors.setter
    def colors(self, value: None):
        ...
    
    @property
    def positions(self) -> list[float]:
        '''Gets or sets the positions along a gradient line.
        
        :returns: An array of values that specify percentages of distance along the gradient line.'''
        ...
    
    @positions.setter
    def positions(self, value: list[float]):
        ...
    
    ...

class HatchBrush(aspose.pydrawing.Brush):
    '''Defines a rectangular brush with a hatch style, a foreground color, and a background color. This class cannot be inherited.'''
    
    @overload
    def __init__(self, hatchstyle: aspose.pydrawing.drawing2d.HatchStyle, fore_color):
        '''Initializes a new instance of the :class:`HatchBrush` class with the specified :class:`HatchStyle` enumeration and foreground color.
        
        :param hatchstyle: One of the :class:`HatchStyle` values that represents the pattern drawn by this :class:`HatchBrush`.
        :param fore_color: The  structure that represents the color of lines drawn by this :class:`HatchBrush`.'''
        ...
    
    @overload
    def __init__(self, hatchstyle: aspose.pydrawing.drawing2d.HatchStyle, fore_color, back_color):
        '''Initializes a new instance of the :class:`HatchBrush` class with the specified :class:`HatchStyle` enumeration, foreground color, and background color.
        
        :param hatchstyle: One of the :class:`HatchStyle` values that represents the pattern drawn by this :class:`HatchBrush`.
        :param fore_color: The  structure that represents the color of lines drawn by this :class:`HatchBrush`.
        :param back_color: The  structure that represents the color of spaces between the lines drawn by this :class:`HatchBrush`.'''
        ...
    
    def clone(self) -> object:
        '''Creates an exact copy of this :class:`HatchBrush` object.
        
        :returns: The :class:`HatchBrush` this method creates, cast as an object.'''
        ...
    
    @property
    def hatch_style(self) -> aspose.pydrawing.drawing2d.HatchStyle:
        '''Gets the hatch style of this :class:`HatchBrush` object.
        
        :returns: One of the :class:`HatchStyle` values that represents the pattern of this :class:`HatchBrush`.'''
        ...
    
    @property
    def foreground_color(self) -> None:
        '''Gets the color of hatch lines drawn by this :class:`HatchBrush` object.
        
        :returns: A  structure that represents the foreground color for this :class:`HatchBrush`.'''
        ...
    
    @property
    def background_color(self) -> None:
        '''Gets the color of spaces between the hatch lines drawn by this :class:`HatchBrush` object.
        
        :returns: A  structure that represents the background color for this :class:`HatchBrush`.'''
        ...
    
    ...

class LinearGradientBrush(aspose.pydrawing.Brush):
    '''Encapsulates a :class:`aspose.pydrawing.Brush` with a linear gradient. This class cannot be inherited.'''
    
    @overload
    def __init__(self, point1, point2, color1, color2):
        '''Initializes a new instance of the :class:`LinearGradientBrush` class with the specified points and colors.
        
        :param point1: A  structure that represents the starting point of the linear gradient.
        :param point2: A  structure that represents the endpoint of the linear gradient.
        :param color1: A  structure that represents the starting color of the linear gradient.
        :param color2: A  structure that represents the ending color of the linear gradient.'''
        ...
    
    @overload
    def __init__(self, point1, point2, color1, color2):
        '''Initializes a new instance of the :class:`LinearGradientBrush` class with the specified points and colors.
        
        :param point1: A  structure that represents the starting point of the linear gradient.
        :param point2: A  structure that represents the endpoint of the linear gradient.
        :param color1: A  structure that represents the starting color of the linear gradient.
        :param color2: A  structure that represents the ending color of the linear gradient.'''
        ...
    
    @overload
    def __init__(self, rect, color1, color2, linear_gradient_mode: aspose.pydrawing.drawing2d.LinearGradientMode):
        '''Creates a new instance of the :class:`LinearGradientBrush` based on a rectangle, starting and ending colors, and an orientation mode.
        
        :param rect: A  structure that specifies the bounds of the linear gradient.
        :param color1: A  structure that represents the starting color for the gradient.
        :param color2: A  structure that represents the ending color for the gradient.
        :param linear_gradient_mode: A :class:`LinearGradientMode` enumeration element that specifies the orientation of the gradient. The orientation determines the starting and ending points of the gradient. For example,  specifies that the starting point is the upper-left corner of the rectangle and the ending point is the lower-right corner of the rectangle.'''
        ...
    
    @overload
    def __init__(self, rect, color1, color2, linear_gradient_mode: aspose.pydrawing.drawing2d.LinearGradientMode):
        '''Creates a new instance of the :class:`LinearGradientBrush` class based on a rectangle, starting and ending colors, and orientation.
        
        :param rect: A  structure that specifies the bounds of the linear gradient.
        :param color1: A  structure that represents the starting color for the gradient.
        :param color2: A  structure that represents the ending color for the gradient.
        :param linear_gradient_mode: A :class:`LinearGradientMode` enumeration element that specifies the orientation of the gradient. The orientation determines the starting and ending points of the gradient. For example,  specifies that the starting point is the upper-left corner of the rectangle and the ending point is the lower-right corner of the rectangle.'''
        ...
    
    @overload
    def __init__(self, rect, color1, color2, angle: float):
        '''Creates a new instance of the :class:`LinearGradientBrush` class based on a rectangle, starting and ending colors, and an orientation angle.
        
        :param rect: A  structure that specifies the bounds of the linear gradient.
        :param color1: A  structure that represents the starting color for the gradient.
        :param color2: A  structure that represents the ending color for the gradient.
        :param angle: The angle, measured in degrees clockwise from the x-axis, of the gradient's orientation line.'''
        ...
    
    @overload
    def __init__(self, rect, color1, color2, angle: float, is_angle_scaleable: bool):
        '''Creates a new instance of the :class:`LinearGradientBrush` class based on a rectangle, starting and ending colors, and an orientation angle.
        
        :param rect: A  structure that specifies the bounds of the linear gradient.
        :param color1: A  structure that represents the starting color for the gradient.
        :param color2: A  structure that represents the ending color for the gradient.
        :param angle: The angle, measured in degrees clockwise from the x-axis, of the gradient's orientation line.
        :param is_angle_scaleable: Set to  to specify that the angle is affected by the transform associated with this :class:`LinearGradientBrush`; otherwise, .'''
        ...
    
    @overload
    def __init__(self, rect, color1, color2, angle: float):
        '''Creates a new instance of the :class:`LinearGradientBrush` class based on a rectangle, starting and ending colors, and an orientation angle.
        
        :param rect: A  structure that specifies the bounds of the linear gradient.
        :param color1: A  structure that represents the starting color for the gradient.
        :param color2: A  structure that represents the ending color for the gradient.
        :param angle: The angle, measured in degrees clockwise from the x-axis, of the gradient's orientation line.'''
        ...
    
    @overload
    def __init__(self, rect, color1, color2, angle: float, is_angle_scaleable: bool):
        '''Creates a new instance of the :class:`LinearGradientBrush` class based on a rectangle, starting and ending colors, and an orientation angle.
        
        :param rect: A  structure that specifies the bounds of the linear gradient.
        :param color1: A  structure that represents the starting color for the gradient.
        :param color2: A  structure that represents the ending color for the gradient.
        :param angle: The angle, measured in degrees clockwise from the x-axis, of the gradient's orientation line.
        :param is_angle_scaleable: Set to  to specify that the angle is affected by the transform associated with this :class:`LinearGradientBrush`; otherwise, .'''
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float) -> None:
        '''Creates a gradient falloff based on a bell-shaped curve.
        
        :param focus: A value from 0 through 1 that specifies the center of the gradient (the point where the starting color and ending color are blended equally).'''
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float, scale: float) -> None:
        '''Creates a gradient falloff based on a bell-shaped curve.
        
        :param focus: A value from 0 through 1 that specifies the center of the gradient (the point where the gradient is composed of only the ending color).
        :param scale: A value from 0 through 1 that specifies how fast the colors falloff from the .'''
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float) -> None:
        '''Creates a linear gradient with a center color and a linear falloff to a single color on both ends.
        
        :param focus: A value from 0 through 1 that specifies the center of the gradient (the point where the gradient is composed of only the ending color).'''
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float, scale: float) -> None:
        '''Creates a linear gradient with a center color and a linear falloff to a single color on both ends.
        
        :param focus: A value from 0 through 1 that specifies the center of the gradient (the point where the gradient is composed of only the ending color).
        :param scale: A value from 0 through1 that specifies how fast the colors falloff from the starting color to  (ending color)'''
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Multiplies the :class:`Matrix` that represents the local geometric transform of this :class:`LinearGradientBrush` by the specified :class:`Matrix` by prepending the specified :class:`Matrix`.
        
        :param matrix: The :class:`Matrix` by which to multiply the geometric transform.'''
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Multiplies the :class:`Matrix` that represents the local geometric transform of this :class:`LinearGradientBrush` by the specified :class:`Matrix` in the specified order.
        
        :param matrix: The :class:`Matrix` by which to multiply the geometric transform.
        :param order: A :class:`MatrixOrder` that specifies in which order to multiply the two matrices.'''
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        '''Translates the local geometric transform by the specified dimensions. This method prepends the translation to the transform.
        
        :param dx: The value of the translation in x.
        :param dy: The value of the translation in y.'''
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Translates the local geometric transform by the specified dimensions in the specified order.
        
        :param dx: The value of the translation in x.
        :param dy: The value of the translation in y.
        :param order: The order (prepend or append) in which to apply the translation.'''
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        '''Scales the local geometric transform by the specified amounts. This method prepends the scaling matrix to the transform.
        
        :param sx: The amount by which to scale the transform in the x-axis direction.
        :param sy: The amount by which to scale the transform in the y-axis direction.'''
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Scales the local geometric transform by the specified amounts in the specified order.
        
        :param sx: The amount by which to scale the transform in the x-axis direction.
        :param sy: The amount by which to scale the transform in the y-axis direction.
        :param order: A :class:`MatrixOrder` that specifies whether to append or prepend the scaling matrix.'''
        ...
    
    @overload
    def rotate_transform(self, angle: float) -> None:
        '''Rotates the local geometric transform by the specified amount. This method prepends the rotation to the transform.
        
        :param angle: The angle of rotation.'''
        ...
    
    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Rotates the local geometric transform by the specified amount in the specified order.
        
        :param angle: The angle of rotation.
        :param order: A :class:`MatrixOrder` that specifies whether to append or prepend the rotation matrix.'''
        ...
    
    def clone(self) -> object:
        '''Creates an exact copy of this :class:`LinearGradientBrush`.
        
        :returns: The :class:`LinearGradientBrush` this method creates, cast as an object.'''
        ...
    
    def reset_transform(self) -> None:
        '''Resets the :attr:`LinearGradientBrush.transform` property to identity.'''
        ...
    
    @property
    def linear_colors(self) -> None:
        '''Gets or sets the starting and ending colors of the gradient.
        
        :returns: An array of two  structures that represents the starting and ending colors of the gradient.'''
        ...
    
    @linear_colors.setter
    def linear_colors(self, value: None):
        ...
    
    @property
    def rectangle(self) -> None:
        '''Gets a rectangular region that defines the starting and ending points of the gradient.
        
        :returns: A  structure that specifies the starting and ending points of the gradient.'''
        ...
    
    @property
    def gamma_correction(self) -> bool:
        '''Gets or sets a value indicating whether gamma correction is enabled for this :class:`LinearGradientBrush`.
        
        :returns: The value is  if gamma correction is enabled for this :class:`LinearGradientBrush`; otherwise, .'''
        ...
    
    @gamma_correction.setter
    def gamma_correction(self, value: bool):
        ...
    
    @property
    def blend(self) -> aspose.pydrawing.drawing2d.Blend:
        '''Gets or sets a :class:`Blend` that specifies positions and factors that define a custom falloff for the gradient.
        
        :returns: A :class:`Blend` that represents a custom falloff for the gradient.'''
        ...
    
    @blend.setter
    def blend(self, value: aspose.pydrawing.drawing2d.Blend):
        ...
    
    @property
    def interpolation_colors(self) -> aspose.pydrawing.drawing2d.ColorBlend:
        '''Gets or sets a :class:`ColorBlend` that defines a multicolor linear gradient.
        
        :returns: A :class:`ColorBlend` that defines a multicolor linear gradient.'''
        ...
    
    @interpolation_colors.setter
    def interpolation_colors(self, value: aspose.pydrawing.drawing2d.ColorBlend):
        ...
    
    @property
    def wrap_mode(self) -> aspose.pydrawing.drawing2d.WrapMode:
        '''Gets or sets a :class:`WrapMode` enumeration that indicates the wrap mode for this :class:`LinearGradientBrush`.
        
        :returns: A :class:`WrapMode` that specifies how fills drawn with this :class:`LinearGradientBrush` are tiled.'''
        ...
    
    @wrap_mode.setter
    def wrap_mode(self, value: aspose.pydrawing.drawing2d.WrapMode):
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.drawing2d.Matrix:
        '''Gets or sets a copy :class:`Matrix` that defines a local geometric transform for this :class:`LinearGradientBrush`.
        
        :returns: A copy of the :class:`Matrix` that defines a geometric transform that applies only to fills drawn with this :class:`LinearGradientBrush`.'''
        ...
    
    @transform.setter
    def transform(self, value: aspose.pydrawing.drawing2d.Matrix):
        ...
    
    ...

class Matrix:
    '''Encapsulates a 3-by-3 affine matrix that represents a geometric transform. This class cannot be inherited.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`Matrix` class as the identity matrix.'''
        ...
    
    @overload
    def __init__(self, m11: float, m12: float, m21: float, m22: float, dx: float, dy: float):
        '''Initializes a new instance of the :class:`Matrix` class with the specified elements.
        
        :param m11: The value in the first row and first column of the new :class:`Matrix`.
        :param m12: The value in the first row and second column of the new :class:`Matrix`.
        :param m21: The value in the second row and first column of the new :class:`Matrix`.
        :param m22: The value in the second row and second column of the new :class:`Matrix`.
        :param dx: The value in the third row and first column of the new :class:`Matrix`.
        :param dy: The value in the third row and second column of the new :class:`Matrix`.'''
        ...
    
    @overload
    def __init__(self, rect, plgpts):
        '''Initializes a new instance of the :class:`Matrix` class to the geometric transform defined by the specified rectangle and array of points.
        
        :param rect: A  structure that represents the rectangle to be transformed.
        :param plgpts: An array of three  structures that represents the points of a parallelogram to which the upper-left, upper-right, and lower-left corners of the rectangle is to be transformed. The lower-right corner of the parallelogram is implied by the first three corners.'''
        ...
    
    @overload
    def __init__(self, rect, plgpts):
        '''Initializes a new instance of the :class:`Matrix` class to the geometric transform defined by the specified rectangle and array of points.
        
        :param rect: A  structure that represents the rectangle to be transformed.
        :param plgpts: An array of three  structures that represents the points of a parallelogram to which the upper-left, upper-right, and lower-left corners of the rectangle is to be transformed. The lower-right corner of the parallelogram is implied by the first three corners.'''
        ...
    
    @overload
    def multiply(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Multiplies this :class:`Matrix` by the matrix specified in the  parameter, by prepending the specified:class:`Matrix`.
        
        :param matrix: The :class:`Matrix` by which this :class:`Matrix` is to be multiplied.'''
        ...
    
    @overload
    def multiply(self, matrix: aspose.pydrawing.drawing2d.Matrix, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Multiplies this :class:`Matrix` by the matrix specified in the  parameter, and in the order specified in the parameter.
        
        :param matrix: The :class:`Matrix` by which this :class:`Matrix` is to be multiplied.
        :param order: The :class:`MatrixOrder` that represents the order of the multiplication.'''
        ...
    
    @overload
    def translate(self, offset_x: float, offset_y: float) -> None:
        '''Applies the specified translation vector ( and) to this:class:`Matrix` by prepending the translation vector.
        
        :param offset_x: The x value by which to translate this :class:`Matrix`.
        :param offset_y: The y value by which to translate this :class:`Matrix`.'''
        ...
    
    @overload
    def translate(self, offset_x: float, offset_y: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Applies the specified translation vector to this :class:`Matrix` in the specified order.
        
        :param offset_x: The x value by which to translate this :class:`Matrix`.
        :param offset_y: The y value by which to translate this :class:`Matrix`.
        :param order: A :class:`MatrixOrder` that specifies the order (append or prepend) in which the translation is applied to this :class:`Matrix`.'''
        ...
    
    @overload
    def scale(self, scale_x: float, scale_y: float) -> None:
        '''Applies the specified scale vector to this :class:`Matrix` by prepending the scale vector.
        
        :param scale_x: The value by which to scale this :class:`Matrix` in the x-axis direction.
        :param scale_y: The value by which to scale this :class:`Matrix` in the y-axis direction.'''
        ...
    
    @overload
    def scale(self, scale_x: float, scale_y: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Applies the specified scale vector ( and) to this:class:`Matrix` using the specified order.
        
        :param scale_x: The value by which to scale this :class:`Matrix` in the x-axis direction.
        :param scale_y: The value by which to scale this :class:`Matrix` in the y-axis direction.
        :param order: A :class:`MatrixOrder` that specifies the order (append or prepend) in which the scale vector is applied to this :class:`Matrix`.'''
        ...
    
    @overload
    def rotate(self, angle: float) -> None:
        '''Prepend to this :class:`Matrix` a clockwise rotation, around the origin and by the specified angle.
        
        :param angle: The angle of the rotation, in degrees.'''
        ...
    
    @overload
    def rotate(self, angle: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Applies a clockwise rotation of an amount specified in the  parameter, around the origin (zero x and y coordinates) for this:class:`Matrix`.
        
        :param angle: The angle (extent) of the rotation, in degrees.
        :param order: A :class:`MatrixOrder` that specifies the order (append or prepend) in which the rotation is applied to this :class:`Matrix`.'''
        ...
    
    @overload
    def rotate_at(self, angle: float, point) -> None:
        '''Applies a clockwise rotation to this :class:`Matrix` around the point specified in the  parameter, and by prepending the rotation.
        
        :param angle: The angle (extent) of the rotation, in degrees.
        :param point: A  that represents the center of the rotation.'''
        ...
    
    @overload
    def rotate_at(self, angle: float, point, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Applies a clockwise rotation about the specified point to this :class:`Matrix` in the specified order.
        
        :param angle: The angle of the rotation, in degrees.
        :param point: A  that represents the center of the rotation.
        :param order: A :class:`MatrixOrder` that specifies the order (append or prepend) in which the rotation is applied.'''
        ...
    
    @overload
    def shear(self, shear_x: float, shear_y: float) -> None:
        '''Applies the specified shear vector to this :class:`Matrix` by prepending the shear transformation.
        
        :param shear_x: The horizontal shear factor.
        :param shear_y: The vertical shear factor.'''
        ...
    
    @overload
    def shear(self, shear_x: float, shear_y: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Applies the specified shear vector to this :class:`Matrix` in the specified order.
        
        :param shear_x: The horizontal shear factor.
        :param shear_y: The vertical shear factor.
        :param order: A :class:`MatrixOrder` that specifies the order (append or prepend) in which the shear is applied.'''
        ...
    
    @overload
    def transform_points(self, pts) -> None:
        '''Applies the geometric transform represented by this :class:`Matrix` to a specified array of points.
        
        :param pts: An array of  structures that represents the points to transform.'''
        ...
    
    @overload
    def transform_points(self, pts) -> None:
        '''Applies the geometric transform represented by this :class:`Matrix` to a specified array of points.
        
        :param pts: An array of  structures that represents the points to transform.'''
        ...
    
    @overload
    def transform_vectors(self, pts) -> None:
        '''Multiplies each vector in an array by the matrix. The translation elements of this matrix (third row) are ignored.
        
        :param pts: An array of  structures that represents the points to transform.'''
        ...
    
    @overload
    def transform_vectors(self, pts) -> None:
        '''Applies only the scale and rotate components of this :class:`Matrix` to the specified array of points.
        
        :param pts: An array of  structures that represents the points to transform.'''
        ...
    
    def clone(self) -> aspose.pydrawing.drawing2d.Matrix:
        '''Creates an exact copy of this :class:`Matrix`.
        
        :returns: The :class:`Matrix` that this method creates.'''
        ...
    
    def reset(self) -> None:
        '''Resets this :class:`Matrix` to have the elements of the identity matrix.'''
        ...
    
    def invert(self) -> None:
        '''Inverts this :class:`Matrix`, if it is invertible.'''
        ...
    
    def vector_transform_points(self, pts) -> None:
        '''Multiplies each vector in an array by the matrix. The translation elements of this matrix (third row) are ignored.
        
        :param pts: An array of  structures that represents the points to transform.'''
        ...
    
    @property
    def elements(self) -> list[float]:
        '''Gets an array of floating-point values that represents the elements of this :class:`Matrix`.
        
        :returns: An array of floating-point values that represents the elements of this :class:`Matrix`.'''
        ...
    
    @property
    def offset_x(self) -> float:
        '''Gets the x translation value (the dx value, or the element in the third row and first column) of this :class:`Matrix`.
        
        :returns: The x translation value of this :class:`Matrix`.'''
        ...
    
    @property
    def offset_y(self) -> float:
        '''Gets the y translation value (the dy value, or the element in the third row and second column) of this :class:`Matrix`.
        
        :returns: The y translation value of this :class:`Matrix`.'''
        ...
    
    @property
    def is_invertible(self) -> bool:
        '''Gets a value indicating whether this :class:`Matrix` is invertible.
        
        :returns: This property is  if this :class:`Matrix` is invertible; otherwise, .'''
        ...
    
    @property
    def is_identity(self) -> bool:
        '''Gets a value indicating whether this :class:`Matrix` is the identity matrix.
        
        :returns: This property is  if this :class:`Matrix` is identity; otherwise, .'''
        ...
    
    ...

class PathData:
    '''Contains the graphical data that makes up a :class:`GraphicsPath` object. This class cannot be inherited.'''
    
    def __init__(self):
        '''Initializes a new instance of the :class:`PathData` class.'''
        ...
    
    @property
    def points(self) -> None:
        '''Gets or sets an array of  structures that represents the points through which the path is constructed.
        
        :returns: An array of  objects that represents the points through which the path is constructed.'''
        ...
    
    @points.setter
    def points(self, value: None):
        ...
    
    @property
    def types(self) -> bytes:
        '''Gets or sets the types of the corresponding points in the path.
        
        :returns: An array of bytes that specify the types of the corresponding points in the path.'''
        ...
    
    @types.setter
    def types(self, value: bytes):
        ...
    
    ...

class PathGradientBrush(aspose.pydrawing.Brush):
    '''Encapsulates a :class:`aspose.pydrawing.Brush` object that fills the interior of a :class:`GraphicsPath` object with a gradient. This class cannot be inherited.'''
    
    @overload
    def __init__(self, points):
        '''Initializes a new instance of the :class:`PathGradientBrush` class with the specified points.
        
        :param points: An array of  structures that represents the points that make up the vertices of the path.'''
        ...
    
    @overload
    def __init__(self, points, wrap_mode: aspose.pydrawing.drawing2d.WrapMode):
        '''Initializes a new instance of the :class:`PathGradientBrush` class with the specified points and wrap mode.
        
        :param points: An array of  structures that represents the points that make up the vertices of the path.
        :param wrap_mode: A :class:`WrapMode` that specifies how fills drawn with this :class:`PathGradientBrush` are tiled.'''
        ...
    
    @overload
    def __init__(self, points):
        '''Initializes a new instance of the :class:`PathGradientBrush` class with the specified points.
        
        :param points: An array of  structures that represents the points that make up the vertices of the path.'''
        ...
    
    @overload
    def __init__(self, points, wrap_mode: aspose.pydrawing.drawing2d.WrapMode):
        '''Initializes a new instance of the :class:`PathGradientBrush` class with the specified points and wrap mode.
        
        :param points: An array of  structures that represents the points that make up the vertices of the path.
        :param wrap_mode: A :class:`WrapMode` that specifies how fills drawn with this :class:`PathGradientBrush` are tiled.'''
        ...
    
    @overload
    def __init__(self, path: aspose.pydrawing.drawing2d.GraphicsPath):
        '''Initializes a new instance of the :class:`PathGradientBrush` class with the specified path.
        
        :param path: The :class:`GraphicsPath` that defines the area filled by this :class:`PathGradientBrush`.'''
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float) -> None:
        '''Creates a gradient brush that changes color starting from the center of the path outward to the path's boundary. The transition from one color to another is based on a bell-shaped curve.
        
        :param focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to the path's boundary, the center color will be at its highest intensity. A value of 1 (the default) places the highest intensity at the center of the path.'''
        ...
    
    @overload
    def set_sigma_bell_shape(self, focus: float, scale: float) -> None:
        '''Creates a gradient brush that changes color starting from the center of the path outward to the path's boundary. The transition from one color to another is based on a bell-shaped curve.
        
        :param focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to the path's boundary, the center color will be at its highest intensity. A value of 1 (the default) places the highest intensity at the center of the path.
        :param scale: A value from 0 through 1 that specifies the maximum intensity of the center color that gets blended with the boundary color. A value of 1 causes the highest possible intensity of the center color, and it is the default value.'''
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float) -> None:
        '''Creates a gradient with a center color and a linear falloff to one surrounding color.
        
        :param focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to the path's boundary, the center color will be at its highest intensity. A value of 1 (the default) places the highest intensity at the center of the path.'''
        ...
    
    @overload
    def set_blend_triangular_shape(self, focus: float, scale: float) -> None:
        '''Creates a gradient with a center color and a linear falloff to each surrounding color.
        
        :param focus: A value from 0 through 1 that specifies where, along any radial from the center of the path to the path's boundary, the center color will be at its highest intensity. A value of 1 (the default) places the highest intensity at the center of the path.
        :param scale: A value from 0 through 1 that specifies the maximum intensity of the center color that gets blended with the boundary color. A value of 1 causes the highest possible intensity of the center color, and it is the default value.'''
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Updates the brush's transformation matrix with the product of brush's transformation matrix multiplied by another matrix.
        
        :param matrix: The :class:`Matrix` that will be multiplied by the brush's current transformation matrix.'''
        ...
    
    @overload
    def multiply_transform(self, matrix: aspose.pydrawing.drawing2d.Matrix, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Updates the brush's transformation matrix with the product of the brush's transformation matrix multiplied by another matrix.
        
        :param matrix: The :class:`Matrix` that will be multiplied by the brush's current transformation matrix.
        :param order: A :class:`MatrixOrder` that specifies in which order to multiply the two matrices.'''
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float) -> None:
        '''Applies the specified translation to the local geometric transform. This method prepends the translation to the transform.
        
        :param dx: The value of the translation in x.
        :param dy: The value of the translation in y.'''
        ...
    
    @overload
    def translate_transform(self, dx: float, dy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Applies the specified translation to the local geometric transform in the specified order.
        
        :param dx: The value of the translation in x.
        :param dy: The value of the translation in y.
        :param order: The order (prepend or append) in which to apply the translation.'''
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float) -> None:
        '''Scales the local geometric transform by the specified amounts. This method prepends the scaling matrix to the transform.
        
        :param sx: The transform scale factor in the x-axis direction.
        :param sy: The transform scale factor in the y-axis direction.'''
        ...
    
    @overload
    def scale_transform(self, sx: float, sy: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Scales the local geometric transform by the specified amounts in the specified order.
        
        :param sx: The transform scale factor in the x-axis direction.
        :param sy: The transform scale factor in the y-axis direction.
        :param order: A :class:`MatrixOrder` that specifies whether to append or prepend the scaling matrix.'''
        ...
    
    @overload
    def rotate_transform(self, angle: float) -> None:
        '''Rotates the local geometric transform by the specified amount. This method prepends the rotation to the transform.
        
        :param angle: The angle (extent) of rotation.'''
        ...
    
    @overload
    def rotate_transform(self, angle: float, order: aspose.pydrawing.drawing2d.MatrixOrder) -> None:
        '''Rotates the local geometric transform by the specified amount in the specified order.
        
        :param angle: The angle (extent) of rotation.
        :param order: A :class:`MatrixOrder` that specifies whether to append or prepend the rotation matrix.'''
        ...
    
    def clone(self) -> object:
        '''Creates an exact copy of this :class:`PathGradientBrush`.
        
        :returns: The :class:`PathGradientBrush` this method creates, cast as an object.'''
        ...
    
    def reset_transform(self) -> None:
        '''Resets the :attr:`PathGradientBrush.transform` property to identity.'''
        ...
    
    @property
    def center_color(self) -> None:
        '''Gets or sets the color at the center of the path gradient.
        
        :returns: A  that represents the color at the center of the path gradient.'''
        ...
    
    @center_color.setter
    def center_color(self, value: None):
        ...
    
    @property
    def surround_colors(self) -> None:
        '''Gets or sets an array of colors that correspond to the points in the path this :class:`PathGradientBrush` fills.
        
        :returns: An array of  structures that represents the colors associated with each point in the path this :class:`PathGradientBrush` fills.'''
        ...
    
    @surround_colors.setter
    def surround_colors(self, value: None):
        ...
    
    @property
    def center_point(self) -> None:
        '''Gets or sets the center point of the path gradient.
        
        :returns: A  that represents the center point of the path gradient.'''
        ...
    
    @center_point.setter
    def center_point(self, value: None):
        ...
    
    @property
    def rectangle(self) -> None:
        '''Gets a bounding rectangle for this :class:`PathGradientBrush`.
        
        :returns: A  that represents a rectangular region that bounds the path this :class:`PathGradientBrush` fills.'''
        ...
    
    @property
    def blend(self) -> aspose.pydrawing.drawing2d.Blend:
        '''Gets or sets a :class:`Blend` that specifies positions and factors that define a custom falloff for the gradient.
        
        :returns: A :class:`Blend` that represents a custom falloff for the gradient.'''
        ...
    
    @blend.setter
    def blend(self, value: aspose.pydrawing.drawing2d.Blend):
        ...
    
    @property
    def interpolation_colors(self) -> aspose.pydrawing.drawing2d.ColorBlend:
        '''Gets or sets a :class:`ColorBlend` that defines a multicolor linear gradient.
        
        :returns: A :class:`ColorBlend` that defines a multicolor linear gradient.'''
        ...
    
    @interpolation_colors.setter
    def interpolation_colors(self, value: aspose.pydrawing.drawing2d.ColorBlend):
        ...
    
    @property
    def transform(self) -> aspose.pydrawing.drawing2d.Matrix:
        '''Gets or sets a copy of the :class:`Matrix` that defines a local geometric transform for this :class:`PathGradientBrush`.
        
        :returns: A copy of the :class:`Matrix` that defines a geometric transform that applies only to fills drawn with this :class:`PathGradientBrush`.'''
        ...
    
    @transform.setter
    def transform(self, value: aspose.pydrawing.drawing2d.Matrix):
        ...
    
    @property
    def focus_scales(self) -> None:
        '''Gets or sets the focus point for the gradient falloff.
        
        :returns: A  that represents the focus point for the gradient falloff.'''
        ...
    
    @focus_scales.setter
    def focus_scales(self, value: None):
        ...
    
    @property
    def wrap_mode(self) -> aspose.pydrawing.drawing2d.WrapMode:
        '''Gets or sets a :class:`WrapMode` that indicates the wrap mode for this :class:`PathGradientBrush`.
        
        :returns: A :class:`WrapMode` that specifies how fills drawn with this :class:`PathGradientBrush` are tiled.'''
        ...
    
    @wrap_mode.setter
    def wrap_mode(self, value: aspose.pydrawing.drawing2d.WrapMode):
        ...
    
    ...

class RegionData:
    '''Encapsulates the data that makes up a :class:`aspose.pydrawing.Region` object. This class cannot be inherited.'''
    
    @property
    def data(self) -> bytes:
        '''Gets or sets an array of bytes that specify the :class:`aspose.pydrawing.Region` object.
        
        :returns: An array of bytes that specify the :class:`aspose.pydrawing.Region` object.'''
        ...
    
    @data.setter
    def data(self, value: bytes):
        ...
    
    ...

class AdjustableArrowCap(aspose.pydrawing.drawing2d.CustomLineCap):
    '''Represents an adjustable arrow-shaped line cap. This class cannot be inherited.'''
    
    @overload
    def __init__(self, width: float, height: float):
        '''Initializes a new instance of the :class:`AdjustableArrowCap` class with the specified width and height. The arrow end caps created with this constructor are always filled.
        
        :param width: The width of the arrow.
        :param height: The height of the arrow.'''
        ...
    
    @overload
    def __init__(self, width: float, height: float, is_filled: bool):
        '''Initializes a new instance of the :class:`AdjustableArrowCap` class with the specified width, height, and fill property. Whether an arrow end cap is filled depends on the argument passed to the  parameter.
        
        :param width: The width of the arrow.
        :param height: The height of the arrow.
        :param is_filled: to fill the arrow cap; otherwise, .'''
        ...
    
    @property
    def height(self) -> float:
        '''Gets or sets the height of the arrow cap.
        
        :returns: The height of the arrow cap.'''
        ...
    
    @height.setter
    def height(self, value: float):
        ...
    
    @property
    def width(self) -> float:
        '''Gets or sets the width of the arrow cap.
        
        :returns: The width, in units, of the arrow cap.'''
        ...
    
    @width.setter
    def width(self, value: float):
        ...
    
    @property
    def middle_inset(self) -> float:
        '''Gets or sets the number of units between the outline of the arrow cap and the fill.
        
        :returns: The number of units between the outline of the arrow cap and the fill of the arrow cap.'''
        ...
    
    @middle_inset.setter
    def middle_inset(self, value: float):
        ...
    
    @property
    def filled(self) -> bool:
        '''Gets or sets whether the arrow cap is filled.
        
        :returns: This property is  if the arrow cap is filled; otherwise, .'''
        ...
    
    @filled.setter
    def filled(self, value: bool):
        ...
    
    ...

class CustomLineCap:
    '''Encapsulates a custom user-defined line cap.'''
    
    @overload
    def __init__(self, fill_path: aspose.pydrawing.drawing2d.GraphicsPath, stroke_path: aspose.pydrawing.drawing2d.GraphicsPath):
        '''Initializes a new instance of the :class:`CustomLineCap` class with the specified outline and fill.
        
        :param fill_path: A :class:`GraphicsPath` object that defines the fill for the custom cap.
        :param stroke_path: A :class:`GraphicsPath` object that defines the outline of the custom cap.'''
        ...
    
    @overload
    def __init__(self, fill_path: aspose.pydrawing.drawing2d.GraphicsPath, stroke_path: aspose.pydrawing.drawing2d.GraphicsPath, base_cap: aspose.pydrawing.drawing2d.LineCap):
        '''Initializes a new instance of the :class:`CustomLineCap` class from the specified existing :class:`LineCap` enumeration with the specified outline and fill.
        
        :param fill_path: A :class:`GraphicsPath` object that defines the fill for the custom cap.
        :param stroke_path: A :class:`GraphicsPath` object that defines the outline of the custom cap.
        :param base_cap: The line cap from which to create the custom cap.'''
        ...
    
    @overload
    def __init__(self, fill_path: aspose.pydrawing.drawing2d.GraphicsPath, stroke_path: aspose.pydrawing.drawing2d.GraphicsPath, base_cap: aspose.pydrawing.drawing2d.LineCap, base_inset: float):
        '''Initializes a new instance of the :class:`CustomLineCap` class from the specified existing :class:`LineCap` enumeration with the specified outline, fill, and inset.
        
        :param fill_path: A :class:`GraphicsPath` object that defines the fill for the custom cap.
        :param stroke_path: A :class:`GraphicsPath` object that defines the outline of the custom cap.
        :param base_cap: The line cap from which to create the custom cap.
        :param base_inset: The distance between the cap and the line.'''
        ...
    
    def clone(self) -> object:
        '''Creates an exact copy of this :class:`CustomLineCap`.
        
        :returns: The :class:`CustomLineCap` this method creates, cast as an object.'''
        ...
    
    def set_stroke_caps(self, start_cap: aspose.pydrawing.drawing2d.LineCap, end_cap: aspose.pydrawing.drawing2d.LineCap) -> None:
        '''Sets the caps used to start and end lines that make up this custom cap.
        
        :param start_cap: The :class:`LineCap` enumeration used at the beginning of a line within this cap.
        :param end_cap: The :class:`LineCap` enumeration used at the end of a line within this cap.'''
        ...
    
    def get_stroke_caps(self, start_cap: aspose.pydrawing.drawing2d.LineCap, end_cap: aspose.pydrawing.drawing2d.LineCap) -> None:
        ...
    
    @property
    def stroke_join(self) -> aspose.pydrawing.drawing2d.LineJoin:
        '''Gets or sets the :class:`LineJoin` enumeration that determines how lines that compose this :class:`CustomLineCap` object are joined.
        
        :returns: The :class:`LineJoin` enumeration this :class:`CustomLineCap` object uses to join lines.'''
        ...
    
    @stroke_join.setter
    def stroke_join(self, value: aspose.pydrawing.drawing2d.LineJoin):
        ...
    
    @property
    def base_cap(self) -> aspose.pydrawing.drawing2d.LineCap:
        '''Gets or sets the :class:`LineCap` enumeration on which this :class:`CustomLineCap` is based.
        
        :returns: The :class:`LineCap` enumeration on which this :class:`CustomLineCap` is based.'''
        ...
    
    @base_cap.setter
    def base_cap(self, value: aspose.pydrawing.drawing2d.LineCap):
        ...
    
    @property
    def base_inset(self) -> float:
        '''Gets or sets the distance between the cap and the line.
        
        :returns: The distance between the beginning of the cap and the end of the line.'''
        ...
    
    @base_inset.setter
    def base_inset(self, value: float):
        ...
    
    @property
    def width_scale(self) -> float:
        '''Gets or sets the amount by which to scale this :class:`CustomLineCap` Class object with respect to the width of the :class:`aspose.pydrawing.Pen` object.
        
        :returns: The amount by which to scale the cap.'''
        ...
    
    @width_scale.setter
    def width_scale(self, value: float):
        ...
    
    ...

class GraphicsPathIterator:
    '''Provides the ability to iterate through subpaths in a :class:`GraphicsPath` and test the types of shapes contained in each subpath. This class cannot be inherited.'''
    
    def __init__(self, path: aspose.pydrawing.drawing2d.GraphicsPath):
        '''Initializes a new instance of the :class:`GraphicsPathIterator` class with the specified :class:`GraphicsPath` object.
        
        :param path: The :class:`GraphicsPath` object for which this helper class is to be initialized.'''
        ...
    
    @overload
    def next_subpath(self, start_index, end_index, is_closed: bool) -> int:
        ...
    
    @overload
    def next_subpath(self, path: aspose.pydrawing.drawing2d.GraphicsPath, is_closed: bool) -> int:
        ...
    
    @overload
    def next_marker(self, start_index, end_index) -> int:
        ...
    
    @overload
    def next_marker(self, path: aspose.pydrawing.drawing2d.GraphicsPath) -> int:
        '''This :class:`GraphicsPathIterator` object has a :class:`GraphicsPath` object associated with it. The :meth:`GraphicsPathIterator.next_marker` method increments the associated :class:`GraphicsPath` to the next marker in its path and copies all the points contained between the current marker and the next marker (or end of path) to a second :class:`GraphicsPath` object passed in to the parameter.
        
        :param path: The :class:`GraphicsPath` object to which the points will be copied.
        :returns: The number of points between this marker and the next.'''
        ...
    
    def next_path_type(self, path_type: int, start_index, end_index) -> int:
        ...
    
    def has_curve(self) -> bool:
        '''Indicates whether the path associated with this :class:`GraphicsPathIterator` contains a curve.
        
        :returns: This method returns  if the current subpath contains a curve; otherwise, .'''
        ...
    
    def rewind(self) -> None:
        '''Rewinds this :class:`GraphicsPathIterator` to the beginning of its associated path.'''
        ...
    
    def enumerate(self, points, types: bytes) -> int:
        ...
    
    def copy_data(self, points, types: bytes, start_index: int, end_index: int) -> int:
        ...
    
    @property
    def count(self) -> int:
        '''Gets the number of points in the path.
        
        :returns: The number of points in the path.'''
        ...
    
    @property
    def subpath_count(self) -> int:
        '''Gets the number of subpaths in the path.
        
        :returns: The number of subpaths in the path.'''
        ...
    
    ...

class GraphicsPath:
    '''Represents a series of connected lines and curves. This class cannot be inherited.'''
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`GraphicsPath` class with a :attr:`GraphicsPath.fill_mode` value of :attr:`FillMode.ALTERNATE`.'''
        ...
    
    @overload
    def __init__(self, fill_mode: aspose.pydrawing.drawing2d.FillMode):
        '''Initializes a new instance of the :class:`GraphicsPath` class with the specified :class:`FillMode` enumeration.
        
        :param fill_mode: The :class:`FillMode` enumeration that determines how the interior of this :class:`GraphicsPath` is filled.'''
        ...
    
    @overload
    def __init__(self, pts, types: bytes):
        '''Initializes a new instance of the :class:`GraphicsPath` array with the specified :class:`PathPointType` and  arrays.
        
        :param pts: An array of  structures that defines the coordinates of the points that make up this :class:`GraphicsPath`.
        :param types: An array of :class:`PathPointType` enumeration elements that specifies the type of each corresponding point in the  array.'''
        ...
    
    @overload
    def __init__(self, pts, types: bytes, fill_mode: aspose.pydrawing.drawing2d.FillMode):
        '''Initializes a new instance of the :class:`GraphicsPath` array with the specified :class:`PathPointType` and  arrays and with the specified :class:`FillMode` enumeration element.
        
        :param pts: An array of  structures that defines the coordinates of the points that make up this :class:`GraphicsPath`.
        :param types: An array of :class:`PathPointType` enumeration elements that specifies the type of each corresponding point in the  array.
        :param fill_mode: A :class:`FillMode` enumeration that specifies how the interiors of shapes in this :class:`GraphicsPath` are filled.'''
        ...
    
    @overload
    def __init__(self, pts, types: bytes):
        '''Initializes a new instance of the :class:`GraphicsPath` class with the specified :class:`PathPointType` and  arrays.
        
        :param pts: An array of  structures that defines the coordinates of the points that make up this :class:`GraphicsPath`.
        :param types: An array of :class:`PathPointType` enumeration elements that specifies the type of each corresponding point in the  array.'''
        ...
    
    @overload
    def __init__(self, pts, types: bytes, fill_mode: aspose.pydrawing.drawing2d.FillMode):
        '''Initializes a new instance of the :class:`GraphicsPath` class with the specified :class:`PathPointType` and  arrays and with the specified :class:`FillMode` enumeration element.
        
        :param pts: An array of  structures that defines the coordinates of the points that make up this :class:`GraphicsPath`.
        :param types: An array of :class:`PathPointType` enumeration elements that specifies the type of each corresponding point in the  array.
        :param fill_mode: A :class:`FillMode` enumeration that specifies how the interiors of shapes in this :class:`GraphicsPath` are filled.'''
        ...
    
    @overload
    def is_visible(self, x: float, y: float) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :returns: This method returns  if the specified point is contained within this :class:`GraphicsPath`; otherwise, .'''
        ...
    
    @overload
    def is_visible(self, point) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath`.
        
        :param point: A  that represents the point to test.
        :returns: This method returns  if the specified point is contained within this :class:`GraphicsPath`; otherwise, .'''
        ...
    
    @overload
    def is_visible(self, x: float, y: float, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath` in the visible clip region of the specified :class:`aspose.pydrawing.Graphics`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within this :class:`GraphicsPath`; otherwise, .'''
        ...
    
    @overload
    def is_visible(self, pt, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath`.
        
        :param pt: A  that represents the point to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within this; otherwise, .'''
        ...
    
    @overload
    def is_visible(self, x: int, y: int) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :returns: This method returns  if the specified point is contained within this :class:`GraphicsPath`; otherwise, .'''
        ...
    
    @overload
    def is_visible(self, point) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath`.
        
        :param point: A  that represents the point to test.
        :returns: This method returns  if the specified point is contained within this :class:`GraphicsPath`; otherwise, .'''
        ...
    
    @overload
    def is_visible(self, x: int, y: int, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath`, using the specified :class:`aspose.pydrawing.Graphics`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within this :class:`GraphicsPath`; otherwise, .'''
        ...
    
    @overload
    def is_visible(self, pt, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within this :class:`GraphicsPath`.
        
        :param pt: A  that represents the point to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within this :class:`GraphicsPath`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, x: float, y: float, pen: aspose.pydrawing.Pen) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :returns: This method returns  if the specified point is contained within the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, point, pen: aspose.pydrawing.Pen) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`.
        
        :param point: A  that specifies the location to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :returns: This method returns  if the specified point is contained within the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, x: float, y: float, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen` and using the specified :class:`aspose.pydrawing.Graphics`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within (under) the outline of this :class:`GraphicsPath` as drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, pt, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen` and using the specified :class:`aspose.pydrawing.Graphics`.
        
        :param pt: A  that specifies the location to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within (under) the outline of this :class:`GraphicsPath` as drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, x: int, y: int, pen: aspose.pydrawing.Pen) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :returns: This method returns  if the specified point is contained within the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, point, pen: aspose.pydrawing.Pen) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`.
        
        :param point: A  that specifies the location to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :returns: This method returns  if the specified point is contained within the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, x: int, y: int, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen` and using the specified :class:`aspose.pydrawing.Graphics`.
        
        :param x: The x-coordinate of the point to test.
        :param y: The y-coordinate of the point to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within the outline of this :class:`GraphicsPath` as drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def is_outline_visible(self, pt, pen: aspose.pydrawing.Pen, graphics: aspose.pydrawing.Graphics) -> bool:
        '''Indicates whether the specified point is contained within (under) the outline of this :class:`GraphicsPath` when drawn with the specified :class:`aspose.pydrawing.Pen` and using the specified :class:`aspose.pydrawing.Graphics`.
        
        :param pt: A  that specifies the location to test.
        :param pen: The :class:`aspose.pydrawing.Pen` to test.
        :param graphics: The :class:`aspose.pydrawing.Graphics` for which to test visibility.
        :returns: This method returns  if the specified point is contained within the outline of this :class:`GraphicsPath` as drawn with the specified :class:`aspose.pydrawing.Pen`; otherwise, .'''
        ...
    
    @overload
    def add_line(self, pt1, pt2) -> None:
        '''Appends a line segment to this :class:`GraphicsPath`.
        
        :param pt1: A  that represents the starting point of the line.
        :param pt2: A  that represents the endpoint of the line.'''
        ...
    
    @overload
    def add_line(self, x1: float, y1: float, x2: float, y2: float) -> None:
        '''Appends a line segment to this :class:`GraphicsPath`.
        
        :param x1: The x-coordinate of the starting point of the line.
        :param y1: The y-coordinate of the starting point of the line.
        :param x2: The x-coordinate of the endpoint of the line.
        :param y2: The y-coordinate of the endpoint of the line.'''
        ...
    
    @overload
    def add_line(self, pt1, pt2) -> None:
        '''Appends a line segment to this :class:`GraphicsPath`.
        
        :param pt1: A  that represents the starting point of the line.
        :param pt2: A  that represents the endpoint of the line.'''
        ...
    
    @overload
    def add_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        '''Appends a line segment to the current figure.
        
        :param x1: The x-coordinate of the starting point of the line.
        :param y1: The y-coordinate of the starting point of the line.
        :param x2: The x-coordinate of the endpoint of the line.
        :param y2: The y-coordinate of the endpoint of the line.'''
        ...
    
    @overload
    def add_lines(self, points) -> None:
        '''Appends a series of connected line segments to the end of this :class:`GraphicsPath`.
        
        :param points: An array of  structures that represents the points that define the line segments to add.'''
        ...
    
    @overload
    def add_lines(self, points) -> None:
        '''Appends a series of connected line segments to the end of this :class:`GraphicsPath`.
        
        :param points: An array of  structures that represents the points that define the line segments to add.'''
        ...
    
    @overload
    def add_arc(self, rect, start_angle: float, sweep_angle: float) -> None:
        '''Appends an elliptical arc to the current figure.
        
        :param rect: A  that represents the rectangular bounds of the ellipse from which the arc is taken.
        :param start_angle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
        :param sweep_angle: The angle between  and the end of the arc.'''
        ...
    
    @overload
    def add_arc(self, x: float, y: float, width: float, height: float, start_angle: float, sweep_angle: float) -> None:
        '''Appends an elliptical arc to the current figure.
        
        :param x: The x-coordinate of the upper-left corner of the rectangular region that defines the ellipse from which the arc is drawn.
        :param y: The y-coordinate of the upper-left corner of the rectangular region that defines the ellipse from which the arc is drawn.
        :param width: The width of the rectangular region that defines the ellipse from which the arc is drawn.
        :param height: The height of the rectangular region that defines the ellipse from which the arc is drawn.
        :param start_angle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
        :param sweep_angle: The angle between  and the end of the arc.'''
        ...
    
    @overload
    def add_arc(self, rect, start_angle: float, sweep_angle: float) -> None:
        '''Appends an elliptical arc to the current figure.
        
        :param rect: A  that represents the rectangular bounds of the ellipse from which the arc is taken.
        :param start_angle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
        :param sweep_angle: The angle between  and the end of the arc.'''
        ...
    
    @overload
    def add_arc(self, x: int, y: int, width: int, height: int, start_angle: float, sweep_angle: float) -> None:
        '''Appends an elliptical arc to the current figure.
        
        :param x: The x-coordinate of the upper-left corner of the rectangular region that defines the ellipse from which the arc is drawn.
        :param y: The y-coordinate of the upper-left corner of the rectangular region that defines the ellipse from which the arc is drawn.
        :param width: The width of the rectangular region that defines the ellipse from which the arc is drawn.
        :param height: The height of the rectangular region that defines the ellipse from which the arc is drawn.
        :param start_angle: The starting angle of the arc, measured in degrees clockwise from the x-axis.
        :param sweep_angle: The angle between  and the end of the arc.'''
        ...
    
    @overload
    def add_bezier(self, pt1, pt2, pt3, pt4) -> None:
        '''Adds a cubic Bézier curve to the current figure.
        
        :param pt1: A  that represents the starting point of the curve.
        :param pt2: A  that represents the first control point for the curve.
        :param pt3: A  that represents the second control point for the curve.
        :param pt4: A  that represents the endpoint of the curve.'''
        ...
    
    @overload
    def add_bezier(self, x1: float, y1: float, x2: float, y2: float, x3: float, y3: float, x4: float, y4: float) -> None:
        '''Adds a cubic Bézier curve to the current figure.
        
        :param x1: The x-coordinate of the starting point of the curve.
        :param y1: The y-coordinate of the starting point of the curve.
        :param x2: The x-coordinate of the first control point for the curve.
        :param y2: The y-coordinate of the first control point for the curve.
        :param x3: The x-coordinate of the second control point for the curve.
        :param y3: The y-coordinate of the second control point for the curve.
        :param x4: The x-coordinate of the endpoint of the curve.
        :param y4: The y-coordinate of the endpoint of the curve.'''
        ...
    
    @overload
    def add_bezier(self, pt1, pt2, pt3, pt4) -> None:
        '''Adds a cubic Bézier curve to the current figure.
        
        :param pt1: A  that represents the starting point of the curve.
        :param pt2: A  that represents the first control point for the curve.
        :param pt3: A  that represents the second control point for the curve.
        :param pt4: A  that represents the endpoint of the curve.'''
        ...
    
    @overload
    def add_bezier(self, x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int) -> None:
        '''Adds a cubic Bézier curve to the current figure.
        
        :param x1: The x-coordinate of the starting point of the curve.
        :param y1: The y-coordinate of the starting point of the curve.
        :param x2: The x-coordinate of the first control point for the curve.
        :param y2: The y-coordinate of the first control point for the curve.
        :param x3: The x-coordinate of the second control point for the curve.
        :param y3: The y-coordinate of the second control point for the curve.
        :param x4: The x-coordinate of the endpoint of the curve.
        :param y4: The y-coordinate of the endpoint of the curve.'''
        ...
    
    @overload
    def add_beziers(self, points) -> None:
        '''Adds a sequence of connected cubic Bézier curves to the current figure.
        
        :param points: An array of  structures that represents the points that define the curves.'''
        ...
    
    @overload
    def add_beziers(self, points) -> None:
        '''Adds a sequence of connected cubic Bézier curves to the current figure.
        
        :param points: An array of  structures that represents the points that define the curves.'''
        ...
    
    @overload
    def add_curve(self, points) -> None:
        '''Adds a spline curve to the current figure. A cardinal spline curve is used because the curve travels through each of the points in the array.
        
        :param points: An array of  structures that represents the points that define the curve.'''
        ...
    
    @overload
    def add_curve(self, points, tension: float) -> None:
        '''Adds a spline curve to the current figure.
        
        :param points: An array of  structures that represents the points that define the curve.
        :param tension: A value that specifies the amount that the curve bends between control points. Values greater than 1 produce unpredictable results.'''
        ...
    
    @overload
    def add_curve(self, points, offset: int, number_of_segments: int, tension: float) -> None:
        '''Adds a spline curve to the current figure.
        
        :param points: An array of  structures that represents the points that define the curve.
        :param offset: The index of the element in the  array that is used as the first point in the curve.
        :param number_of_segments: The number of segments used to draw the curve. A segment can be thought of as a line connecting two points.
        :param tension: A value that specifies the amount that the curve bends between control points. Values greater than 1 produce unpredictable results.'''
        ...
    
    @overload
    def add_curve(self, points) -> None:
        '''Adds a spline curve to the current figure. A cardinal spline curve is used because the curve travels through each of the points in the array.
        
        :param points: An array of  structures that represents the points that define the curve.'''
        ...
    
    @overload
    def add_curve(self, points, tension: float) -> None:
        '''Adds a spline curve to the current figure.
        
        :param points: An array of  structures that represents the points that define the curve.
        :param tension: A value that specifies the amount that the curve bends between control points. Values greater than 1 produce unpredictable results.'''
        ...
    
    @overload
    def add_curve(self, points, offset: int, number_of_segments: int, tension: float) -> None:
        '''Adds a spline curve to the current figure.
        
        :param points: An array of  structures that represents the points that define the curve.
        :param offset: The index of the element in the  array that is used as the first point in the curve.
        :param number_of_segments: A value that specifies the amount that the curve bends between control points. Values greater than 1 produce unpredictable results.
        :param tension: A value that specifies the amount that the curve bends between control points. Values greater than 1 produce unpredictable results.'''
        ...
    
    @overload
    def add_closed_curve(self, points) -> None:
        '''Adds a closed curve to this path. A cardinal spline curve is used because the curve travels through each of the points in the array.
        
        :param points: An array of  structures that represents the points that define the curve.'''
        ...
    
    @overload
    def add_closed_curve(self, points, tension: float) -> None:
        '''Adds a closed curve to this path. A cardinal spline curve is used because the curve travels through each of the points in the array.
        
        :param points: An array of  structures that represents the points that define the curve.
        :param tension: A value between from 0 through 1 that specifies the amount that the curve bends between points, with 0 being the smallest curve (sharpest corner) and 1 being the smoothest curve.'''
        ...
    
    @overload
    def add_closed_curve(self, points) -> None:
        '''Adds a closed curve to this path. A cardinal spline curve is used because the curve travels through each of the points in the array.
        
        :param points: An array of  structures that represents the points that define the curve.'''
        ...
    
    @overload
    def add_closed_curve(self, points, tension: float) -> None:
        '''Adds a closed curve to this path. A cardinal spline curve is used because the curve travels through each of the points in the array.
        
        :param points: An array of  structures that represents the points that define the curve.
        :param tension: A value between from 0 through 1 that specifies the amount that the curve bends between points, with 0 being the smallest curve (sharpest corner) and 1 being the smoothest curve.'''
        ...
    
    @overload
    def add_rectangle(self, rect) -> None:
        '''Adds a rectangle to this path.
        
        :param rect: A  that represents the rectangle to add.'''
        ...
    
    @overload
    def add_rectangle(self, rect) -> None:
        '''Adds a rectangle to this path.
        
        :param rect: A  that represents the rectangle to add.'''
        ...
    
    @overload
    def add_rectangles(self, rects) -> None:
        '''Adds a series of rectangles to this path.
        
        :param rects: An array of  structures that represents the rectangles to add.'''
        ...
    
    @overload
    def add_rectangles(self, rects) -> None:
        '''Adds a series of rectangles to this path.
        
        :param rects: An array of  structures that represents the rectangles to add.'''
        ...
    
    @overload
    def add_ellipse(self, rect) -> None:
        '''Adds an ellipse to the current path.
        
        :param rect: A  that represents the bounding rectangle that defines the ellipse.'''
        ...
    
    @overload
    def add_ellipse(self, x: float, y: float, width: float, height: float) -> None:
        '''Adds an ellipse to the current path.
        
        :param x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
        :param y: The y-coordinate of the upper left corner of the bounding rectangle that defines the ellipse.
        :param width: The width of the bounding rectangle that defines the ellipse.
        :param height: The height of the bounding rectangle that defines the ellipse.'''
        ...
    
    @overload
    def add_ellipse(self, rect) -> None:
        '''Adds an ellipse to the current path.
        
        :param rect: A  that represents the bounding rectangle that defines the ellipse.'''
        ...
    
    @overload
    def add_ellipse(self, x: int, y: int, width: int, height: int) -> None:
        '''Adds an ellipse to the current path.
        
        :param x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
        :param y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse.
        :param width: The width of the bounding rectangle that defines the ellipse.
        :param height: The height of the bounding rectangle that defines the ellipse.'''
        ...
    
    @overload
    def add_pie(self, rect, start_angle: float, sweep_angle: float) -> None:
        '''Adds the outline of a pie shape to this path.
        
        :param rect: A  that represents the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param start_angle: The starting angle for the pie section, measured in degrees clockwise from the x-axis.
        :param sweep_angle: The angle between  and the end of the pie section, measured in degrees clockwise from.'''
        ...
    
    @overload
    def add_pie(self, x: float, y: float, width: float, height: float, start_angle: float, sweep_angle: float) -> None:
        '''Adds the outline of a pie shape to this path.
        
        :param x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param width: The width of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param height: The height of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param start_angle: The starting angle for the pie section, measured in degrees clockwise from the x-axis.
        :param sweep_angle: The angle between  and the end of the pie section, measured in degrees clockwise from.'''
        ...
    
    @overload
    def add_pie(self, x: int, y: int, width: int, height: int, start_angle: float, sweep_angle: float) -> None:
        '''Adds the outline of a pie shape to this path.
        
        :param x: The x-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param y: The y-coordinate of the upper-left corner of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param width: The width of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param height: The height of the bounding rectangle that defines the ellipse from which the pie is drawn.
        :param start_angle: The starting angle for the pie section, measured in degrees clockwise from the x-axis.
        :param sweep_angle: The angle between  and the end of the pie section, measured in degrees clockwise from.'''
        ...
    
    @overload
    def add_polygon(self, points) -> None:
        '''Adds a polygon to this path.
        
        :param points: An array of  structures that defines the polygon to add.'''
        ...
    
    @overload
    def add_polygon(self, points) -> None:
        '''Adds a polygon to this path.
        
        :param points: An array of  structures that defines the polygon to add.'''
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, origin, format: aspose.pydrawing.StringFormat) -> None:
        '''Adds a text string to this path.
        
        :param s: The  to add.
        :param family: A :class:`aspose.pydrawing.FontFamily` that represents the name of the font with which the test is drawn.
        :param style: A :class:`aspose.pydrawing.FontStyle` enumeration that represents style information about the text (bold, italic, and so on). This must be cast as an integer (see the example code later in this section).
        :param em_size: The height of the em square box that bounds the character.
        :param origin: A  that represents the point where the text starts.
        :param format: A :class:`aspose.pydrawing.StringFormat` that specifies text formatting information, such as line spacing and alignment.'''
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, origin, format: aspose.pydrawing.StringFormat) -> None:
        '''Adds a text string to this path.
        
        :param s: The  to add.
        :param family: A :class:`aspose.pydrawing.FontFamily` that represents the name of the font with which the test is drawn.
        :param style: A :class:`aspose.pydrawing.FontStyle` enumeration that represents style information about the text (bold, italic, and so on). This must be cast as an integer (see the example code later in this section).
        :param em_size: The height of the em square box that bounds the character.
        :param origin: A  that represents the point where the text starts.
        :param format: A :class:`aspose.pydrawing.StringFormat` that specifies text formatting information, such as line spacing and alignment.'''
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, layout_rect, format: aspose.pydrawing.StringFormat) -> None:
        '''Adds a text string to this path.
        
        :param s: The  to add.
        :param family: A :class:`aspose.pydrawing.FontFamily` that represents the name of the font with which the test is drawn.
        :param style: A :class:`aspose.pydrawing.FontStyle` enumeration that represents style information about the text (bold, italic, and so on). This must be cast as an integer (see the example code later in this section).
        :param em_size: The height of the em square box that bounds the character.
        :param layout_rect: A  that represents the rectangle that bounds the text.
        :param format: A :class:`aspose.pydrawing.StringFormat` that specifies text formatting information, such as line spacing and alignment.'''
        ...
    
    @overload
    def add_string(self, s: str, family: aspose.pydrawing.FontFamily, style: int, em_size: float, layout_rect, format: aspose.pydrawing.StringFormat) -> None:
        '''Adds a text string to this path.
        
        :param s: The  to add.
        :param family: A :class:`aspose.pydrawing.FontFamily` that represents the name of the font with which the test is drawn.
        :param style: A :class:`aspose.pydrawing.FontStyle` enumeration that represents style information about the text (bold, italic, and so on). This must be cast as an integer (see the example code later in this section).
        :param em_size: The height of the em square box that bounds the character.
        :param layout_rect: A  that represents the rectangle that bounds the text.
        :param format: A :class:`aspose.pydrawing.StringFormat` that specifies text formatting information, such as line spacing and alignment.'''
        ...
    
    @overload
    def get_bounds(self) -> None:
        '''Returns a rectangle that bounds this :class:`GraphicsPath`.
        
        :returns: A  that represents a rectangle that bounds this :class:`GraphicsPath`.'''
        ...
    
    @overload
    def get_bounds(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Returns a rectangle that bounds this :class:`GraphicsPath` when this path is transformed by the specified :class:`Matrix`.
        
        :param matrix: The :class:`Matrix` that specifies a transformation to be applied to this path before the bounding rectangle is calculated. This path is not permanently transformed; the transformation is used only during the process of calculating the bounding rectangle.
        :returns: A  that represents a rectangle that bounds this :class:`GraphicsPath`.'''
        ...
    
    @overload
    def get_bounds(self, matrix: aspose.pydrawing.drawing2d.Matrix, pen: aspose.pydrawing.Pen) -> None:
        '''Returns a rectangle that bounds this :class:`GraphicsPath` when the current path is transformed by the specified :class:`Matrix` and drawn with the specified :class:`aspose.pydrawing.Pen`.
        
        :param matrix: The :class:`Matrix` that specifies a transformation to be applied to this path before the bounding rectangle is calculated. This path is not permanently transformed; the transformation is used only during the process of calculating the bounding rectangle.
        :param pen: The :class:`aspose.pydrawing.Pen` with which to draw the :class:`GraphicsPath`.
        :returns: A  that represents a rectangle that bounds this :class:`GraphicsPath`.'''
        ...
    
    @overload
    def flatten(self) -> None:
        '''Converts each curve in this path into a sequence of connected line segments.'''
        ...
    
    @overload
    def flatten(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Applies the specified transform and then converts each curve in this :class:`GraphicsPath` into a sequence of connected line segments.
        
        :param matrix: A :class:`Matrix` by which to transform this :class:`GraphicsPath` before flattening.'''
        ...
    
    @overload
    def flatten(self, matrix: aspose.pydrawing.drawing2d.Matrix, flatness: float) -> None:
        '''Converts each curve in this :class:`GraphicsPath` into a sequence of connected line segments.
        
        :param matrix: A :class:`Matrix` by which to transform this :class:`GraphicsPath` before flattening.
        :param flatness: Specifies the maximum permitted error between the curve and its flattened approximation. A value of 0.25 is the default. Reducing the flatness value will increase the number of line segments in the approximation.'''
        ...
    
    @overload
    def widen(self, pen: aspose.pydrawing.Pen) -> None:
        '''Adds an additional outline to the path.
        
        :param pen: A :class:`aspose.pydrawing.Pen` that specifies the width between the original outline of the path and the new outline this method creates.'''
        ...
    
    @overload
    def widen(self, pen: aspose.pydrawing.Pen, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Adds an additional outline to the :class:`GraphicsPath`.
        
        :param pen: A :class:`aspose.pydrawing.Pen` that specifies the width between the original outline of the path and the new outline this method creates.
        :param matrix: A :class:`Matrix` that specifies a transform to apply to the path before widening.'''
        ...
    
    @overload
    def widen(self, pen: aspose.pydrawing.Pen, matrix: aspose.pydrawing.drawing2d.Matrix, flatness: float) -> None:
        '''Replaces this :class:`GraphicsPath` with curves that enclose the area that is filled when this path is drawn by the specified pen.
        
        :param pen: A :class:`aspose.pydrawing.Pen` that specifies the width between the original outline of the path and the new outline this method creates.
        :param matrix: A :class:`Matrix` that specifies a transform to apply to the path before widening.
        :param flatness: A value that specifies the flatness for curves.'''
        ...
    
    @overload
    def warp(self, dest_points, src_rect) -> None:
        '''Applies a warp transform, defined by a rectangle and a parallelogram, to this :class:`GraphicsPath`.
        
        :param dest_points: An array of  structures that define a parallelogram to which the rectangle defined by  is transformed. The array can contain either three or four elements. If the array contains three elements, the lower-right corner of the parallelogram is implied by the first three points.
        :param src_rect: A  that represents the rectangle that is transformed to the parallelogram defined by .'''
        ...
    
    @overload
    def warp(self, dest_points, src_rect, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Applies a warp transform, defined by a rectangle and a parallelogram, to this :class:`GraphicsPath`.
        
        :param dest_points: An array of  structures that define a parallelogram to which the rectangle defined by  is transformed. The array can contain either three or four elements. If the array contains three elements, the lower-right corner of the parallelogram is implied by the first three points.
        :param src_rect: A  that represents the rectangle that is transformed to the parallelogram defined by .
        :param matrix: A :class:`Matrix` that specifies a geometric transform to apply to the path.'''
        ...
    
    @overload
    def warp(self, dest_points, src_rect, matrix: aspose.pydrawing.drawing2d.Matrix, warp_mode: aspose.pydrawing.drawing2d.WarpMode) -> None:
        '''Applies a warp transform, defined by a rectangle and a parallelogram, to this :class:`GraphicsPath`.
        
        :param dest_points: An array of  structures that defines a parallelogram to which the rectangle defined by  is transformed. The array can contain either three or four elements. If the array contains three elements, the lower-right corner of the parallelogram is implied by the first three points.
        :param src_rect: A  that represents the rectangle that is transformed to the parallelogram defined by .
        :param matrix: A :class:`Matrix` that specifies a geometric transform to apply to the path.
        :param warp_mode: A :class:`WarpMode` enumeration that specifies whether this warp operation uses perspective or bilinear mode.'''
        ...
    
    @overload
    def warp(self, dest_points, src_rect, matrix: aspose.pydrawing.drawing2d.Matrix, warp_mode: aspose.pydrawing.drawing2d.WarpMode, flatness: float) -> None:
        '''Applies a warp transform, defined by a rectangle and a parallelogram, to this :class:`GraphicsPath`.
        
        :param dest_points: An array of  structures that define a parallelogram to which the rectangle defined by  is transformed. The array can contain either three or four elements. If the array contains three elements, the lower-right corner of the parallelogram is implied by the first three points.
        :param src_rect: A  that represents the rectangle that is transformed to the parallelogram defined by .
        :param matrix: A :class:`Matrix` that specifies a geometric transform to apply to the path.
        :param warp_mode: A :class:`WarpMode` enumeration that specifies whether this warp operation uses perspective or bilinear mode.
        :param flatness: A value from 0 through 1 that specifies how flat the resulting path is. For more information, see the :meth:`GraphicsPath.flatten` methods.'''
        ...
    
    def clone(self) -> object:
        '''Creates an exact copy of this path.
        
        :returns: The :class:`GraphicsPath` this method creates, cast as an object.'''
        ...
    
    def reset(self) -> None:
        '''Empties the :attr:`GraphicsPath.path_points` and :attr:`GraphicsPath.path_types` arrays and sets the :class:`FillMode` to :attr:`FillMode.ALTERNATE`.'''
        ...
    
    def start_figure(self) -> None:
        '''Starts a new figure without closing the current figure. All subsequent points added to the path are added to this new figure.'''
        ...
    
    def close_figure(self) -> None:
        '''Closes the current figure and starts a new figure. If the current figure contains a sequence of connected lines and curves, the method closes the loop by connecting a line from the endpoint to the starting point.'''
        ...
    
    def close_all_figures(self) -> None:
        '''Closes all open figures in this path and starts a new figure. It closes each open figure by connecting a line from its endpoint to its starting point.'''
        ...
    
    def set_markers(self) -> None:
        '''Sets a marker on this :class:`GraphicsPath`.'''
        ...
    
    def clear_markers(self) -> None:
        '''Clears all markers from this path.'''
        ...
    
    def reverse(self) -> None:
        '''Reverses the order of points in the :attr:`GraphicsPath.path_points` array of this :class:`GraphicsPath`.'''
        ...
    
    def get_last_point(self) -> None:
        '''Gets the last point in the :attr:`GraphicsPath.path_points` array of this :class:`GraphicsPath`.
        
        :returns: A  that represents the last point in this :class:`GraphicsPath`.'''
        ...
    
    def add_path(self, adding_path: aspose.pydrawing.drawing2d.GraphicsPath, connect: bool) -> None:
        '''Appends the specified :class:`GraphicsPath` to this path.
        
        :param adding_path: The :class:`GraphicsPath` to add.
        :param connect: A Boolean value that specifies whether the first figure in the added path is part of the last figure in this path. A value of  specifies that (if possible) the first figure in the added path is part of the last figure in this path. A value of  specifies that the first figure in the added path is separate from the last figure in this path.'''
        ...
    
    def transform(self, matrix: aspose.pydrawing.drawing2d.Matrix) -> None:
        '''Applies a transform matrix to this :class:`GraphicsPath`.
        
        :param matrix: A :class:`Matrix` that represents the transformation to apply.'''
        ...
    
    @property
    def fill_mode(self) -> aspose.pydrawing.drawing2d.FillMode:
        '''Gets or sets a :class:`FillMode` enumeration that determines how the interiors of shapes in this :class:`GraphicsPath` are filled.
        
        :returns: A :class:`FillMode` enumeration that specifies how the interiors of shapes in this :class:`GraphicsPath` are filled.'''
        ...
    
    @fill_mode.setter
    def fill_mode(self, value: aspose.pydrawing.drawing2d.FillMode):
        ...
    
    @property
    def path_data(self) -> aspose.pydrawing.drawing2d.PathData:
        '''Gets a :class:`PathData` that encapsulates arrays of points () and types () for this:class:`GraphicsPath`.
        
        :returns: A :class:`PathData` that encapsulates arrays for both the points and types for this :class:`GraphicsPath`.'''
        ...
    
    @property
    def point_count(self) -> int:
        '''Gets the number of elements in the :attr:`GraphicsPath.path_points` or the :attr:`GraphicsPath.path_types` array.
        
        :returns: An integer that specifies the number of elements in the :attr:`GraphicsPath.path_points` or the :attr:`GraphicsPath.path_types` array.'''
        ...
    
    @property
    def path_types(self) -> bytes:
        '''Gets the types of the corresponding points in the :attr:`GraphicsPath.path_points` array.
        
        :returns: An array of bytes that specifies the types of the corresponding points in the path.'''
        ...
    
    @property
    def path_points(self) -> None:
        '''Gets the points in the path.
        
        :returns: An array of  objects that represent the path.'''
        ...
    
    ...

class DashStyle:
    '''Specifies the style of dashed lines drawn with a :class:`aspose.pydrawing.Pen` object.'''
    
    SOLID: int
    DASH: int
    DOT: int
    DASH_DOT: int
    DASH_DOT_DOT: int
    CUSTOM: int

class FillMode:
    '''Specifies how the interior of a closed path is filled.'''
    
    ALTERNATE: int
    WINDING: int

class HatchStyle:
    '''Specifies the different patterns available for :class:`HatchBrush` objects.'''
    
    HORIZONTAL: int
    VERTICAL: int
    FORWARD_DIAGONAL: int
    BACKWARD_DIAGONAL: int
    CROSS: int
    DIAGONAL_CROSS: int
    PERCENT05: int
    PERCENT10: int
    PERCENT20: int
    PERCENT25: int
    PERCENT30: int
    PERCENT40: int
    PERCENT50: int
    PERCENT60: int
    PERCENT70: int
    PERCENT75: int
    PERCENT80: int
    PERCENT90: int
    LIGHT_DOWNWARD_DIAGONAL: int
    LIGHT_UPWARD_DIAGONAL: int
    DARK_DOWNWARD_DIAGONAL: int
    DARK_UPWARD_DIAGONAL: int
    WIDE_DOWNWARD_DIAGONAL: int
    WIDE_UPWARD_DIAGONAL: int
    LIGHT_VERTICAL: int
    LIGHT_HORIZONTAL: int
    NARROW_VERTICAL: int
    NARROW_HORIZONTAL: int
    DARK_VERTICAL: int
    DARK_HORIZONTAL: int
    DASHED_DOWNWARD_DIAGONAL: int
    DASHED_UPWARD_DIAGONAL: int
    DASHED_HORIZONTAL: int
    DASHED_VERTICAL: int
    SMALL_CONFETTI: int
    LARGE_CONFETTI: int
    ZIG_ZAG: int
    WAVE: int
    DIAGONAL_BRICK: int
    HORIZONTAL_BRICK: int
    WEAVE: int
    PLAID: int
    DIVOT: int
    DOTTED_GRID: int
    DOTTED_DIAMOND: int
    SHINGLE: int
    TRELLIS: int
    SPHERE: int
    SMALL_GRID: int
    SMALL_CHECKER_BOARD: int
    LARGE_CHECKER_BOARD: int
    OUTLINED_DIAMOND: int
    SOLID_DIAMOND: int
    LARGE_GRID: int
    MIN: int
    MAX: int

class InterpolationMode:
    '''The :class:`InterpolationMode` enumeration specifies the algorithm that is used when images are scaled or rotated.'''
    
    INVALID: int
    DEFAULT: int
    LOW: int
    HIGH: int
    BILINEAR: int
    BICUBIC: int
    NEAREST_NEIGHBOR: int
    HIGH_QUALITY_BILINEAR: int
    HIGH_QUALITY_BICUBIC: int

class LinearGradientMode:
    '''Specifies the direction of a linear gradient.'''
    
    HORIZONTAL: int
    VERTICAL: int
    FORWARD_DIAGONAL: int
    BACKWARD_DIAGONAL: int

class LineCap:
    '''Specifies the available cap styles with which a :class:`aspose.pydrawing.Pen` object can end a line.'''
    
    FLAT: int
    SQUARE: int
    ROUND: int
    TRIANGLE: int
    NO_ANCHOR: int
    SQUARE_ANCHOR: int
    ROUND_ANCHOR: int
    DIAMOND_ANCHOR: int
    ARROW_ANCHOR: int
    CUSTOM: int
    ANCHOR_MASK: int

class LineJoin:
    '''Specifies how to join consecutive line or curve segments in a figure (subpath) contained in a :class:`GraphicsPath` object.'''
    
    MITER: int
    BEVEL: int
    ROUND: int
    MITER_CLIPPED: int

class MatrixOrder:
    '''Specifies the order for matrix transform operations.'''
    
    PREPEND: int
    APPEND: int

class PathPointType:
    '''Specifies the type of point in a :class:`GraphicsPath` object.'''
    
    START: int
    LINE: int
    BEZIER: int
    PATH_TYPE_MASK: int
    DASH_MODE: int
    PATH_MARKER: int
    CLOSE_SUBPATH: int
    BEZIER3: int

class PenAlignment:
    '''Specifies the alignment of a :class:`aspose.pydrawing.Pen` object in relation to the theoretical, zero-width line.'''
    
    CENTER: int
    INSET: int
    OUTSET: int
    LEFT: int
    RIGHT: int

class PenType:
    '''Specifies the type of fill a :class:`aspose.pydrawing.Pen` object uses to fill lines.'''
    
    SOLID_COLOR: int
    HATCH_FILL: int
    TEXTURE_FILL: int
    PATH_GRADIENT: int
    LINEAR_GRADIENT: int

class WrapMode:
    '''Specifies how a texture or gradient is tiled when it is smaller than the area being filled.'''
    
    TILE: int
    TILE_FLIP_X: int
    TILE_FLIP_Y: int
    TILE_FLIP_XY: int
    CLAMP: int

class DashCap:
    '''Specifies the type of graphic shape to use on both ends of each dash in a dashed line.'''
    
    FLAT: int
    ROUND: int
    TRIANGLE: int


class SmoothingMode:
    '''Specifies whether smoothing (antialiasing) is applied to lines and curves and the edges of filled areas.'''

    INVALID: int
    DEFAULT: int
    HIGH_SPEED: int
    HIGH_QUALITY: int
    NONE: int
    ANTI_ALIAS: int

