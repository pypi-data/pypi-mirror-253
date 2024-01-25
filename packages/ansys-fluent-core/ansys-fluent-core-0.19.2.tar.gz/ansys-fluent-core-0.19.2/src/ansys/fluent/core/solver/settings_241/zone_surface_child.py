#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .zone_name_1 import zone_name as zone_name_cls
from .display_3 import display as display_cls
class zone_surface_child(Group):
    """
    'child_object_type' of zone_surface.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'zone_name']

    name: name_cls = name_cls
    """
    name child of zone_surface_child.
    """
    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name child of zone_surface_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of zone_surface_child.
    """
