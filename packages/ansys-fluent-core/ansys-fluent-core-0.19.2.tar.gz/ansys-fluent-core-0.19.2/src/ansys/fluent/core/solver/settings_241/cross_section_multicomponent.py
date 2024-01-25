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
from .cross_section_multicomponent_child import cross_section_multicomponent_child

class cross_section_multicomponent(NamedObject[cross_section_multicomponent_child], _NonCreatableNamedObjectMixin[cross_section_multicomponent_child]):
    """
    'cross_section_multicomponent' child.
    """

    fluent_name = "cross-section-multicomponent"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of cross_section_multicomponent.
    """
    list: list_cls = list_cls
    """
    list command of cross_section_multicomponent.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of cross_section_multicomponent.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of cross_section_multicomponent.
    """
    child_object_type: cross_section_multicomponent_child = cross_section_multicomponent_child
    """
    child_object_type of cross_section_multicomponent.
    """
