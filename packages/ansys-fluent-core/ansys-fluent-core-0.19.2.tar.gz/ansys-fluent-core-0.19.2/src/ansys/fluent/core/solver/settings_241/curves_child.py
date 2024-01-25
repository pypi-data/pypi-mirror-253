#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .line import line as line_cls
from .line_in_file import line_in_file as line_in_file_cls
from .marker import marker as marker_cls
from .marker_in_file import marker_in_file as marker_in_file_cls
class curves_child(Group):
    """
    'child_object_type' of curves.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['line', 'line_in_file', 'marker', 'marker_in_file']

    line: line_cls = line_cls
    """
    line child of curves_child.
    """
    line_in_file: line_in_file_cls = line_in_file_cls
    """
    line_in_file child of curves_child.
    """
    marker: marker_cls = marker_cls
    """
    marker child of curves_child.
    """
    marker_in_file: marker_in_file_cls = marker_in_file_cls
    """
    marker_in_file child of curves_child.
    """
