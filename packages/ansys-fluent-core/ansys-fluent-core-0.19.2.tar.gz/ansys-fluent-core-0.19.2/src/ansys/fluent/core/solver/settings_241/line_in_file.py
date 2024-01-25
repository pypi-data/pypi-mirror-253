#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .pattern import pattern as pattern_cls
from .weight_1 import weight as weight_cls
from .color_1 import color as color_cls
class line_in_file(Group):
    """
    Set parameters for plot lines (file).
    """

    fluent_name = "line-in-file"

    child_names = \
        ['pattern', 'weight', 'color']

    pattern: pattern_cls = pattern_cls
    """
    pattern child of line_in_file.
    """
    weight: weight_cls = weight_cls
    """
    weight child of line_in_file.
    """
    color: color_cls = color_cls
    """
    color child of line_in_file.
    """
