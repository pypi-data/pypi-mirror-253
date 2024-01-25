#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .names import names as names_cls
class compute(Command):
    """
    'compute' command.
    
    Parameters
    ----------
        names : typing.List[str]
            'names' child.
    
    """

    fluent_name = "compute"

    argument_names = \
        ['names']

    names: names_cls = names_cls
    """
    names argument of compute.
    """
