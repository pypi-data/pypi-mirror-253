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
from .custom_vectors_child import custom_vectors_child

class custom_vectors(NamedObject[custom_vectors_child], _CreatableNamedObjectMixin[custom_vectors_child]):
    """
    'custom_vectors' child.
    """

    fluent_name = "custom-vectors"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of custom_vectors.
    """
    list: list_cls = list_cls
    """
    list command of custom_vectors.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of custom_vectors.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of custom_vectors.
    """
    child_object_type: custom_vectors_child = custom_vectors_child
    """
    child_object_type of custom_vectors.
    """
