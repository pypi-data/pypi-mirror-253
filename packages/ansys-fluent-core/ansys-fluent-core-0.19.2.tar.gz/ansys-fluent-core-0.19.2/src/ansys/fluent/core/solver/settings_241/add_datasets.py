#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .zone_names_4 import zone_names as zone_names_cls
from .domain import domain as domain_cls
from .quantities import quantities as quantities_cls
from .min_2 import min as min_cls
from .max_2 import max as max_cls
from .mean_1 import mean as mean_cls
from .rmse_1 import rmse as rmse_cls
from .moving_average_1 import moving_average as moving_average_cls
from .average_over import average_over as average_over_cls
class add_datasets(Command):
    """
    Add datasets.
    
    Parameters
    ----------
        zone_names : typing.List[str]
            Enter zone name list.
        domain : str
            'domain' child.
        quantities : typing.List[str]
            'quantities' child.
        min : bool
            'min' child.
        max : bool
            'max' child.
        mean : bool
            'mean' child.
        rmse : bool
            'rmse' child.
        moving_average : bool
            'moving_average' child.
        average_over : int
            'average_over' child.
    
    """

    fluent_name = "add-datasets"

    argument_names = \
        ['zone_names', 'domain', 'quantities', 'min', 'max', 'mean', 'rmse',
         'moving_average', 'average_over']

    zone_names: zone_names_cls = zone_names_cls
    """
    zone_names argument of add_datasets.
    """
    domain: domain_cls = domain_cls
    """
    domain argument of add_datasets.
    """
    quantities: quantities_cls = quantities_cls
    """
    quantities argument of add_datasets.
    """
    min: min_cls = min_cls
    """
    min argument of add_datasets.
    """
    max: max_cls = max_cls
    """
    max argument of add_datasets.
    """
    mean: mean_cls = mean_cls
    """
    mean argument of add_datasets.
    """
    rmse: rmse_cls = rmse_cls
    """
    rmse argument of add_datasets.
    """
    moving_average: moving_average_cls = moving_average_cls
    """
    moving_average argument of add_datasets.
    """
    average_over: average_over_cls = average_over_cls
    """
    average_over argument of add_datasets.
    """
