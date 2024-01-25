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
class udf_side_child(Group):
    """
    'child_object_type' of udf_side.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'value']

    name: name_cls = name_cls
    """
    name child of udf_side_child.
    """
    value: value_cls = value_cls
    """
    value child of udf_side_child.
    """
