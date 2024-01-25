#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .interrupt_at import interrupt_at as interrupt_at_cls
class interrupt(Command):
    """
    Interrupt the iterations.
    
    Parameters
    ----------
        interrupt_at : str
            Select when should the solution be interrupted.
    
    """

    fluent_name = "interrupt"

    argument_names = \
        ['interrupt_at']

    interrupt_at: interrupt_at_cls = interrupt_at_cls
    """
    interrupt_at argument of interrupt.
    """
