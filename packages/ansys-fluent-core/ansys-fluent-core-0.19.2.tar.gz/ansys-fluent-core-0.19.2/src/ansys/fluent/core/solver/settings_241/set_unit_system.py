#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .unit_system import unit_system as unit_system_cls
class set_unit_system(Command):
    """
    To apply standard set of units to all quantities.
    
    Parameters
    ----------
        unit_system : str
            'unit_system' child.
    
    """

    fluent_name = "set-unit-system"

    argument_names = \
        ['unit_system']

    unit_system: unit_system_cls = unit_system_cls
    """
    unit_system argument of set_unit_system.
    """
