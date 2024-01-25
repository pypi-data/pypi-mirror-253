#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_21 import enabled as enabled_cls
from .sampling_interval import sampling_interval as sampling_interval_cls
from .flow_shear_stresses import flow_shear_stresses as flow_shear_stresses_cls
from .flow_heat_fluxes import flow_heat_fluxes as flow_heat_fluxes_cls
from .wall_statistics import wall_statistics as wall_statistics_cls
from .force_statistics import force_statistics as force_statistics_cls
from .dpm_variables import dpm_variables as dpm_variables_cls
from .species_list import species_list as species_list_cls
from .statistics_mixture_fraction import statistics_mixture_fraction as statistics_mixture_fraction_cls
from .statistics_reaction_progress import statistics_reaction_progress as statistics_reaction_progress_cls
from .enable_custom_field_functions import enable_custom_field_functions as enable_custom_field_functions_cls
from .custom_field_functions import custom_field_functions as custom_field_functions_cls
class data_sampling(Group):
    """
    Enter data sampling menu.
    """

    fluent_name = "data-sampling"

    child_names = \
        ['enabled', 'sampling_interval', 'flow_shear_stresses',
         'flow_heat_fluxes', 'wall_statistics', 'force_statistics',
         'dpm_variables', 'species_list', 'statistics_mixture_fraction',
         'statistics_reaction_progress', 'enable_custom_field_functions',
         'custom_field_functions']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of data_sampling.
    """
    sampling_interval: sampling_interval_cls = sampling_interval_cls
    """
    sampling_interval child of data_sampling.
    """
    flow_shear_stresses: flow_shear_stresses_cls = flow_shear_stresses_cls
    """
    flow_shear_stresses child of data_sampling.
    """
    flow_heat_fluxes: flow_heat_fluxes_cls = flow_heat_fluxes_cls
    """
    flow_heat_fluxes child of data_sampling.
    """
    wall_statistics: wall_statistics_cls = wall_statistics_cls
    """
    wall_statistics child of data_sampling.
    """
    force_statistics: force_statistics_cls = force_statistics_cls
    """
    force_statistics child of data_sampling.
    """
    dpm_variables: dpm_variables_cls = dpm_variables_cls
    """
    dpm_variables child of data_sampling.
    """
    species_list: species_list_cls = species_list_cls
    """
    species_list child of data_sampling.
    """
    statistics_mixture_fraction: statistics_mixture_fraction_cls = statistics_mixture_fraction_cls
    """
    statistics_mixture_fraction child of data_sampling.
    """
    statistics_reaction_progress: statistics_reaction_progress_cls = statistics_reaction_progress_cls
    """
    statistics_reaction_progress child of data_sampling.
    """
    enable_custom_field_functions: enable_custom_field_functions_cls = enable_custom_field_functions_cls
    """
    enable_custom_field_functions child of data_sampling.
    """
    custom_field_functions: custom_field_functions_cls = custom_field_functions_cls
    """
    custom_field_functions child of data_sampling.
    """
