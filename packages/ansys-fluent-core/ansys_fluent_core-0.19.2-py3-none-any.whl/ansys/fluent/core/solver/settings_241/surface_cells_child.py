#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .surface_3 import surface as surface_cls
from .display_3 import display as display_cls
class surface_cells_child(Group):
    """
    'child_object_type' of surface_cells.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'surface']

    name: name_cls = name_cls
    """
    name child of surface_cells_child.
    """
    surface: surface_cls = surface_cls
    """
    surface child of surface_cells_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of surface_cells_child.
    """
