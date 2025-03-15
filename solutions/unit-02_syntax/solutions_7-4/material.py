"""
Material classes for the stress-strain calculator.
"""

# Import from our own modules
from properties import MaterialProperties


class Material:
    """Base class for all materials."""

    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def __repr__(self) -> str:
        return f"Material('{self.name}', {self.properties})"

    def can_withstand_stress(self, stress: float) -> bool:
        """Check if the material can withstand the given stress."""
        return stress < self.properties.yield_strength


class Metal(Material):
    """A metal material."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        is_ferrous: bool = False,
        is_alloy: bool = False,
    ):
        super().__init__(name, properties)
        self.is_ferrous = is_ferrous
        self.is_alloy = is_alloy

    def __str__(self) -> str:
        ferrous_text = "Ferrous" if self.is_ferrous else "Non-ferrous"
        alloy_text = "alloy" if self.is_alloy else "pure metal"
        return f"{self.name} ({ferrous_text} {alloy_text}, Density: {self.properties.density} kg/m³)"


class Plastic(Material):
    """A plastic material."""

    def __init__(
        self, name: str, properties: MaterialProperties, is_thermoplastic: bool = True
    ):
        super().__init__(name, properties)
        self.is_thermoplastic = is_thermoplastic

    def __str__(self) -> str:
        plastic_type = "Thermoplastic" if self.is_thermoplastic else "Thermoset"
        return f"{self.name} ({plastic_type}, Density: {self.properties.density} kg/m³)"


class Composite(Material):
    """A composite material with matrix and reinforcement."""

    def __init__(
        self,
        name: str,
        properties: MaterialProperties,
        matrix_material: str,
        reinforcement_material: str,
    ):
        super().__init__(name, properties)
        self.matrix_material = matrix_material
        self.reinforcement_material = reinforcement_material

    def __str__(self) -> str:
        return (
            f"{self.name} (Composite: {self.reinforcement_material} in "
            f"{self.matrix_material} matrix, Density: {self.properties.density} kg/m³)"
        )
