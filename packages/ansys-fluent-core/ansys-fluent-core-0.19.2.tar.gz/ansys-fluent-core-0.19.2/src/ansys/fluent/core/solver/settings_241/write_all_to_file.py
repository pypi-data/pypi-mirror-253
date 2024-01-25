#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
from .append_data import append_data as append_data_cls
class write_all_to_file(Command):
    """
    Write all parameters value to file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
        append_data : bool
            'append_data' child.
    
    """

    fluent_name = "write-all-to-file"

    argument_names = \
        ['file_name', 'append_data']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of write_all_to_file.
    """
    append_data: append_data_cls = append_data_cls
    """
    append_data argument of write_all_to_file.
    """
