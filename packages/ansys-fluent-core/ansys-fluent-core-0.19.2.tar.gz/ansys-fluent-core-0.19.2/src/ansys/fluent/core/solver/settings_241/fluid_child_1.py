#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .name import name as name_cls
from .phase import phase as phase_cls
from .material_1 import material as material_cls
from .cylindrical_fixed_var import cylindrical_fixed_var as cylindrical_fixed_var_cls
from .participates_in_radiation import participates_in_radiation as participates_in_radiation_cls
from .contact_property import contact_property as contact_property_cls
from .active_wetsteam_zone import active_wetsteam_zone as active_wetsteam_zone_cls
from .vapor_phase_realgas import vapor_phase_realgas as vapor_phase_realgas_cls
from .laminar import laminar as laminar_cls
from .glass import glass as glass_cls
from .reference_frame_1 import reference_frame as reference_frame_cls
from .mesh_motion_1 import mesh_motion as mesh_motion_cls
from .porous_zone import porous_zone as porous_zone_cls
from .fan_zone_1 import fan_zone as fan_zone_cls
from .embedded_les import embedded_les as embedded_les_cls
from .reaction import reaction as reaction_cls
from .source_terms_3 import source_terms as source_terms_cls
from .fixed_values import fixed_values as fixed_values_cls
from .multiphase_1 import multiphase as multiphase_cls
from .disabled import disabled as disabled_cls
class fluid_child(Group):
    """
    'child_object_type' of fluid.
    """

    fluent_name = "child-object-type"

    child_names = \
        ['name', 'phase', 'material', 'cylindrical_fixed_var',
         'participates_in_radiation', 'contact_property',
         'active_wetsteam_zone', 'vapor_phase_realgas', 'laminar', 'glass',
         'reference_frame', 'mesh_motion', 'porous_zone', 'fan_zone',
         'embedded_les', 'reaction', 'source_terms', 'fixed_values',
         'multiphase', 'disabled']

    name: name_cls = name_cls
    """
    name child of fluid_child.
    """
    phase: phase_cls = phase_cls
    """
    phase child of fluid_child.
    """
    material: material_cls = material_cls
    """
    material child of fluid_child.
    """
    cylindrical_fixed_var: cylindrical_fixed_var_cls = cylindrical_fixed_var_cls
    """
    cylindrical_fixed_var child of fluid_child.
    """
    participates_in_radiation: participates_in_radiation_cls = participates_in_radiation_cls
    """
    participates_in_radiation child of fluid_child.
    """
    contact_property: contact_property_cls = contact_property_cls
    """
    contact_property child of fluid_child.
    """
    active_wetsteam_zone: active_wetsteam_zone_cls = active_wetsteam_zone_cls
    """
    active_wetsteam_zone child of fluid_child.
    """
    vapor_phase_realgas: vapor_phase_realgas_cls = vapor_phase_realgas_cls
    """
    vapor_phase_realgas child of fluid_child.
    """
    laminar: laminar_cls = laminar_cls
    """
    laminar child of fluid_child.
    """
    glass: glass_cls = glass_cls
    """
    glass child of fluid_child.
    """
    reference_frame: reference_frame_cls = reference_frame_cls
    """
    reference_frame child of fluid_child.
    """
    mesh_motion: mesh_motion_cls = mesh_motion_cls
    """
    mesh_motion child of fluid_child.
    """
    porous_zone: porous_zone_cls = porous_zone_cls
    """
    porous_zone child of fluid_child.
    """
    fan_zone: fan_zone_cls = fan_zone_cls
    """
    fan_zone child of fluid_child.
    """
    embedded_les: embedded_les_cls = embedded_les_cls
    """
    embedded_les child of fluid_child.
    """
    reaction: reaction_cls = reaction_cls
    """
    reaction child of fluid_child.
    """
    source_terms: source_terms_cls = source_terms_cls
    """
    source_terms child of fluid_child.
    """
    fixed_values: fixed_values_cls = fixed_values_cls
    """
    fixed_values child of fluid_child.
    """
    multiphase: multiphase_cls = multiphase_cls
    """
    multiphase child of fluid_child.
    """
    disabled: disabled_cls = disabled_cls
    """
    disabled child of fluid_child.
    """
