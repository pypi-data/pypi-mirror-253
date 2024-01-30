"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1612 import Acceleration
    from ._1613 import Angle
    from ._1614 import AnglePerUnitTemperature
    from ._1615 import AngleSmall
    from ._1616 import AngleVerySmall
    from ._1617 import AngularAcceleration
    from ._1618 import AngularCompliance
    from ._1619 import AngularJerk
    from ._1620 import AngularStiffness
    from ._1621 import AngularVelocity
    from ._1622 import Area
    from ._1623 import AreaSmall
    from ._1624 import CarbonEmissionFactor
    from ._1625 import CurrentDensity
    from ._1626 import CurrentPerLength
    from ._1627 import Cycles
    from ._1628 import Damage
    from ._1629 import DamageRate
    from ._1630 import DataSize
    from ._1631 import Decibel
    from ._1632 import Density
    from ._1633 import ElectricalResistance
    from ._1634 import ElectricalResistivity
    from ._1635 import ElectricCurrent
    from ._1636 import Energy
    from ._1637 import EnergyPerUnitArea
    from ._1638 import EnergyPerUnitAreaSmall
    from ._1639 import EnergySmall
    from ._1640 import Enum
    from ._1641 import FlowRate
    from ._1642 import Force
    from ._1643 import ForcePerUnitLength
    from ._1644 import ForcePerUnitPressure
    from ._1645 import ForcePerUnitTemperature
    from ._1646 import FractionMeasurementBase
    from ._1647 import FractionPerTemperature
    from ._1648 import Frequency
    from ._1649 import FuelConsumptionEngine
    from ._1650 import FuelEfficiencyVehicle
    from ._1651 import Gradient
    from ._1652 import HeatConductivity
    from ._1653 import HeatTransfer
    from ._1654 import HeatTransferCoefficientForPlasticGearTooth
    from ._1655 import HeatTransferResistance
    from ._1656 import Impulse
    from ._1657 import Index
    from ._1658 import Inductance
    from ._1659 import Integer
    from ._1660 import InverseShortLength
    from ._1661 import InverseShortTime
    from ._1662 import Jerk
    from ._1663 import KinematicViscosity
    from ._1664 import LengthLong
    from ._1665 import LengthMedium
    from ._1666 import LengthPerUnitTemperature
    from ._1667 import LengthShort
    from ._1668 import LengthToTheFourth
    from ._1669 import LengthVeryLong
    from ._1670 import LengthVeryShort
    from ._1671 import LengthVeryShortPerLengthShort
    from ._1672 import LinearAngularDamping
    from ._1673 import LinearAngularStiffnessCrossTerm
    from ._1674 import LinearDamping
    from ._1675 import LinearFlexibility
    from ._1676 import LinearStiffness
    from ._1677 import MagneticFieldStrength
    from ._1678 import MagneticFlux
    from ._1679 import MagneticFluxDensity
    from ._1680 import MagneticVectorPotential
    from ._1681 import MagnetomotiveForce
    from ._1682 import Mass
    from ._1683 import MassPerUnitLength
    from ._1684 import MassPerUnitTime
    from ._1685 import MomentOfInertia
    from ._1686 import MomentOfInertiaPerUnitLength
    from ._1687 import MomentPerUnitPressure
    from ._1688 import Number
    from ._1689 import Percentage
    from ._1690 import Power
    from ._1691 import PowerPerSmallArea
    from ._1692 import PowerPerUnitTime
    from ._1693 import PowerSmall
    from ._1694 import PowerSmallPerArea
    from ._1695 import PowerSmallPerMass
    from ._1696 import PowerSmallPerUnitAreaPerUnitTime
    from ._1697 import PowerSmallPerUnitTime
    from ._1698 import PowerSmallPerVolume
    from ._1699 import Pressure
    from ._1700 import PressurePerUnitTime
    from ._1701 import PressureVelocityProduct
    from ._1702 import PressureViscosityCoefficient
    from ._1703 import Price
    from ._1704 import PricePerUnitMass
    from ._1705 import QuadraticAngularDamping
    from ._1706 import QuadraticDrag
    from ._1707 import RescaledMeasurement
    from ._1708 import Rotatum
    from ._1709 import SafetyFactor
    from ._1710 import SpecificAcousticImpedance
    from ._1711 import SpecificHeat
    from ._1712 import SquareRootOfUnitForcePerUnitArea
    from ._1713 import StiffnessPerUnitFaceWidth
    from ._1714 import Stress
    from ._1715 import Temperature
    from ._1716 import TemperatureDifference
    from ._1717 import TemperaturePerUnitTime
    from ._1718 import Text
    from ._1719 import ThermalContactCoefficient
    from ._1720 import ThermalExpansionCoefficient
    from ._1721 import ThermoElasticFactor
    from ._1722 import Time
    from ._1723 import TimeShort
    from ._1724 import TimeVeryShort
    from ._1725 import Torque
    from ._1726 import TorqueConverterInverseK
    from ._1727 import TorqueConverterK
    from ._1728 import TorquePerCurrent
    from ._1729 import TorquePerSquareRootOfPower
    from ._1730 import TorquePerUnitTemperature
    from ._1731 import Velocity
    from ._1732 import VelocitySmall
    from ._1733 import Viscosity
    from ._1734 import Voltage
    from ._1735 import VoltagePerAngularVelocity
    from ._1736 import Volume
    from ._1737 import WearCoefficient
    from ._1738 import Yank
