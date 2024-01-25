#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .format_name import format_name as format_name_cls
from .file_name import file_name as file_name_cls
class write_animation(Command):
    """
    Write keyframe Animation file.
    
    Parameters
    ----------
        format_name : str
            'format_name' child.
        file_name : str
            'file_name' child.
    
    """

    fluent_name = "write-animation"

    argument_names = \
        ['format_name', 'file_name']

    format_name: format_name_cls = format_name_cls
    """
    format_name argument of write_animation.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of write_animation.
    """
