#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .surface_3 import surface as surface_cls
from .priority import priority as priority_cls
class set_rendering_priority(Command):
    """
    'set_rendering_priority' command.
    
    Parameters
    ----------
        surface : str
            Select surface.
        priority : str
            Select surface.
    
    """

    fluent_name = "set-rendering-priority"

    argument_names = \
        ['surface', 'priority']

    surface: surface_cls = surface_cls
    """
    surface argument of set_rendering_priority.
    """
    priority: priority_cls = priority_cls
    """
    priority argument of set_rendering_priority.
    """
