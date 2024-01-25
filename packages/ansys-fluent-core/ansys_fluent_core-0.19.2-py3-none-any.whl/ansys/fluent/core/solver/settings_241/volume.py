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
from .volume_child import volume_child

class volume(NamedObject[volume_child], _CreatableNamedObjectMixin[volume_child]):
    """
    'volume' child.
    """

    fluent_name = "volume"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of volume.
    """
    list: list_cls = list_cls
    """
    list command of volume.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of volume.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of volume.
    """
    child_object_type: volume_child = volume_child
    """
    child_object_type of volume.
    """
