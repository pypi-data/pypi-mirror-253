#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .echem_heating_enabled import echem_heating_enabled as echem_heating_enabled_cls
from .zone_assignment import zone_assignment as zone_assignment_cls
from .butler_volmer_rate import butler_volmer_rate as butler_volmer_rate_cls
from .material_property import material_property as material_property_cls
class lithium_battery(Group):
    """
    'lithium_battery' child.
    """

    fluent_name = "lithium-battery"

    child_names = \
        ['echem_heating_enabled', 'zone_assignment', 'butler_volmer_rate',
         'material_property']

    echem_heating_enabled: echem_heating_enabled_cls = echem_heating_enabled_cls
    """
    echem_heating_enabled child of lithium_battery.
    """
    zone_assignment: zone_assignment_cls = zone_assignment_cls
    """
    zone_assignment child of lithium_battery.
    """
    butler_volmer_rate: butler_volmer_rate_cls = butler_volmer_rate_cls
    """
    butler_volmer_rate child of lithium_battery.
    """
    material_property: material_property_cls = material_property_cls
    """
    material_property child of lithium_battery.
    """
