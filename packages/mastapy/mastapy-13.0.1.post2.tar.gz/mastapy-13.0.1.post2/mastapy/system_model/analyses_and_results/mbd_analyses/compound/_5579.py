"""CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5576
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5429


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis")


class CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis(
    _5576.CylindricalGearCompoundMultibodyDynamicsAnalysis
):
    """CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
            parent: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            return self._parent._cast(
                _5576.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5587,
            )

            return self._parent._cast(_5587.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(
                _5606.MountableComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5608,
            )

            return self._parent._cast(_5608.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7546

            return self._parent._cast(_7546.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ):
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
        ) -> "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5429.CylindricalPlanetGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalPlanetGearMultibodyDynamicsAnalysis]

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
    ) -> "List[_5429.CylindricalPlanetGearMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CylindricalPlanetGearMultibodyDynamicsAnalysis]

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
    ) -> "CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis(self)
