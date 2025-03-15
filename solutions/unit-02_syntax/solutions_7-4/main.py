"""
Main module for the stress-strain calculator.

This module imports and uses all other modules to create a complete
system for analyzing materials under stress and strain.
"""

import csv
import json
import os
from datetime import datetime

# Import our modules
try:
    # Try to import our modules
    import utils
    from database import create_material_database, save_database_to_file
    from tests import StressStrainTest, TestCollection
except ImportError as e:
    print(f"Error importing modules: {e}")
    print("Please make sure all required modules are in the same directory.")
    exit(1)


def export_to_csv(collection: TestCollection, filename: str) -> bool:
    """Export test data to a CSV file.

    Args:
        collection: The test collection to export
        filename: The name of the CSV file to create

    Returns:
        bool: True if export was successful, False otherwise
    """
    try:
        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            # Write header
            writer.writerow(
                [
                    "Test ID",
                    "Material",
                    "Force (N)",
                    "Area (mm²)",
                    "Original Length (mm)",
                    "Change in Length (mm)",
                    "Stress (MPa)",
                    "Strain",
                    "Young's Modulus (GPa)",
                    "Timestamp",
                    "Will Fail",
                ]
            )

            # Write data
            for test in collection.tests:
                writer.writerow(
                    [
                        test.test_id,
                        test.material.name,
                        test._force,
                        test._area,
                        test._original_length,
                        test._change_in_length,
                        test.stress,
                        test.strain,
                        test.youngs_modulus,
                        test.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                        "Yes" if test.will_fail() else "No",
                    ]
                )
        return True
    except Exception as e:
        print(f"Error exporting to CSV: {e}")
        return False


def save_to_json(collection: TestCollection, filename: str) -> bool:
    """Save test collection to a JSON file.

    Args:
        collection: The test collection to save
        filename: The name of the JSON file to create

    Returns:
        bool: True if save was successful, False otherwise
    """
    try:
        # Convert to serializable dictionary
        data = collection.to_dict()

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False


def create_output_directory() -> str:
    """Create a directory for output files if it doesn't exist.

    Returns:
        str: The path to the output directory
    """
    output_dir = "solutions\\unit-02_syntax\\solutions_7-4\\output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir


def main():
    """Main function to run the stress calculator program."""
    print("=== Modular Stress-Strain Analysis System ===\n")

    # Create output directory
    output_dir = create_output_directory()

    # Create a timestamp for this run
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Create material database
    print("Creating material database...")
    materials = create_material_database()
    print(f"Database contains {len(materials)} materials:")
    for mat in materials.values():
        print(f"- {mat}")

    # Save database to file
    db_filename = os.path.join(output_dir, f"material_database_{timestamp}.json")
    if save_database_to_file(materials, db_filename):
        print(f"Material database saved to {db_filename}")

    # Create a test collection
    collection = TestCollection("Materials Testing Lab")

    # Generate random tests for each material
    print("\n=== Generating Random Tests ===")
    random_tests = utils.generate_tests_for_materials(materials, tests_per_material=2)

    for test in random_tests:
        collection.add_test(test)
        print(test)

    # Create some manual tests
    print("\n=== Creating Manual Tests ===")

    # 1. Steel test with high stress (will fail)
    high_stress_test = StressStrainTest(
        materials["steel"],
        force=150000,  # N
        area=250,  # mm²
        original_length=100,  # mm
        change_in_length=0.15,  # mm
        test_id="Steel-HighStress",
    )
    collection.add_test(high_stress_test)
    print(high_stress_test)
    print(f"Will fail: {'Yes' if high_stress_test.will_fail() else 'No'}")

    # 2. Aluminum test (normal)
    aluminum_test = StressStrainTest(
        materials["aluminum"],
        force=20000,  # N
        area=300,  # mm²
        original_length=150,  # mm
        change_in_length=0.3,  # mm
        test_id="Aluminum-Normal",
    )
    collection.add_test(aluminum_test)
    print(aluminum_test)

    # Generate and print the report
    print("\n=== Test Report ===")
    report = collection.generate_report()
    print(report)

    # Save the report to a file using file I/O
    report_filename = os.path.join(output_dir, f"test_report_{timestamp}.txt")
    with open(report_filename, "w") as f:
        f.write(report)
    print(f"\nReport saved to {report_filename}")

    # Export data to CSV
    csv_filename = os.path.join(output_dir, f"test_data_{timestamp}.csv")
    if export_to_csv(collection, csv_filename):
        print(f"Test data exported to {csv_filename}")

    # Save the test collection as JSON
    json_filename = os.path.join(output_dir, f"test_collection_{timestamp}.json")
    if save_to_json(collection, json_filename):
        print(f"Test collection saved to {json_filename}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error in main program: {e}")
