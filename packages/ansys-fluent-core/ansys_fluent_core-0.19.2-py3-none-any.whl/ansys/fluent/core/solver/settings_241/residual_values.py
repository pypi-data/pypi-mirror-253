#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .scale_residuals import scale_residuals as scale_residuals_cls
from .compute_local_scale import compute_local_scale as compute_local_scale_cls
from .scale_type import scale_type as scale_type_cls
class residual_values(Group):
    """
    Enable/disable scaling of residuals by coefficient sum in printed and plotted output.
    """

    fluent_name = "residual-values"

    child_names = \
        ['scale_residuals', 'compute_local_scale', 'scale_type']

    scale_residuals: scale_residuals_cls = scale_residuals_cls
    """
    scale_residuals child of residual_values.
    """
    compute_local_scale: compute_local_scale_cls = compute_local_scale_cls
    """
    compute_local_scale child of residual_values.
    """
    scale_type: scale_type_cls = scale_type_cls
    """
    scale_type child of residual_values.
    """
