#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .linearization import linearization as linearization_cls
from .impl_mom_cplg_enabled import impl_mom_cplg_enabled as impl_mom_cplg_enabled_cls
from .impl_cplg_enabled import impl_cplg_enabled as impl_cplg_enabled_cls
from .linear_change_enabled import linear_change_enabled as linear_change_enabled_cls
from .reset_sources_at_timestep import reset_sources_at_timestep as reset_sources_at_timestep_cls
from .underrelaxation_factor import underrelaxation_factor as underrelaxation_factor_cls
from .time_accurate_sources_enabled import time_accurate_sources_enabled as time_accurate_sources_enabled_cls
class source_terms(Group):
    """
    'source_terms' child.
    """

    fluent_name = "source-terms"

    child_names = \
        ['linearization', 'impl_mom_cplg_enabled', 'impl_cplg_enabled',
         'linear_change_enabled', 'reset_sources_at_timestep',
         'underrelaxation_factor', 'time_accurate_sources_enabled']

    linearization: linearization_cls = linearization_cls
    """
    linearization child of source_terms.
    """
    impl_mom_cplg_enabled: impl_mom_cplg_enabled_cls = impl_mom_cplg_enabled_cls
    """
    impl_mom_cplg_enabled child of source_terms.
    """
    impl_cplg_enabled: impl_cplg_enabled_cls = impl_cplg_enabled_cls
    """
    impl_cplg_enabled child of source_terms.
    """
    linear_change_enabled: linear_change_enabled_cls = linear_change_enabled_cls
    """
    linear_change_enabled child of source_terms.
    """
    reset_sources_at_timestep: reset_sources_at_timestep_cls = reset_sources_at_timestep_cls
    """
    reset_sources_at_timestep child of source_terms.
    """
    underrelaxation_factor: underrelaxation_factor_cls = underrelaxation_factor_cls
    """
    underrelaxation_factor child of source_terms.
    """
    time_accurate_sources_enabled: time_accurate_sources_enabled_cls = time_accurate_sources_enabled_cls
    """
    time_accurate_sources_enabled child of source_terms.
    """
