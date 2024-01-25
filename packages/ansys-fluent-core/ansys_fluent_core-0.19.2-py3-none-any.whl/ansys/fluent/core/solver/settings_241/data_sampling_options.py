#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .data_sets import data_sets as data_sets_cls
from .add_datasets import add_datasets as add_datasets_cls
from .list_datasets import list_datasets as list_datasets_cls
class data_sampling_options(Group):
    """
    Data sampling options for statistics.
    """

    fluent_name = "data-sampling-options"

    child_names = \
        ['data_sets']

    data_sets: data_sets_cls = data_sets_cls
    """
    data_sets child of data_sampling_options.
    """
    command_names = \
        ['add_datasets', 'list_datasets']

    add_datasets: add_datasets_cls = add_datasets_cls
    """
    add_datasets command of data_sampling_options.
    """
    list_datasets: list_datasets_cls = list_datasets_cls
    """
    list_datasets command of data_sampling_options.
    """
