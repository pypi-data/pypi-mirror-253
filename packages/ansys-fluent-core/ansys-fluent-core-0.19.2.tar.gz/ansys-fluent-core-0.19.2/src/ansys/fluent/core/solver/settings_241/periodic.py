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
from .periodic_child import periodic_child

class periodic(NamedObject[periodic_child], _NonCreatableNamedObjectMixin[periodic_child]):
    """
    'periodic' child.
    """

    fluent_name = "periodic"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of periodic.
    """
    list: list_cls = list_cls
    """
    list command of periodic.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of periodic.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of periodic.
    """
    child_object_type: periodic_child = periodic_child
    """
    child_object_type of periodic.
    """
