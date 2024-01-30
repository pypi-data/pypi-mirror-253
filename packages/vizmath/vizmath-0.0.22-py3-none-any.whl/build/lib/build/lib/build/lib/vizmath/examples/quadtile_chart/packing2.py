#%%
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

#%%
# Function to generate shapes with initial positions
def generate_sizes(num_shapes):
    sizes = [np.random.uniform(0.5, 2.0) for _ in range(num_shapes)]
    # sizes = [abs(np.random.normal()) for _ in range(num_shapes)]
    sizes.sort(reverse=True)  # Sort sizes from largest to smallest
    return sizes

# Initialize grid and place shapes
def place_shapes_in_grid(sizes, grid_size, largest_size, shape_type):
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

# Optimization functions for circles and squares
def shape_touching_bonus(shapes, touch_threshold=0.5, shape_type='circle'):
    bonus = 0
    for i, shape in enumerate(shapes):
        for j, other_shape in enumerate(shapes):
            if i != j:
                dist = np.linalg.norm(shape['center'] - other_shape['center'])
                if shape_type == 'circle':
                    if 0 < dist < shape['radius'] + other_shape['radius'] + touch_threshold:
                        bonus += 1
                elif shape_type == 'square':
                    if dist < shape['size'] + other_shape['size'] + touch_threshold:
                        bonus += 1
    return bonus

def calculate_bounding_box_area(shapes, shape_type='circle'):
    if shape_type == 'circle':
        min_x = min(shape['center'][0] - shape['radius'] for shape in shapes)
        max_x = max(shape['center'][0] + shape['radius'] for shape in shapes)
        min_y = min(shape['center'][1] - shape['radius'] for shape in shapes)
        max_y = max(shape['center'][1] + shape['radius'] for shape in shapes)
    elif shape_type == 'square':
        min_x = min(shape['center'][0] - shape['size'] / 2 for shape in shapes)
        max_x = max(shape['center'][0] + shape['size'] / 2 for shape in shapes)
        min_y = min(shape['center'][1] - shape['size'] / 2 for shape in shapes)
        max_y = max(shape['center'][1] + shape['size'] / 2 for shape in shapes)
    return (max_x - min_x) * (max_y - min_y)

def sum_of_shape_areas(shapes, shape_type='circle'):
    if shape_type == 'circle':
        return sum(np.pi * shape['radius']**2 for shape in shapes)
    elif shape_type == 'square':
        return sum(shape['size']**2 for shape in shapes)

def distance_to_largest_shape_penalty(shapes, shape_type='circle'):
    largest_shape_center = shapes[0]['center']  # The largest shape is the first one in the list
    penalty = 0
    for shape in shapes[1:]:  # Exclude the largest shape itself
        distance = np.linalg.norm(shape['center'] - largest_shape_center)
        penalty += distance  # Add the distance as a penalty
    return penalty

def objective_function_for_circles(positions, circles):
    """ Objective function specifically for circle packing. """
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

    # touching_bonus = shape_touching_bonus(circles, shape_type='circle') * 5
    bounding_box_area = calculate_bounding_box_area(circles, shape_type='circle')
    circle_areas_sum = sum_of_shape_areas(circles, shape_type='circle')
    area_difference_penalty = abs(bounding_box_area - circle_areas_sum) * 100
    largest_shape_distance_penalty = distance_to_largest_shape_penalty(circles, shape_type='circle') * 1000  

    return overlap_penalty + area_difference_penalty + largest_shape_distance_penalty #- touching_bonus 

def optimize_circle_packing(circles, initial_positions):
    """ Optimize circle positions using a modified objective function. """
    flat_initial_positions = np.array(initial_positions).flatten()
    result = minimize(objective_function_for_circles, flat_initial_positions, args=(circles,), 
                      method='L-BFGS-B')
    if result.success:
        packed_positions = result.x.reshape(-1, 2)
        for i, circle in enumerate(circles):
            circle['center'] = packed_positions[i]
    return circles

