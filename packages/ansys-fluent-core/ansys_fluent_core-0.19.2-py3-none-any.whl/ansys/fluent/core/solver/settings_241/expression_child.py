#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .average_over import average_over as average_over_cls
from .expr_value import expr_value as expr_value_cls
from .define import define as define_cls
from .list_valid_report_names import list_valid_report_names as list_valid_report_names_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class expression_child(Group):
    """
    'child_object_type' of expression.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'average_over', 'expr_value', 'define',
         'list_valid_report_names']

    name: name_cls = name_cls
    """
    name child of expression_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of expression_child.
    """
    expr_value: expr_value_cls = expr_value_cls
    """
    expr_value child of expression_child.
    """
    define: define_cls = define_cls
    """
    define child of expression_child.
    """
    list_valid_report_names: list_valid_report_names_cls = list_valid_report_names_cls
    """
    list_valid_report_names child of expression_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of expression_child.
    """
