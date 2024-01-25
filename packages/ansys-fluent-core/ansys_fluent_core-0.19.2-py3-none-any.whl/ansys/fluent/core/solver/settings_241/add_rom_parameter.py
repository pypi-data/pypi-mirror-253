#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .parameter_type import parameter_type as parameter_type_cls
from .entity_list import entity_list as entity_list_cls
from .individual_or_group import individual_or_group as individual_or_group_cls
from .individual_value import individual_value as individual_value_cls
from .group_value import group_value as group_value_cls
from .value_list import value_list as value_list_cls
class add_rom_parameter(Command):
    """
    'add_rom_parameter' command.
    
    Parameters
    ----------
        parameter_type : int
            'parameter_type' child.
        entity_list : typing.List[str]
            'entity_list' child.
        individual_or_group : bool
            'individual_or_group' child.
        individual_value : bool
            'individual_value' child.
        group_value : real
            'group_value' child.
        value_list : typing.List[real]
            'value_list' child.
    
    """

    fluent_name = "add-rom-parameter"

    argument_names = \
        ['parameter_type', 'entity_list', 'individual_or_group',
         'individual_value', 'group_value', 'value_list']

    parameter_type: parameter_type_cls = parameter_type_cls
    """
    parameter_type argument of add_rom_parameter.
    """
    entity_list: entity_list_cls = entity_list_cls
    """
    entity_list argument of add_rom_parameter.
    """
    individual_or_group: individual_or_group_cls = individual_or_group_cls
    """
    individual_or_group argument of add_rom_parameter.
    """
    individual_value: individual_value_cls = individual_value_cls
    """
    individual_value argument of add_rom_parameter.
    """
    group_value: group_value_cls = group_value_cls
    """
    group_value argument of add_rom_parameter.
    """
    value_list: value_list_cls = value_list_cls
    """
    value_list argument of add_rom_parameter.
    """
