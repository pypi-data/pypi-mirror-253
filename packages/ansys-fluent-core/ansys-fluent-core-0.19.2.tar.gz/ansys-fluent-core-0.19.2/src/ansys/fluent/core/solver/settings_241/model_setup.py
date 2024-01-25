#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .ninjections import ninjections as ninjections_cls
from .urf import urf as urf_cls
from .injection import injection as injection_cls
class model_setup(Group):
    """
    'model_setup' child.
    """

    fluent_name = "model-setup"

    child_names = \
        ['ninjections', 'urf', 'injection']

    ninjections: ninjections_cls = ninjections_cls
    """
    ninjections child of model_setup.
    """
    urf: urf_cls = urf_cls
    """
    urf child of model_setup.
    """
    injection: injection_cls = injection_cls
    """
    injection child of model_setup.
    """
