"""CVTCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CVTCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5419


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CVTCompoundMultibodyDynamicsAnalysis")


class CVTCompoundMultibodyDynamicsAnalysis(
    _5538.BeltDriveCompoundMultibodyDynamicsAnalysis
):
    """CVTCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTCompoundMultibodyDynamicsAnalysis")

    class _Cast_CVTCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CVTCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
            parent: "CVTCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_multibody_dynamics_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5538.BeltDriveCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5626,
            )

            return self._parent._cast(
                _5626.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5528,
            )

            return self._parent._cast(
                _5528.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(_5607.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cvt_compound_multibody_dynamics_analysis(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
        ) -> "CVTCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "CVTCompoundMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5419.CVTMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CVTMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5419.CVTMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CVTMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CVTCompoundMultibodyDynamicsAnalysis._Cast_CVTCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CVTCompoundMultibodyDynamicsAnalysis(self)
