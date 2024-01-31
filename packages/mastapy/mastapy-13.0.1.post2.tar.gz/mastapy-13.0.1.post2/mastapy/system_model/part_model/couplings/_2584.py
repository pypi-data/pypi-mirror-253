"""CouplingHalf"""
from __future__ import annotations

from typing import TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2464
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Couplings", "CouplingHalf"
)


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalf",)


Self = TypeVar("Self", bound="CouplingHalf")


class CouplingHalf(_2464.MountableComponent):
    """CouplingHalf

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalf")

    class _Cast_CouplingHalf:
        """Special nested class for casting CouplingHalf to subclasses."""

        def __init__(self: "CouplingHalf._Cast_CouplingHalf", parent: "CouplingHalf"):
            self._parent = parent

        @property
        def mountable_component(self: "CouplingHalf._Cast_CouplingHalf"):
            return self._parent._cast(_2464.MountableComponent)

        @property
        def component(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model import _2444

            return self._parent._cast(_2444.Component)

        @property
        def part(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model import _2468

            return self._parent._cast(_2468.Part)

        @property
        def design_entity(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model import _2203

            return self._parent._cast(_2203.DesignEntity)

        @property
        def clutch_half(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2579

            return self._parent._cast(_2579.ClutchHalf)

        @property
        def concept_coupling_half(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2582

            return self._parent._cast(_2582.ConceptCouplingHalf)

        @property
        def cvt_pulley(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2587

            return self._parent._cast(_2587.CVTPulley)

        @property
        def part_to_part_shear_coupling_half(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2589

            return self._parent._cast(_2589.PartToPartShearCouplingHalf)

        @property
        def pulley(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2590

            return self._parent._cast(_2590.Pulley)

        @property
        def rolling_ring(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2596

            return self._parent._cast(_2596.RollingRing)

        @property
        def spring_damper_half(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2601

            return self._parent._cast(_2601.SpringDamperHalf)

        @property
        def synchroniser_half(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2604

            return self._parent._cast(_2604.SynchroniserHalf)

        @property
        def synchroniser_part(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2605

            return self._parent._cast(_2605.SynchroniserPart)

        @property
        def synchroniser_sleeve(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2606

            return self._parent._cast(_2606.SynchroniserSleeve)

        @property
        def torque_converter_pump(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2608

            return self._parent._cast(_2608.TorqueConverterPump)

        @property
        def torque_converter_turbine(self: "CouplingHalf._Cast_CouplingHalf"):
            from mastapy.system_model.part_model.couplings import _2610

            return self._parent._cast(_2610.TorqueConverterTurbine)

        @property
        def coupling_half(self: "CouplingHalf._Cast_CouplingHalf") -> "CouplingHalf":
            return self._parent

        def __getattr__(self: "CouplingHalf._Cast_CouplingHalf", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalf.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bore(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Bore

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @bore.setter
    @enforce_parameter_types
    def bore(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Bore = value

    @property
    def diameter(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Diameter

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @diameter.setter
    @enforce_parameter_types
    def diameter(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Diameter = value

    @property
    def width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.Width

        if temp is None:
            return 0.0

        return temp

    @width.setter
    @enforce_parameter_types
    def width(self: Self, value: "float"):
        self.wrapped.Width = float(value) if value is not None else 0.0

    @property
    def cast_to(self: Self) -> "CouplingHalf._Cast_CouplingHalf":
        return self._Cast_CouplingHalf(self)
