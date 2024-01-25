#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .init_from_data_file import init_from_data_file as init_from_data_file_cls
from .init_from_solution import init_from_solution as init_from_solution_cls
class initialization_method(Group):
    """
    'initialization_method' child.
    """

    fluent_name = "initialization-method"

    child_names = \
        ['init_from_data_file', 'init_from_solution']

    init_from_data_file: init_from_data_file_cls = init_from_data_file_cls
    """
    init_from_data_file child of initialization_method.
    """
    init_from_solution: init_from_solution_cls = init_from_solution_cls
    """
    init_from_solution child of initialization_method.
    """
