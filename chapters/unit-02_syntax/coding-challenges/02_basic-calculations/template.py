# Part 1: Basic Stress and Strain Calculator Template
# TODO: Complete this template by filling in the missing code


def main():
    """Main function for the stress and strain calculator."""

    # TODO: Print a header for your program
    print("=== Stress and Strain Calculator ===")
    print()
    """
    # TODO: Get user input for the four required values
    # Hint: Use input() to get strings, then convert with float()
    force = # TODO: Get applied force from user
    area = # TODO: Get cross-sectional area from user
    original_length = # TODO: Get original length from user
    change_in_length = # TODO: Get change in length from user
    
    # TODO: Calculate stress and strain
    # Hint: Stress = Force / Area, Strain = Change in Length / Original Length
    stress = # TODO: Calculate stress
    strain = # TODO: Calculate strain
    """

    # TODO: Display the input values using f-string formatting
    print()
    print("=== RESULTS ===")
    # TODO: Print each input value with appropriate formatting
    # Hint: Use {variable:.2f} for 2 decimal places

    print()

    # TODO: Display the calculated results
    # TODO: Print stress with 2 decimal places and units (Pa)
    # TODO: Print strain with 6 decimal places (no units - it's dimensionless)

    print()

    # BONUS TODO: Convert stress to MPa (divide by 1,000,000)
    # BONUS TODO: Determine if loading is tension or compression

    print()
    print("=== Analysis Complete ===")


# TODO: Add the standard Python execution pattern
# Hint: if __name__ == "__main__":
# Read this if you are still confused about this pattern:
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
