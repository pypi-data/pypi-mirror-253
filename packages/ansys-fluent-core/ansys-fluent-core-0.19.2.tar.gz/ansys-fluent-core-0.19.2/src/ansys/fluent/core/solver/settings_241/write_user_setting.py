#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
class write_user_setting(Command):
    """
    Write the contents of the Modified Settings Summary table to a file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
    
    """

    fluent_name = "write-user-setting"

    argument_names = \
        ['file_name']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of write_user_setting.
    """
