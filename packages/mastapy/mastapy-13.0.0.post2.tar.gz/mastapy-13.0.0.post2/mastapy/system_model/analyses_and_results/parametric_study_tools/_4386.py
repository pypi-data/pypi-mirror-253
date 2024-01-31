"""ParametricStudyStaticLoad"""
from __future__ import annotations

from typing import TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6804
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PARAMETRIC_STUDY_STATIC_LOAD = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "ParametricStudyStaticLoad",
)


__docformat__ = "restructuredtext en"
__all__ = ("ParametricStudyStaticLoad",)


Self = TypeVar("Self", bound="ParametricStudyStaticLoad")


class ParametricStudyStaticLoad(_6804.StaticLoadCase):
    """ParametricStudyStaticLoad

    This is a mastapy class.
    """

    TYPE = _PARAMETRIC_STUDY_STATIC_LOAD
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ParametricStudyStaticLoad")

    class _Cast_ParametricStudyStaticLoad:
        """Special nested class for casting ParametricStudyStaticLoad to subclasses."""

        def __init__(
            self: "ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad",
            parent: "ParametricStudyStaticLoad",
        ):
            self._parent = parent

        @property
        def static_load_case(
            self: "ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad",
        ):
            return self._parent._cast(_6804.StaticLoadCase)

        @property
        def load_case(
            self: "ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad",
        ):
            from mastapy.system_model.analyses_and_results.static_loads import _6803

            return self._parent._cast(_6803.LoadCase)

        @property
        def context(self: "ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad"):
            from mastapy.system_model.analyses_and_results import _2650

            return self._parent._cast(_2650.Context)

        @property
        def parametric_study_static_load(
            self: "ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad",
        ) -> "ParametricStudyStaticLoad":
            return self._parent

        def __getattr__(
            self: "ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ParametricStudyStaticLoad.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ParametricStudyStaticLoad._Cast_ParametricStudyStaticLoad":
        return self._Cast_ParametricStudyStaticLoad(self)
