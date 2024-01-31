"""PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5566
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5470


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis")


class PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis(
    _5566.CouplingCompoundMultibodyDynamicsAnalysis
):
    """PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
            parent: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_compound_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(_5566.CouplingCompoundMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_compound_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.SpecialisedAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_assembly_compound_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5529,
            )

            return self._parent._cast(
                _5529.AbstractAssemblyCompoundMultibodyDynamicsAnalysis
            )

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_compound_multibody_dynamics_analysis(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
        ) -> "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2588.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2588.PartToPartShearCoupling":
        """mastapy.system_model.part_model.couplings.PartToPartShearCoupling

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
    ) -> "List[_5470.PartToPartShearCouplingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingMultibodyDynamicsAnalysis]

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
    ) -> "List[_5470.PartToPartShearCouplingMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.PartToPartShearCouplingMultibodyDynamicsAnalysis]

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
    ) -> "PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis":
        return self._Cast_PartToPartShearCouplingCompoundMultibodyDynamicsAnalysis(self)
