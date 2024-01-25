#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .file_name_1 import file_name as file_name_cls
class icemcfd_for_icepak(Command):
    """
    Write a binary ICEMCFD domain file.
    
    Parameters
    ----------
        file_name : str
            'file_name' child.
    
    """

    fluent_name = "icemcfd-for-icepak"

    argument_names = \
        ['file_name']

    file_name: file_name_cls = file_name_cls
    """
    file_name argument of icemcfd_for_icepak.
    """
