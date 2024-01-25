#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .print_process_statistics import print_process_statistics as print_process_statistics_cls
from .print_system_statistics import print_system_statistics as print_system_statistics_cls
from .print_gpgpu_statistics import print_gpgpu_statistics as print_gpgpu_statistics_cls
from .print_time_statistics import print_time_statistics as print_time_statistics_cls
class system(Group):
    """
    System menu.
    """

    fluent_name = "system"

    command_names = \
        ['print_process_statistics', 'print_system_statistics',
         'print_gpgpu_statistics', 'print_time_statistics']

    print_process_statistics: print_process_statistics_cls = print_process_statistics_cls
    """
    print_process_statistics command of system.
    """
    print_system_statistics: print_system_statistics_cls = print_system_statistics_cls
    """
    print_system_statistics command of system.
    """
    print_gpgpu_statistics: print_gpgpu_statistics_cls = print_gpgpu_statistics_cls
    """
    print_gpgpu_statistics command of system.
    """
    print_time_statistics: print_time_statistics_cls = print_time_statistics_cls
    """
    print_time_statistics command of system.
    """
