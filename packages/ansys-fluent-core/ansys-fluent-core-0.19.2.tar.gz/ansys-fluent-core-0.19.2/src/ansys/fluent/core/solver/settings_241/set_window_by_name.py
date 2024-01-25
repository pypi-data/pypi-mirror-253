#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .window_name import window_name as window_name_cls
class set_window_by_name(Command):
    """
    Set a reserved graphics window to be the active window by its name.
    
    Parameters
    ----------
        window_name : str
            'window_name' child.
    
    """

    fluent_name = "set-window-by-name"

    argument_names = \
        ['window_name']

    window_name: window_name_cls = window_name_cls
    """
    window_name argument of set_window_by_name.
    """
