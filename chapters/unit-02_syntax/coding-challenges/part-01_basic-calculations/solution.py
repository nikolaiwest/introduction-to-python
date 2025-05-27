# Part 1: Basic Stress and Strain Calculator
# Demonstrates Chapter 2 concepts: variables, data types, operators, I/O, string formatting


def main():
    """Main function for the stress and strain calculator."""

    # Program header
    print("=== Stress and Strain Calculator ===")
    print()

    # Get user input and convert to appropriate data types
    force = float(input("Enter the applied force (N): "))
    area = float(input("Enter the cross-sectional area (m²): "))
    original_length = float(input("Enter the original length (m): "))
    change_in_length = float(input("Enter the change in length (m): "))

    # Calculate stress and strain using basic arithmetic operators
    stress = force / area  # Stress = Force / Area (Pa)
    strain = change_in_length / original_length  # Strain = ΔL / L₀ (dimensionless)

    # Display input summary using f-string formatting
    print()
    print("=== RESULTS ===")
    print(f"Applied Force: {force:.2f} N")
    print(f"Cross-sectional Area: {area:.6f} m²")
    print(f"Original Length: {original_length:.3f} m")
    print(f"Change in Length: {change_in_length:.6f} m")
    print()

    # Display calculated results with appropriate precision
    print(f"Stress: {stress:.2f} Pa")
    print(f"Strain: {strain:.6f}")
    print()

    # Additional information using string concatenation and formatting
    stress_mpa = stress / 1_000_000  # Convert Pa to MPa for readability
    print(f"Stress: {stress_mpa:.2f} MPa")

    # Simple analysis using conditional expressions (ternary operator)
    strain_type = "Tension" if change_in_length > 0 else "Compression"
    print(f"Loading Type: {strain_type}")

    print()
    print("=== Analysis Complete ===")


# Program execution using the standard Python pattern
# Read this if you are still confused about this pattern:
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
if __name__ == "__main__":
    main()
