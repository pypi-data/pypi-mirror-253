#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_9 import enabled as enabled_cls
from .turbulent_approximation import turbulent_approximation as turbulent_approximation_cls
class convective_heat_transfer(Group):
    """
    'convective_heat_transfer' child.
    """

    fluent_name = "convective-heat-transfer"

    child_names = \
        ['enabled', 'turbulent_approximation']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of convective_heat_transfer.
    """
    turbulent_approximation: turbulent_approximation_cls = turbulent_approximation_cls
    """
    turbulent_approximation child of convective_heat_transfer.
    """
