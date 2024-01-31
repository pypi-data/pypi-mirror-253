"""FESubstructureWithSelectionComponents"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import (
    _209,
    _210,
    _211,
    _208,
    _212,
    _213,
    _214,
    _215,
)
from mastapy.system_model.fe import _2390
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_SUBSTRUCTURE_WITH_SELECTION_COMPONENTS = python_net_import(
    "SMT.MastaAPI.SystemModel.FE", "FESubstructureWithSelectionComponents"
)

if TYPE_CHECKING:
    from mastapy.math_utility import _1499
    from mastapy.system_model.fe import _2376, _2367, _2368, _2399
    from mastapy.system_model.fe.links import _2420


__docformat__ = "restructuredtext en"
__all__ = ("FESubstructureWithSelectionComponents",)


Self = TypeVar("Self", bound="FESubstructureWithSelectionComponents")


class FESubstructureWithSelectionComponents(_2390.FESubstructureWithSelection):
    """FESubstructureWithSelectionComponents

    This is a mastapy class.
    """

    TYPE = _FE_SUBSTRUCTURE_WITH_SELECTION_COMPONENTS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FESubstructureWithSelectionComponents"
    )

    class _Cast_FESubstructureWithSelectionComponents:
        """Special nested class for casting FESubstructureWithSelectionComponents to subclasses."""

        def __init__(
            self: "FESubstructureWithSelectionComponents._Cast_FESubstructureWithSelectionComponents",
            parent: "FESubstructureWithSelectionComponents",
        ):
            self._parent = parent

        @property
        def fe_substructure_with_selection(
            self: "FESubstructureWithSelectionComponents._Cast_FESubstructureWithSelectionComponents",
        ):
            return self._parent._cast(_2390.FESubstructureWithSelection)

        @property
        def base_fe_with_selection(
            self: "FESubstructureWithSelectionComponents._Cast_FESubstructureWithSelectionComponents",
        ):
            from mastapy.system_model.fe import _2360

            return self._parent._cast(_2360.BaseFEWithSelection)

        @property
        def fe_substructure_with_selection_components(
            self: "FESubstructureWithSelectionComponents._Cast_FESubstructureWithSelectionComponents",
        ) -> "FESubstructureWithSelectionComponents":
            return self._parent

        def __getattr__(
            self: "FESubstructureWithSelectionComponents._Cast_FESubstructureWithSelectionComponents",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "FESubstructureWithSelectionComponents.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def radius_of_circle_through_selected_nodes(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadiusOfCircleThroughSelectedNodes

        if temp is None:
            return 0.0

        return temp

    @property
    def centre_of_circle_through_selected_nodes(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CentreOfCircleThroughSelectedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def distance_between_selected_nodes(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceBetweenSelectedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def manual_alignment(self: Self) -> "_1499.CoordinateSystemEditor":
        """mastapy.math_utility.CoordinateSystemEditor

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ManualAlignment

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def midpoint_of_selected_nodes(self: Self) -> "Vector3D":
        """Vector3D

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MidpointOfSelectedNodes

        if temp is None:
            return None

        value = conversion.pn_to_mp_vector3d(temp)

        if value is None:
            return None

        return value

    @property
    def beam_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_209.ElementPropertiesBeam]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesBeam]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BeamElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_links(self: Self) -> "List[_2420.FELinkWithSelection]":
        """List[mastapy.system_model.fe.links.FELinkWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLinks

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def contact_pairs(self: Self) -> "List[_2367.ContactPairWithSelection]":
        """List[mastapy.system_model.fe.ContactPairWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ContactPairs

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def coordinate_systems(self: Self) -> "List[_2368.CoordinateSystemWithSelection]":
        """List[mastapy.system_model.fe.CoordinateSystemWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoordinateSystems

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def interface_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_210.ElementPropertiesInterface]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesInterface]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.InterfaceElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def links_for_electric_machine(self: Self) -> "List[_2420.FELinkWithSelection]":
        """List[mastapy.system_model.fe.links.FELinkWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinksForElectricMachine

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def links_for_selected_component(self: Self) -> "List[_2420.FELinkWithSelection]":
        """List[mastapy.system_model.fe.links.FELinkWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinksForSelectedComponent

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def mass_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_211.ElementPropertiesMass]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesMass]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def materials(self: Self) -> "List[_2399.MaterialPropertiesWithSelection]":
        """List[mastapy.system_model.fe.MaterialPropertiesWithSelection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Materials

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def other_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_208.ElementPropertiesBase]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesBase]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.OtherElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def rigid_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_212.ElementPropertiesRigid]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesRigid]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shell_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_213.ElementPropertiesShell]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesShell]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShellElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def solid_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_214.ElementPropertiesSolid]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesSolid]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SolidElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def spring_dashpot_element_properties(
        self: Self,
    ) -> "List[_2376.ElementPropertiesWithSelection[_215.ElementPropertiesSpringDashpot]]":
        """List[mastapy.system_model.fe.ElementPropertiesWithSelection[mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting.ElementPropertiesSpringDashpot]]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpringDashpotElementProperties

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def auto_select_node_ring(self: Self):
        """Method does not return."""
        self.wrapped.AutoSelectNodeRing()

    def replace_selected_shaft(self: Self):
        """Method does not return."""
        self.wrapped.ReplaceSelectedShaft()

    def use_selected_component_for_alignment(self: Self):
        """Method does not return."""
        self.wrapped.UseSelectedComponentForAlignment()

    @property
    def cast_to(
        self: Self,
    ) -> "FESubstructureWithSelectionComponents._Cast_FESubstructureWithSelectionComponents":
        return self._Cast_FESubstructureWithSelectionComponents(self)
