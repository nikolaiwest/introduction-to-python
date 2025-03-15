"""
Utility functions for stress-strain calculations.
"""

import random
from datetime import datetime
from typing import Dict, List, Tuple

# Import from our own modules
from material import Material
from tests import StressStrainTest


def pascals_to_mpa(pascals: float) -> float:
    """Convert Pascals to MegaPascals."""
    return pascals / 1_000_000


def mpa_to_pascals(mpa: float) -> float:
    """Convert MegaPascals to Pascals."""
    return mpa * 1_000_000


def calculate_strain(original_length: float, final_length: float) -> float:
    """Calculate strain from original and final lengths."""
    return (final_length - original_length) / original_length


def calculate_stress(force: float, area: float) -> float:
    """Calculate stress from force and area."""
    return force / area


def calculate_youngs_modulus(stress: float, strain: float) -> float:
    """Calculate Young's modulus from stress and strain."""
    return stress / strain


def convert_to_gpa(pascals: float) -> float:
    """Convert Pascals to GigaPascals."""
    return pascals / 1_000_000_000


def generate_random_test(
    material: Material,
    force_range: Tuple[float, float],
    area_range: Tuple[float, float],
    length_range: Tuple[float, float],
    strain_range: Tuple[float, float],
) -> StressStrainTest:
    """Generate a random test for the given material."""
    force = random.uniform(*force_range)
    area = random.uniform(*area_range)
    original_length = random.uniform(*length_range)

    # Calculate change in length based on desired strain range
    strain = random.uniform(*strain_range)
    change_in_length = strain * original_length

    # Generate a timestamp-based ID
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    test_id = f"{material.name[:3]}-{timestamp}-{random.randint(1000, 9999)}"

    return StressStrainTest(
        material=material,
        force=force,
        area=area,
        original_length=original_length,
        change_in_length=change_in_length,
        test_id=test_id,
    )


def generate_tests_for_materials(
    materials: Dict[str, Material], tests_per_material: int = 3
) -> List[StressStrainTest]:
    """Generate random tests for each material in the database."""
    all_tests = []

    for material_name, material in materials.items():
        # Set ranges based on material type
        if material_name.lower() in ["steel", "aluminum", "titanium"]:
            # Metals - higher forces
            force_range = (30000, 100000)  # N
            area_range = (200, 500)  # mm²
            length_range = (50, 200)  # mm
            strain_range = (0.001, 0.005)  # typical elastic range
        elif material_name.lower() in ["pvc", "hdpe", "polycarbonate"]:
            # Plastics - lower forces
            force_range = (5000, 20000)  # N
            area_range = (300, 600)  # mm²
            length_range = (100, 300)  # mm
            strain_range = (0.01, 0.05)  # plastics deform more
        else:
            # Default ranges
            force_range = (10000, 50000)  # N
            area_range = (250, 400)  # mm²
            length_range = (100, 150)  # mm
            strain_range = (0.001, 0.01)

        # Generate tests for this material
        for _ in range(tests_per_material):
            test = generate_random_test(
                material=material,
                force_range=force_range,
                area_range=area_range,
                length_range=length_range,
                strain_range=strain_range,
            )
            all_tests.append(test)

    return all_tests
