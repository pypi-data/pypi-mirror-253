#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .param_name import param_name as param_name_cls
from .file_name_1 import file_name as file_name_cls
from .append_data import append_data as append_data_cls
class write_to_file(Command):
    """
    Write parameter value to file.
    
    Parameters
    ----------
        param_name : str
            'param_name' child.
        file_name : str
            'file_name' child.
        append_data : bool
            'append_data' child.
    
    """

    fluent_name = "write-to-file"

    argument_names = \
        ['param_name', 'file_name', 'append_data']

    param_name: param_name_cls = param_name_cls
    """
    param_name argument of write_to_file.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of write_to_file.
    """
    append_data: append_data_cls = append_data_cls
    """
    append_data argument of write_to_file.
    """
