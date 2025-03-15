"""
Test classes for the stress-strain calculator.
"""

from datetime import datetime
from typing import List, Optional

# Import from our own modules
from material import Material


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
        self.timestamp = datetime.now()

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

    def to_dict(self) -> dict:
        """Convert test data to dictionary for serialization."""
        return {
            "test_id": self.test_id,
            "material": self.material.name,
            "force": self._force,
            "area": self._area,
            "original_length": self._original_length,
            "change_in_length": self._change_in_length,
            "stress": self.stress,
            "strain": self.strain,
            "youngs_modulus": self.youngs_modulus,
            "timestamp": self.timestamp.isoformat(),
            "will_fail": self.will_fail(),
        }


class TestCollection:
    """A collection of stress-strain tests with analysis capabilities."""

    def __init__(self, name: str):
        self.name = name
        self.tests: List[StressStrainTest] = []
        self.created_at = datetime.now()

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
        report.append(
            f"Collection created: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )
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

    def to_dict(self) -> dict:
        """Convert collection to dictionary for serialization."""
        return {
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "tests": [test.to_dict() for test in self.tests],
        }

    def __str__(self) -> str:
        return f"Test Collection '{self.name}' with {len(self.tests)} tests"
