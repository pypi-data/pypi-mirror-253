#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enable_4 import enable as enable_cls
from .zone_name_5 import zone_name as zone_name_cls
class inlet_temperature_for_operating_density(Group):
    """
    Enable/disable non-zero operating density computed from inlet temperature.
    """

    fluent_name = "inlet-temperature-for-operating-density"

    child_names = \
        ['enable', 'zone_name']

    enable: enable_cls = enable_cls
    """
    enable child of inlet_temperature_for_operating_density.
    """
    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name child of inlet_temperature_for_operating_density.
    """
