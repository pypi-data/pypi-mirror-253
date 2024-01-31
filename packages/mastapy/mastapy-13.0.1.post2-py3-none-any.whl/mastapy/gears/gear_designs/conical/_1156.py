"""ConicalGearSetDesign"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.gear_designs import _950
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalGearSetDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1155


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetDesign",)


Self = TypeVar("Self", bound="ConicalGearSetDesign")


class ConicalGearSetDesign(_950.GearSetDesign):
    """ConicalGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetDesign")

    class _Cast_ConicalGearSetDesign:
        """Special nested class for casting ConicalGearSetDesign to subclasses."""

        def __init__(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
            parent: "ConicalGearSetDesign",
        ):
            self._parent = parent

        @property
        def gear_set_design(self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign"):
            return self._parent._cast(_950.GearSetDesign)

        @property
        def gear_design_component(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs import _948

            return self._parent._cast(_948.GearDesignComponent)

        @property
        def zerol_bevel_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.zerol_bevel import _954

            return self._parent._cast(_954.ZerolBevelGearSetDesign)

        @property
        def straight_bevel_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.straight_bevel import _963

            return self._parent._cast(_963.StraightBevelGearSetDesign)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.straight_bevel_diff import _967

            return self._parent._cast(_967.StraightBevelDiffGearSetDesign)

        @property
        def spiral_bevel_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.spiral_bevel import _971

            return self._parent._cast(_971.SpiralBevelGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _975

            return self._parent._cast(
                _975.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _979

            return self._parent._cast(_979.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_conical_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.klingelnberg_conical import _983

            return self._parent._cast(_983.KlingelnbergConicalGearSetDesign)

        @property
        def hypoid_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.hypoid import _987

            return self._parent._cast(_987.HypoidGearSetDesign)

        @property
        def bevel_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.bevel import _1182

            return self._parent._cast(_1182.BevelGearSetDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1195

            return self._parent._cast(_1195.AGMAGleasonConicalGearSetDesign)

        @property
        def conical_gear_set_design(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign",
        ) -> "ConicalGearSetDesign":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetDesign._Cast_ConicalGearSetDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def circular_pitch(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CircularPitch

        if temp is None:
            return 0.0

        return temp

    @property
    def cutter_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CutterRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def dominant_pinion(
        self: Self,
    ) -> "list_with_selected_item.ListWithSelectedItem_str":
        """ListWithSelectedItem[str]"""
        temp = self.wrapped.DominantPinion

        if temp is None:
            return ""

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.list_with_selected_item",
            "ListWithSelectedItem_str",
        )(temp)

    @dominant_pinion.setter
    @enforce_parameter_types
    def dominant_pinion(self: Self, value: "str"):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else ""
        )
        self.wrapped.DominantPinion = value

    @property
    def imported_xml_file_name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ImportedXMLFileName

        if temp is None:
            return ""

        return temp

    @property
    def mean_normal_module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MeanNormalModule

        if temp is None:
            return 0.0

        return temp

    @mean_normal_module.setter
    @enforce_parameter_types
    def mean_normal_module(self: Self, value: "float"):
        self.wrapped.MeanNormalModule = float(value) if value is not None else 0.0

    @property
    def module(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @module.setter
    @enforce_parameter_types
    def module(self: Self, value: "float"):
        self.wrapped.Module = float(value) if value is not None else 0.0

    @property
    def wheel_finish_cutter_point_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelFinishCutterPointWidth

        if temp is None:
            return 0.0

        return temp

    @wheel_finish_cutter_point_width.setter
    @enforce_parameter_types
    def wheel_finish_cutter_point_width(self: Self, value: "float"):
        self.wrapped.WheelFinishCutterPointWidth = (
            float(value) if value is not None else 0.0
        )

    @property
    def wheel_mean_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelMeanConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_outer_cone_distance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelOuterConeDistance

        if temp is None:
            return 0.0

        return temp

    @property
    def wheel_pitch_diameter(self: Self) -> "float":
        """float"""
        temp = self.wrapped.WheelPitchDiameter

        if temp is None:
            return 0.0

        return temp

    @wheel_pitch_diameter.setter
    @enforce_parameter_types
    def wheel_pitch_diameter(self: Self, value: "float"):
        self.wrapped.WheelPitchDiameter = float(value) if value is not None else 0.0

    @property
    def conical_meshes(self: Self) -> "List[_1155.ConicalGearMeshDesign]":
        """List[mastapy.gears.gear_designs.conical.ConicalGearMeshDesign]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearSetDesign._Cast_ConicalGearSetDesign":
        return self._Cast_ConicalGearSetDesign(self)
