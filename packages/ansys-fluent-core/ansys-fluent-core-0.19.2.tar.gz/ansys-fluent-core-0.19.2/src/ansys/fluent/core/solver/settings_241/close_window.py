#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .window_id import window_id as window_id_cls
class close_window(Command):
    """
    Close a user graphics window.
    
    Parameters
    ----------
        window_id : int
            'window_id' child.
    
    """

    fluent_name = "close-window"

    argument_names = \
        ['window_id']

    window_id: window_id_cls = window_id_cls
    """
    window_id argument of close_window.
    """
