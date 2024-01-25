#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_data_list import file_data_list as file_data_list_cls
class free_file_data(Command):
    """
    Free file-data.
    
    Parameters
    ----------
        file_data_list : typing.List[str]
            File-data to delete.
    
    """

    fluent_name = "free-file-data"

    argument_names = \
        ['file_data_list']

    file_data_list: file_data_list_cls = file_data_list_cls
    """
    file_data_list argument of free_file_data.
    """
