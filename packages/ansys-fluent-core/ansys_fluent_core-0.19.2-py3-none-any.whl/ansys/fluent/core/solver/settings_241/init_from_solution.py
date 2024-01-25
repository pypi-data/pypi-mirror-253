#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option_12 import option as option_cls
from .init_from_data_file import init_from_data_file as init_from_data_file_cls
class init_from_solution(Group):
    """
    Choose how to initialize if no solution data exists.
    """

    fluent_name = "init-from-solution"

    child_names = \
        ['option', 'init_from_data_file']

    option: option_cls = option_cls
    """
    option child of init_from_solution.
    """
    init_from_data_file: init_from_data_file_cls = init_from_data_file_cls
    """
    init_from_data_file child of init_from_solution.
    """