def square_touching(s1_center, s1_size, s2_center, s2_size):
    dx = abs(s1_center[0] - s2_center[0])
    dy = abs(s1_center[1] - s2_center[1])
    return (dx < (s1_size / 2 + s2_size / 2)) and (dy < (s1_size / 2 + s2_size / 2))

def calculate_square_overlap(s1_center, s1_size, s2_center, s2_size):
    dx = max(0, min(s1_center[0] + s1_size / 2, s2_center[0] + s2_size / 2) - max(s1_center[0] - s1_size / 2, s2_center[0] - s2_size / 2))
    dy = max(0, min(s1_center[1] + s1_size / 2, s2_center[1] + s2_size / 2) - max(s1_center[1] - s1_size / 2, s2_center[1] - s2_size / 2))
    return dx * dy

def objective_function_for_squares(positions, squares):
    for i, square in enumerate(squares):
        square['center'] = positions[i*2:i*2+2]

    overlap_penalty = 0
    for square in squares:
        for other_square in squares:
            if square is not other_square:
                if square_touching(square['center'], square['size'], other_square['center'], other_square['size']):
                    overlap = calculate_square_overlap(square['center'], square['size'], other_square['center'], other_square['size'])
                    overlap_penalty += (overlap ** 2) * 8000

    # touching_bonus = shape_touching_bonus(squares, shape_type='square') * 5
    bounding_box_area = calculate_bounding_box_area(squares, shape_type='square')
    square_areas_sum = sum_of_shape_areas(squares, shape_type='square')
    area_difference_penalty = abs(bounding_box_area - square_areas_sum) * 3
    largest_shape_distance_penalty = distance_to_largest_shape_penalty(squares, shape_type='square') * 50

    return overlap_penalty + largest_shape_distance_penalty + area_difference_penalty #- touching_bonus

def optimize_square_packing(squares, initial_positions):
    flat_initial_positions = np.array(initial_positions).flatten()
    result = minimize(objective_function_for_squares, flat_initial_positions, args=(squares,), method='L-BFGS-B')
    if result.success:
        packed_positions = result.x.reshape(-1, 2)
        for i, square in enumerate(squares):
            square['center'] = packed_positions[i]
    return squares

# Post-optimization processing
# def drag_to_collision(shapes, center_of_mass, step_size=0.005, shape_type='circle'):
#     for shape in shapes:
#         touching = False
#         while not touching:
#             direction = center_of_mass - shape['center']
#             if np.linalg.norm(direction) < step_size:
#                 break
#             direction /= np.linalg.norm(direction)
#             new_position = shape['center'] + direction * step_size
#             # Check for collision with other shapes at new position
#             for other_shape in shapes:
#                 if shape is not other_shape:
#                     dist = np.linalg.norm(new_position - other_shape['center'])
#                     if shape_type == 'circle':
#                         if dist < shape['radius'] + other_shape['radius']:
#                             touching = True
#                             break
#                     elif shape_type == 'square':
#                         if dist < shape['size']/2 + other_shape['size']/2:
#                             touching = True
#                             break
#             if not touching:
#                 shape['center'] = new_position

def drag_to_collision(shapes, center_of_mass, step_size=0.01, shape_type='circle'):
    for shape in shapes:
        touching = False
        while not touching:
            direction = center_of_mass - shape['center']
            if np.linalg.norm(direction) < step_size:
                break
            direction /= np.linalg.norm(direction)
            new_position = shape['center'] + direction * step_size
            # Check for collision with other shapes at new position
            for other_shape in shapes:
                if shape is not other_shape:
                    dist = np.linalg.norm(new_position - other_shape['center'])
                    if shape_type == 'circle':
                        if dist < shape['radius'] + other_shape['radius']:
                            touching = True
                            break
                    elif shape_type == 'square':
                        # Adjusting for square using square_touching
                        if square_touching(new_position, shape['size'], other_shape['center'], other_shape['size']):
                            touching = True
                            break
            if not touching:
                shape['center'] = new_position

