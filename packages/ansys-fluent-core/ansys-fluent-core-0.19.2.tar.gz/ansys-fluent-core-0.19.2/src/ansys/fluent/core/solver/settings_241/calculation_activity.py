#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .execute_commands import execute_commands as execute_commands_cls
from .solution_animations import solution_animations as solution_animations_cls
from .case_modification_1 import case_modification as case_modification_cls
from .poor_mesh_numerics import poor_mesh_numerics as poor_mesh_numerics_cls
class calculation_activity(Group):
    """
    'calculation_activity' child.
    """

    fluent_name = "calculation-activity"

    child_names = \
        ['execute_commands', 'solution_animations', 'case_modification',
         'poor_mesh_numerics']

    execute_commands: execute_commands_cls = execute_commands_cls
    """
    execute_commands child of calculation_activity.
    """
    solution_animations: solution_animations_cls = solution_animations_cls
    """
    solution_animations child of calculation_activity.
    """
    case_modification: case_modification_cls = case_modification_cls
    """
    case_modification child of calculation_activity.
    """
    poor_mesh_numerics: poor_mesh_numerics_cls = poor_mesh_numerics_cls
    """
    poor_mesh_numerics child of calculation_activity.
    """
