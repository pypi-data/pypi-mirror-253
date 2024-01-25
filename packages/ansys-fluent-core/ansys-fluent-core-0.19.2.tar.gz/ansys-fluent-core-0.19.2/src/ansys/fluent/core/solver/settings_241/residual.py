#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .equations_1 import equations as equations_cls
from .options_9 import options as options_cls
from .axes import axes as axes_cls
from .curves import curves as curves_cls
from .reset import reset as reset_cls
from .renormalize import renormalize as renormalize_cls
from .plot_1 import plot as plot_cls
class residual(Group):
    """
    Enter the residual monitors menu.
    """

    fluent_name = "residual"

    child_names = \
        ['equations', 'options', 'axes', 'curves']

    equations: equations_cls = equations_cls
    """
    equations child of residual.
    """
    options: options_cls = options_cls
    """
    options child of residual.
    """
    axes: axes_cls = axes_cls
    """
    axes child of residual.
    """
    curves: curves_cls = curves_cls
    """
    curves child of residual.
    """
    command_names = \
        ['reset', 'renormalize', 'plot']

    reset: reset_cls = reset_cls
    """
    reset command of residual.
    """
    renormalize: renormalize_cls = renormalize_cls
    """
    renormalize command of residual.
    """
    plot: plot_cls = plot_cls
    """
    plot command of residual.
    """
