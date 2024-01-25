#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .omega_pe import omega_pe as omega_pe_cls
from .omega_ne import omega_ne as omega_ne_cls
from .e_elastic_pe import e_elastic_pe as e_elastic_pe_cls
from .e_elastic_sp import e_elastic_sp as e_elastic_sp_cls
from .e_elastic_ne import e_elastic_ne as e_elastic_ne_cls
from .soc_ref import soc_ref as soc_ref_cls
from .cell_type import cell_type as cell_type_cls
from .axis_vec import axis_vec as axis_vec_cls
from .normal_vec import normal_vec as normal_vec_cls
from .prism_axis_vec import prism_axis_vec as prism_axis_vec_cls
from .prism_vec2 import prism_vec2 as prism_vec2_cls
from .udf_name import udf_name as udf_name_cls
class swelling_model_parameter(Group):
    """
    'swelling_model_parameter' child.
    """

    fluent_name = "swelling-model-parameter"

    child_names = \
        ['omega_pe', 'omega_ne', 'e_elastic_pe', 'e_elastic_sp',
         'e_elastic_ne', 'soc_ref', 'cell_type', 'axis_vec', 'normal_vec',
         'prism_axis_vec', 'prism_vec2', 'udf_name']

    omega_pe: omega_pe_cls = omega_pe_cls
    """
    omega_pe child of swelling_model_parameter.
    """
    omega_ne: omega_ne_cls = omega_ne_cls
    """
    omega_ne child of swelling_model_parameter.
    """
    e_elastic_pe: e_elastic_pe_cls = e_elastic_pe_cls
    """
    e_elastic_pe child of swelling_model_parameter.
    """
    e_elastic_sp: e_elastic_sp_cls = e_elastic_sp_cls
    """
    e_elastic_sp child of swelling_model_parameter.
    """
    e_elastic_ne: e_elastic_ne_cls = e_elastic_ne_cls
    """
    e_elastic_ne child of swelling_model_parameter.
    """
    soc_ref: soc_ref_cls = soc_ref_cls
    """
    soc_ref child of swelling_model_parameter.
    """
    cell_type: cell_type_cls = cell_type_cls
    """
    cell_type child of swelling_model_parameter.
    """
    axis_vec: axis_vec_cls = axis_vec_cls
    """
    axis_vec child of swelling_model_parameter.
    """
    normal_vec: normal_vec_cls = normal_vec_cls
    """
    normal_vec child of swelling_model_parameter.
    """
    prism_axis_vec: prism_axis_vec_cls = prism_axis_vec_cls
    """
    prism_axis_vec child of swelling_model_parameter.
    """
    prism_vec2: prism_vec2_cls = prism_vec2_cls
    """
    prism_vec2 child of swelling_model_parameter.
    """
    udf_name: udf_name_cls = udf_name_cls
    """
    udf_name child of swelling_model_parameter.
    """
