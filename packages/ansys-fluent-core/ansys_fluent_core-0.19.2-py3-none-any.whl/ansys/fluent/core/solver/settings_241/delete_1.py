#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name_list import name_list as name_list_cls
class delete(Command):
    """
    Delete selected objects.
    
    Parameters
    ----------
        name_list : typing.List[str]
            Select objects to be deleted.
    
    """

    fluent_name = "delete"

    argument_names = \
        ['name_list']

    name_list: name_list_cls = name_list_cls
    """
    name_list argument of delete.
    """
