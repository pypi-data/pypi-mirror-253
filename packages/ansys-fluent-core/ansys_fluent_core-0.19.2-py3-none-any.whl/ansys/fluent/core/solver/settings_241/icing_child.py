#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .report_type import report_type as report_type_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class icing_child(Group):
    """
    'child_object_type' of icing.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_type']

    name: name_cls = name_cls
    """
    name child of icing_child.
    """
    report_type: report_type_cls = report_type_cls
    """
    report_type child of icing_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of icing_child.
    """
