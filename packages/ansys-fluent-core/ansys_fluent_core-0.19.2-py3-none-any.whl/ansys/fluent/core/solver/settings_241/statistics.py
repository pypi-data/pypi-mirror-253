#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .reset_statistics import reset_statistics as reset_statistics_cls
from .statistics_controls import statistics_controls as statistics_controls_cls
class statistics(Group):
    """
    Enter the statistics menu, where you can set up the sampling of the fluid density field during the calculation.
    """

    fluent_name = "statistics"

    child_names = \
        ['reset_statistics']

    reset_statistics: reset_statistics_cls = reset_statistics_cls
    """
    reset_statistics child of statistics.
    """
    command_names = \
        ['statistics_controls']

    statistics_controls: statistics_controls_cls = statistics_controls_cls
    """
    statistics_controls command of statistics.
    """
