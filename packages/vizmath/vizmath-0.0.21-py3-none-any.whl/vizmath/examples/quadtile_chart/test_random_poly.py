

#%%
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

#%%
def angle_between(p1, p2, p3):
    """Calculate the angle in degrees between points p1-p2-p3."""
    v1, v2 = p1 - p2, p3 - p2
    angle = np.degrees(np.math.atan2(np.linalg.det([v1,v2]),np.dot(v1,v2)))
    return abs(angle)

def generate_random_convex_polygon_adjusted_centroid():
    # Randomly choose the number of sides between 4 and 8
    num_sides = np.random.randint(4, 9)

    # Generate points on a circle with random radii
    angles = np.sort(np.random.uniform(0, 2*np.pi, num_sides))
    radii = np.random.uniform(0.1, np.sqrt(200/np.pi), num_sides)
    points = np.array([radii * np.cos(angles), radii * np.sin(angles)]).T

    # Create the polygon using ConvexHull
    hull = ConvexHull(points)
    polygon = points[hull.vertices]

    # Check for minimum angle and area condition
    area = ConvexHull(polygon).volume
    num_polygon_sides = len(polygon)
    min_angle = min([angle_between(polygon[i-1], polygon[i], polygon[(i+1) % num_polygon_sides]) for i in range(num_polygon_sides)])
    
    if area >= 200 or min_angle <= 20:
        return generate_random_convex_polygon_adjusted_centroid()

    # Adjust the centroid to be at (0,0)
    centroid = np.mean(polygon, axis=0)
    adjusted_polygon = polygon - centroid

    return adjusted_polygon

#%%
print(generate_random_convex_polygon_adjusted_centroid())