else:
    import_structure = {
        "_1612": ["Acceleration"],
        "_1613": ["Angle"],
        "_1614": ["AnglePerUnitTemperature"],
        "_1615": ["AngleSmall"],
        "_1616": ["AngleVerySmall"],
        "_1617": ["AngularAcceleration"],
        "_1618": ["AngularCompliance"],
        "_1619": ["AngularJerk"],
        "_1620": ["AngularStiffness"],
        "_1621": ["AngularVelocity"],
        "_1622": ["Area"],
        "_1623": ["AreaSmall"],
        "_1624": ["CarbonEmissionFactor"],
        "_1625": ["CurrentDensity"],
        "_1626": ["CurrentPerLength"],
        "_1627": ["Cycles"],
        "_1628": ["Damage"],
        "_1629": ["DamageRate"],
        "_1630": ["DataSize"],
        "_1631": ["Decibel"],
        "_1632": ["Density"],
        "_1633": ["ElectricalResistance"],
        "_1634": ["ElectricalResistivity"],
        "_1635": ["ElectricCurrent"],
        "_1636": ["Energy"],
        "_1637": ["EnergyPerUnitArea"],
        "_1638": ["EnergyPerUnitAreaSmall"],
        "_1639": ["EnergySmall"],
        "_1640": ["Enum"],
        "_1641": ["FlowRate"],
        "_1642": ["Force"],
        "_1643": ["ForcePerUnitLength"],
        "_1644": ["ForcePerUnitPressure"],
        "_1645": ["ForcePerUnitTemperature"],
        "_1646": ["FractionMeasurementBase"],
        "_1647": ["FractionPerTemperature"],
        "_1648": ["Frequency"],
        "_1649": ["FuelConsumptionEngine"],
        "_1650": ["FuelEfficiencyVehicle"],
        "_1651": ["Gradient"],
        "_1652": ["HeatConductivity"],
        "_1653": ["HeatTransfer"],
        "_1654": ["HeatTransferCoefficientForPlasticGearTooth"],
        "_1655": ["HeatTransferResistance"],
        "_1656": ["Impulse"],
        "_1657": ["Index"],
        "_1658": ["Inductance"],
        "_1659": ["Integer"],
        "_1660": ["InverseShortLength"],
        "_1661": ["InverseShortTime"],
        "_1662": ["Jerk"],
        "_1663": ["KinematicViscosity"],
        "_1664": ["LengthLong"],
        "_1665": ["LengthMedium"],
        "_1666": ["LengthPerUnitTemperature"],
        "_1667": ["LengthShort"],
        "_1668": ["LengthToTheFourth"],
        "_1669": ["LengthVeryLong"],
        "_1670": ["LengthVeryShort"],
        "_1671": ["LengthVeryShortPerLengthShort"],
        "_1672": ["LinearAngularDamping"],
        "_1673": ["LinearAngularStiffnessCrossTerm"],
        "_1674": ["LinearDamping"],
        "_1675": ["LinearFlexibility"],
        "_1676": ["LinearStiffness"],
        "_1677": ["MagneticFieldStrength"],
        "_1678": ["MagneticFlux"],
        "_1679": ["MagneticFluxDensity"],
        "_1680": ["MagneticVectorPotential"],
        "_1681": ["MagnetomotiveForce"],
        "_1682": ["Mass"],
        "_1683": ["MassPerUnitLength"],
        "_1684": ["MassPerUnitTime"],
        "_1685": ["MomentOfInertia"],
        "_1686": ["MomentOfInertiaPerUnitLength"],
        "_1687": ["MomentPerUnitPressure"],
        "_1688": ["Number"],
        "_1689": ["Percentage"],
        "_1690": ["Power"],
        "_1691": ["PowerPerSmallArea"],
        "_1692": ["PowerPerUnitTime"],
        "_1693": ["PowerSmall"],
        "_1694": ["PowerSmallPerArea"],
        "_1695": ["PowerSmallPerMass"],
        "_1696": ["PowerSmallPerUnitAreaPerUnitTime"],
        "_1697": ["PowerSmallPerUnitTime"],
        "_1698": ["PowerSmallPerVolume"],
        "_1699": ["Pressure"],
        "_1700": ["PressurePerUnitTime"],
        "_1701": ["PressureVelocityProduct"],
        "_1702": ["PressureViscosityCoefficient"],
        "_1703": ["Price"],
        "_1704": ["PricePerUnitMass"],
        "_1705": ["QuadraticAngularDamping"],
        "_1706": ["QuadraticDrag"],
        "_1707": ["RescaledMeasurement"],
        "_1708": ["Rotatum"],
        "_1709": ["SafetyFactor"],
        "_1710": ["SpecificAcousticImpedance"],
        "_1711": ["SpecificHeat"],
        "_1712": ["SquareRootOfUnitForcePerUnitArea"],
        "_1713": ["StiffnessPerUnitFaceWidth"],
        "_1714": ["Stress"],
        "_1715": ["Temperature"],
        "_1716": ["TemperatureDifference"],
        "_1717": ["TemperaturePerUnitTime"],
        "_1718": ["Text"],
        "_1719": ["ThermalContactCoefficient"],
        "_1720": ["ThermalExpansionCoefficient"],
        "_1721": ["ThermoElasticFactor"],
        "_1722": ["Time"],
        "_1723": ["TimeShort"],
        "_1724": ["TimeVeryShort"],
        "_1725": ["Torque"],
        "_1726": ["TorqueConverterInverseK"],
        "_1727": ["TorqueConverterK"],
        "_1728": ["TorquePerCurrent"],
        "_1729": ["TorquePerSquareRootOfPower"],
        "_1730": ["TorquePerUnitTemperature"],
        "_1731": ["Velocity"],
        "_1732": ["VelocitySmall"],
        "_1733": ["Viscosity"],
        "_1734": ["Voltage"],
        "_1735": ["VoltagePerAngularVelocity"],
        "_1736": ["Volume"],
        "_1737": ["WearCoefficient"],
        "_1738": ["Yank"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "Acceleration",
    "Angle",
    "AnglePerUnitTemperature",
    "AngleSmall",
    "AngleVerySmall",
    "AngularAcceleration",
    "AngularCompliance",
    "AngularJerk",
    "AngularStiffness",
    "AngularVelocity",
    "Area",
    "AreaSmall",
    "CarbonEmissionFactor",
    "CurrentDensity",
    "CurrentPerLength",
    "Cycles",
    "Damage",
    "DamageRate",
    "DataSize",
    "Decibel",
    "Density",
    "ElectricalResistance",
    "ElectricalResistivity",
    "ElectricCurrent",
    "Energy",
    "EnergyPerUnitArea",
    "EnergyPerUnitAreaSmall",
    "EnergySmall",
    "Enum",
    "FlowRate",
    "Force",
    "ForcePerUnitLength",
    "ForcePerUnitPressure",
    "ForcePerUnitTemperature",
    "FractionMeasurementBase",
    "FractionPerTemperature",
    "Frequency",
    "FuelConsumptionEngine",
    "FuelEfficiencyVehicle",
    "Gradient",
    "HeatConductivity",
    "HeatTransfer",
    "HeatTransferCoefficientForPlasticGearTooth",
    "HeatTransferResistance",
    "Impulse",
    "Index",
    "Inductance",
    "Integer",
    "InverseShortLength",
    "InverseShortTime",
    "Jerk",
    "KinematicViscosity",
    "LengthLong",
    "LengthMedium",
    "LengthPerUnitTemperature",
    "LengthShort",
    "LengthToTheFourth",
    "LengthVeryLong",
    "LengthVeryShort",
    "LengthVeryShortPerLengthShort",
    "LinearAngularDamping",
    "LinearAngularStiffnessCrossTerm",
    "LinearDamping",
    "LinearFlexibility",
    "LinearStiffness",
    "MagneticFieldStrength",
    "MagneticFlux",
    "MagneticFluxDensity",
    "MagneticVectorPotential",
    "MagnetomotiveForce",
    "Mass",
    "MassPerUnitLength",
    "MassPerUnitTime",
    "MomentOfInertia",
    "MomentOfInertiaPerUnitLength",
    "MomentPerUnitPressure",
    "Number",
    "Percentage",
    "Power",
    "PowerPerSmallArea",
    "PowerPerUnitTime",
    "PowerSmall",
    "PowerSmallPerArea",
    "PowerSmallPerMass",
    "PowerSmallPerUnitAreaPerUnitTime",
    "PowerSmallPerUnitTime",
    "PowerSmallPerVolume",
    "Pressure",
    "PressurePerUnitTime",
    "PressureVelocityProduct",
    "PressureViscosityCoefficient",
    "Price",
    "PricePerUnitMass",
    "QuadraticAngularDamping",
    "QuadraticDrag",
    "RescaledMeasurement",
    "Rotatum",
    "SafetyFactor",
    "SpecificAcousticImpedance",
    "SpecificHeat",
    "SquareRootOfUnitForcePerUnitArea",
    "StiffnessPerUnitFaceWidth",
    "Stress",
    "Temperature",
    "TemperatureDifference",
    "TemperaturePerUnitTime",
    "Text",
    "ThermalContactCoefficient",
    "ThermalExpansionCoefficient",
    "ThermoElasticFactor",
    "Time",
    "TimeShort",
    "TimeVeryShort",
    "Torque",
    "TorqueConverterInverseK",
    "TorqueConverterK",
    "TorquePerCurrent",
    "TorquePerSquareRootOfPower",
    "TorquePerUnitTemperature",
    "Velocity",
    "VelocitySmall",
    "Viscosity",
    "Voltage",
    "VoltagePerAngularVelocity",
    "Volume",
    "WearCoefficient",
    "Yank",
)
