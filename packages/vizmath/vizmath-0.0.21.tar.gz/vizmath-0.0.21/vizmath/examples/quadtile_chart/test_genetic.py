#%%
import numpy as np
from scipy.optimize import minimize
from shapely.geometry import Point, Polygon
from shapely.ops import unary_union
from math import sqrt
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from itertools import combinations
from shapely.geometry import MultiPoint

#%%
def shapely_total_overlap_area(shapes, shape_type):
    """
    Calculate the total overlap area for a set of shapes using Shapely.
    """
    if shape_type == 'circle':
        shapely_shapes = [Point(s[0], s[1]).buffer(s[2]) for s in shapes]
    elif shape_type == 'square':
        shapely_shapes = [Polygon([(s[0], s[1]), (s[0] + s[2], s[1]), 
                                  (s[0] + s[2], s[1] + s[2]), (s[0], s[1] + s[2])]) for s in shapes]

    merged_area = unary_union(shapely_shapes).area
    individual_areas = sum(shape.area for shape in shapely_shapes)

    return abs(individual_areas - merged_area)

def shapely_area_difference_with_bounding_box(shapes, shape_type):
    """
    Calculate the absolute difference in the sum of the shape areas and their bounding box area.
    """
    if shape_type == 'circle':
        shapely_shapes = [Point(s[0], s[1]).buffer(s[2]) for s in shapes]
    elif shape_type == 'square':
        shapely_shapes = [Polygon([(s[0], s[1]), (s[0] + s[2], s[1]), 
                                  (s[0] + s[2], s[1] + s[2]), (s[0], s[1] + s[2])]) for s in shapes]

    total_shapes_area = sum(shape.area for shape in shapely_shapes)
    bounding_box = unary_union(shapely_shapes).bounds
    bounding_box_area = (bounding_box[2] - bounding_box[0]) * (bounding_box[3] - bounding_box[1])

    return abs(total_shapes_area - bounding_box_area)

# def objective_function(variables, shape_type):
#     """
#     Unified objective function that combines the overlap area and the bounding box difference area.
#     """
#     # Reshape the variables array into a list of shapes
#     if shape_type == 'circle':
#         shapes = [(variables[i], variables[i + 1], variables[i + 2]) for i in range(0, len(variables), 3)]
#     elif shape_type == 'square':
#         shapes = [(variables[i], variables[i + 1], variables[i + 2]) for i in range(0, len(variables), 3)]

#     overlap_area = shapely_total_overlap_area(shapes, shape_type)
#     bbox_difference = shapely_area_difference_with_bounding_box(shapes, shape_type)

#     return overlap_area *10 + bbox_difference

# def objective_function(variables, shapes, shape_type):
#     """
#     Objective function that combines the overlap area and the bounding box difference area,
#     considering only the positions of the shapes.
#     """
#     # Update the positions of the shapes
#     if shape_type == 'circle':
#         for i, circle in enumerate(shapes):
#             shapes[i] = (variables[i*2], variables[i*2 + 1], circle[2])  # Update x, y, keep radius constant
#     elif shape_type == 'square':
#         for i, square in enumerate(shapes):
#             shapes[i] = (variables[i*2], variables[i*2 + 1], square[2])  # Update x, y, keep side length constant

#     overlap_area = shapely_total_overlap_area(shapes, shape_type)
#     bbox_difference = shapely_area_difference_with_bounding_box(shapes, shape_type)

#     return overlap_area*10 + bbox_difference

def polygon_surrounding_area(shapes, shape_type, circle_point_resolution=4):
    """
    Calculate the area of the polygon that surrounds the shapes.
    """
    points = []
    if shape_type == 'circle':
        # For each circle, add points around the circle to the list
        for x, y, r in shapes:
            circle_points = [Point(x + r * np.cos(theta), y + r * np.sin(theta)) for theta in np.linspace(0, 2 * np.pi, circle_point_resolution)]
            points.extend(circle_points)
    elif shape_type == 'square':
        # For each square, add its corners to the list
        for x, y, side in shapes:
            square_points = [Point(x, y), Point(x + side, y), Point(x + side, y + side), Point(x, y + side)]
            points.extend(square_points)

    # Create a polygon that surrounds all the points
    polygon = MultiPoint(points).convex_hull
    return polygon.area

