#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .list_properties import list_properties as list_properties_cls
from .user_defined_coupling_variables_via_udm_child import user_defined_coupling_variables_via_udm_child

class user_defined_coupling_variables_via_udm(ListObject[user_defined_coupling_variables_via_udm_child]):
    """
    'user_defined_coupling_variables_via_udm' child.
    """

    fluent_name = "user-defined-coupling-variables-via-udm"

    command_names = \
        ['list_properties']

    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of user_defined_coupling_variables_via_udm.
    """
    child_object_type: user_defined_coupling_variables_via_udm_child = user_defined_coupling_variables_via_udm_child
    """
    child_object_type of user_defined_coupling_variables_via_udm.
    """
