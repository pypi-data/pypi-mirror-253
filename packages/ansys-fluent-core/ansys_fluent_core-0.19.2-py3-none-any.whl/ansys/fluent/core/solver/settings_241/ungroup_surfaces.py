#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .surface import surface as surface_cls
class ungroup_surfaces(Command):
    """
    'ungroup_surfaces' command.
    
    Parameters
    ----------
        surface : str
            'surface' child.
    
    """

    fluent_name = "ungroup-surfaces"

    argument_names = \
        ['surface']

    surface: surface_cls = surface_cls
    """
    surface argument of ungroup_surfaces.
    """
