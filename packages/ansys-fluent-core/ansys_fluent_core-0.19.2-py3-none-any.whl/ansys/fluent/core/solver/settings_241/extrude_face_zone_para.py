#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .face_zone import face_zone as face_zone_cls
from .normal_distance import normal_distance as normal_distance_cls
from .parametric_coordinates import parametric_coordinates as parametric_coordinates_cls
class extrude_face_zone_para(Command):
    """
    Extrude a face thread a specified distance based on a distance and a list of parametric locations between 0 and 1 (eg. 0 0.2 0.4 0.8 1.0).
    
    Parameters
    ----------
        face_zone : str
            Enter a zone name.
        normal_distance : real
            'normal_distance' child.
        parametric_coordinates : typing.List[real]
            'parametric_coordinates' child.
    
    """

    fluent_name = "extrude-face-zone-para"

    argument_names = \
        ['face_zone', 'normal_distance', 'parametric_coordinates']

    face_zone: face_zone_cls = face_zone_cls
    """
    face_zone argument of extrude_face_zone_para.
    """
    normal_distance: normal_distance_cls = normal_distance_cls
    """
    normal_distance argument of extrude_face_zone_para.
    """
    parametric_coordinates: parametric_coordinates_cls = parametric_coordinates_cls
    """
    parametric_coordinates argument of extrude_face_zone_para.
    """
