#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .symbol import symbol as symbol_cls
from .size import size as size_cls
from .color_1 import color as color_cls
class marker(Group):
    """
    Set parameters for data markers.
    """

    fluent_name = "marker"

    child_names = \
        ['symbol', 'size', 'color']

    symbol: symbol_cls = symbol_cls
    """
    symbol child of marker.
    """
    size: size_cls = size_cls
    """
    size child of marker.
    """
    color: color_cls = color_cls
    """
    color child of marker.
    """
