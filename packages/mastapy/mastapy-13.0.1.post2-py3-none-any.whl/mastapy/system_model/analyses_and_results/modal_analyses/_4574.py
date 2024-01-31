"""AbstractShaftOrHousingModalAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "AbstractShaftOrHousingModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.system_deflections import _2686


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftOrHousingModalAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftOrHousingModalAnalysis")


class AbstractShaftOrHousingModalAnalysis(_4597.ComponentModalAnalysis):
    """AbstractShaftOrHousingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_OR_HOUSING_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaftOrHousingModalAnalysis")

    class _Cast_AbstractShaftOrHousingModalAnalysis:
        """Special nested class for casting AbstractShaftOrHousingModalAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
            parent: "AbstractShaftOrHousingModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            return self._parent._cast(_4597.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2657

            return self._parent._cast(_2657.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4573

            return self._parent._cast(_4573.AbstractShaftModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CycloidalDiscModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.FEPartModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.ShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
        ) -> "AbstractShaftOrHousingModalAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftOrHousingModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractShaftOrHousing":
        """mastapy.system_model.part_model.AbstractShaftOrHousing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2686.AbstractShaftOrHousingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftOrHousingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> (
        "AbstractShaftOrHousingModalAnalysis._Cast_AbstractShaftOrHousingModalAnalysis"
    ):
        return self._Cast_AbstractShaftOrHousingModalAnalysis(self)
