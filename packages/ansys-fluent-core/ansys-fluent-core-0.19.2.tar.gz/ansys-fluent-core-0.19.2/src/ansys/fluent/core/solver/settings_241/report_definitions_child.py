#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .report_definition import report_definition as report_definition_cls
class report_definitions_child(Group):
    """
    'child_object_type' of report_definitions.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'report_definition']

    name: name_cls = name_cls
    """
    name child of report_definitions_child.
    """
    report_definition: report_definition_cls = report_definition_cls
    """
    report_definition child of report_definitions_child.
    """
