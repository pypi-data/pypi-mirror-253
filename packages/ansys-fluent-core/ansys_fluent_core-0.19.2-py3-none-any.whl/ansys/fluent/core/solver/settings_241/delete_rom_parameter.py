#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .parameter_names import parameter_names as parameter_names_cls
class delete_rom_parameter(Command):
    """
    Delete ROM-related paramters.
    
    Parameters
    ----------
        parameter_names : typing.List[str]
            Set deleted parameter lists.
    
    """

    fluent_name = "delete-rom-parameter"

    argument_names = \
        ['parameter_names']

    parameter_names: parameter_names_cls = parameter_names_cls
    """
    parameter_names argument of delete_rom_parameter.
    """
