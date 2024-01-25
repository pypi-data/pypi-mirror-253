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
from .report_files_child import report_files_child

class report_files(NamedObject[report_files_child], _CreatableNamedObjectMixin[report_files_child]):
    """
    'report_files' child.
    """

    fluent_name = "report-files"

    command_names = \
        ['delete', 'list', 'list_properties', 'make_a_copy']

    delete: delete_cls = delete_cls
    """
    delete command of report_files.
    """
    list: list_cls = list_cls
    """
    list command of report_files.
    """
    list_properties: list_properties_cls = list_properties_cls
    """
    list_properties command of report_files.
    """
    make_a_copy: make_a_copy_cls = make_a_copy_cls
    """
    make_a_copy command of report_files.
    """
    child_object_type: report_files_child = report_files_child
    """
    child_object_type of report_files.
    """
