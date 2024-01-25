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
from .display_2 import display as display_cls
from .copy_4 import copy as copy_cls
from .add_to_graphics import add_to_graphics as add_to_graphics_cls
from .clear_history import clear_history as clear_history_cls
from .pathline_child import pathline_child

class pathline(NamedObject[pathline_child], _CreatableNamedObjectMixin[pathline_child]):
    """
    'pathline' child.
    """

    fluent_name = "pathline"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy', 'display',
         'copy', 'add_to_graphics', 'clear_history']

    delete: delete_cls = delete_cls
    """
    delete command of pathline.
    """
    list: list_cls = list_cls
    """
    list command of pathline.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of pathline.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of pathline.
    """
    display: display_cls = display_cls
    """
    display command of pathline.
    """
    copy: copy_cls = copy_cls
    """
    copy command of pathline.
    """
    add_to_graphics: add_to_graphics_cls = add_to_graphics_cls
    """
    add_to_graphics command of pathline.
    """
    clear_history: clear_history_cls = clear_history_cls
    """
    clear_history command of pathline.
    """
    child_object_type: pathline_child = pathline_child
    """
    child_object_type of pathline.
    """
