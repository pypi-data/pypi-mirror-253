"""TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5567
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2610
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5512


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis")


class TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis(
    _5567.CouplingHalfCompoundMultibodyDynamicsAnalysis
):
    """TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
            parent: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5567.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5605,
            )

            return self._parent._cast(
                _5605.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5553,
            )

            return self._parent._cast(_5553.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
        ) -> "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis",
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
        self: Self,
        instance_to_wrap: "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2610.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5512.TorqueConverterTurbineMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterTurbineMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5512.TorqueConverterTurbineMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.TorqueConverterTurbineMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
        return self._Cast_TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis(self)
