#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .initialization_type import initialization_type as initialization_type_cls
from .reference_frame_3 import reference_frame as reference_frame_cls
from .defaults import defaults as defaults_cls
from .localized_turb_init import localized_turb_init as localized_turb_init_cls
from .hybrid_init_options import hybrid_init_options as hybrid_init_options_cls
from .patch import patch as patch_cls
from .open_channel_auto_init import open_channel_auto_init as open_channel_auto_init_cls
from .fmg import fmg as fmg_cls
from .initialize_1 import initialize as initialize_cls
from .compute_defaults import compute_defaults as compute_defaults_cls
from .standard_initialize import standard_initialize as standard_initialize_cls
from .hybrid_initialize import hybrid_initialize as hybrid_initialize_cls
from .list_defaults import list_defaults as list_defaults_cls
from .init_turb_vel_fluctuations import init_turb_vel_fluctuations as init_turb_vel_fluctuations_cls
from .init_flow_statistics import init_flow_statistics as init_flow_statistics_cls
from .show_iterations_sampled import show_iterations_sampled as show_iterations_sampled_cls
from .show_time_sampled import show_time_sampled as show_time_sampled_cls
from .dpm_reset import dpm_reset as dpm_reset_cls
from .lwf_reset import lwf_reset as lwf_reset_cls
from .init_lwf import init_lwf as init_lwf_cls
from .init_acoustics_options import init_acoustics_options as init_acoustics_options_cls
from .levelset_auto_init import levelset_auto_init as levelset_auto_init_cls
class initialization(Group):
    """
    Enter solution initialization menu.
    """

    fluent_name = "initialization"

    child_names = \
        ['initialization_type', 'reference_frame', 'defaults',
         'localized_turb_init', 'hybrid_init_options', 'patch',
         'open_channel_auto_init', 'fmg']

    initialization_type: initialization_type_cls = initialization_type_cls
    """
    initialization_type child of initialization.
    """
    reference_frame: reference_frame_cls = reference_frame_cls
    """
    reference_frame child of initialization.
    """
    defaults: defaults_cls = defaults_cls
    """
    defaults child of initialization.
    """
    localized_turb_init: localized_turb_init_cls = localized_turb_init_cls
    """
    localized_turb_init child of initialization.
    """
    hybrid_init_options: hybrid_init_options_cls = hybrid_init_options_cls
    """
    hybrid_init_options child of initialization.
    """
    patch: patch_cls = patch_cls
    """
    patch child of initialization.
    """
    open_channel_auto_init: open_channel_auto_init_cls = open_channel_auto_init_cls
    """
    open_channel_auto_init child of initialization.
    """
    fmg: fmg_cls = fmg_cls
    """
    fmg child of initialization.
    """
    command_names = \
        ['initialize', 'compute_defaults', 'standard_initialize',
         'hybrid_initialize', 'list_defaults', 'init_turb_vel_fluctuations',
         'init_flow_statistics', 'show_iterations_sampled',
         'show_time_sampled', 'dpm_reset', 'lwf_reset', 'init_lwf',
         'init_acoustics_options', 'levelset_auto_init']

    initialize: initialize_cls = initialize_cls
    """
    initialize command of initialization.
    """
    compute_defaults: compute_defaults_cls = compute_defaults_cls
    """
    compute_defaults command of initialization.
    """
    standard_initialize: standard_initialize_cls = standard_initialize_cls
    """
    standard_initialize command of initialization.
    """
    hybrid_initialize: hybrid_initialize_cls = hybrid_initialize_cls
    """
    hybrid_initialize command of initialization.
    """
    list_defaults: list_defaults_cls = list_defaults_cls
    """
    list_defaults command of initialization.
    """
    init_turb_vel_fluctuations: init_turb_vel_fluctuations_cls = init_turb_vel_fluctuations_cls
    """
    init_turb_vel_fluctuations command of initialization.
    """
    init_flow_statistics: init_flow_statistics_cls = init_flow_statistics_cls
    """
    init_flow_statistics command of initialization.
    """
    show_iterations_sampled: show_iterations_sampled_cls = show_iterations_sampled_cls
    """
    show_iterations_sampled command of initialization.
    """
    show_time_sampled: show_time_sampled_cls = show_time_sampled_cls
    """
    show_time_sampled command of initialization.
    """
    dpm_reset: dpm_reset_cls = dpm_reset_cls
    """
    dpm_reset command of initialization.
    """
    lwf_reset: lwf_reset_cls = lwf_reset_cls
    """
    lwf_reset command of initialization.
    """
    init_lwf: init_lwf_cls = init_lwf_cls
    """
    init_lwf command of initialization.
    """
    init_acoustics_options: init_acoustics_options_cls = init_acoustics_options_cls
    """
    init_acoustics_options command of initialization.
    """
    levelset_auto_init: levelset_auto_init_cls = levelset_auto_init_cls
    """
    levelset_auto_init command of initialization.
    """
