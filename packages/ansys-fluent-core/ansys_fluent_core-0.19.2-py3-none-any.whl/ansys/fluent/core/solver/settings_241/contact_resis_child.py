#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_name_1 import zone_name as zone_name_cls
from .value_1 import value as value_cls
class contact_resis_child(Group):
    """
    'child_object_type' of contact_resis.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['zone_name', 'value']

    zone_name: zone_name_cls = zone_name_cls
    """
    zone_name child of contact_resis_child.
    """
    value: value_cls = value_cls
    """
    value child of contact_resis_child.
    """
