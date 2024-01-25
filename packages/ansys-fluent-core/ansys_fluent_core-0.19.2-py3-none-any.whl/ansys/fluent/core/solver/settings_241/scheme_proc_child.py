#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .value_1 import value as value_cls
from .apply_function import apply_function as apply_function_cls
class scheme_proc_child(Group):
    """
    'child_object_type' of scheme_proc.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'value', 'apply_function']

    name: name_cls = name_cls
    """
    name child of scheme_proc_child.
    """
    value: value_cls = value_cls
    """
    value child of scheme_proc_child.
    """
    apply_function: apply_function_cls = apply_function_cls
    """
    apply_function child of scheme_proc_child.
    """
