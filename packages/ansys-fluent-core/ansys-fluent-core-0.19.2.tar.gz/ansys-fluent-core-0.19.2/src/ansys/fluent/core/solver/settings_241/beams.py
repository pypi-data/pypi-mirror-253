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
from .copy import copy as copy_cls
from .beams_child import beams_child

class beams(NamedObject[beams_child], _CreatableNamedObjectMixin[beams_child]):
    """
    Enter the optical beams menu.
    """

    fluent_name = "beams"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy', 'copy']

    delete: delete_cls = delete_cls
    """
    delete command of beams.
    """
    list: list_cls = list_cls
    """
    list command of beams.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of beams.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of beams.
    """
    copy: copy_cls = copy_cls
    """
    copy command of beams.
    """
    child_object_type: beams_child = beams_child
    """
    child_object_type of beams.
    """
