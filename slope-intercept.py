def main():
    # Prompt user for input
    print("Enter the first point:")
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    
    print("Enter the second point:")
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    # Check if the points are the same
    if x1 == x2 and y1 == y2:
        print("The two points are the same. A line cannot be determined.")
        return

    # Check if the line is vertical
    if x1 == x2:
        print("The line is vertical with x = " + str(x1) + ".")
        return

    # Calculate slope
    slope = (y2 - y1) / (x2 - x1)

    # Calculate y-intercept (b = y - mx)
    intercept = y1 - slope * x1

    # Calculate coefficients for standard form Ax + By = C
    # Rearrange y = mx + b to mx - y + b = 0, then multiply by -1 to get Ax + By = C
    A = -slope
    B = 1
    C = intercept

    # If A is negative, normalize it to be positive
    if A < 0:
        A = -A
        B = -B
        C = -C

    # Display results
    print("Slope (m):")
    print(slope)
    print("Y-Intercept (b):")
    print(intercept)
    print("Slope-Intercept Form:")
    print("y = " + str(slope) + "x + " + str(intercept))
    print("Standard Form:")
    print(str(A) + "x + " + str(B) + "y = " + str(C))

# Run the program
main()