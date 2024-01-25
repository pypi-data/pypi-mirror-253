#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enabled_1 import enabled as enabled_cls
from .clip_factor import clip_factor as clip_factor_cls
class production_limiter(Group):
    """
    'production_limiter' child.
    """

    fluent_name = "production-limiter"

    child_names = \
        ['enabled', 'clip_factor']

    enabled: enabled_cls = enabled_cls
    """
    enabled child of production_limiter.
    """
    clip_factor: clip_factor_cls = clip_factor_cls
    """
    clip_factor child of production_limiter.
    """
