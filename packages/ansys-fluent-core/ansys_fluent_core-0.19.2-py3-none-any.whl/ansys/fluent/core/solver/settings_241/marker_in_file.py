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
class marker_in_file(Group):
    """
    Set parameters for data markers (file).
    """

    fluent_name = "marker-in-file"

    child_names = \
        ['symbol', 'size', 'color']

    symbol: symbol_cls = symbol_cls
    """
    symbol child of marker_in_file.
    """
    size: size_cls = size_cls
    """
    size child of marker_in_file.
    """
    color: color_cls = color_cls
    """
    color child of marker_in_file.
    """
