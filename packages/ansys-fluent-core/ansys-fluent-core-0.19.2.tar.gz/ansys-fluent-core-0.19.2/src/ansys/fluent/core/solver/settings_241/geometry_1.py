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
from .geometry_child import geometry_child

class geometry(NamedObject[geometry_child], _CreatableNamedObjectMixin[geometry_child]):
    """
    Main menu to define a disk-section:
    
     - delete : delete a disk-section% - edit   : edit a disk-section
     - new    : create a new disk-section
     - rename : rename a vbm disk-section.
    
    """

    fluent_name = "geometry"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of geometry.
    """
    list: list_cls = list_cls
    """
    list command of geometry.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of geometry.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of geometry.
    """
    child_object_type: geometry_child = geometry_child
    """
    child_object_type of geometry.
    """
