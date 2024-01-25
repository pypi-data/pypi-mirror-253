#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .data_reduction_interval import data_reduction_interval as data_reduction_interval_cls
from .target_num_parcels_per_face import target_num_parcels_per_face as target_num_parcels_per_face_cls
class data_reduction(Group):
    """
    Help not available.
    """

    fluent_name = "data-reduction"

    child_names = \
        ['data_reduction_interval', 'target_num_parcels_per_face']

    data_reduction_interval: data_reduction_interval_cls = data_reduction_interval_cls
    """
    data_reduction_interval child of data_reduction.
    """
    target_num_parcels_per_face: target_num_parcels_per_face_cls = target_num_parcels_per_face_cls
    """
    target_num_parcels_per_face child of data_reduction.
    """
