#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .color import color as color_cls
from .weight import weight as weight_cls
class major_gridlines(Group):
    """
    Set properties of gridlines on axis.
    """

    fluent_name = "major-gridlines"

    child_names = \
        ['color', 'weight']

    color: color_cls = color_cls
    """
    color child of major_gridlines.
    """
    weight: weight_cls = weight_cls
    """
    weight child of major_gridlines.
    """
