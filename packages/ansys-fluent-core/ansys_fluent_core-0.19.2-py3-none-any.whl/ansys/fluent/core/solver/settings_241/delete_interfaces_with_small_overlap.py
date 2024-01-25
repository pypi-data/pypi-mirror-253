#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .delete_3 import delete as delete_cls
from .overlapping_percentage_threshold import overlapping_percentage_threshold as overlapping_percentage_threshold_cls
class delete_interfaces_with_small_overlap(Command):
    """
    Delete mesh interfaces that have an area percentage under a specified value.
    
    Parameters
    ----------
        delete : bool
            'delete' child.
        overlapping_percentage_threshold : real
            'overlapping_percentage_threshold' child.
    
    """

    fluent_name = "delete-interfaces-with-small-overlap"

    argument_names = \
        ['delete', 'overlapping_percentage_threshold']

    delete: delete_cls = delete_cls
    """
    delete argument of delete_interfaces_with_small_overlap.
    """
    overlapping_percentage_threshold: overlapping_percentage_threshold_cls = overlapping_percentage_threshold_cls
    """
    overlapping_percentage_threshold argument of delete_interfaces_with_small_overlap.
    """
