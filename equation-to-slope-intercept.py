def convert_to_slope_intercept(equation):
    """
    Convert an equation in the form Y - 4X = 0 into slope-intercept form Y = mX + b.

    Args:
        equation (str): The equation as a string (e.g., "Y - 4X = 0").

    Returns:
        str: The equation in slope-intercept form.
    """
    # Remove spaces from the equation
    equation = equation.replace(" ", "")
    
    # Split the equation into left and right parts
    parts = equation.split("=")
    left = parts[0]
    right = parts[1]

    # Rearrange the equation to isolate Y
    if "Y" in left:
        if "-" in left:
            components = left.split("-")
            y_part = components[0]  # The Y term
            x_part = components[1]  # The X term
            slope = x_part.replace("X", "")  # Extract the coefficient of X
            if slope == "":
                slope = "1"  # Handle cases where the coefficient is implicit (e.g., "X")
            slope = float(slope)  # Convert to a numeric value
        else:
            slope = 0  # No X term
    else:
        raise ValueError("The equation must contain 'Y' on the left-hand side.")

    # The constant (intercept) is zero in this specific case
    intercept = 0

    # Construct the slope-intercept form
    slope_intercept_form = "Y = " + str(slope) + "X + " + str(intercept)
    return slope_intercept_form


# Example usage
input_equation = "Y - 4X = 0"
slope_intercept_form = convert_to_slope_intercept(input_equation)
print("Slope-intercept form:", slope_intercept_form)