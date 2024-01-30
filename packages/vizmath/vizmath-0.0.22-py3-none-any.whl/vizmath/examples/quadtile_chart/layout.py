#%%
from vizmath.quadtile_chart import quadtile as qt
from vizmath.quadtile_chart import polyquadtile as pqt
import pandas as pd
from vizmath import functions as vf
import numpy as np
import math

#%%
def rotate_polygon(polygon, origin, angle_degrees):
    angle_radians = math.radians(-angle_degrees)
    ox, oy = origin
    rotated_polygon = []
    for x, y in polygon:
        # Translate point to origin
        temp_x, temp_y = x - ox, y - oy
        # Rotate point
        rotated_x = temp_x * math.cos(angle_radians) - temp_y * math.sin(angle_radians)
        rotated_y = temp_x * math.sin(angle_radians) + temp_y * math.cos(angle_radians)
        # Translate point back
        final_x, final_y = rotated_x + ox, rotated_y + oy
        rotated_polygon.append((final_x, final_y))
    return rotated_polygon

#%%
circle = vf.circle(0,0,10)
poly = [(x,y) for x,y,_ in circle]
poly = rotate_polygon(poly,(0,0),-30)
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=30, collapse=True, buffer=.1)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, squares_off=False, show_constraints=False)

#%% 2.75, 2.33
poly = [(-2.75,-1.33),(0,3.33),(2.75,-1.33)]
poly = rotate_polygon(poly,(0,0),-45)
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=45, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, squares_off=False, show_constraints=False)

#%% 3.76, 4.55
poly = [(-1.76,-5.55),(-1.76,3.55),(5.76,3.55)]
poly = rotate_polygon(poly,(0,0),15)
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=-15, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, squares_off=False, show_constraints=False)

#%% 2.85, 3.76
poly = [(-2.85,-3.67),(-2.85,3.67),(2.85,3.67),(2.85,-3.67)]
poly = rotate_polygon(poly,(0,0),-45)
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=45, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, squares_off=False, show_constraints=False)

#%% w: (3.67,7.67) d:-1.9 -w:(7.67, 2.06)  
# poly = [(-1.67, 0.995),(2.67,0.995),(2.67,-0.995),(-3.28,-0.995)]
poly = [(-2.39, 1.99),(5.61,1.99),(5.61,-1.99),(-5.61,-1.99)]
poly = rotate_polygon(poly,(0,0),20)
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=-20, collapse=True, buffer=.03)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, squares_off=False, show_constraints=False)

#%% w: (2.06,4.82) d:-3.67 -w:(4.82)  d:(1.11)
poly = [(-0.7,3.67),(4.82,3.67),(4.82,-3.67),(-4.82,-3.67),(-4.82,-1.45)]
poly = rotate_polygon(poly,(0,0),-20)
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=20, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, squares_off=False, show_constraints=False)

#%% 
pqt_o = pqt.random_polyquadtile(100, constraints=[(1,1)], rotate=45, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, squares_off=False, show_constraints=False)
#%% 
pqt_o = pqt.random_polyquadtile(100, constraints=[(2,1)], rotate=45, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, squares_off=False, show_constraints=False)
#%% 
pqt_o = pqt.random_polyquadtile(100, constraints=[(3,1)], rotate=45, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, squares_off=False, show_constraints=False)
#%% 
pqt_o = pqt.random_polyquadtile(100, constraints=[(4,1)], 
    rotate=45, collapse=True, buffer=.02)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9)