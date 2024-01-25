#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .randomize_every_iteration import randomize_every_iteration as randomize_every_iteration_cls
from .randomize_every_timestep import randomize_every_timestep as randomize_every_timestep_cls
from .tracking_statistics_format import tracking_statistics_format as tracking_statistics_format_cls
from .verbosity_1 import verbosity as verbosity_cls
class expert(Group):
    """
    Menu containing not frequently used (expert level) settings.
    """

    fluent_name = "expert"

    child_names = \
        ['randomize_every_iteration', 'randomize_every_timestep',
         'tracking_statistics_format', 'verbosity']

    randomize_every_iteration: randomize_every_iteration_cls = randomize_every_iteration_cls
    """
    randomize_every_iteration child of expert.
    """
    randomize_every_timestep: randomize_every_timestep_cls = randomize_every_timestep_cls
    """
    randomize_every_timestep child of expert.
    """
    tracking_statistics_format: tracking_statistics_format_cls = tracking_statistics_format_cls
    """
    tracking_statistics_format child of expert.
    """
    verbosity: verbosity_cls = verbosity_cls
    """
    verbosity child of expert.
    """
