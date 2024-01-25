#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .hybrid_model import hybrid_model as hybrid_model_cls
from .user_defined_1 import user_defined as user_defined_cls
from .update_interval_k_omega import update_interval_k_omega as update_interval_k_omega_cls
from .les_subgrid_scale_model import les_subgrid_scale_model as les_subgrid_scale_model_cls
from .les_subgrid_dynamic_fvar import les_subgrid_dynamic_fvar as les_subgrid_dynamic_fvar_cls
class sbes_options(Group):
    """
    'sbes_options' child.
    """

    fluent_name = "sbes-options"

    child_names = \
        ['hybrid_model', 'user_defined', 'update_interval_k_omega',
         'les_subgrid_scale_model', 'les_subgrid_dynamic_fvar']

    hybrid_model: hybrid_model_cls = hybrid_model_cls
    """
    hybrid_model child of sbes_options.
    """
    user_defined: user_defined_cls = user_defined_cls
    """
    user_defined child of sbes_options.
    """
    update_interval_k_omega: update_interval_k_omega_cls = update_interval_k_omega_cls
    """
    update_interval_k_omega child of sbes_options.
    """
    les_subgrid_scale_model: les_subgrid_scale_model_cls = les_subgrid_scale_model_cls
    """
    les_subgrid_scale_model child of sbes_options.
    """
    les_subgrid_dynamic_fvar: les_subgrid_dynamic_fvar_cls = les_subgrid_dynamic_fvar_cls
    """
    les_subgrid_dynamic_fvar child of sbes_options.
    """
