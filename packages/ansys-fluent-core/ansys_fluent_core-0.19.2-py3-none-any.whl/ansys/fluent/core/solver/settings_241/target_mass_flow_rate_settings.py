#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .under_relaxation_factor import under_relaxation_factor as under_relaxation_factor_cls
from .verbosity_6 import verbosity as verbosity_cls
class target_mass_flow_rate_settings(Group):
    """
    Enter the targeted mass flow rate setting menu.
    """

    fluent_name = "target-mass-flow-rate-settings"

    child_names = \
        ['under_relaxation_factor', 'verbosity']

    under_relaxation_factor: under_relaxation_factor_cls = under_relaxation_factor_cls
    """
    under_relaxation_factor child of target_mass_flow_rate_settings.
    """
    verbosity: verbosity_cls = verbosity_cls
    """
    verbosity child of target_mass_flow_rate_settings.
    """
