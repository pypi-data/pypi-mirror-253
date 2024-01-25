#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .initial_dod import initial_dod as initial_dod_cls
from .ref_capacity import ref_capacity as ref_capacity_cls
from .data_type import data_type as data_type_cls
from .poly_u_function import poly_u_function as poly_u_function_cls
from .poly_y_function import poly_y_function as poly_y_function_cls
from .poly_t_dependence import poly_t_dependence as poly_t_dependence_cls
from .u_table import u_table as u_table_cls
from .y_table import y_table as y_table_cls
class ntgk_model_settings(Group):
    """
    'ntgk_model_settings' child.
    """

    fluent_name = "ntgk-model-settings"

    child_names = \
        ['initial_dod', 'ref_capacity', 'data_type', 'poly_u_function',
         'poly_y_function', 'poly_t_dependence', 'u_table', 'y_table']

    initial_dod: initial_dod_cls = initial_dod_cls
    """
    initial_dod child of ntgk_model_settings.
    """
    ref_capacity: ref_capacity_cls = ref_capacity_cls
    """
    ref_capacity child of ntgk_model_settings.
    """
    data_type: data_type_cls = data_type_cls
    """
    data_type child of ntgk_model_settings.
    """
    poly_u_function: poly_u_function_cls = poly_u_function_cls
    """
    poly_u_function child of ntgk_model_settings.
    """
    poly_y_function: poly_y_function_cls = poly_y_function_cls
    """
    poly_y_function child of ntgk_model_settings.
    """
    poly_t_dependence: poly_t_dependence_cls = poly_t_dependence_cls
    """
    poly_t_dependence child of ntgk_model_settings.
    """
    u_table: u_table_cls = u_table_cls
    """
    u_table child of ntgk_model_settings.
    """
    y_table: y_table_cls = y_table_cls
    """
    y_table child of ntgk_model_settings.
    """
