"""CMSElementFaceGroupOfAllFreeFaces"""
from __future__ import annotations

from typing import TypeVar

from mastapy.nodal_analysis.component_mode_synthesis import _224
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CMS_ELEMENT_FACE_GROUP_OF_ALL_FREE_FACES = python_net_import(
    "SMT.MastaAPI.NodalAnalysis.ComponentModeSynthesis",
    "CMSElementFaceGroupOfAllFreeFaces",
)


__docformat__ = "restructuredtext en"
__all__ = ("CMSElementFaceGroupOfAllFreeFaces",)


Self = TypeVar("Self", bound="CMSElementFaceGroupOfAllFreeFaces")


class CMSElementFaceGroupOfAllFreeFaces(_224.CMSElementFaceGroup):
    """CMSElementFaceGroupOfAllFreeFaces

    This is a mastapy class.
    """

    TYPE = _CMS_ELEMENT_FACE_GROUP_OF_ALL_FREE_FACES
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CMSElementFaceGroupOfAllFreeFaces")

    class _Cast_CMSElementFaceGroupOfAllFreeFaces:
        """Special nested class for casting CMSElementFaceGroupOfAllFreeFaces to subclasses."""

        def __init__(
            self: "CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces",
            parent: "CMSElementFaceGroupOfAllFreeFaces",
        ):
            self._parent = parent

        @property
        def cms_element_face_group(
            self: "CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces",
        ):
            return self._parent._cast(_224.CMSElementFaceGroup)

        @property
        def element_face_group(
            self: "CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces",
        ):
            from mastapy.nodal_analysis.dev_tools_analyses import _180

            return self._parent._cast(_180.ElementFaceGroup)

        @property
        def fe_entity_group(
            self: "CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces",
        ):
            pass

            from mastapy.nodal_analysis.dev_tools_analyses import _182

            return self._parent._cast(_182.FEEntityGroup)

        @property
        def cms_element_face_group_of_all_free_faces(
            self: "CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces",
        ) -> "CMSElementFaceGroupOfAllFreeFaces":
            return self._parent

        def __getattr__(
            self: "CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces",
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
        self: Self, instance_to_wrap: "CMSElementFaceGroupOfAllFreeFaces.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CMSElementFaceGroupOfAllFreeFaces._Cast_CMSElementFaceGroupOfAllFreeFaces":
        return self._Cast_CMSElementFaceGroupOfAllFreeFaces(self)
