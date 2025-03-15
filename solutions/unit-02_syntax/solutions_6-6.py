from dataclasses import dataclass
from typing import Dict, List, Optional


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


class StressStrainTest:
    """A single stress-strain test."""

    def __init__(
        self,
        material: Material,
        force: float,
        area: float,
        original_length: float,
        change_in_length: float,
        test_id: Optional[str] = None,
    ):
        self.material = material
        self._force = force
        self._area = area
        self._original_length = original_length
        self._change_in_length = change_in_length
        self.test_id = test_id or f"Test-{id(self)}"

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

    def modulus_difference(self) -> float:
        """Calculate difference from typical modulus in percent."""
        typical = self.material.properties.typical_youngs_modulus
        actual = self.youngs_modulus
        return ((actual - typical) / typical) * 100

    def __str__(self) -> str:
        return (
            f"Test {self.test_id} on {self.material.name}: "
            f"Stress={self.stress:.2f} MPa, "
            f"Strain={self.strain:.6f}, "
            f"Young's Modulus={self.youngs_modulus:.2f} GPa"
        )


class TestCollection:
    """A collection of stress-strain tests with analysis capabilities."""

    def __init__(self, name: str):
        self.name = name
        self.tests: List[StressStrainTest] = []

    def add_test(self, test: StressStrainTest) -> None:
        """Add a test to the collection."""
        self.tests.append(test)

    def get_tests_by_material(self, material_name: str) -> List[StressStrainTest]:
        """Get all tests for a specific material by name."""
        return [
            test
            for test in self.tests
            if test.material.name.lower() == material_name.lower()
        ]

    def average_youngs_modulus(self, material_name: str) -> float:
        """Calculate the average Young's modulus from tests of a material."""
        tests = self.get_tests_by_material(material_name)
        if not tests:
            return 0.0
        return sum(test.youngs_modulus for test in tests) / len(tests)

    def generate_report(self) -> str:
        """Generate a comprehensive report of all tests."""
        if not self.tests:
            return "No tests to report."

        report = [f"=== Test Collection: {self.name} ===\n"]
        report.append(f"Total Tests: {len(self.tests)}\n")

        # Group tests by material
        materials = {}
        for test in self.tests:
            mat_name = test.material.name
            if mat_name not in materials:
                materials[mat_name] = []
            materials[mat_name].append(test)

        # Report for each material
        for mat_name, mat_tests in materials.items():
            report.append(f"\n== {mat_name} ==")
            report.append(f"Number of tests: {len(mat_tests)}")

            # Calculate average values
            avg_stress = sum(test.stress for test in mat_tests) / len(mat_tests)
            avg_strain = sum(test.strain for test in mat_tests) / len(mat_tests)
            avg_modulus = sum(test.youngs_modulus for test in mat_tests) / len(
                mat_tests
            )

            report.append(f"Average stress: {avg_stress:.2f} MPa")
            report.append(f"Average strain: {avg_strain:.6f}")
            report.append(f"Average Young's modulus: {avg_modulus:.2f} GPa")

            # Check against typical modulus
            typical = mat_tests[0].material.properties.typical_youngs_modulus
            percent_diff = ((avg_modulus - typical) / typical) * 100
            report.append(f"Difference from typical modulus: {percent_diff:.2f}%")

            # Check if any tests might result in failure
            failure_tests = [test for test in mat_tests if test.will_fail()]
            if failure_tests:
                report.append(
                    f"WARNING: {len(failure_tests)} test(s) exceed the yield strength!"
                )

            report.append("")  # Empty line

        return "\n".join(report)

    def __str__(self) -> str:
        return f"Test Collection '{self.name}' with {len(self.tests)} tests"


# Example material database
def create_material_database() -> Dict[str, Material]:
    """Create a database of common materials with their properties."""
    database = {}

    # Metals
    steel_props = MaterialProperties(
        density=7850, yield_strength=250, typical_youngs_modulus=200  # MPa  # GPa
    )
    database["steel"] = Metal("Steel", steel_props, is_ferrous=True)

    aluminum_props = MaterialProperties(
        density=2700, yield_strength=95, typical_youngs_modulus=69  # MPa  # GPa
    )
    database["aluminum"] = Metal("Aluminum", aluminum_props, is_ferrous=False)

    titanium_props = MaterialProperties(
        density=4500, yield_strength=140, typical_youngs_modulus=110  # MPa  # GPa
    )
    database["titanium"] = Metal(
        "Titanium", titanium_props, is_ferrous=False, is_alloy=True
    )

    # Plastics
    pvc_props = MaterialProperties(
        density=1400, yield_strength=40, typical_youngs_modulus=3.5  # MPa  # GPa
    )
    database["pvc"] = Plastic("PVC", pvc_props, is_thermoplastic=True)

    # Composites
    carbon_fiber_props = MaterialProperties(
        density=1600, yield_strength=600, typical_youngs_modulus=70  # MPa  # GPa
    )
    database["carbon_fiber"] = Composite(
        "Carbon Fiber Composite",
        carbon_fiber_props,
        matrix_material="Epoxy resin",
        reinforcement_material="Carbon fiber",
    )

    return database


# Demo function
def run_demo():
    """Run a demonstration of the material stress-strain system."""
    print("=== Material Stress-Strain Analysis System ===\n")

    # Create material database
    print("Creating material database...")
    materials = create_material_database()
    print(f"Database contains {len(materials)} materials:")
    for mat in materials.values():
        print(f"- {mat}")

    print("\n=== Creating Tests ===")
    # Crea
