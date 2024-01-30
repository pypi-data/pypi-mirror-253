#%%
import pandas as pd
import numpy as np
from vizmath.quadtile_chart import polyquadtile as pqt
from vizmath.quadtile_chart import squaremap as sm
from vizmath import functions as vf


#%%
t = np.linspace(0, 2 * np.pi, 50)
x = 16 * np.sin(t)**3 + 5
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
poly = [(x,y) for x,y in zip(x,y)]
o_sm1 = sm.random_squaremap(num_levels=3, num_top_level_items=70, items_range=(2,4), 
    value_range=(1,10), sig=0.8, collapse=True, constraints=poly, 
    rotate=0, buffer=.5)
o_sm1.o_squaremap.plot_levels(level=3, fill='w')

#%%
import os
poly = [(10.0, 0.0),
 (4.045084971874737, 2.938926261462366),
 (3.0901699437494745, 9.510565162951535),
 (-1.5450849718747368, 4.755282581475768),
 (-8.090169943749473, 5.877852522924733),
 (-5.0, 6.123233995736766e-16),
 (-8.090169943749476, -5.87785252292473),
 (-1.5450849718747377, -4.755282581475767),
 (3.0901699437494723, -9.510565162951536),
 (4.045084971874736, -2.938926261462367)]

#%%
circle = vf.circle(0,0,10)
poly = [(x,y) for x,y,_ in circle]

#%%
t = np.linspace(0, 2 * np.pi, 50)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
poly = [(x,y) for x,y in zip(x,y)]

o_pqt4 = pqt.random_polyquadtile(300, constraints=poly, collapse=True, 
    xc=5, rotate=0, buffer=0.2)
o_pqt4.polyquadtile_plot(show_constraints=True, color='quad', poly_line='grey')

#%%

poly = vf.rotate_polygon(poly,-45)
o_pqt4 = pqt.random_polyquadtile(45, constraints=poly, collapse=True, rotate=0, sides=['top'], buffer=0.1)
o_pqt4.polyquadtile_plot(show_constraints=True, color='quad', poly_line='grey')

#%%
o_pqt4.df.to_csv(os.path.dirname(__file__) + '/debug_collapse_3.csv', encoding='utf-8', index=False)

#%%
import os
poly = [
    # (10.0, 0.0),
 (4.045084971874737, 2.938926261462366),
 (3.0901699437494745, 9.510565162951535),
 (-1.5450849718747368, 4.755282581475768),
 (-8.090169943749473, 5.877852522924733),
#  (-5.0, 6.123233995736766e-16),
#  (-8.090169943749476, -5.87785252292473),
 (-1.5450849718747377, -4.755282581475767),
#  (3.0901699437494723, -9.510565162951536),
#  (4.045084971874736, -2.938926261462367)
 ]
poly = vf.rotate_polygon(poly,-45)
df = pd.read_csv(os.path.dirname(__file__) + '/debug_collapse_1.csv')
o_pqt3 = pqt(df, 'id', 'apqt_norm', constraints=poly, collapse=True, rotate=0, sides=['top'], buffer=0.1, auto=False)
o_pqt3.polyquadtile_plot(show_constraints=True, color='quad', poly_line='grey')