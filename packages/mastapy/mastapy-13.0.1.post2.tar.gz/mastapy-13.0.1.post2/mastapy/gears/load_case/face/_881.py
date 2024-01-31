"""FaceMeshLoadCase"""
from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.gears.load_case import _875
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.LoadCase.Face", "FaceMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.gears import _324


__docformat__ = "restructuredtext en"
__all__ = ("FaceMeshLoadCase",)


Self = TypeVar("Self", bound="FaceMeshLoadCase")


class FaceMeshLoadCase(_875.MeshLoadCase):
    """FaceMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceMeshLoadCase")

    class _Cast_FaceMeshLoadCase:
        """Special nested class for casting FaceMeshLoadCase to subclasses."""

        def __init__(
            self: "FaceMeshLoadCase._Cast_FaceMeshLoadCase", parent: "FaceMeshLoadCase"
        ):
            self._parent = parent

        @property
        def mesh_load_case(self: "FaceMeshLoadCase._Cast_FaceMeshLoadCase"):
            return self._parent._cast(_875.MeshLoadCase)

        @property
        def gear_mesh_design_analysis(self: "FaceMeshLoadCase._Cast_FaceMeshLoadCase"):
            from mastapy.gears.analysis import _1222

            return self._parent._cast(_1222.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "FaceMeshLoadCase._Cast_FaceMeshLoadCase",
        ):
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearMeshAnalysis)

        @property
        def face_mesh_load_case(
            self: "FaceMeshLoadCase._Cast_FaceMeshLoadCase",
        ) -> "FaceMeshLoadCase":
            return self._parent

        def __getattr__(self: "FaceMeshLoadCase._Cast_FaceMeshLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_misalignment_due_to_system_deflection(self: Self) -> "float":
        """float"""
        temp = self.wrapped.EquivalentMisalignmentDueToSystemDeflection

        if temp is None:
            return 0.0

        return temp

    @equivalent_misalignment_due_to_system_deflection.setter
    @enforce_parameter_types
    def equivalent_misalignment_due_to_system_deflection(self: Self, value: "float"):
        self.wrapped.EquivalentMisalignmentDueToSystemDeflection = (
            float(value) if value is not None else 0.0
        )

    @property
    def misalignment_source(self: Self) -> "_324.CylindricalMisalignmentDataSource":
        """mastapy.gears.CylindricalMisalignmentDataSource"""
        temp = self.wrapped.MisalignmentSource

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.Gears.CylindricalMisalignmentDataSource"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.gears._324", "CylindricalMisalignmentDataSource"
        )(value)

    @misalignment_source.setter
    @enforce_parameter_types
    def misalignment_source(
        self: Self, value: "_324.CylindricalMisalignmentDataSource"
    ):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.Gears.CylindricalMisalignmentDataSource"
        )
        self.wrapped.MisalignmentSource = value

    @property
    def cast_to(self: Self) -> "FaceMeshLoadCase._Cast_FaceMeshLoadCase":
        return self._Cast_FaceMeshLoadCase(self)
