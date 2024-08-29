import matplotlib.pyplot as plt
import numpy as np
import uuid

# Function to create and save a dot plot
def create_dotplot(data, filename=None):
    # If no filename is provided, create a unique one
    if not filename:
        filename = f"dotplot_{uuid.uuid4().hex[:8]}.png"
    
    # Count occurrences of each data point
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    
    # Prepare data for plotting
    x = []
    y = []
    for value, count in counts.items():
        x.extend([value] * count)
        y.extend(range(1, count + 1))
    
    # Create the dot plot
    plt.figure(figsize=(12, 6))
    plt.plot(x, y, 'o', color='blue', markersize=12)
    
    # Set plot limits
    plt.xlim(min(data) - 1, max(data) + 1)
    plt.ylim(0, max(y) + 1)
    
    # Title and labels
    plt.title('Dot Plot', fontsize=16)
    plt.xlabel('Variable x-axis', fontsize=14)
    plt.ylabel('Variable y-axis', fontsize=14)
    
    # Save the plot as an image
    plt.savefig(filename)
    plt.close()

    print(f"Dot plot saved as '{filename}'")

# Get user input for the data
user_input = input("Enter your data separated by commas (e.g., 8, 9, 9, 10, 10, 10, 11, 14): ")
data = list(map(int, user_input.split(',')))

# Create the dot plot with the provided data
create_dotplot(data)
