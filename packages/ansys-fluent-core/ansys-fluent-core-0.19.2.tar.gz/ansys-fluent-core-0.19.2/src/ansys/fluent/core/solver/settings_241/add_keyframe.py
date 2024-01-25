#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .key import key as key_cls
class add_keyframe(Command):
    """
    Add keyframe.
    
    Parameters
    ----------
        key : int
            'key' child.
    
    """

    fluent_name = "add-keyframe"

    argument_names = \
        ['key']

    key: key_cls = key_cls
    """
    key argument of add_keyframe.
    """
