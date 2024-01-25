#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .fensapice_flow_bc_subtype import fensapice_flow_bc_subtype as fensapice_flow_bc_subtype_cls
class icing(Group):
    """
    Help not available.
    """

    fluent_name = "icing"

    child_names = \
        ['fensapice_flow_bc_subtype']

    fensapice_flow_bc_subtype: fensapice_flow_bc_subtype_cls = fensapice_flow_bc_subtype_cls
    """
    fensapice_flow_bc_subtype child of icing.
    """
