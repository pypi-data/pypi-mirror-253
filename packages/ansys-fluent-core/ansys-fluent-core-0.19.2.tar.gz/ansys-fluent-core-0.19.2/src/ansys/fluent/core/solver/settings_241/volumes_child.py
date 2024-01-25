#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .type_4 import type as type_cls
from .boundaries import boundaries as boundaries_cls
from .locations import locations as locations_cls
class volumes_child(Group):
    """
    'child_object_type' of volumes.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'type', 'boundaries', 'locations']

    name: name_cls = name_cls
    """
    name child of volumes_child.
    """
    type: type_cls = type_cls
    """
    type child of volumes_child.
    """
    boundaries: boundaries_cls = boundaries_cls
    """
    boundaries child of volumes_child.
    """
    locations: locations_cls = locations_cls
    """
    locations child of volumes_child.
    """
