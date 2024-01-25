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
from .relaxation_factor_child import relaxation_factor_child

class relaxation_factor(NamedObject[relaxation_factor_child], _NonCreatableNamedObjectMixin[relaxation_factor_child]):
    """
    Enter explicit relaxation menu.
    """

    fluent_name = "relaxation-factor"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of relaxation_factor.
    """
    list: list_cls = list_cls
    """
    list command of relaxation_factor.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of relaxation_factor.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of relaxation_factor.
    """
    child_object_type: relaxation_factor_child = relaxation_factor_child
    """
    child_object_type of relaxation_factor.
    """
