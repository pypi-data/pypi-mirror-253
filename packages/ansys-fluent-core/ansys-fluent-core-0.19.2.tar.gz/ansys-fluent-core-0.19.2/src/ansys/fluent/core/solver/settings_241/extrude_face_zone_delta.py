#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .face_zone import face_zone as face_zone_cls
from .distance_delta import distance_delta as distance_delta_cls
class extrude_face_zone_delta(Command):
    """
    Extrude a face thread a specified distance based on a list of deltas.
    
    Parameters
    ----------
        face_zone : str
            Enter a zone name.
        distance_delta : typing.List[real]
            'distance_delta' child.
    
    """

    fluent_name = "extrude-face-zone-delta"

    argument_names = \
        ['face_zone', 'distance_delta']

    face_zone: face_zone_cls = face_zone_cls
    """
    face_zone argument of extrude_face_zone_delta.
    """
    distance_delta: distance_delta_cls = distance_delta_cls
    """
    distance_delta argument of extrude_face_zone_delta.
    """
