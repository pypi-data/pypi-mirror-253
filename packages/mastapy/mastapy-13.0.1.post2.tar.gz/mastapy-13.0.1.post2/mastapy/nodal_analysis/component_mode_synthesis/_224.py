"""CMSElementFaceGroup"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.dev_tools_analyses import _180
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_ELEMENT_FACE_GROUP = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis", "CMSElementFaceGroup"
)


__docformat__ = "restructuredtext en"
__all__ = ("CMSElementFaceGroup",)


Self = TypeVar("Self", bound="CMSElementFaceGroup")


class CMSElementFaceGroup(_180.ElementFaceGroup):
    """CMSElementFaceGroup

    This is a mastapy class.
    """

    TYPE = _CMS_ELEMENT_FACE_GROUP
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSElementFaceGroup")

    class _Cast_CMSElementFaceGroup:
        """Special nested class for casting CMSElementFaceGroup to subclasses."""

        def __init__(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
            parent: "CMSElementFaceGroup",
        ):
            self._parent = parent

        @property
        def element_face_group(self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup"):
            return self._parent._cast(_180.ElementFaceGroup)

        @property
        def fe_entity_group(self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup"):
            pass

            from mastapy.nodal_analysis.dev_tools_analyses import _182

            return self._parent._cast(_182.FEEntityGroup)

        @property
        def cms_element_face_group_of_all_free_faces(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
        ):
            from mastapy.nodal_analysis.component_mode_synthesis import _225

            return self._parent._cast(_225.CMSElementFaceGroupOfAllFreeFaces)

        @property
        def cms_element_face_group(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup",
        ) -> "CMSElementFaceGroup":
            return self._parent

        def __getattr__(
            self: "CMSElementFaceGroup._Cast_CMSElementFaceGroup", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CMSElementFaceGroup.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def area(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Area

        if temp is None:
            return 0.0

        return temp

    def create_node_group(self: Self):
        """Method does not return."""
        self.wrapped.CreateNodeGroup()

    def populate_rms_values_cache(self: Self):
        """Method does not return."""
        self.wrapped.PopulateRMSValuesCache()

    @property
    def cast_to(self: Self) -> "CMSElementFaceGroup._Cast_CMSElementFaceGroup":
        return self._Cast_CMSElementFaceGroup(self)
