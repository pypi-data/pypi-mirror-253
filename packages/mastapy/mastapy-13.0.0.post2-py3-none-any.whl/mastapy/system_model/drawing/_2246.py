"""ContourDrawStyle"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.geometry import _308
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONTOUR_DRAW_STYLE = python_net_import(
    "SMT.MastaAPI.SystemModel.Drawing", "ContourDrawStyle"
)

if TYPE_CHECKING:
    from mastapy.utility.enums import _1821
    from mastapy.utility_gui import _1851
    from mastapy.system_model.drawing import _2252


__docformat__ = "restructuredtext en"
__all__ = ("ContourDrawStyle",)


Self = TypeVar("Self", bound="ContourDrawStyle")


class ContourDrawStyle(_308.DrawStyleBase):
    """ContourDrawStyle

    This is a mastapy class.
    """

    TYPE = _CONTOUR_DRAW_STYLE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ContourDrawStyle")

    class _Cast_ContourDrawStyle:
        """Special nested class for casting ContourDrawStyle to subclasses."""

        def __init__(
            self: "ContourDrawStyle._Cast_ContourDrawStyle", parent: "ContourDrawStyle"
        ):
            self._parent = parent

        @property
        def draw_style_base(self: "ContourDrawStyle._Cast_ContourDrawStyle"):
            return self._parent._cast(_308.DrawStyleBase)

        @property
        def system_deflection_draw_style(
            self: "ContourDrawStyle._Cast_ContourDrawStyle",
        ):
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.SystemDeflectionDrawStyle)

        @property
        def steady_state_synchronous_response_draw_style(
            self: "ContourDrawStyle._Cast_ContourDrawStyle",
        ):
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3090,
            )

            return self._parent._cast(_3090.SteadyStateSynchronousResponseDrawStyle)

        @property
        def stability_analysis_draw_style(
            self: "ContourDrawStyle._Cast_ContourDrawStyle",
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3871,
            )

            return self._parent._cast(_3871.StabilityAnalysisDrawStyle)

        @property
        def rotor_dynamics_draw_style(self: "ContourDrawStyle._Cast_ContourDrawStyle"):
            from mastapy.system_model.analyses_and_results.rotor_dynamics import _4026

            return self._parent._cast(_4026.RotorDynamicsDrawStyle)

        @property
        def modal_analysis_draw_style(self: "ContourDrawStyle._Cast_ContourDrawStyle"):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.ModalAnalysisDrawStyle)

        @property
        def mbd_analysis_draw_style(self: "ContourDrawStyle._Cast_ContourDrawStyle"):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(_5459.MBDAnalysisDrawStyle)

        @property
        def harmonic_analysis_draw_style(
            self: "ContourDrawStyle._Cast_ContourDrawStyle",
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5761,
            )

            return self._parent._cast(_5761.HarmonicAnalysisDrawStyle)

        @property
        def dynamic_analysis_draw_style(
            self: "ContourDrawStyle._Cast_ContourDrawStyle",
        ):
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.DynamicAnalysisDrawStyle)

        @property
        def critical_speed_analysis_draw_style(
            self: "ContourDrawStyle._Cast_ContourDrawStyle",
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6583,
            )

            return self._parent._cast(_6583.CriticalSpeedAnalysisDrawStyle)

        @property
        def contour_draw_style(
            self: "ContourDrawStyle._Cast_ContourDrawStyle",
        ) -> "ContourDrawStyle":
            return self._parent

        def __getattr__(self: "ContourDrawStyle._Cast_ContourDrawStyle", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ContourDrawStyle.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contour(self: Self) -> "_1821.ThreeDViewContourOption":
        """mastapy.utility.enums.ThreeDViewContourOption"""
        temp = self.wrapped.Contour

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Utility.Enums.ThreeDViewContourOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.utility.enums._1821", "ThreeDViewContourOption"
        )(value)

    @contour.setter
    @enforce_parameter_types
    def contour(self: Self, value: "_1821.ThreeDViewContourOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Utility.Enums.ThreeDViewContourOption"
        )
        self.wrapped.Contour = value

    @property
    def minimum_peak_value_displacement(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumPeakValueDisplacement

        if temp is None:
            return 0.0

        return temp

    @minimum_peak_value_displacement.setter
    @enforce_parameter_types
    def minimum_peak_value_displacement(self: Self, value: "float"):
        self.wrapped.MinimumPeakValueDisplacement = (
            float(value) if value is not None else 0.0
        )

    @property
    def minimum_peak_value_stress(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MinimumPeakValueStress

        if temp is None:
            return 0.0

        return temp

    @minimum_peak_value_stress.setter
    @enforce_parameter_types
    def minimum_peak_value_stress(self: Self, value: "float"):
        self.wrapped.MinimumPeakValueStress = float(value) if value is not None else 0.0

    @property
    def show_local_maxima(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.ShowLocalMaxima

        if temp is None:
            return False

        return temp

    @show_local_maxima.setter
    @enforce_parameter_types
    def show_local_maxima(self: Self, value: "bool"):
        self.wrapped.ShowLocalMaxima = bool(value) if value is not None else False

    @property
    def deflection_scaling(self: Self) -> "_1851.ScalingDrawStyle":
        """mastapy.utility_gui.ScalingDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DeflectionScaling

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def model_view_options(self: Self) -> "_2252.ModelViewOptionsDrawStyle":
        """mastapy.system_model.drawing.ModelViewOptionsDrawStyle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModelViewOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ContourDrawStyle._Cast_ContourDrawStyle":
        return self._Cast_ContourDrawStyle(self)
