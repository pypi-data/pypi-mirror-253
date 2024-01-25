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
from .fluid_child import fluid_child

class volumetric_species(NamedObject[fluid_child], _CreatableNamedObjectMixin[fluid_child]):
    """
    'volumetric_species' child.
    """

    fluent_name = "volumetric-species"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of volumetric_species.
    """
    list: list_cls = list_cls
    """
    list command of volumetric_species.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of volumetric_species.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of volumetric_species.
    """
    child_object_type: fluid_child = fluid_child
    """
    child_object_type of volumetric_species.
    """
