#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .option import option as option_cls
from .domain import domain as domain_cls
from .all_wall_zones import all_wall_zones as all_wall_zones_cls
from .wall_zones_1 import wall_zones as wall_zones_cls
from .direction_vector_2 import direction_vector as direction_vector_cls
from .momentum_center import momentum_center as momentum_center_cls
from .momentum_axis import momentum_axis as momentum_axis_cls
from .pressure_coordinate import pressure_coordinate as pressure_coordinate_cls
from .coordinate_value import coordinate_value as coordinate_value_cls
from .write_to_file_1 import write_to_file as write_to_file_cls
from .file_name_1 import file_name as file_name_cls
from .append_data import append_data as append_data_cls
class forces(Command):
    """
    'forces' command.
    
    Parameters
    ----------
        option : str
            'option' child.
        domain : str
            'domain' child.
        all_wall_zones : bool
            Select all wall zones available.
        wall_zones : typing.List[str]
            Enter wall zone name list.
        direction_vector : typing.List[real]
            'direction_vector' child.
        momentum_center : typing.List[real]
            'momentum_center' child.
        momentum_axis : typing.List[real]
            'momentum_axis' child.
        pressure_coordinate : str
            'pressure_coordinate' child.
        coordinate_value : real
            'coordinate_value' child.
        write_to_file : bool
            'write_to_file' child.
        file_name : str
            'file_name' child.
        append_data : bool
            'append_data' child.
    
    """

    fluent_name = "forces"

    argument_names = \
        ['option', 'domain', 'all_wall_zones', 'wall_zones',
         'direction_vector', 'momentum_center', 'momentum_axis',
         'pressure_coordinate', 'coordinate_value', 'write_to_file',
         'file_name', 'append_data']

    option: option_cls = option_cls
    """
    option argument of forces.
    """
    domain: domain_cls = domain_cls
    """
    domain argument of forces.
    """
    all_wall_zones: all_wall_zones_cls = all_wall_zones_cls
    """
    all_wall_zones argument of forces.
    """
    wall_zones: wall_zones_cls = wall_zones_cls
    """
    wall_zones argument of forces.
    """
    direction_vector: direction_vector_cls = direction_vector_cls
    """
    direction_vector argument of forces.
    """
    momentum_center: momentum_center_cls = momentum_center_cls
    """
    momentum_center argument of forces.
    """
    momentum_axis: momentum_axis_cls = momentum_axis_cls
    """
    momentum_axis argument of forces.
    """
    pressure_coordinate: pressure_coordinate_cls = pressure_coordinate_cls
    """
    pressure_coordinate argument of forces.
    """
    coordinate_value: coordinate_value_cls = coordinate_value_cls
    """
    coordinate_value argument of forces.
    """
    write_to_file: write_to_file_cls = write_to_file_cls
    """
    write_to_file argument of forces.
    """
    file_name: file_name_cls = file_name_cls
    """
    file_name argument of forces.
    """
    append_data: append_data_cls = append_data_cls
    """
    append_data argument of forces.
    """
