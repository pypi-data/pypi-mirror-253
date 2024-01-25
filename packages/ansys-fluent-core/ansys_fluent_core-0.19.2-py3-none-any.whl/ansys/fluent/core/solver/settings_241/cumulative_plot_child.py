#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option_14 import option as option_cls
from .zones_2 import zones as zones_cls
from .split_direction import split_direction as split_direction_cls
from .number_of_divisions import number_of_divisions as number_of_divisions_cls
from .force_direction import force_direction as force_direction_cls
from .moment_center import moment_center as moment_center_cls
from .moment_axis import moment_axis as moment_axis_cls
from .x_axis_quantity import x_axis_quantity as x_axis_quantity_cls
from .compute_from_stats import compute_from_stats as compute_from_stats_cls
from .name_1 import name as name_cls
from .axes import axes as axes_cls
from .curves import curves as curves_cls
from .display_3 import display as display_cls
class cumulative_plot_child(Group):
    """
    'child_object_type' of cumulative_plot.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['option', 'zones', 'split_direction', 'number_of_divisions',
         'force_direction', 'moment_center', 'moment_axis', 'x_axis_quantity',
         'compute_from_stats', 'name', 'axes', 'curves']

    option: option_cls = option_cls
    """
    option child of cumulative_plot_child.
    """
    zones: zones_cls = zones_cls
    """
    zones child of cumulative_plot_child.
    """
    split_direction: split_direction_cls = split_direction_cls
    """
    split_direction child of cumulative_plot_child.
    """
    number_of_divisions: number_of_divisions_cls = number_of_divisions_cls
    """
    number_of_divisions child of cumulative_plot_child.
    """
    force_direction: force_direction_cls = force_direction_cls
    """
    force_direction child of cumulative_plot_child.
    """
    moment_center: moment_center_cls = moment_center_cls
    """
    moment_center child of cumulative_plot_child.
    """
    moment_axis: moment_axis_cls = moment_axis_cls
    """
    moment_axis child of cumulative_plot_child.
    """
    x_axis_quantity: x_axis_quantity_cls = x_axis_quantity_cls
    """
    x_axis_quantity child of cumulative_plot_child.
    """
    compute_from_stats: compute_from_stats_cls = compute_from_stats_cls
    """
    compute_from_stats child of cumulative_plot_child.
    """
    name: name_cls = name_cls
    """
    name child of cumulative_plot_child.
    """
    axes: axes_cls = axes_cls
    """
    axes child of cumulative_plot_child.
    """
    curves: curves_cls = curves_cls
    """
    curves child of cumulative_plot_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of cumulative_plot_child.
    """
