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
from .point_surface_child import point_surface_child

class point_surface(NamedObject[point_surface_child], _CreatableNamedObjectMixin[point_surface_child]):
    """
    'point_surface' child.
    """

    fluent_name = "point-surface"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of point_surface.
    """
    list: list_cls = list_cls
    """
    list command of point_surface.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of point_surface.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of point_surface.
    """
    child_object_type: point_surface_child = point_surface_child
    """
    child_object_type of point_surface.
    """
