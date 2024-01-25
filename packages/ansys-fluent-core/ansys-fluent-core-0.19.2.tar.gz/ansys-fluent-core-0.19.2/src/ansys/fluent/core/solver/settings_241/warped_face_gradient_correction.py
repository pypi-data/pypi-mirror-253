#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .enable_14 import enable as enable_cls
from .mode_1 import mode as mode_cls
from .turbulence_options import turbulence_options as turbulence_options_cls
class warped_face_gradient_correction(Group):
    """
    Enter warped-face-gradient-correction menu.
    """

    fluent_name = "warped-face-gradient-correction"

    child_names = \
        ['enable', 'mode', 'turbulence_options']

    enable: enable_cls = enable_cls
    """
    enable child of warped_face_gradient_correction.
    """
    mode: mode_cls = mode_cls
    """
    mode child of warped_face_gradient_correction.
    """
    turbulence_options: turbulence_options_cls = turbulence_options_cls
    """
    turbulence_options child of warped_face_gradient_correction.
    """