def drag_to_collision_until_touch(shapes, center_of_mass, step_size=0.01, shape_type='circle'):
    def is_touching_any(shape, other_shapes, shape_type):
        for other_shape in other_shapes:
            if shape is not other_shape:
                if shape_type == 'circle':
                    if np.linalg.norm(shape['center'] - other_shape['center']) < shape['radius'] + other_shape['radius']:
                        return True
                elif shape_type == 'square':
                    if square_touching(shape['center'], shape['size'], other_shape['center'], other_shape['size']):
                        return True
        return False

    any_shape_moved = True
    while any_shape_moved:
        any_shape_moved = False
        for shape in shapes:
            if not is_touching_any(shape, shapes, shape_type):
                direction = center_of_mass - shape['center']
                if np.linalg.norm(direction) < step_size:
                    continue
                direction /= np.linalg.norm(direction)
                new_position = shape['center'] + direction * step_size
                shape['center'] = new_position
                any_shape_moved = True

def post_optimization_processing(shapes, shape_type='circle'):
    cm_x = np.mean([shape['center'][0] for shape in shapes])
    cm_y = np.mean([shape['center'][1] for shape in shapes])
    center_of_mass = np.array([cm_x, cm_y])
    drag_to_collision_until_touch(shapes, center_of_mass, shape_type=shape_type)

# Plotting function for circles and squares
def plot_shapes(shapes, title, shape_type='circle'):
    plt.figure(figsize=(8, 8))
    ax = plt.gca()
    # Plotting shapes depending on the type
    for shape in shapes:
        if shape_type == 'circle':
            shape_plot = plt.Circle(shape['center'], shape['radius'], fill=False, color='blue', edgecolor='black')
        elif shape_type == 'square':
            bottom_left = (shape['center'][0] - shape['size'] / 2, shape['center'][1] - shape['size'] / 2)
            shape_plot = plt.Rectangle(bottom_left, shape['size'], shape['size'], fill=False, color='green', edgecolor='black')
        ax.add_patch(shape_plot)
        plt.scatter(*shape['center'], color='red')

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title(title)
    plt.show()


#%%
sizes = 21
shape_sizes = generate_sizes(sizes)
shape_sizes
# shape_sizes = [1.9952962739797337,
#  1.9932037754720924,
#  1.563145965390636,
#  1.514583052170552,
#  1.4202680068629192,
#  1.317556890922284,
#  1.0455445699482027,
#  0.952116752150763,
#  0.6753090922192]

#%%
# Circle Packing Example
circle_grid_size = int(np.ceil(np.sqrt(sizes)) * shape_sizes[0] * 2 * 2)
circle_positions = place_shapes_in_grid(shape_sizes, circle_grid_size, shape_sizes[0] * 2, 'circle')
circles_for_optimization = [{'center': pos, 'radius': size} for pos, size in zip(circle_positions, shape_sizes)]
optimized_circles = optimize_circle_packing(circles_for_optimization, circle_positions)
post_optimization_processing(optimized_circles, 'circle')
plot_shapes(optimized_circles, "Circle Packing", 'circle')

#%%
# Square Packing Example
square_grid_size = int(np.ceil(np.sqrt(sizes)) * shape_sizes[0] * 2 * 2)
square_positions = place_shapes_in_grid(shape_sizes, square_grid_size, shape_sizes[0] * 2, 'square')
squares_for_optimization = [{'center': pos, 'size': size} for pos, size in zip(square_positions, shape_sizes)]
optimized_squares = optimize_square_packing(squares_for_optimization, square_positions)
post_optimization_processing(optimized_squares, 'square')
plot_shapes(optimized_squares, "Square Packing", 'square')