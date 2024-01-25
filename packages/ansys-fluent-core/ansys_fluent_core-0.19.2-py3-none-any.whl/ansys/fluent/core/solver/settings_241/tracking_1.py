#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .expert_2 import expert as expert_cls
from .high_res_tracking import high_res_tracking as high_res_tracking_cls
from .max_num_steps import max_num_steps as max_num_steps_cls
from .step_size_controls import step_size_controls as step_size_controls_cls
from .track_in_absolute_frame_enabled import track_in_absolute_frame_enabled as track_in_absolute_frame_enabled_cls
class tracking(Group):
    """
    Main menu to control the time integration of the particle trajectory equations.
    """

    fluent_name = "tracking"

    child_names = \
        ['expert', 'high_res_tracking', 'max_num_steps', 'step_size_controls',
         'track_in_absolute_frame_enabled']

    expert: expert_cls = expert_cls
    """
    expert child of tracking.
    """
    high_res_tracking: high_res_tracking_cls = high_res_tracking_cls
    """
    high_res_tracking child of tracking.
    """
    max_num_steps: max_num_steps_cls = max_num_steps_cls
    """
    max_num_steps child of tracking.
    """
    step_size_controls: step_size_controls_cls = step_size_controls_cls
    """
    step_size_controls child of tracking.
    """
    track_in_absolute_frame_enabled: track_in_absolute_frame_enabled_cls = track_in_absolute_frame_enabled_cls
    """
    track_in_absolute_frame_enabled child of tracking.
    """
