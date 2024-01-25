#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_name import zone_name as zone_name_cls
from .value_1 import value as value_cls
class add_zone(Command):
    """
    'add_zone' command.
    
    Parameters
    ----------
        zone_name : str
            'zone_name' child.
        value : real
            'value' child.
    
    """

    fluent_name = "add-zone"

    argument_names = \
        ['zone_name', 'value']

    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name argument of add_zone.
    """
    value: value_cls = value_cls
    """
    value argument of add_zone.
    """
