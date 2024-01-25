#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .surface import surface as surface_cls
from .zones_4 import zones as zones_cls
from .display_3 import display as display_cls
class imprint_surface_child(Group):
    """
    'child_object_type' of imprint_surface.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'surface', 'zones']

    name: name_cls = name_cls
    """
    name child of imprint_surface_child.
    """
    surface: surface_cls = surface_cls
    """
    surface child of imprint_surface_child.
    """
    zones: zones_cls = zones_cls
    """
    zones child of imprint_surface_child.
    """
    command_names = \
        ['display']

    display: display_cls = display_cls
    """
    display command of imprint_surface_child.
    """
