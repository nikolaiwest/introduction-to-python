from dataclasses import dataclass
from typing import Optional, List


@dataclass
class MaterialProperties:
    """Properties of a material."""

    density: float  # kg/m³
    yield_strength: float  # MPa
    typical_youngs_modulus: float  # GPa

    def __post_init__(self):
        """Validate properties."""
        if self.density <= 0:
            raise ValueError("Density must be positive")
        if self.yield_strength <= 0:
            raise ValueError("Yield strength must be positive")
        if self.typical_youngs_modulus <= 0:
            raise ValueError("Young's modulus must be positive")


class Material:
    """Base class for all materials."""

    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def can_withstand_stress(self, stress: float) -> bool:
        """Check if the material can withstand the given stress."""
        # Convert GPa to MPa for comparison
        return stress < self.properties.yield_strength


class StressStrainTest:
    """A single stress-strain test."""

    def __init__(
        self,
        material: Material,
        force: float,
        area: float,
        original_length: float,
        change_in_length: float,
    ):
        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length

        # Validate inputs
        if force <= 0:
            raise ValueError("Force must be positive")
        if area <= 0:
            raise ValueError("Area must be positive")
        if original_length <= 0:
            raise ValueError("Original length must be positive")
        # Change in length can be negative (compression)

    @property
    def stress(self) -> float:
        """Calculate stress in MPa."""
        return self._force / self._area

    @property
    def strain(self) -> float:
        """Calculate strain (dimensionless)."""
        return self._change_in_length / self._original_length

    @property
    def youngs_modulus(self) -> float:
        """Calculate Young's modulus in GPa."""
        # Convert to GPa from MPa
        return (self.stress / self.strain) / 1000

    def will_fail(self) -> bool:
        """Determine if the material is likely to fail under this test."""
        return not self.material.can_withstand_stress(self.stress)

    def __str__(self) -> str:
        return (
            f"Test on {self.material.name}: "
            f"Stress={self.stress:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={self.youngs_modulus:.2f} GPa"
        )


# Example material subclass
class Metal(Material):
    """A metal material."""

    def __init__(
        self, name: str, properties: MaterialProperties, is_ferrous: bool = False
    ):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        return f"{self.name} ({ferrous_text} metal, Density: {self.properties.density} kg/m³)"


# Example usage
steel_properties = MaterialProperties(
    density=7850, yield_strength=250, typical_youngs_modulus=200  # MPa  # GPa
)

steel = Metal("Steel", steel_properties, is_ferrous=True)
test = StressStrainTest(
    steel, force=5000, area=25, original_length=100, change_in_length=0.5
)

print(steel)
print(test)
print(f"Will the material fail? {'Yes' if test.will_fail() else 'No'}")
print(f"Calculated Young's modulus: {test.youngs_modulus:.2f} GPa")
print(f"Typical Young's modulus: {steel.properties.typical_youngs_modulus:.2f} GPa")
