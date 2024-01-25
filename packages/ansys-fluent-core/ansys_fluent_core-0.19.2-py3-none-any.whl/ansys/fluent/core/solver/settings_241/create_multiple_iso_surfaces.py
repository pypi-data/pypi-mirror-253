#
# This is an auto-generated file.  DO NOT EDIT!
#

from ansys.fluent.core.solver.flobject import *

from ansys.fluent.core.solver.flobject import _ChildNamedObjectAccessorMixin

from ansys.fluent.core.solver.flobject import _CreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _NonCreatableNamedObjectMixin

from ansys.fluent.core.solver.flobject import _HasAllowedValuesMixin

from .field_1 import field as field_cls
from .name_1 import name as name_cls
from .surfaces import surfaces as surfaces_cls
from .zones_4 import zones as zones_cls
from .iso_value import iso_value as iso_value_cls
from .no_of_surfaces import no_of_surfaces as no_of_surfaces_cls
from .spacing import spacing as spacing_cls
class create_multiple_iso_surfaces(Command):
    """
    'create_multiple_iso_surfaces' command.
    
    Parameters
    ----------
        field : str
            Specify Field.
        name : str
            'name' child.
        surfaces : typing.List[str]
            Select surface.
        zones : typing.List[str]
            Enter cell zone name list.
        iso_value : real
            'iso_value' child.
        no_of_surfaces : int
            'no_of_surfaces' child.
        spacing : real
            'spacing' child.
    
    """

    fluent_name = "create-multiple-iso-surfaces"

    argument_names = \
        ['field', 'name', 'surfaces', 'zones', 'iso_value', 'no_of_surfaces',
         'spacing']

    field: field_cls = field_cls
    """
    field argument of create_multiple_iso_surfaces.
    """
    name: name_cls = name_cls
    """
    name argument of create_multiple_iso_surfaces.
    """
    surfaces: surfaces_cls = surfaces_cls
    """
    surfaces argument of create_multiple_iso_surfaces.
    """
    zones: zones_cls = zones_cls
    """
    zones argument of create_multiple_iso_surfaces.
    """
    iso_value: iso_value_cls = iso_value_cls
    """
    iso_value argument of create_multiple_iso_surfaces.
    """
    no_of_surfaces: no_of_surfaces_cls = no_of_surfaces_cls
    """
    no_of_surfaces argument of create_multiple_iso_surfaces.
    """
    spacing: spacing_cls = spacing_cls
    """
    spacing argument of create_multiple_iso_surfaces.
    """
