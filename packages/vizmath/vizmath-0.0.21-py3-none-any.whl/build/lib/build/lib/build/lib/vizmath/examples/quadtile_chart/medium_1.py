#%%
import pandas as pd
from vizmath.quadtile_chart import polyquadtile as pq
from vizmath.crystal_bar_chart import crystals
from vizmath.beeswarm import swarm
import numpy as np
from math import pi

def create_rotated_rectangle(width, height, rotation_degrees=0, area=50):
    """
    Create a rotated rectangle with given width, height, rotation, and area, 
    centered at coordinates (0,0).

    Args:
    width (float): Width of the rectangle.
    height (float): Height of the rectangle.
    rotation_degrees (float): Rotation of the rectangle in degrees.
    area (float): The area of the rectangle.

    Returns:
    np.ndarray: Coordinates of the rectangle's vertices after rotation.
    """
    # Adjust width and height according to the specified area
    scale_factor = (area / (width * height)) ** 0.5
    width *= scale_factor
    height *= scale_factor

    # Rectangle vertices before rotation
    rectangle = np.array([
        [-width / 2, -height / 2],
        [-width / 2, height / 2],
        [width / 2, height / 2],
        [width / 2, -height / 2]
    ])

    # Rotation matrix
    theta = np.radians(rotation_degrees)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta), np.cos(theta)]
    ])

    # Rotated rectangle
    rotated_rectangle = np.dot(rectangle, rotation_matrix)

    return rotated_rectangle

#%%
data = {
    'id' : [str(i) for i in range(1, 21)],
    'speeds' : [242,200,105,100,100,95,92.5,88,80,79,75,67.85,61.06,60,56,55.003,55.002,55.001,50.002,50.001]
}

#%%
#%%

o_pq = pq.random_polyquadtile(50, buffer=0.0, collapse=True) #, constraints=[(2,1)], xc=0., yc=0.)
# o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black')
o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black', suqares_off=True, circles=True)

#%%
df = pd.DataFrame(data)
# o_pq = pq(df,'id','speeds',buffer=0.05, collapse=True, constraints=[(2,1)])
o_pq = pq(df,'id','speeds',buffer=0.0, collapse=True, constraints=[(2,1)])
# o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black')
o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black', suqares_off=True, circles=True)

#%%
df = pd.DataFrame(data)
cbc = crystals(df, 'id', 'speeds', 5, width_override=5,
    rotation=90, offset=50, bottom_up=False) # new offset
cbc.cbc_plot(legend=False, alternate_color=True, color=False)

#%%
df = pd.DataFrame(data)
bs = swarm(df, 'id', 'speeds', None, size_override=pi*(5/2)**2)
bs.beeswarm_plot(color=False)