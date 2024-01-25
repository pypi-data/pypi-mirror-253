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
from .compute_1 import compute as compute_cls
from .named_expressions_child import named_expressions_child

class named_expressions(NamedObject[named_expressions_child], _CreatableNamedObjectMixin[named_expressions_child]):
    """
    'named_expressions' child.
    """

    fluent_name = "named-expressions"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy', 'compute']

    delete: delete_cls = delete_cls
    """
    delete command of named_expressions.
    """
    list: list_cls = list_cls
    """
    list command of named_expressions.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of named_expressions.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of named_expressions.
    """
    compute: compute_cls = compute_cls
    """
    compute command of named_expressions.
    """
    child_object_type: named_expressions_child = named_expressions_child
    """
    child_object_type of named_expressions.
    """
