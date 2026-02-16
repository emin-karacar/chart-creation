import matplotlib.pyplot as plt
import numpy as np

def create_physics_graph():
    print("--- Data Analysis and Graph Plotter ---")
    
    # 1. Get the number of data points
    try:
        num_points = int(input("How many data points do you have? : "))
    except ValueError:
        print("Please enter a valid integer number.")
        return

    x_values = []
    y_values = []

    # 2. Loop to get x and y values for each point
    print("\n--- Enter Data Points ---")
    for i in range(num_points):
        print(f"Point {i + 1}:")
        try:
            x = float(input("  Enter X value: "))
            y = float(input("  Enter Y value: "))
            x_values.append(x)
            y_values.append(y)
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            return

    # 3. Get labels and title
    print("\n--- Graph Settings ---")
    x_label = input("Enter label for X-axis (e.g., Time [s]): ")
    y_label = input("Enter label for Y-axis (e.g., Velocity [m/s]): ")
    plot_title = input("Enter title for the graph: ")

    # 4. Convert lists to numpy arrays for calculation
    x_array = np.array(x_values)
    y_array = np.array(y_values)

    # 5. Calculate Linear Fit (y = mx + b)
    # polyfit returns [slope, intercept] for degree 1
    slope, intercept = np.polyfit(x_array, y_array, 1)

    # Calculate R-squared value (to see how good the fit is)
    correlation_matrix = np.corrcoef(x_array, y_array)
    correlation_xy = correlation_matrix[0, 1]
    r_squared = correlation_xy**2

    print("\n" + "="*30)
    print(f"RESULTS:")
    print(f"Slope (m): {slope:.4f}")
    print(f"Intercept (b): {intercept:.4f}")
    print(f"Equation: y = {slope:.2f}x + {intercept:.2f}")
    print(f"R-squared: {r_squared:.4f}") # 1.0 means perfect fit
    print("="*30)

    # 6. Plotting
    plt.figure(figsize=(10, 6))
    
    # Plot original data points as scatter
    plt.scatter(x_values, y_values, color='blue', label='Experimental Data', zorder=5)
    
    # Plot the best fit line
    # We create a line using the equation y = mx + b
    fit_line = slope * x_array + intercept
    plt.plot(x_values, fit_line, color='red', linestyle='--', label=f'Fit: y={slope:.2f}x + {intercept:.2f}')

    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Save the graph as an image file (optional but useful in cloud)
    plt.savefig("my_graph.png")
    print("\nGraph saved as 'my_graph.png' and displayed on screen.")
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    create_physics_graph()