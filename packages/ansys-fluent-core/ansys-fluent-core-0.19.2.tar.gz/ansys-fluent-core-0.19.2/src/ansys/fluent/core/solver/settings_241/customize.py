#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .multi_level_grid import multi_level_grid as multi_level_grid_cls
from .residual_reduction import residual_reduction as residual_reduction_cls
from .cycle_count import cycle_count as cycle_count_cls
class customize(Command):
    """
    Enter FMG customization menu.
    
    Parameters
    ----------
        multi_level_grid : int
            Enter number of multigrid levels.
        residual_reduction : typing.List[real]
            Enter number of residual reduction levels.
        cycle_count : typing.List[real]
            Enter number of cycles.
    
    """

    fluent_name = "customize"

    argument_names = \
        ['multi_level_grid', 'residual_reduction', 'cycle_count']

    multi_level_grid: multi_level_grid_cls = multi_level_grid_cls
    """
    multi_level_grid argument of customize.
    """
    residual_reduction: residual_reduction_cls = residual_reduction_cls
    """
    residual_reduction argument of customize.
    """
    cycle_count: cycle_count_cls = cycle_count_cls
    """
    cycle_count argument of customize.
    """