def objective_function(variables, shapes, shape_type):
    """
    Objective function that combines the overlap area and the polygon surrounding area.
    """
    # Update the positions of the shapes
    if shape_type == 'circle':
        for i, circle in enumerate(shapes):
            shapes[i] = (variables[i*2], variables[i*2 + 1], circle[2])  # Update x, y, keep radius constant
    elif shape_type == 'square':
        for i, square in enumerate(shapes):
            shapes[i] = (variables[i*2], variables[i*2 + 1], square[2])  # Update x, y, keep side length constant

    overlap_area = shapely_total_overlap_area(shapes, shape_type)
    polygon_area = polygon_surrounding_area(shapes, shape_type)

    return overlap_area*20 + polygon_area

def plot_shapes(shapes, shape_type):
    """
    Dynamically plot the shapes (circles or squares) based on their sizes and positions.
    """
    fig, ax = plt.subplots()

    # Initialize variables to determine the plot boundaries
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')

    for s in shapes:
        if shape_type == 'circle':
            circle = patches.Circle((s[0], s[1]), s[2], facecolor='whitesmoke', edgecolor='black')
            ax.add_patch(circle)
            # Update plot boundaries
            min_x = min(min_x, s[0] - s[2])
            min_y = min(min_y, s[1] - s[2])
            max_x = max(max_x, s[0] + s[2])
            max_y = max(max_y, s[1] + s[2])
        elif shape_type == 'square':
            square = patches.Rectangle((s[0], s[1]), s[2], s[2], facecolor='whitesmoke', edgecolor='black')
            ax.add_patch(square)
            # Update plot boundaries
            min_x = min(min_x, s[0])
            min_y = min(min_y, s[1])
            max_x = max(max_x, s[0] + s[2])
            max_y = max(max_y, s[1] + s[2])

    # Set dynamic plot boundaries with some padding
    padding = 1
    ax.set_xlim(min_x - padding, max_x + padding)
    ax.set_ylim(min_y - padding, max_y + padding)
    ax.set_aspect('equal', 'box')
    plt.show()

def calculate_dynamic_bounds(shapes, shape_type):
    """
    Calculate dynamic bounds based on the number of shapes and their sizes.
    """
    total_area = 0
    if shape_type == 'circle':
        # Sum up the areas of all circles
        total_area = sum(np.pi * (r**2) for _, _, r in shapes)
    elif shape_type == 'square':
        # Sum up the areas of all squares
        total_area = sum(side**2 for _, _, side in shapes)

    # Estimate a side length for a square that could contain all shapes
    estimated_side_length = sqrt(total_area)

    # Provide some additional space to allow free movement of shapes
    padding = estimated_side_length / 2

    # Calculate bounds (assuming a central starting point of (estimated_side_length/2, estimated_side_length/2))
    lower_bound = 0 - padding
    upper_bound = estimated_side_length + padding

    return (lower_bound, upper_bound)

def spiral(count):
    """
    Generate positions in a spiral pattern, starting from the center and moving outward in a clockwise manner.
    """
    # Start in the middle of the grid
    x, y = 0, 0
    positions = [(x, y)]

    # Spiral pattern: right, down, left, up
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    direction_index = 0
    steps = 1
    step_count = 0
    change_direction = False

    for _ in range(1, count):
        dx, dy = directions[direction_index]
        x += dx
        y += dy
        positions.append((x, y))

        step_count += 1
        if step_count == steps:
            # Change direction after a certain number of steps
            direction_index = (direction_index + 1) % 4
            change_direction = not change_direction
            step_count = 0
            if change_direction:
                steps += 1

    return positions

