# Please note, the solutions here contain extensive comments to explain the code and concepts.
# In practice, you should aim to write clean, concise code with appropriate comments.

# First, we'll create a materials database with relevant properties
# Each material includes Young's modulus (in GPa) and yield strength (in MPa)


def create_materials_database():
    """
    Create and return a dictionary containing material properties.

    Returns:
        dict: A dictionary with materials as keys and their properties (Young's modulus and yield strength) as values
    """
    # Create a dictionary with material properties
    # Young's modulus in GPa (gigapascals)
    # Yield strength in MPa (megapascals)
    materials = {
        "steel": {
            "name": "Structural Steel",
            "youngs_modulus": 200,  # GPa
            "yield_strength": 250,  # MPa
            "description": "Common structural material with high strength and stiffness",
        },
        "aluminum": {
            "name": "Aluminum Alloy",
            "youngs_modulus": 70,  # GPa
            "yield_strength": 95,  # MPa
            "description": "Lightweight material used in aerospace and consumer products",
        },
        "copper": {
            "name": "Copper",
            "youngs_modulus": 110,  # GPa
            "yield_strength": 70,  # MPa
            "description": "Excellent electrical and thermal conductivity",
        },
        "titanium": {
            "name": "Titanium Alloy",
            "youngs_modulus": 120,  # GPa
            "yield_strength": 900,  # MPa
            "description": "High strength-to-weight ratio, excellent corrosion resistance",
        },
    }

    return materials


def validate_input(
    material, force, area, original_length, change_in_length, materials_db
):
    """
    Validate that all input values are appropriate for calculations.

    Args:
        material (str): The material name to check in the database
        force (float): Applied force in Newtons
        area (float): Cross-sectional area in square meters
        original_length (float): Original length in meters
        change_in_length (float): Change in length in meters
        materials_db (dict): Materials database for validation

    Returns:
        tuple: (is_valid, error_message)
            - is_valid (bool): True if all inputs are valid, False otherwise
            - error_message (str): Description of the error if validation fails
    """
    # Check if material exists in database
    if material.lower() not in materials_db:
        return (
            False,
            f"Error: Material '{material}' not found in database. Available materials: {', '.join(materials_db.keys())}",
        )

    # Check for negative or zero values where inappropriate
    if force <= 0:
        return False, "Error: Force must be greater than zero"

    if area <= 0:
        return False, "Error: Area must be greater than zero"

    if original_length <= 0:
        return False, "Error: Original length must be greater than zero"

    # Change in length can be negative (compression) but shouldn't equal original length
    if abs(change_in_length) >= original_length:
        return (
            False,
            "Error: Absolute value of change in length must be less than original length",
        )

    # All checks passed
    return True, ""


def calculate_stress(force, area):
    """
    Calculate stress based on force and area.

    Stress (σ) is defined as force per unit area and indicates how the
    internal forces are distributed within a material.

    Args:
        force (float): Applied force in Newtons
        area (float): Cross-sectional area in square meters

    Returns:
        float: Stress in Pascals (N/m²)

    Raises:
        ZeroDivisionError: If area is zero
    """
    try:
        stress = force / area
        return stress
    except ZeroDivisionError:
        # This should be caught by validation, but we're being defensive
        raise ZeroDivisionError("Cannot calculate stress: Area cannot be zero")


def calculate_strain(original_length, change_in_length):
    """
    Calculate strain based on original length and change in length.

    Strain (ε) is the measure of deformation representing the displacement
    between particles in a material relative to a reference length.

    Args:
        original_length (float): Original length in meters
        change_in_length (float): Change in length in meters

    Returns:
        float: Strain (dimensionless)

    Raises:
        ZeroDivisionError: If original_length is zero
    """
    try:
        strain = change_in_length / original_length
        return strain
    except ZeroDivisionError:
        # This should be caught by validation, but we're being defensive
        raise ZeroDivisionError(
            "Cannot calculate strain: Original length cannot be zero"
        )


