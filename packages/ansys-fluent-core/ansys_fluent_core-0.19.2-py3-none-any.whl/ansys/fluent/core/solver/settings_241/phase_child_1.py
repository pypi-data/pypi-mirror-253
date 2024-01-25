#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .material_1 import material as material_cls
from .participates_in_radiation import participates_in_radiation as participates_in_radiation_cls
from .reference_frame_1 import reference_frame as reference_frame_cls
from .mesh_motion_1 import mesh_motion as mesh_motion_cls
from .solid_motion_1 import solid_motion as solid_motion_cls
from .source_terms_3 import source_terms as source_terms_cls
from .fixed_values_1 import fixed_values as fixed_values_cls
from .material_orientation import material_orientation as material_orientation_cls
from .disabled_1 import disabled as disabled_cls
from .internal import internal as internal_cls
class phase_child(Group):
    """
    'child_object_type' of phase.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['material', 'participates_in_radiation', 'reference_frame',
         'mesh_motion', 'solid_motion', 'source_terms', 'fixed_values',
         'material_orientation', 'disabled', 'internal']

    material: material_cls = material_cls
    """
    material child of phase_child.
    """
    participates_in_radiation: participates_in_radiation_cls = participates_in_radiation_cls
    """
    participates_in_radiation child of phase_child.
    """
    reference_frame: reference_frame_cls = reference_frame_cls
    """
    reference_frame child of phase_child.
    """
    mesh_motion: mesh_motion_cls = mesh_motion_cls
    """
    mesh_motion child of phase_child.
    """
    solid_motion: solid_motion_cls = solid_motion_cls
    """
    solid_motion child of phase_child.
    """
    source_terms: source_terms_cls = source_terms_cls
    """
    source_terms child of phase_child.
    """
    fixed_values: fixed_values_cls = fixed_values_cls
    """
    fixed_values child of phase_child.
    """
    material_orientation: material_orientation_cls = material_orientation_cls
    """
    material_orientation child of phase_child.
    """
    disabled: disabled_cls = disabled_cls
    """
    disabled child of phase_child.
    """
    internal: internal_cls = internal_cls
    """
    internal child of phase_child.
    """
