#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .create_output_parameter import create_output_parameter as create_output_parameter_cls
class custom_child(Group):
    """
    'child_object_type' of custom.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name']

    name: name_cls = name_cls
    """
    name child of custom_child.
    """
    command_names = \
        ['create_output_parameter']

    create_output_parameter: create_output_parameter_cls = create_output_parameter_cls
    """
    create_output_parameter command of custom_child.
    """