def calculate_youngs_modulus(stress, strain):
    """
    Calculate Young's modulus from stress and strain.

    Young's modulus (E) is a measure of a material's stiffness and is defined
    as the ratio of stress to strain in the linear elastic region.

    Args:
        stress (float): Stress in Pascals
        strain (float): Strain (dimensionless)

    Returns:
        float: Young's modulus in Pascals

    Raises:
        ZeroDivisionError: If strain is zero
        ValueError: If strain is too small to give meaningful results
    """
    # Check if strain is too small (might indicate measurement error or rigid body)
    if abs(strain) < 1e-10:
        raise ValueError("Strain is too small for accurate Young's modulus calculation")

    try:
        youngs_modulus = stress / strain
        return youngs_modulus
    except ZeroDivisionError:
        raise ZeroDivisionError(
            "Cannot calculate Young's modulus: Strain cannot be zero"
        )


def assess_material_failure(stress, material_data):
    """
    Assess whether a material is likely to fail under the given stress.

    Args:
        stress (float): Calculated stress in Pascals
        material_data (dict): Material properties from the database

    Returns:
        dict: Assessment information including:
            - will_fail (bool): True if the material is likely to fail
            - safety_factor (float): Ratio of yield strength to applied stress
            - assessment (str): Textual assessment of the situation
    """
    # Convert stress from Pa to MPa for comparison with yield strength
    stress_mpa = stress / 1e6

    # Get yield strength from material data
    yield_strength = material_data["yield_strength"]

    # Calculate safety factor (how many times stronger the material is than needed)
    safety_factor = yield_strength / stress_mpa if stress_mpa > 0 else float("inf")

    # Determine if material will fail
    will_fail = stress_mpa > yield_strength

    # Create assessment message
    if will_fail:
        assessment = f"WARNING: Material will likely fail! Stress ({stress_mpa:.2f} MPa) exceeds yield strength ({yield_strength} MPa)"
    elif safety_factor < 1.5:
        assessment = f"CAUTION: Safety factor ({safety_factor:.2f}) is lower than recommended (1.5)"
    else:
        assessment = f"SAFE: Material can handle the load with a safety factor of {safety_factor:.2f}"

    return {
        "will_fail": will_fail,
        "safety_factor": safety_factor,
        "assessment": assessment,
    }


def format_results(results):
    """
    Format the calculation results into a readable string.

    Args:
        results (dict): Dictionary containing all calculation results

    Returns:
        str: Formatted string with calculation results
    """
    # Convert Pa to more readable units if needed
    stress_pa = results["stress"]
    stress_mpa = stress_pa / 1e6  # Convert to MPa for easier reading

    youngs_calculated_pa = results["youngs_modulus_calculated"]
    youngs_calculated_gpa = youngs_calculated_pa / 1e9  # Convert to GPa
    youngs_typical_gpa = results["youngs_modulus_typical"]

    # Format the output with alignment and units
    output = [
        "=" * 60,
        "STRESS AND STRAIN CALCULATION RESULTS",
        "=" * 60,
        f"Material: {results['material_name']} ({results['material_description']})",
        "-" * 60,
        "Input Parameters:",
        f"  Force: {results['force']:.2f} N",
        f"  Area: {results['area']:.6f} m²",
        f"  Original Length: {results['original_length']:.4f} m",
        f"  Change in Length: {results['change_in_length']:.6f} m",
        "-" * 60,
        "Calculated Results:",
        f"  Stress: {stress_pa:.2f} Pa ({stress_mpa:.2f} MPa)",
        f"  Strain: {results['strain']:.6f} (dimensionless)",
        f"  Young's Modulus (calculated): {youngs_calculated_pa:.2f} Pa ({youngs_calculated_gpa:.2f} GPa)",
        "-" * 60,
        "Material Properties:",
        f"  Typical Young's Modulus: {youngs_typical_gpa} GPa",
        f"  Yield Strength: {results['yield_strength']} MPa",
        "-" * 60,
        "Assessment:",
        f"  {results['assessment']}",
        "=" * 60,
    ]

    return "\n".join(output)


