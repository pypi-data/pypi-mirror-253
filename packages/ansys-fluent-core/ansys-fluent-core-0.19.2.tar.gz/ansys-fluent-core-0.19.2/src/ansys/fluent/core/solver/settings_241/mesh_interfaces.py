#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .auto_options import auto_options as auto_options_cls
from .interface_1 import interface as interface_cls
from .turbo_interface import turbo_interface as turbo_interface_cls
from .enforce_continuity_after_bc import enforce_continuity_after_bc as enforce_continuity_after_bc_cls
from .coupled_interfaces_inherit_bcs import coupled_interfaces_inherit_bcs as coupled_interfaces_inherit_bcs_cls
from .verbosity_7 import verbosity as verbosity_cls
from .enable_si_with_nodes import enable_si_with_nodes as enable_si_with_nodes_cls
from .enforce_coupled_wall_between_solids import enforce_coupled_wall_between_solids as enforce_coupled_wall_between_solids_cls
from .enable_visualization_of_interfaces import enable_visualization_of_interfaces as enable_visualization_of_interfaces_cls
from .mapped_interface_options import mapped_interface_options as mapped_interface_options_cls
from .non_conformal_interface_numerics import non_conformal_interface_numerics as non_conformal_interface_numerics_cls
from .delete_2 import delete as delete_cls
from .display_1 import display as display_cls
from .list_1 import list as list_cls
from .make_phaselag_from_boundaries import make_phaselag_from_boundaries as make_phaselag_from_boundaries_cls
from .make_phaselag_from_periodic import make_phaselag_from_periodic as make_phaselag_from_periodic_cls
from .delete_interfaces_with_small_overlap import delete_interfaces_with_small_overlap as delete_interfaces_with_small_overlap_cls
from .delete_all import delete_all as delete_all_cls
from .improve_quality_1 import improve_quality as improve_quality_cls
from .one_to_one_pairing import one_to_one_pairing as one_to_one_pairing_cls
from .auto_pairing import auto_pairing as auto_pairing_cls
from .transfer_motion_across_interfaces import transfer_motion_across_interfaces as transfer_motion_across_interfaces_cls
from .remove_left_handed_interface_faces import remove_left_handed_interface_faces as remove_left_handed_interface_faces_cls
from .non_overlapping_zone_name_1 import non_overlapping_zone_name as non_overlapping_zone_name_cls
class mesh_interfaces(Group):
    """
    Enter the mesh interfaces menu.
    """

    fluent_name = "mesh-interfaces"

    child_names = \
        ['auto_options', 'interface', 'turbo_interface',
         'enforce_continuity_after_bc', 'coupled_interfaces_inherit_bcs',
         'verbosity', 'enable_si_with_nodes',
         'enforce_coupled_wall_between_solids',
         'enable_visualization_of_interfaces', 'mapped_interface_options',
         'non_conformal_interface_numerics']

    auto_options: auto_options_cls = auto_options_cls
    """
    auto_options child of mesh_interfaces.
    """
    interface: interface_cls = interface_cls
    """
    interface child of mesh_interfaces.
    """
    turbo_interface: turbo_interface_cls = turbo_interface_cls
    """
    turbo_interface child of mesh_interfaces.
    """
    enforce_continuity_after_bc: enforce_continuity_after_bc_cls = enforce_continuity_after_bc_cls
    """
    enforce_continuity_after_bc child of mesh_interfaces.
    """
    coupled_interfaces_inherit_bcs: coupled_interfaces_inherit_bcs_cls = coupled_interfaces_inherit_bcs_cls
    """
    coupled_interfaces_inherit_bcs child of mesh_interfaces.
    """
    verbosity: verbosity_cls = verbosity_cls
    """
    verbosity child of mesh_interfaces.
    """
    enable_si_with_nodes: enable_si_with_nodes_cls = enable_si_with_nodes_cls
    """
    enable_si_with_nodes child of mesh_interfaces.
    """
    enforce_coupled_wall_between_solids: enforce_coupled_wall_between_solids_cls = enforce_coupled_wall_between_solids_cls
    """
    enforce_coupled_wall_between_solids child of mesh_interfaces.
    """
    enable_visualization_of_interfaces: enable_visualization_of_interfaces_cls = enable_visualization_of_interfaces_cls
    """
    enable_visualization_of_interfaces child of mesh_interfaces.
    """
    mapped_interface_options: mapped_interface_options_cls = mapped_interface_options_cls
    """
    mapped_interface_options child of mesh_interfaces.
    """
    non_conformal_interface_numerics: non_conformal_interface_numerics_cls = non_conformal_interface_numerics_cls
    """
    non_conformal_interface_numerics child of mesh_interfaces.
    """
    command_names = \
        ['delete', 'display', 'list', 'make_phaselag_from_boundaries',
         'make_phaselag_from_periodic',
         'delete_interfaces_with_small_overlap', 'delete_all',
         'improve_quality', 'one_to_one_pairing', 'auto_pairing',
         'transfer_motion_across_interfaces',
         'remove_left_handed_interface_faces', 'non_overlapping_zone_name']

    delete: delete_cls = delete_cls
    """
    delete command of mesh_interfaces.
    """
    display: display_cls = display_cls
    """
    display command of mesh_interfaces.
    """
    list: list_cls = list_cls
    """
    list command of mesh_interfaces.
    """
    make_phaselag_from_boundaries: make_phaselag_from_boundaries_cls = make_phaselag_from_boundaries_cls
    """
    make_phaselag_from_boundaries command of mesh_interfaces.
    """
    make_phaselag_from_periodic: make_phaselag_from_periodic_cls = make_phaselag_from_periodic_cls
    """
    make_phaselag_from_periodic command of mesh_interfaces.
    """
    delete_interfaces_with_small_overlap: delete_interfaces_with_small_overlap_cls = delete_interfaces_with_small_overlap_cls
    """
    delete_interfaces_with_small_overlap command of mesh_interfaces.
    """
    delete_all: delete_all_cls = delete_all_cls
    """
    delete_all command of mesh_interfaces.
    """
    improve_quality: improve_quality_cls = improve_quality_cls
    """
    improve_quality command of mesh_interfaces.
    """
    one_to_one_pairing: one_to_one_pairing_cls = one_to_one_pairing_cls
    """
    one_to_one_pairing command of mesh_interfaces.
    """
    auto_pairing: auto_pairing_cls = auto_pairing_cls
    """
    auto_pairing command of mesh_interfaces.
    """
    transfer_motion_across_interfaces: transfer_motion_across_interfaces_cls = transfer_motion_across_interfaces_cls
    """
    transfer_motion_across_interfaces command of mesh_interfaces.
    """
    remove_left_handed_interface_faces: remove_left_handed_interface_faces_cls = remove_left_handed_interface_faces_cls
    """
    remove_left_handed_interface_faces command of mesh_interfaces.
    """
    non_overlapping_zone_name: non_overlapping_zone_name_cls = non_overlapping_zone_name_cls
    """
    non_overlapping_zone_name command of mesh_interfaces.
    """
