#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .htc import htc as htc_cls
from .unsteady_statistics import unsteady_statistics as unsteady_statistics_cls
from .user_defined_coupling_variables_via_udm import user_defined_coupling_variables_via_udm as user_defined_coupling_variables_via_udm_cls
from .use_face_or_element_based_data_transfer import use_face_or_element_based_data_transfer as use_face_or_element_based_data_transfer_cls
from .write_scp_file import write_scp_file as write_scp_file_cls
from .connect_parallel import connect_parallel as connect_parallel_cls
from .init_and_solve import init_and_solve as init_and_solve_cls
from .solve import solve as solve_cls
class system_coupling(Group):
    """
    Enter the system coupling model menu.
    """

    fluent_name = "system-coupling"

    child_names = \
        ['htc', 'unsteady_statistics',
         'user_defined_coupling_variables_via_udm',
         'use_face_or_element_based_data_transfer']

    htc: htc_cls = htc_cls
    """
    htc child of system_coupling.
    """
    unsteady_statistics: unsteady_statistics_cls = unsteady_statistics_cls
    """
    unsteady_statistics child of system_coupling.
    """
    user_defined_coupling_variables_via_udm: user_defined_coupling_variables_via_udm_cls = user_defined_coupling_variables_via_udm_cls
    """
    user_defined_coupling_variables_via_udm child of system_coupling.
    """
    use_face_or_element_based_data_transfer: use_face_or_element_based_data_transfer_cls = use_face_or_element_based_data_transfer_cls
    """
    use_face_or_element_based_data_transfer child of system_coupling.
    """
    command_names = \
        ['write_scp_file', 'connect_parallel', 'init_and_solve', 'solve']

    write_scp_file: write_scp_file_cls = write_scp_file_cls
    """
    write_scp_file command of system_coupling.
    """
    connect_parallel: connect_parallel_cls = connect_parallel_cls
    """
    connect_parallel command of system_coupling.
    """
    init_and_solve: init_and_solve_cls = init_and_solve_cls
    """
    init_and_solve command of system_coupling.
    """
    solve: solve_cls = solve_cls
    """
    solve command of system_coupling.
    """
