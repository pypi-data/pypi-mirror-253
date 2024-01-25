#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .animation_file_name import animation_file_name as animation_file_name_cls
class read_animation_file(Command):
    """
    Read new animation from file or already-defined animations.
    
    Parameters
    ----------
        animation_file_name : str
            'animation_file_name' child.
    
    """

    fluent_name = "read-animation-file"

    argument_names = \
        ['animation_file_name']

    animation_file_name: animation_file_name_cls = animation_file_name_cls
    """
    animation_file_name argument of read_animation_file.
    """
