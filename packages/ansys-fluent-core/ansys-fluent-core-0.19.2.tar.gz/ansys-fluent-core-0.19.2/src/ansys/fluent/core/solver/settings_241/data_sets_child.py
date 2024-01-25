#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zones_3 import zones as zones_cls
from .min_1 import min as min_cls
from .max_1 import max as max_cls
from .mean import mean as mean_cls
from .rmse import rmse as rmse_cls
from .moving_average import moving_average as moving_average_cls
from .average_over_1 import average_over as average_over_cls
class data_sets_child(Group):
    """
    'child_object_type' of data_sets.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['zones', 'min', 'max', 'mean', 'rmse', 'moving_average',
         'average_over']

    zones: zones_cls = zones_cls
    """
    zones child of data_sets_child.
    """
    min: min_cls = min_cls
    """
    min child of data_sets_child.
    """
    max: max_cls = max_cls
    """
    max child of data_sets_child.
    """
    mean: mean_cls = mean_cls
    """
    mean child of data_sets_child.
    """
    rmse: rmse_cls = rmse_cls
    """
    rmse child of data_sets_child.
    """
    moving_average: moving_average_cls = moving_average_cls
    """
    moving_average child of data_sets_child.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over child of data_sets_child.
    """
