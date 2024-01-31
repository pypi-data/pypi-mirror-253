"""GearDesignComponent"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Any, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN_COMPONENT = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns", "GearDesignComponent"
)

if TYPE_CHECKING:
    from mastapy.utility.scripting import _1741


__docformat__ = "restructuredtext en"
__all__ = ("GearDesignComponent",)


Self = TypeVar("Self", bound="GearDesignComponent")


class GearDesignComponent(_0.APIBase):
    """GearDesignComponent

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN_COMPONENT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesignComponent")

    class _Cast_GearDesignComponent:
        """Special nested class for casting GearDesignComponent to subclasses."""

        def __init__(
            self: "GearDesignComponent._Cast_GearDesignComponent",
            parent: "GearDesignComponent",
        ):
            self._parent = parent

        @property
        def gear_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs import _947

            return self._parent._cast(_947.GearDesign)

        @property
        def gear_mesh_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearMeshDesign)

        @property
        def gear_set_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs import _950

            return self._parent._cast(_950.GearSetDesign)

        @property
        def zerol_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.zerol_bevel import _952

            return self._parent._cast(_952.ZerolBevelGearDesign)

        @property
        def zerol_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.zerol_bevel import _953

            return self._parent._cast(_953.ZerolBevelGearMeshDesign)

        @property
        def zerol_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.zerol_bevel import _954

            return self._parent._cast(_954.ZerolBevelGearSetDesign)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.zerol_bevel import _955

            return self._parent._cast(_955.ZerolBevelMeshedGearDesign)

        @property
        def worm_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.worm import _956

            return self._parent._cast(_956.WormDesign)

        @property
        def worm_gear_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.worm import _957

            return self._parent._cast(_957.WormGearDesign)

        @property
        def worm_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.worm import _958

            return self._parent._cast(_958.WormGearMeshDesign)

        @property
        def worm_gear_set_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.worm import _959

            return self._parent._cast(_959.WormGearSetDesign)

        @property
        def worm_wheel_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.worm import _960

            return self._parent._cast(_960.WormWheelDesign)

        @property
        def straight_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel import _961

            return self._parent._cast(_961.StraightBevelGearDesign)

        @property
        def straight_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel import _962

            return self._parent._cast(_962.StraightBevelGearMeshDesign)

        @property
        def straight_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel import _963

            return self._parent._cast(_963.StraightBevelGearSetDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel import _964

            return self._parent._cast(_964.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel_diff import _965

            return self._parent._cast(_965.StraightBevelDiffGearDesign)

        @property
        def straight_bevel_diff_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel_diff import _966

            return self._parent._cast(_966.StraightBevelDiffGearMeshDesign)

        @property
        def straight_bevel_diff_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel_diff import _967

            return self._parent._cast(_967.StraightBevelDiffGearSetDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.straight_bevel_diff import _968

            return self._parent._cast(_968.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.spiral_bevel import _969

            return self._parent._cast(_969.SpiralBevelGearDesign)

        @property
        def spiral_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.spiral_bevel import _970

            return self._parent._cast(_970.SpiralBevelGearMeshDesign)

        @property
        def spiral_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.spiral_bevel import _971

            return self._parent._cast(_971.SpiralBevelGearSetDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.spiral_bevel import _972

            return self._parent._cast(_972.SpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _973

            return self._parent._cast(
                _973.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _974

            return self._parent._cast(
                _974.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _975

            return self._parent._cast(
                _975.KlingelnbergCycloPalloidSpiralBevelGearSetDesign
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _976

            return self._parent._cast(
                _976.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _977

            return self._parent._cast(_977.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _978

            return self._parent._cast(_978.KlingelnbergCycloPalloidHypoidGearMeshDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _979

            return self._parent._cast(_979.KlingelnbergCycloPalloidHypoidGearSetDesign)

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _980

            return self._parent._cast(
                _980.KlingelnbergCycloPalloidHypoidMeshedGearDesign
            )

        @property
        def klingelnberg_conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_conical import _981

            return self._parent._cast(_981.KlingelnbergConicalGearDesign)

        @property
        def klingelnberg_conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_conical import _982

            return self._parent._cast(_982.KlingelnbergConicalGearMeshDesign)

        @property
        def klingelnberg_conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_conical import _983

            return self._parent._cast(_983.KlingelnbergConicalGearSetDesign)

        @property
        def klingelnberg_conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.klingelnberg_conical import _984

            return self._parent._cast(_984.KlingelnbergConicalMeshedGearDesign)

        @property
        def hypoid_gear_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.hypoid import _985

            return self._parent._cast(_985.HypoidGearDesign)

        @property
        def hypoid_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.hypoid import _986

            return self._parent._cast(_986.HypoidGearMeshDesign)

        @property
        def hypoid_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.hypoid import _987

            return self._parent._cast(_987.HypoidGearSetDesign)

        @property
        def hypoid_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.hypoid import _988

            return self._parent._cast(_988.HypoidMeshedGearDesign)

        @property
        def face_gear_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.face import _989

            return self._parent._cast(_989.FaceGearDesign)

        @property
        def face_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.face import _991

            return self._parent._cast(_991.FaceGearMeshDesign)

        @property
        def face_gear_pinion_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.face import _994

            return self._parent._cast(_994.FaceGearPinionDesign)

        @property
        def face_gear_set_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.face import _995

            return self._parent._cast(_995.FaceGearSetDesign)

        @property
        def face_gear_wheel_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.face import _997

            return self._parent._cast(_997.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1012

            return self._parent._cast(_1012.CylindricalGearDesign)

        @property
        def cylindrical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1018

            return self._parent._cast(_1018.CylindricalGearMeshDesign)

        @property
        def cylindrical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1028

            return self._parent._cast(_1028.CylindricalGearSetDesign)

        @property
        def cylindrical_planetary_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1041

            return self._parent._cast(_1041.CylindricalPlanetaryGearSetDesign)

        @property
        def cylindrical_planet_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.cylindrical import _1042

            return self._parent._cast(_1042.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.conical import _1154

            return self._parent._cast(_1154.ConicalGearDesign)

        @property
        def conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.conical import _1155

            return self._parent._cast(_1155.ConicalGearMeshDesign)

        @property
        def conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.conical import _1156

            return self._parent._cast(_1156.ConicalGearSetDesign)

        @property
        def conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.conical import _1159

            return self._parent._cast(_1159.ConicalMeshedGearDesign)

        @property
        def concept_gear_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.concept import _1176

            return self._parent._cast(_1176.ConceptGearDesign)

        @property
        def concept_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.concept import _1177

            return self._parent._cast(_1177.ConceptGearMeshDesign)

        @property
        def concept_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.concept import _1178

            return self._parent._cast(_1178.ConceptGearSetDesign)

        @property
        def bevel_gear_design(self: "GearDesignComponent._Cast_GearDesignComponent"):
            from mastapy.gears.gear_designs.bevel import _1180

            return self._parent._cast(_1180.BevelGearDesign)

        @property
        def bevel_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.bevel import _1181

            return self._parent._cast(_1181.BevelGearMeshDesign)

        @property
        def bevel_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.bevel import _1182

            return self._parent._cast(_1182.BevelGearSetDesign)

        @property
        def bevel_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.bevel import _1183

            return self._parent._cast(_1183.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1193

            return self._parent._cast(_1193.AGMAGleasonConicalGearDesign)

        @property
        def agma_gleason_conical_gear_mesh_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1194

            return self._parent._cast(_1194.AGMAGleasonConicalGearMeshDesign)

        @property
        def agma_gleason_conical_gear_set_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1195

            return self._parent._cast(_1195.AGMAGleasonConicalGearSetDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ):
            from mastapy.gears.gear_designs.agma_gleason_conical import _1196

            return self._parent._cast(_1196.AGMAGleasonConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "GearDesignComponent._Cast_GearDesignComponent",
        ) -> "GearDesignComponent":
            return self._parent

        def __getattr__(
            self: "GearDesignComponent._Cast_GearDesignComponent", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesignComponent.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def user_specified_data(self: Self) -> "_1741.UserSpecifiedData":
        """mastapy.utility.scripting.UserSpecifiedData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedData

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def report_names(self: Self) -> "List[str]":
        """List[str]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReportNames

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp, str)

        if value is None:
            return None

        return value

    def dispose(self: Self):
        """Method does not return."""
        self.wrapped.Dispose()

    @enforce_parameter_types
    def output_default_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else "")

    def get_default_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_active_report_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else "")

    @enforce_parameter_types
    def output_active_report_as_text_to(self: Self, file_path: "str"):
        """Method does not return.

        Args:
            file_path (str)
        """
        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else "")

    def get_active_report_with_encoded_images(self: Self) -> "str":
        """str"""
        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    @enforce_parameter_types
    def output_named_report_to(self: Self, report_name: "str", file_path: "str"):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_masta_report(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def output_named_report_as_text_to(
        self: Self, report_name: "str", file_path: "str"
    ):
        """Method does not return.

        Args:
            report_name (str)
            file_path (str)
        """
        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(
            report_name if report_name else "", file_path if file_path else ""
        )

    @enforce_parameter_types
    def get_named_report_with_encoded_images(self: Self, report_name: "str") -> "str":
        """str

        Args:
            report_name (str)
        """
        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(
            report_name if report_name else ""
        )
        return method_result

    def __enter__(self: Self):
        return self

    def __exit__(self: Self, exception_type: Any, exception_value: Any, traceback: Any):
        self.dispose()

    @property
    def cast_to(self: Self) -> "GearDesignComponent._Cast_GearDesignComponent":
        return self._Cast_GearDesignComponent(self)
