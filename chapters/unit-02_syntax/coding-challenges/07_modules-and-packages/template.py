# material.py
from dataclasses import dataclass
from typing import Optional

# Import from our own modules
from properties import MaterialProperties


class Material:
    """Base class for all materials."""

    def __init__(self, name: str, properties: MaterialProperties):
        self.name = name
        self.properties = properties

    def __str__(self) -> str:
        return f"{self.name} (Density: {self.properties.density} kg/m³)"

    def can_withstand_stress(self, stress: float) -> bool:
        """Check if the material can withstand the given stress."""
        return stress < self.properties.yield_strength


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


# Add Plastic and Composite classes here
