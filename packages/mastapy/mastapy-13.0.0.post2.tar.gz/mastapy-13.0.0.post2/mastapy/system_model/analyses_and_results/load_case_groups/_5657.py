"""AbstractDesignStateLoadCaseGroup"""
from __future__ import annotations

from typing import TypeVar

from PIL.Image import Image

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.load_case_groups import _5659
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_DESIGN_STATE_LOAD_CASE_GROUP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups",
    "AbstractDesignStateLoadCaseGroup",
)


__docformat__ = "restructuredtext en"
__all__ = ("AbstractDesignStateLoadCaseGroup",)


Self = TypeVar("Self", bound="AbstractDesignStateLoadCaseGroup")


class AbstractDesignStateLoadCaseGroup(_5659.AbstractStaticLoadCaseGroup):
    """AbstractDesignStateLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_DESIGN_STATE_LOAD_CASE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractDesignStateLoadCaseGroup")

    class _Cast_AbstractDesignStateLoadCaseGroup:
        """Special nested class for casting AbstractDesignStateLoadCaseGroup to subclasses."""

        def __init__(
            self: "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup",
            parent: "AbstractDesignStateLoadCaseGroup",
        ):
            self._parent = parent

        @property
        def abstract_static_load_case_group(
            self: "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup",
        ):
            return self._parent._cast(_5659.AbstractStaticLoadCaseGroup)

        @property
        def abstract_load_case_group(
            self: "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup",
        ):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5658

            return self._parent._cast(_5658.AbstractLoadCaseGroup)

        @property
        def design_state(
            self: "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup",
        ):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5662

            return self._parent._cast(_5662.DesignState)

        @property
        def sub_group_in_single_design_state(
            self: "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup",
        ):
            from mastapy.system_model.analyses_and_results.load_case_groups import _5666

            return self._parent._cast(_5666.SubGroupInSingleDesignState)

        @property
        def abstract_design_state_load_case_group(
            self: "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup",
        ) -> "AbstractDesignStateLoadCaseGroup":
            return self._parent

        def __getattr__(
            self: "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractDesignStateLoadCaseGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Ratio

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractDesignStateLoadCaseGroup._Cast_AbstractDesignStateLoadCaseGroup":
        return self._Cast_AbstractDesignStateLoadCaseGroup(self)
