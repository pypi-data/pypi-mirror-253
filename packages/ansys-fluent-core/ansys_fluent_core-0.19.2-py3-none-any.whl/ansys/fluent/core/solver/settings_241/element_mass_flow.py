#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .domain import domain as domain_cls
class element_mass_flow(Command):
    """
    'element_mass_flow' command.
    
    Parameters
    ----------
        domain : str
            'domain' child.
    
    """

    fluent_name = "element-mass-flow"

    argument_names = \
        ['domain']

    domain: domain_cls = domain_cls
    """
    domain argument of element_mass_flow.
    """
