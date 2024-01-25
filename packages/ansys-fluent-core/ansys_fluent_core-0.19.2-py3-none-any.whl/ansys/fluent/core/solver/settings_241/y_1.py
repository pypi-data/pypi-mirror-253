#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .label import label as label_cls
from .number_format import number_format as number_format_cls
from .log_scale import log_scale as log_scale_cls
from .auto_range import auto_range as auto_range_cls
from .min import min as min_cls
from .max import max as max_cls
from .show_major_gridlines import show_major_gridlines as show_major_gridlines_cls
from .major_gridlines import major_gridlines as major_gridlines_cls
from .show_minor_gridlines import show_minor_gridlines as show_minor_gridlines_cls
from .minor_gridlines import minor_gridlines as minor_gridlines_cls
class y(Group):
    """
    Y-axis properties.
    """

    fluent_name = "y"

    child_names = \
        ['label', 'number_format', 'log_scale', 'auto_range', 'min', 'max',
         'show_major_gridlines', 'major_gridlines', 'show_minor_gridlines',
         'minor_gridlines']

    label: label_cls = label_cls
    """
    label child of y.
    """
    number_format: number_format_cls = number_format_cls
    """
    number_format child of y.
    """
    log_scale: log_scale_cls = log_scale_cls
    """
    log_scale child of y.
    """
    auto_range: auto_range_cls = auto_range_cls
    """
    auto_range child of y.
    """
    min: min_cls = min_cls
    """
    min child of y.
    """
    max: max_cls = max_cls
    """
    max child of y.
    """
    show_major_gridlines: show_major_gridlines_cls = show_major_gridlines_cls
    """
    show_major_gridlines child of y.
    """
    major_gridlines: major_gridlines_cls = major_gridlines_cls
    """
    major_gridlines child of y.
    """
    show_minor_gridlines: show_minor_gridlines_cls = show_minor_gridlines_cls
    """
    show_minor_gridlines child of y.
    """
    minor_gridlines: minor_gridlines_cls = minor_gridlines_cls
    """
    minor_gridlines child of y.
    """
