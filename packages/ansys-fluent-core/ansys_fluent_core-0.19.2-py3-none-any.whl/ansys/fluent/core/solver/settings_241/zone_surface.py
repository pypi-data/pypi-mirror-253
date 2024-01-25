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
from .zone_surface_child import zone_surface_child

class zone_surface(NamedObject[zone_surface_child], _CreatableNamedObjectMixin[zone_surface_child]):
    """
    'zone_surface' child.
    """

    fluent_name = "zone-surface"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of zone_surface.
    """
    list: list_cls = list_cls
    """
    list command of zone_surface.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of zone_surface.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of zone_surface.
    """
    child_object_type: zone_surface_child = zone_surface_child
    """
    child_object_type of zone_surface.
    """
