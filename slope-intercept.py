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
        print(f"The line is vertical with x = {x1}.")
        return

    # Calculate slope
    slope = (y2 - y1) / (x2 - x1)

    # Calculate y-intercept (b = y - mx)
    intercept = y1 - slope * x1

    # Display results
    print(f"Slope (m): {slope}")
    print(f"Y-Intercept (b): {intercept}")
    print(f"Equation of the line: y = {slope}x + {intercept}")

# Run the program
main()