def main_calculator(material, force, area, original_length, change_in_length):
    """
    Main function to orchestrate the stress-strain calculations.

    This function coordinates the entire calculation process:
    1. Validates all inputs
    2. Calculates stress and strain
    3. Calculates Young's modulus
    4. Compares results with typical values
    5. Assesses potential material failure
    6. Returns formatted results

    Args:
        material (str): Material name to lookup in the database
        force (float): Applied force in Newtons
        area (float): Cross-sectional area in square meters
        original_length (float): Original length in meters
        change_in_length (float): Change in length in meters

    Returns:
        str: Formatted results if successful, error message if not
    """
    # Create materials database
    materials_db = create_materials_database()

    # Validate inputs
    is_valid, error_message = validate_input(
        material, force, area, original_length, change_in_length, materials_db
    )

    if not is_valid:
        return error_message

    try:
        # Get material properties
        material_data = materials_db[material.lower()]

        # Calculate stress and strain
        stress = calculate_stress(force, area)
        strain = calculate_strain(original_length, change_in_length)

        # Calculate Young's modulus from our measurements
        youngs_modulus = calculate_youngs_modulus(stress, strain)

        # Assess potential material failure
        failure_assessment = assess_material_failure(stress, material_data)

        # Compile all results into a dictionary
        results = {
            "material_name": material_data["name"],
            "material_description": material_data["description"],
            "force": force,
            "area": area,
            "original_length": original_length,
            "change_in_length": change_in_length,
            "stress": stress,
            "strain": strain,
            "youngs_modulus_calculated": youngs_modulus,
            "youngs_modulus_typical": material_data["youngs_modulus"],
            "yield_strength": material_data["yield_strength"],
            "assessment": failure_assessment["assessment"],
        }

        # Format and return results
        return format_results(results)

    except Exception as e:
        return f"Error during calculation: {str(e)}"


def interactive_calculator():
    """
    Run an interactive version of the stress and strain calculator.

    This function prompts the user for inputs and displays the results.
    """
    print("\nSTRESS AND STRAIN CALCULATOR")
    print("===========================\n")

    # Display available materials
    materials_db = create_materials_database()
    print("Available materials:")
    for key, data in materials_db.items():
        print(
            f"  - {key}: {data['name']} (E = {data['youngs_modulus']} GPa, Yield = {data['yield_strength']} MPa)"
        )

    # Get user inputs
    material = input("\nEnter material name: ").strip()

    try:
        force = float(input("Enter force (N): "))
        area = float(input("Enter cross-sectional area (m²): "))
        original_length = float(input("Enter original length (m): "))
        change_in_length = float(input("Enter change in length (m): "))

        # Calculate and display results
        result = main_calculator(
            material, force, area, original_length, change_in_length
        )
        print("\n" + result)

    except ValueError:
        print(
            "Error: Please enter numeric values for force, area, original length, and change in length."
        )


# Example usage

# Again, this if statement is used to check if the script is being run directly
# it is not necessary for the functions to work but considered good practice

if __name__ == "__main__":
    # Example 1: Using the main_calculator function directly
    print("\nEXAMPLE CALCULATION 1: Steel under tension")
    result1 = main_calculator(
        material="steel",
        force=50000,  # 50 kN
        area=0.001,  # 1000 mm²
        original_length=1.0,  # 1 meter
        change_in_length=0.0005,  # 0.5 mm elongation
    )
    print(result1)

    # Example 2: Another material with higher stress
    print("\nEXAMPLE CALCULATION 2: Aluminum under high stress")
    result2 = main_calculator(
        material="aluminum",
        force=100000,  # 100 kN
        area=0.001,  # 1000 mm²
        original_length=0.5,  # 0.5 meter
        change_in_length=0.002,  # 2 mm elongation
    )
    print(result2)

    # Example 3: Invalid input
    print("\nEXAMPLE CALCULATION 3: Invalid input")
    result3 = main_calculator(
        material="gold",  # Not in our database
        force=5000,
        area=0.002,
        original_length=1.0,
        change_in_length=0.0005,
    )
    print(result3)
