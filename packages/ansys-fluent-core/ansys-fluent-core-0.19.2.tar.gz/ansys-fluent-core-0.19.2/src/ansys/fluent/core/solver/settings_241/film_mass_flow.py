#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .domain import domain as domain_cls
from .all_boundary_zones import all_boundary_zones as all_boundary_zones_cls
from .zones_1 import zones as zones_cls
from .physics_1 import physics as physics_cls
from .write_to_file_1 import write_to_file as write_to_file_cls
from .file_name_1 import file_name as file_name_cls
from .append_data import append_data as append_data_cls
class film_mass_flow(Command):
    """
    Print film mass flow rate at boundaries.
    
    Parameters
    ----------
        domain : str
            'domain' child.
        all_boundary_zones : bool
            Select all the boundary/interior zones.
        zones : typing.List[str]
            Enter zone name list.
        physics : typing.List[str]
            'physics' child.
        write_to_file : bool
            'write_to_file' child.
        file_name : str
            'file_name' child.
        append_data : bool
            'append_data' child.
    
    """

    fluent_name = "film-mass-flow"

    argument_names = \
        ['domain', 'all_boundary_zones', 'zones', 'physics', 'write_to_file',
         'file_name', 'append_data']

    domain: domain_cls = domain_cls
    """
    domain argument of film_mass_flow.
    """
    all_boundary_zones: all_boundary_zones_cls = all_boundary_zones_cls
    """
    all_boundary_zones argument of film_mass_flow.
    """
    zones: zones_cls = zones_cls
    """
    zones argument of film_mass_flow.
    """
    physics: physics_cls = physics_cls
    """
    physics argument of film_mass_flow.
    """
    write_to_file: write_to_file_cls = write_to_file_cls
    """
    write_to_file argument of film_mass_flow.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of film_mass_flow.
    """
    append_data: append_data_cls = append_data_cls
    """
    append_data argument of film_mass_flow.
    """