def position(sizes, shape_type):
    """
    Generate positions in a spiral pattern with a corrected offset, starting with the second shape.
    The first shape will be placed in the cell above the center.
    """
    # Determine the cell size based on the largest shape
    if shape_type == 'circle':
        cell_size = max(2 * r for r in sizes)  # Diameter of the largest circle
    elif shape_type == 'square':
        cell_size = max(side for side in sizes)  # Width of the largest square

    # Generate spiral positions starting with the second shape
    offset_positions = spiral(len(sizes) - 1)

    # Adjust positions to start with the second shape
    # The first shape will be placed in the cell above the center
    positions = [(0, cell_size)]  # Position for the first (largest) shape
    positions += [(x * cell_size, y * cell_size) for x, y in offset_positions]
    shapes =  [(pos[0], pos[1], size) for pos, size in zip(positions, sizes)]

    return shapes

def calculate_bounds_from_arrangement(shapes):
    """
    Calculate dynamic bounds for optimization based on the extents of the shapes' arrangement.
    """
    # Extract only the position coordinates
    positions = [(x, y) for x, y, _ in shapes]

    # Extents of the arrangement
    min_x = min(x for x, y in positions)
    max_x = max(x for x, y in positions)
    min_y = min(y for x, y in positions)
    max_y = max(y for x, y in positions)

    # Adding some padding for optimization flexibility
    padding = max(max_x - min_x, max_y - min_y) * 0.1

    # Define the bounds
    # bounds_x = (min_x - padding, max_x + padding)
    # bounds_y = (min_y - padding, max_y + padding)

    b_min = min(min_x, min_y)
    b_max = max(max_x, max_y)

    # # Pair the bounds for each position variable
    # combined_bounds = [(bounds_x, bounds_y) for _ in positions]
    # # Flatten the bounds list
    # flattened_bounds = [b for bounds in combined_bounds for b in bounds]

    return (b_min, b_max)

def callback_function(i):
    """
    Callback function to print the current iteration number.
    """
    global iteration
    iteration += 1
    # print(f"Iteration {iteration}: Current parameters {i}")
    print(f"Iteration {iteration}")

#%% TESTING DATA
# Initialize 7 circles and 7 squares with random sizes but fixed during optimization
# np.random.seed(0)
# shapes = 20
# random_circles = [(np.random.uniform(0, 8), np.random.uniform(0, 8), np.random.uniform(0.5, 1.5)) for _ in range(shapes)]
# random_squares = [(np.random.uniform(0, 8), np.random.uniform(0, 8), np.random.uniform(1, 2)) for _ in range(shapes)]

#%%
# data = {
#     'id' : [str(i) for i in range(1, 21)],
#     'speed' : [242,200,105,100,100,95,92.5,88,80,79,
#         75,67.85,61.06,60,56,55,55,55,50,50]
# }
# max_v = np.max(data['speed'])
# sizes = [v/max_v*10 for v in data['speed']]

# # Test the function with 20 circles and 20 squares (sorted, no overlap, with corrected offset)
# circles = position(sizes, 'circle')
# squares = position(sizes, 'square')
# i_circles = circles.copy()
# i_squares = squares.copy()

# initial_positions_circles = [val for circle in circles for val in circle[:2]]
# initial_positions_squares = [val for square in squares for val in square[:2]]

# # # Calculate bounds for circles and squares based on their new arrangement
# dynamic_bounds_circles = calculate_bounds_from_arrangement(circles)#, 'circle')
# dynamic_bounds_squares = calculate_bounds_from_arrangement(squares)#, 'square')
# bounds_circles = [(dynamic_bounds_circles[0], dynamic_bounds_circles[1]) for _ in range(len(initial_positions_circles))]
# bounds_squares = [(dynamic_bounds_squares[0], dynamic_bounds_squares[1]) for _ in range(len(initial_positions_squares))]

