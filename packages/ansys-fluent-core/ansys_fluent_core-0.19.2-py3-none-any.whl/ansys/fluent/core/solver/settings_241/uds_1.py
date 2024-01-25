#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .uds_bc import uds_bc as uds_bc_cls
from .uds import uds as uds_cls
class uds(Group):
    """
    Help not available.
    """

    fluent_name = "uds"

    child_names = \
        ['uds_bc', 'uds']

    uds_bc: uds_bc_cls = uds_bc_cls
    """
    uds_bc child of uds.
    """
    uds: uds_cls = uds_cls
    """
    uds child of uds.
    """
