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
from .iso_clip_child import iso_clip_child

class iso_clip(NamedObject[iso_clip_child], _CreatableNamedObjectMixin[iso_clip_child]):
    """
    'iso_clip' child.
    """

    fluent_name = "iso-clip"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of iso_clip.
    """
    list: list_cls = list_cls
    """
    list command of iso_clip.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of iso_clip.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of iso_clip.
    """
    child_object_type: iso_clip_child = iso_clip_child
    """
    child_object_type of iso_clip.
    """
