#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delete_all_1 import delete_all as delete_all_cls
from .name_4 import name as name_cls
class delete(Command):
    """
    Delete animation sequence.
    
    Parameters
    ----------
        delete_all : bool
            Yes: "Delete all animations", no: "Delete single animation.".
        name : str
            Select animation to delete.
    
    """

    fluent_name = "delete"

    argument_names = \
        ['delete_all', 'name']

    delete_all: delete_all_cls = delete_all_cls
    """
    delete_all argument of delete.
    """
    name: name_cls = name_cls
    """
    name argument of delete.
    """
