
#%%
from vizmath.quadtile_chart import polyquadtile as pqt
from vizmath.radial_treemap import rad_treemap as rt

#%%
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

o_pqt = pqt.random_polyquadtile(300, constraints=poly, collapse=False, rotate=54)

#%%
o_pqt.polyquadtile_plot(show_constraints=True, color='quad', poly_line='grey')