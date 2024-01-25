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
from .recirculation_inlet_child import recirculation_inlet_child

class recirculation_inlet(NamedObject[recirculation_inlet_child], _NonCreatableNamedObjectMixin[recirculation_inlet_child]):
    """
    'recirculation_inlet' child.
    """

    fluent_name = "recirculation-inlet"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of recirculation_inlet.
    """
    list: list_cls = list_cls
    """
    list command of recirculation_inlet.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of recirculation_inlet.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of recirculation_inlet.
    """
    child_object_type: recirculation_inlet_child = recirculation_inlet_child
    """
    child_object_type of recirculation_inlet.
    """
