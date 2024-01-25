#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .ntgk_model_parameter import ntgk_model_parameter as ntgk_model_parameter_cls
from .ecm_model_parameter import ecm_model_parameter as ecm_model_parameter_cls
from .user_defined_echem_model import user_defined_echem_model as user_defined_echem_model_cls
from .p2d_bv_rate import p2d_bv_rate as p2d_bv_rate_cls
from .p2d_postprocessing import p2d_postprocessing as p2d_postprocessing_cls
from .p2d_porosity_p import p2d_porosity_p as p2d_porosity_p_cls
from .p2d_porosity_n import p2d_porosity_n as p2d_porosity_n_cls
class udf_hooks(Group):
    """
    'udf_hooks' child.
    """

    fluent_name = "udf-hooks"

    child_names = \
        ['ntgk_model_parameter', 'ecm_model_parameter',
         'user_defined_echem_model', 'p2d_bv_rate', 'p2d_postprocessing',
         'p2d_porosity_p', 'p2d_porosity_n']

    ntgk_model_parameter: ntgk_model_parameter_cls = ntgk_model_parameter_cls
    """
    ntgk_model_parameter child of udf_hooks.
    """
    ecm_model_parameter: ecm_model_parameter_cls = ecm_model_parameter_cls
    """
    ecm_model_parameter child of udf_hooks.
    """
    user_defined_echem_model: user_defined_echem_model_cls = user_defined_echem_model_cls
    """
    user_defined_echem_model child of udf_hooks.
    """
    p2d_bv_rate: p2d_bv_rate_cls = p2d_bv_rate_cls
    """
    p2d_bv_rate child of udf_hooks.
    """
    p2d_postprocessing: p2d_postprocessing_cls = p2d_postprocessing_cls
    """
    p2d_postprocessing child of udf_hooks.
    """
    p2d_porosity_p: p2d_porosity_p_cls = p2d_porosity_p_cls
    """
    p2d_porosity_p child of udf_hooks.
    """
    p2d_porosity_n: p2d_porosity_n_cls = p2d_porosity_n_cls
    """
    p2d_porosity_n child of udf_hooks.
    """
