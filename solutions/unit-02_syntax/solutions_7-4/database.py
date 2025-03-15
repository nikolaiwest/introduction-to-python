"""
Material database for stress-strain calculator.
"""

import json
import os
from typing import Dict

# Import from our own modules
from material import Composite, Material, Metal, Plastic
from properties import MaterialProperties


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


def save_database_to_file(database: Dict[str, Material], filename: str) -> bool:
    """Save the material database to a JSON file."""
    try:
        # Convert the database to a serializable format
        serializable_db = {}
        for key, material in database.items():
            material_type = material.__class__.__name__

            # Basic properties all materials have
            material_data = {
                "type": material_type,
                "name": material.name,
                "properties": {
                    "density": material.properties.density,
                    "yield_strength": material.properties.yield_strength,
                    "typical_youngs_modulus": material.properties.typical_youngs_modulus,
                },
            }

            # Add type-specific properties
            if material_type == "Metal":
                material_data["is_ferrous"] = material.is_ferrous
                material_data["is_alloy"] = material.is_alloy
            elif material_type == "Plastic":
                material_data["is_thermoplastic"] = material.is_thermoplastic
            elif material_type == "Composite":
                material_data["matrix_material"] = material.matrix_material
                material_data["reinforcement_material"] = (
                    material.reinforcement_material
                )

            serializable_db[key] = material_data

        # Write to file
        with open(filename, "w") as f:
            json.dump(serializable_db, f, indent=2)

        return True
    except Exception as e:
        print(f"Error saving database: {e}")
        return False


def load_database_from_file(filename: str) -> Dict[str, Material]:
    """Load a material database from a JSON file."""
    if not os.path.exists(filename):
        print(f"Database file {filename} not found")
        return {}

    try:
        with open(filename, "r") as f:
            data = json.load(f)

        database = {}
        for key, material_data in data.items():
            # Create material properties
            props = MaterialProperties(
                density=material_data["properties"]["density"],
                yield_strength=material_data["properties"]["yield_strength"],
                typical_youngs_modulus=material_data["properties"][
                    "typical_youngs_modulus"
                ],
            )

            # Create the appropriate material type
            material_type = material_data["type"]
            if material_type == "Metal":
                material = Metal(
                    name=material_data["name"],
                    properties=props,
                    is_ferrous=material_data["is_ferrous"],
                    is_alloy=material_data.get("is_alloy", False),
                )
            elif material_type == "Plastic":
                material = Plastic(
                    name=material_data["name"],
                    properties=props,
                    is_thermoplastic=material_data["is_thermoplastic"],
                )
            elif material_type == "Composite":
                material = Composite(
                    name=material_data["name"],
                    properties=props,
                    matrix_material=material_data["matrix_material"],
                    reinforcement_material=material_data["reinforcement_material"],
                )
            else:
                # Fallback to base Material class
                material = Material(name=material_data["name"], properties=props)

            database[key] = material

        return database
    except Exception as e:
        print(f"Error loading database: {e}")
        return {}