# #%%
# iteration = 0
# result_dynamic_circles = minimize(objective_function, initial_positions_circles,
#                                   args=(circles, 'circle'), method='L-BFGS-B', bounds=bounds_circles,
#                                   callback=callback_function) #options={'maxiter': max_iterations}, 
# optimized_dynamic_circles = [(result_dynamic_circles.x[i*2], result_dynamic_circles.x[i*2 + 1], circles[i][2]) 
#                              for i in range(len(circles))]
# plot_shapes(optimized_dynamic_circles, 'circle')

# #%%
# plot_shapes(i_circles, 'circle')


# #%%
# iteration = 0
# result_dynamic_squares = minimize(objective_function, initial_positions_squares,
#                                   args=(squares, 'square'), method='L-BFGS-B', bounds=bounds_squares,
#                                   callback=callback_function) #options={'maxiter': max_iterations}, 
# optimized_dynamic_squares = [(result_dynamic_squares.x[i*2], result_dynamic_squares.x[i*2 + 1], squares[i][2]) 
#                              for i in range(len(squares))]
# plot_shapes(optimized_dynamic_squares, 'square')

# #%%
# plot_shapes(i_squares, 'square')

#%%
data = {
    'id' : [str(i) for i in range(1, 21)],
    'speed' : [242,200,105,100,100,95,92.5,88,80,79,
        75,67.85,61.06,60,56,55,55,55,50,50]
}
max_v = np.max(data['speed'])
np.random.seed(123)
random_circles = [(np.random.uniform(0, 8), np.random.uniform(0, 8), v/max_v*10) for v in data['speed']]
random_squares = [(np.random.uniform(0, 8), np.random.uniform(0, 8), v/max_v*10) for v in data['speed']]

i_random_circles = random_circles.copy()
i_random_squares = random_squares.copy()

# Flatten the lists for optimization (only positions)
initial_positions_circles = [val for circle in random_circles for val in circle[:2]]
initial_positions_squares = [val for square in random_squares for val in square[:2]]

# Calculate dynamic bounds for circles and squares
dynamic_bounds_circles = calculate_dynamic_bounds(random_circles, 'circle')
dynamic_bounds_squares = calculate_dynamic_bounds(random_squares, 'square')

# Adjust bounds in optimization (using only positions)
bounds_circles = [(dynamic_bounds_circles[0], dynamic_bounds_circles[1]) for _ in range(len(initial_positions_circles))]
bounds_squares = [(dynamic_bounds_squares[0], dynamic_bounds_squares[1]) for _ in range(len(initial_positions_squares))]

#%%
max_iterations = 250

#%%
iteration = 0
result_dynamic_circles = minimize(objective_function, initial_positions_circles,
                                  args=(random_circles, 'circle'), method='L-BFGS-B', bounds=bounds_circles,
                                  callback=callback_function) #options={'maxiter': max_iterations}, 
optimized_dynamic_circles = [(result_dynamic_circles.x[i*2], result_dynamic_circles.x[i*2 + 1], random_circles[i][2]) 
                             for i in range(len(random_circles))]
plot_shapes(i_random_circles, 'circle')
plot_shapes(optimized_dynamic_circles, 'circle')

#%%
iteration = 0
result_dynamic_squares = minimize(objective_function, initial_positions_squares,
                                  args=(random_squares, 'square'), method='L-BFGS-B', bounds=bounds_squares,
                                  callback=callback_function) #options={'maxiter': max_iterations}, 
optimized_dynamic_squares = [(result_dynamic_squares.x[i*2], result_dynamic_squares.x[i*2 + 1], random_squares[i][2]) 
                             for i in range(len(random_squares))]
plot_shapes(i_random_squares, 'square')
plot_shapes(optimized_dynamic_squares, 'square')
