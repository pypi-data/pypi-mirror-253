#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .domain_1 import domain as domain_cls
from .cell_zones_5 import cell_zones as cell_zones_cls
from .registers import registers as registers_cls
from .variable import variable as variable_cls
from .reference_frame_4 import reference_frame as reference_frame_cls
from .use_custom_field_function import use_custom_field_function as use_custom_field_function_cls
from .custom_field_function_name import custom_field_function_name as custom_field_function_name_cls
from .value_5 import value as value_cls
class calculate_patch(Command):
    """
    Patch a value for a flow variable in the domain.
    
    Parameters
    ----------
        domain : str
            Enter domain.
        cell_zones : typing.List[str]
            Enter cell zone.
        registers : typing.List[str]
            Enter register.
        variable : str
            Enter variable.
        reference_frame : str
            Select velocity Reference Frame.
        use_custom_field_function : bool
            Enable/disable custom field function for patching.
        custom_field_function_name : str
            Enter custom function.
        value : real
            Enter patch value.
    
    """

    fluent_name = "calculate-patch"

    argument_names = \
        ['domain', 'cell_zones', 'registers', 'variable', 'reference_frame',
         'use_custom_field_function', 'custom_field_function_name', 'value']

    domain: domain_cls = domain_cls
    """
    domain argument of calculate_patch.
    """
    cell_zones: cell_zones_cls = cell_zones_cls
    """
    cell_zones argument of calculate_patch.
    """
    registers: registers_cls = registers_cls
    """
    registers argument of calculate_patch.
    """
    variable: variable_cls = variable_cls
    """
    variable argument of calculate_patch.
    """
    reference_frame: reference_frame_cls = reference_frame_cls
    """
    reference_frame argument of calculate_patch.
    """
    use_custom_field_function: use_custom_field_function_cls = use_custom_field_function_cls
    """
    use_custom_field_function argument of calculate_patch.
    """
    custom_field_function_name: custom_field_function_name_cls = custom_field_function_name_cls
    """
    custom_field_function_name argument of calculate_patch.
    """
    value: value_cls = value_cls
    """
    value argument of calculate_patch.
    """
