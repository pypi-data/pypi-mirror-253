#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .user_defined_functions import user_defined_functions as user_defined_functions_cls
from .sort_sample_files import sort_sample_files as sort_sample_files_cls
from .compute_3 import compute as compute_cls
from .start_file_write import start_file_write as start_file_write_cls
from .stop_file_write import stop_file_write as stop_file_write_cls
class sample_trajectories(Group):
    """
    'sample_trajectories' child.
    """

    fluent_name = "sample-trajectories"

    child_names = \
        ['user_defined_functions', 'sort_sample_files']

    user_defined_functions: user_defined_functions_cls = user_defined_functions_cls
    """
    user_defined_functions child of sample_trajectories.
    """
    sort_sample_files: sort_sample_files_cls = sort_sample_files_cls
    """
    sort_sample_files child of sample_trajectories.
    """
    command_names = \
        ['compute', 'start_file_write', 'stop_file_write']

    compute: compute_cls = compute_cls
    """
    compute command of sample_trajectories.
    """
    start_file_write: start_file_write_cls = start_file_write_cls
    """
    start_file_write command of sample_trajectories.
    """
    stop_file_write: stop_file_write_cls = stop_file_write_cls
    """
    stop_file_write command of sample_trajectories.
    """
