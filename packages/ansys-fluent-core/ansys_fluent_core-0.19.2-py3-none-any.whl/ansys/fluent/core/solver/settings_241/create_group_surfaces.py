#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .surfaces_4 import surfaces as surfaces_cls
from .name_1 import name as name_cls
class create_group_surfaces(Command):
    """
    'create_group_surfaces' command.
    
    Parameters
    ----------
        surfaces : typing.List[str]
            Select list of surfaces.
        name : str
            'name' child.
    
    """

    fluent_name = "create-group-surfaces"

    argument_names = \
        ['surfaces', 'name']

    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of create_group_surfaces.
    """
    name: name_cls = name_cls
    """
    name argument of create_group_surfaces.
    """
