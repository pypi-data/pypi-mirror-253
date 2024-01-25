#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .object_at import object_at as object_at_cls
class list_properties(Command):
    """
    List properties of selected object.
    
    Parameters
    ----------
        object_at : int
            Select object index to delete.
    
    """

    fluent_name = "list-properties"

    argument_names = \
        ['object_at']

    object_at: object_at_cls = object_at_cls
    """
    object_at argument of list_properties.
    """
