#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_16 import enabled as enabled_cls
from .initialization_method import initialization_method as initialization_method_cls
from .case_modification import case_modification as case_modification_cls
from .automatic_initialization import automatic_initialization as automatic_initialization_cls
from .execute_strategy import execute_strategy as execute_strategy_cls
from .enable_strategy import enable_strategy as enable_strategy_cls
from .copy_modification import copy_modification as copy_modification_cls
from .delete_modification import delete_modification as delete_modification_cls
from .enable_modification import enable_modification as enable_modification_cls
from .disable_modification import disable_modification as disable_modification_cls
from .import_modifications import import_modifications as import_modifications_cls
from .export_modifications import export_modifications as export_modifications_cls
from .continue_strategy_execution import continue_strategy_execution as continue_strategy_execution_cls
class case_modification(Group):
    """
    'case_modification' child.
    """

    fluent_name = "case-modification"

    child_names = \
        ['enabled', 'initialization_method', 'case_modification']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of case_modification.
    """
    initialization_method: initialization_method_cls = initialization_method_cls
    """
    initialization_method child of case_modification.
    """
    case_modification: case_modification_cls = case_modification_cls
    """
    case_modification child of case_modification.
    """
    command_names = \
        ['automatic_initialization', 'execute_strategy', 'enable_strategy',
         'copy_modification', 'delete_modification', 'enable_modification',
         'disable_modification', 'import_modifications',
         'export_modifications', 'continue_strategy_execution']

    automatic_initialization: automatic_initialization_cls = automatic_initialization_cls
    """
    automatic_initialization command of case_modification.
    """
    execute_strategy: execute_strategy_cls = execute_strategy_cls
    """
    execute_strategy command of case_modification.
    """
    enable_strategy: enable_strategy_cls = enable_strategy_cls
    """
    enable_strategy command of case_modification.
    """
    copy_modification: copy_modification_cls = copy_modification_cls
    """
    copy_modification command of case_modification.
    """
    delete_modification: delete_modification_cls = delete_modification_cls
    """
    delete_modification command of case_modification.
    """
    enable_modification: enable_modification_cls = enable_modification_cls
    """
    enable_modification command of case_modification.
    """
    disable_modification: disable_modification_cls = disable_modification_cls
    """
    disable_modification command of case_modification.
    """
    import_modifications: import_modifications_cls = import_modifications_cls
    """
    import_modifications command of case_modification.
    """
    export_modifications: export_modifications_cls = export_modifications_cls
    """
    export_modifications command of case_modification.
    """
    continue_strategy_execution: continue_strategy_execution_cls = continue_strategy_execution_cls
    """
    continue_strategy_execution command of case_modification.
    """
