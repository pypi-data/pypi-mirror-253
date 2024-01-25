#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .criterion_type import criterion_type as criterion_type_cls
from .n_save import n_save as n_save_cls
from .normalize import normalize as normalize_cls
from .n_maximize_norms import n_maximize_norms as n_maximize_norms_cls
from .enhanced_continuity_residual import enhanced_continuity_residual as enhanced_continuity_residual_cls
from .residual_values import residual_values as residual_values_cls
from .print_2 import print as print_cls
from .plot import plot as plot_cls
from .n_display import n_display as n_display_cls
class options(Group):
    """
    'options' child.
    """

    fluent_name = "options"

    child_names = \
        ['criterion_type', 'n_save', 'normalize', 'n_maximize_norms',
         'enhanced_continuity_residual', 'residual_values', 'print', 'plot',
         'n_display']

    criterion_type: criterion_type_cls = criterion_type_cls
    """
    criterion_type child of options.
    """
    n_save: n_save_cls = n_save_cls
    """
    n_save child of options.
    """
    normalize: normalize_cls = normalize_cls
    """
    normalize child of options.
    """
    n_maximize_norms: n_maximize_norms_cls = n_maximize_norms_cls
    """
    n_maximize_norms child of options.
    """
    enhanced_continuity_residual: enhanced_continuity_residual_cls = enhanced_continuity_residual_cls
    """
    enhanced_continuity_residual child of options.
    """
    residual_values: residual_values_cls = residual_values_cls
    """
    residual_values child of options.
    """
    print: print_cls = print_cls
    """
    print child of options.
    """
    plot: plot_cls = plot_cls
    """
    plot child of options.
    """
    n_display: n_display_cls = n_display_cls
    """
    n_display child of options.
    """
