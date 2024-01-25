#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option_3 import option as option_cls
from .create_particles_every_dpm_step import create_particles_every_dpm_step as create_particles_every_dpm_step_cls
from .dpm_time_step_size import dpm_time_step_size as dpm_time_step_size_cls
from .number_of_time_steps import number_of_time_steps as number_of_time_steps_cls
from .clear_all_particles import clear_all_particles as clear_all_particles_cls
class unsteady_tracking(Group):
    """
    'unsteady_tracking' child.
    """

    fluent_name = "unsteady-tracking"

    child_names = \
        ['option', 'create_particles_every_dpm_step', 'dpm_time_step_size',
         'number_of_time_steps']

    option: option_cls = option_cls
    """
    option child of unsteady_tracking.
    """
    create_particles_every_dpm_step: create_particles_every_dpm_step_cls = create_particles_every_dpm_step_cls
    """
    create_particles_every_dpm_step child of unsteady_tracking.
    """
    dpm_time_step_size: dpm_time_step_size_cls = dpm_time_step_size_cls
    """
    dpm_time_step_size child of unsteady_tracking.
    """
    number_of_time_steps: number_of_time_steps_cls = number_of_time_steps_cls
    """
    number_of_time_steps child of unsteady_tracking.
    """
    command_names = \
        ['clear_all_particles']

    clear_all_particles: clear_all_particles_cls = clear_all_particles_cls
    """
    clear_all_particles command of unsteady_tracking.
    """
