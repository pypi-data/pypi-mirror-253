#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .save_mode import save_mode as save_mode_cls
from .continue_with_current_mesh import continue_with_current_mesh as continue_with_current_mesh_cls
from .discard_all_data import discard_all_data as discard_all_data_cls
class execute_strategy(Command):
    """
    Execute the automatic initialization and case modification strategy defined at present .
    
    Parameters
    ----------
        save_mode : str
            'save_mode' child.
        continue_with_current_mesh : bool
            Reloading of the upstream mesh data is desired. Is it needed to continue with currently loaded mesh?.
        discard_all_data : bool
            'discard_all_data' child.
    
    """

    fluent_name = "execute-strategy"

    argument_names = \
        ['save_mode', 'continue_with_current_mesh', 'discard_all_data']

    save_mode: save_mode_cls = save_mode_cls
    """
    save_mode argument of execute_strategy.
    """
    continue_with_current_mesh: continue_with_current_mesh_cls = continue_with_current_mesh_cls
    """
    continue_with_current_mesh argument of execute_strategy.
    """
    discard_all_data: discard_all_data_cls = discard_all_data_cls
    """
    discard_all_data argument of execute_strategy.
    """
