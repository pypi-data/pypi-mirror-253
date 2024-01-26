#%%
import numpy as np
from scipy.optimize import minimize
from shapely.geometry import Point, Polygon
from shapely.ops import unary_union
from math import sqrt, inf
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import copy

#%%

def calc_distance_from_point(shapes, shape_type, origin):
    penalty = 0
    ref_point = Point(origin)
    if shape_type == 'circle':
        for x, y, _ in shapes:
            centroid = Point(x, y)
            penalty += centroid.distance(ref_point)
    elif shape_type == 'square':
        for x, y, side in shapes:
            centroid = Polygon([(x, y), (x + side, y),
                (x + side, y + side), (x, y + side)]).centroid
            penalty += centroid.distance(ref_point)
    return penalty

def calc_containment(shapes, shape_type):
    penalty = 0
    shapely_shapes = []
    if shape_type == 'circle':
        shapely_shapes = [Point(x, y).buffer(r) 
            for x, y, r in shapes]
    elif shape_type == 'square':
        shapely_shapes = [Polygon([(x, y), (x + side, y),
            (x + side, y + side), (x, y + side)]) 
            for x, y, side in shapes]
    for i, shape1 in enumerate(shapely_shapes):
        for j, shape2 in enumerate(shapely_shapes):
            if i != j and shape1.contains(shape2):
                penalty += 1
    return penalty

def calc_overlap_area(shapes, shape_type):
    if shape_type == 'circle':
        shapely_shapes = [Point(s[0], s[1]).buffer(s[2]) 
            for s in shapes]
    elif shape_type == 'square':
        shapely_shapes = [Polygon([(s[0], s[1]), (s[0] + s[2], s[1]), 
            (s[0] + s[2], s[1] + s[2]), (s[0], s[1] + s[2])]) 
            for s in shapes]
    merged_area = unary_union(shapely_shapes).area
    individual_areas = sum(shape.area for shape in shapely_shapes)
    return abs(individual_areas - merged_area)

def objective_function(variables, shapes, shape_type, 
    origin=(0,0), prevent_overlap_factor=2):
    for i, shape in enumerate(shapes):
        shapes[i] = (variables[i*2], variables[i*2 + 1], shape[2])
    overlap_area = calc_overlap_area(shapes, shape_type)
    contained = calc_containment(shapes, shape_type)
    sum_distance = calc_distance_from_point(shapes, shape_type, origin)
    return overlap_area*prevent_overlap_factor*(1+contained)+sum_distance

def plot_shapes(shapes, shape_type):
    fig, ax = plt.subplots()
    min_x, min_y, max_x, max_y = 0.,0.,0.,0.
    for s in shapes:
        if shape_type == 'circle':
            circle = patches.Circle((s[0], s[1]), s[2],
                facecolor='lightgrey', edgecolor='black')
            ax.add_patch(circle)
            min_x = min(min_x, s[0] - s[2])
            min_y = min(min_y, s[1] - s[2])
            max_x = max(max_x, s[0] + s[2])
            max_y = max(max_y, s[1] + s[2])
        elif shape_type == 'square':
            square = patches.Rectangle((s[0], s[1]), s[2], s[2],
                facecolor='lightgrey', edgecolor='black')
            ax.add_patch(square)
            min_x = min(min_x, s[0])
            min_y = min(min_y, s[1])
            max_x = max(max_x, s[0] + s[2])
            max_y = max(max_y, s[1] + s[2])
    padding = 1
    ax.set_xlim(min_x - padding, max_x + padding)
    ax.set_ylim(min_y - padding, max_y + padding)
    ax.set_aspect('equal', 'box')
    plt.show()

def calc_bounds(shapes, shape_type):
    total_area = 0
    if shape_type == 'circle':
        total_area = sum(np.pi * (r**2) for _, _, r in shapes)
    elif shape_type == 'square':
        total_area = sum(side**2 for _, _, side in shapes)
    estimated_side_length = sqrt(total_area)
    padding = estimated_side_length / 2
    lower_bound = 0 - padding
    upper_bound = estimated_side_length + padding
    return (lower_bound, upper_bound)

def callback(i):
    global iteration
    iteration += 1
    print(f'Iteration {iteration}')

#%%
data = {
    'id' : [str(i) for i in range(1, 21)],
    'speed' : [242,200,105,100,100,95,92.5,88,80,79,
        75,67.85,61.06,60,56,55,55,55,50,50]
}

multiplier = 10
position_seed = 123

max_v = np.max(data['speed'])
np.random.seed(position_seed)

shapes = [(np.random.uniform(0, multiplier*1.5),
    np.random.uniform(0, multiplier*1.5),
    v/max_v*multiplier) for v in data['speed']]

circles = copy.deepcopy(shapes)
squares = copy.deepcopy(shapes)

# Flatten the lists for optimization (only positions)
initial_positions = [val for s in shapes for val in s[:2]]

# Calculate dynamic bounds for circles and squares
bounds_circle = calc_bounds(circles, 'circle')
bounds_square = calc_bounds(squares, 'square')

# Adjust bounds in optimization (using only positions)
bounds_circles = [(bounds_circle[0], bounds_circle[1]) 
    for _ in range(len(initial_positions))]
bounds_squares = [(bounds_square[0], bounds_square[1])
    for _ in range(len(initial_positions))]

origin_circle = (bounds_circle[1]-bounds_circle[0])/2+bounds_circle[0]
origin_square = (bounds_square[1]-bounds_square[0])/2+bounds_square[0]

origin_circles = (origin_circle, origin_circle)
origin_squares = (origin_square, origin_square)

#%%
import time
start = time.time()

iteration = 0
optimized_circles = minimize(objective_function, initial_positions,
    args=(circles, 'circle', origin_circles), method='L-BFGS-B',
    bounds=bounds_circles, callback=callback,
    options={'maxiter': 300, 'maxfun': inf, 'ftol': 0, 'gtol': 0})
packed_circles = [(optimized_circles.x[i*2],
    optimized_circles.x[i*2 + 1], circles[i][2])
    for i in range(len(circles))]
plot_shapes(shapes, 'circle')
plot_shapes(packed_circles, 'circle')

end = time.time()
length = start - end
print("It took", start-end, "seconds")

#%%
import time
start = time.time()

iteration = 0
optimized_squares = minimize(objective_function, initial_positions,
    args=(squares, 'square', origin_squares), method='L-BFGS-B',
    bounds=bounds_squares, callback=callback,
    options={'maxiter': 300, 'maxfun': inf, 'ftol': 0, 'gtol': 0})
packed_squares = [(optimized_squares.x[i*2],
    optimized_squares.x[i*2 + 1], squares[i][2])
    for i in range(len(squares))]
plot_shapes(shapes, 'square')
plot_shapes(packed_squares, 'square')

end = time.time()
length = start - end
print("It took", start-end, "seconds")