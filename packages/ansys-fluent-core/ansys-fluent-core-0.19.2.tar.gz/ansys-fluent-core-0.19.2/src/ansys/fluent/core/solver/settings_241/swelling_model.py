#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_12 import enabled as enabled_cls
from .soc_ref import soc_ref as soc_ref_cls
from .cell_type import cell_type as cell_type_cls
from .axis_vec import axis_vec as axis_vec_cls
from .normal_vec import normal_vec as normal_vec_cls
from .prism_axis_vec import prism_axis_vec as prism_axis_vec_cls
from .prism_vec2 import prism_vec2 as prism_vec2_cls
from .orientation_udf_name import orientation_udf_name as orientation_udf_name_cls
from .customize_swelling_strain import customize_swelling_strain as customize_swelling_strain_cls
from .strain_udf_name import strain_udf_name as strain_udf_name_cls
class swelling_model(Group):
    """
    'swelling_model' child.
    """

    fluent_name = "swelling-model"

    child_names = \
        ['enabled', 'soc_ref', 'cell_type', 'axis_vec', 'normal_vec',
         'prism_axis_vec', 'prism_vec2', 'orientation_udf_name',
         'customize_swelling_strain', 'strain_udf_name']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of swelling_model.
    """
    soc_ref: soc_ref_cls = soc_ref_cls
    """
    soc_ref child of swelling_model.
    """
    cell_type: cell_type_cls = cell_type_cls
    """
    cell_type child of swelling_model.
    """
    axis_vec: axis_vec_cls = axis_vec_cls
    """
    axis_vec child of swelling_model.
    """
    normal_vec: normal_vec_cls = normal_vec_cls
    """
    normal_vec child of swelling_model.
    """
    prism_axis_vec: prism_axis_vec_cls = prism_axis_vec_cls
    """
    prism_axis_vec child of swelling_model.
    """
    prism_vec2: prism_vec2_cls = prism_vec2_cls
    """
    prism_vec2 child of swelling_model.
    """
    orientation_udf_name: orientation_udf_name_cls = orientation_udf_name_cls
    """
    orientation_udf_name child of swelling_model.
    """
    customize_swelling_strain: customize_swelling_strain_cls = customize_swelling_strain_cls
    """
    customize_swelling_strain child of swelling_model.
    """
    strain_udf_name: strain_udf_name_cls = strain_udf_name_cls
    """
    strain_udf_name child of swelling_model.
    """
