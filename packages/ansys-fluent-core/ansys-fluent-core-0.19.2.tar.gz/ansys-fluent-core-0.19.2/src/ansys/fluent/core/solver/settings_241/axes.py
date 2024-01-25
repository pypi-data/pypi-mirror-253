#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .x_1 import x as x_cls
from .y_1 import y as y_cls
from .background_color import background_color as background_color_cls
class axes(Group):
    """
    Axes-properties.
    """

    fluent_name = "axes"

    child_names = \
        ['x', 'y', 'background_color']

    x: x_cls = x_cls
    """
    x child of axes.
    """
    y: y_cls = y_cls
    """
    y child of axes.
    """
    background_color: background_color_cls = background_color_cls
    """
    background_color child of axes.
    """
