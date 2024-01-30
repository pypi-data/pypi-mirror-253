#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

#%%
# Function to generate circles with initial positions
def generate_shapes(num_shapes, shape_type):
    sizes = [np.random.uniform(0.5, 2.0) for _ in range(num_shapes)]
    sizes.sort(reverse=True)  # Sort sizes from largest to smallest
    return sizes

# Initialize grid and place shapes
def place_shapes_in_grid(sizes, grid_size, largest_size):
    center = grid_size // 2
    positions = [(center, center)]  # Start with the largest shape in the center
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Left, Down, Right, Up
    dir_idx = 0
    steps = 1
    x, y = center, center
    for size in sizes[1:]:
        for _ in range(2):
            for _ in range(steps):
                dx, dy = directions[dir_idx]
                x, y = x + dx * largest_size, y + dy * largest_size
                if 0 <= x < grid_size and 0 <= y < grid_size:
                    positions.append((x, y))
            dir_idx = (dir_idx + 1) % 4
        steps += 1
    return positions

# Optimization functions
def circle_touching_bonus(circles, touch_threshold=0.5):
    bonus = 0
    for i, circle in enumerate(circles):
        for j, other_circle in enumerate(circles):
            if i != j:
                dist = np.linalg.norm(circle['center'] - other_circle['center'])
                if 0 < dist < circle['radius'] + other_circle['radius'] + touch_threshold:
                    bonus += 1
    return bonus

def calculate_bounding_box_area(circles):
    min_x = min(circle['center'][0] - circle['radius'] for circle in circles)
    max_x = max(circle['center'][0] + circle['radius'] for circle in circles)
    min_y = min(circle['center'][1] - circle['radius'] for circle in circles)
    max_y = max(circle['center'][1] + circle['radius'] for circle in circles)
    return (max_x - min_x) * (max_y - min_y)

def sum_of_circle_areas(circles):
    return sum(np.pi * circle['radius']**2 for circle in circles)

def distance_to_largest_shape_penalty(circles):
    largest_shape_center = circles[0]['center']  # The largest shape is the first one in the list
    penalty = 0
    for circle in circles[1:]:  # Exclude the largest shape itself
        distance = np.linalg.norm(circle['center'] - largest_shape_center)
        penalty += distance  # Add the distance as a penalty
    return penalty

def objective_function(positions, circles):
    for i, circle in enumerate(circles):
        circle['center'] = positions[i*2:i*2+2]

    overlap_penalty = 0
    for circle in circles:
        for other_circle in circles:
            if circle is not other_circle:
                dist = np.linalg.norm(circle['center'] - other_circle['center'])
                overlap = circle['radius'] + other_circle['radius'] - dist
                if overlap > 0:
                    overlap_penalty += (overlap ** 2) * 30000

    touching_bonus = circle_touching_bonus(circles) * 5
    bounding_box_area = calculate_bounding_box_area(circles)
    circle_areas_sum = sum_of_circle_areas(circles)
    area_difference_penalty = abs(bounding_box_area - circle_areas_sum) * 100

    # Heavily weighted penalty for distance to the largest shape
    largest_shape_distance_penalty = distance_to_largest_shape_penalty(circles) * 1000  

    return overlap_penalty - touching_bonus + area_difference_penalty + largest_shape_distance_penalty

def optimize_packing(circles, initial_positions):
    """Optimizes circle positions using the heavily weighted significant bounding box penalty objective function."""
    flat_initial_positions = np.array(initial_positions).flatten()
    result = minimize(objective_function, flat_initial_positions, args=(circles,), 
                      method='L-BFGS-B')
    if result.success:
        packed_positions = result.x.reshape(-1, 2)
        for i, circle in enumerate(circles):
            circle['center'] = packed_positions[i]
    return circles

# Post-optimization processing
def drag_to_collision(circles, center_of_mass, step_size=0.01):
    for circle in circles:
        touching = False
        while not touching:
            direction = center_of_mass - circle['center']
            if np.linalg.norm(direction) < step_size:
                break
            direction /= np.linalg.norm(direction)
            new_position = circle['center'] + direction * step_size
            # Check for collision with other circles at new position
            for other_circle in circles:
                if circle is not other_circle:
                    dist = np.linalg.norm(new_position - other_circle['center'])
                    if dist < circle['radius'] + other_circle['radius']:
                        touching = True
                        break
            if not touching:
                circle['center'] = new_position

def post_optimization_processing(circles):
    cm_x = np.mean([circle['center'][0] for circle in circles])
    cm_y = np.mean([circle['center'][1] for circle in circles])
    center_of_mass = np.array([cm_x, cm_y])
    drag_to_collision(circles, center_of_mass)

# Plotting function
def plot_circles(circles, title):
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    for circle in circles:
        circle_plot = plt.Circle(circle['center'], circle['radius'], fill=False, color='blue', edgecolor='black')
        ax.add_patch(circle_plot)
        plt.scatter(*circle['center'], color='red')
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.show()

#%%
# Circle Packing Example
num_shapes = 7
circle_sizes = generate_shapes(num_shapes, 'circle')
circle_grid_size = int(np.ceil(np.sqrt(num_shapes)) * circle_sizes[0] * 2 * 2)
circle_positions = place_shapes_in_grid(circle_sizes, circle_grid_size, circle_sizes[0] * 2)
circles_for_optimization = [{'center': pos, 'radius': size} for pos, size in zip(circle_positions, circle_sizes)]
optimized_circles = optimize_packing(circles_for_optimization, circle_positions)
post_optimization_processing(optimized_circles)
plot_circles(optimized_circles, "Circle Packing")