#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .cell_function_1 import cell_function as cell_function_cls
from .auto_range_2 import auto_range as auto_range_cls
from .minimum_1 import minimum as minimum_cls
from .maximum_1 import maximum as maximum_cls
from .num_divisions import num_divisions as num_divisions_cls
from .all_zones import all_zones as all_zones_cls
from .zones_1 import zones as zones_cls
from .axes import axes as axes_cls
from .curves import curves as curves_cls
from .print_4 import print as print_cls
from .plot_5 import plot as plot_cls
from .write_3 import write as write_cls
class histogram(Group):
    """
    'histogram' child.
    """

    fluent_name = "histogram"

    child_names = \
        ['cell_function', 'auto_range', 'minimum', 'maximum', 'num_divisions',
         'all_zones', 'zones', 'axes', 'curves']

    cell_function: cell_function_cls = cell_function_cls
    """
    cell_function child of histogram.
    """
    auto_range: auto_range_cls = auto_range_cls
    """
    auto_range child of histogram.
    """
    minimum: minimum_cls = minimum_cls
    """
    minimum child of histogram.
    """
    maximum: maximum_cls = maximum_cls
    """
    maximum child of histogram.
    """
    num_divisions: num_divisions_cls = num_divisions_cls
    """
    num_divisions child of histogram.
    """
    all_zones: all_zones_cls = all_zones_cls
    """
    all_zones child of histogram.
    """
    zones: zones_cls = zones_cls
    """
    zones child of histogram.
    """
    axes: axes_cls = axes_cls
    """
    axes child of histogram.
    """
    curves: curves_cls = curves_cls
    """
    curves child of histogram.
    """
    command_names = \
        ['print', 'plot', 'write']

    print: print_cls = print_cls
    """
    print command of histogram.
    """
    plot: plot_cls = plot_cls
    """
    plot command of histogram.
    """
    write: write_cls = write_cls
    """
    write command of histogram.
    """
