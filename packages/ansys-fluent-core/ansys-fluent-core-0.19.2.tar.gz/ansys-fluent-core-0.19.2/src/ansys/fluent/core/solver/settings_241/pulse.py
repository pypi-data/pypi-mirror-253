#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .pulse_mode import pulse_mode as pulse_mode_cls
from .write_2 import write as write_cls
class pulse(Group):
    """
    Enter save pathline/particle tracks pulse menu.
    """

    fluent_name = "pulse"

    child_names = \
        ['pulse_mode']

    pulse_mode: pulse_mode_cls = pulse_mode_cls
    """
    pulse_mode child of pulse.
    """
    command_names = \
        ['write']

    write: write_cls = write_cls
    """
    write command of pulse.
    """
