#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delete_1 import delete as delete_cls
from .list import list as list_cls
from .list_properties_1 import list_properties as list_properties_cls
from .make_a_copy import make_a_copy as make_a_copy_cls
from .surface_cells_child import surface_cells_child

class surface_cells(NamedObject[surface_cells_child], _CreatableNamedObjectMixin[surface_cells_child]):
    """
    'surface_cells' child.
    """

    fluent_name = "surface-cells"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of surface_cells.
    """
    list: list_cls = list_cls
    """
    list command of surface_cells.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of surface_cells.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of surface_cells.
    """
    child_object_type: surface_cells_child = surface_cells_child
    """
    child_object_type of surface_cells.
    """
