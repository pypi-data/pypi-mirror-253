#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delete_1 import delete as delete_cls
from .list import list as list_cls
from .list_properties_1 import list_properties as list_properties_cls
from .make_a_copy import make_a_copy as make_a_copy_cls
from .rake_surface_child import rake_surface_child

class rake_surface(NamedObject[rake_surface_child], _CreatableNamedObjectMixin[rake_surface_child]):
    """
    'rake_surface' child.
    """

    fluent_name = "rake-surface"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of rake_surface.
    """
    list: list_cls = list_cls
    """
    list command of rake_surface.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of rake_surface.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of rake_surface.
    """
    child_object_type: rake_surface_child = rake_surface_child
    """
    child_object_type of rake_surface.
    """
