"""BoltedJointCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5627
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "BoltedJointCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2443
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5397


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BoltedJointCompoundMultibodyDynamicsAnalysis")


class BoltedJointCompoundMultibodyDynamicsAnalysis(
    _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
):
    """BoltedJointCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BoltedJointCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_BoltedJointCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting BoltedJointCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
            parent: "BoltedJointCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def bolted_joint_compound_multibody_dynamics_analysis(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
        ) -> "BoltedJointCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BoltedJointCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2443.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2443.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5397.BoltedJointMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BoltedJointMultibodyDynamicsAnalysis]

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
    ) -> "List[_5397.BoltedJointMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.BoltedJointMultibodyDynamicsAnalysis]

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
    ) -> "BoltedJointCompoundMultibodyDynamicsAnalysis._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis":
        return self._Cast_BoltedJointCompoundMultibodyDynamicsAnalysis(self)
