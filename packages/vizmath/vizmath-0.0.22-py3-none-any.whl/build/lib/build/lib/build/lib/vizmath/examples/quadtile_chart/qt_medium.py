#%%
from vizmath.quadtile_chart import quadtile as qt
from vizmath.quadtile_chart import polyquadtile as pqt
import pandas as pd
from vizmath import functions as vf

data = {
    'id' : [str(i) for i in range(1, 21)],
    'speed' : [242,200,105,100,100,95,92.5,88,80,79,
        75,67.85,61.06,60,56,55,55,55,50,50]
}
# test = 6
# test += 1
# data = {
#     'id' : [str(i) for i in range(1, test)],
#     'speed' : [10 for _ in range(1, test)]
# }
df = pd.DataFrame(data)
# df

#%%
qt_o = qt(df,'id','speed', size_by='width', buffer=0)
qt_o.quadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)

#%%
poly = [(-200,-100),(-200,100),(200,100),(200,-100)]
qt_o = qt.random_quadtile(100, constraints=poly, packing='inc')
qt_o.quadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, show_constraints=True)

#%%
pqt_o = pqt(df,'id','speed', collapse=True, size_by='width', constraints=[(1,1)], buffer=0)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)

#%%
import numpy as np
t = np.linspace(0, 2 * np.pi, 50)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
poly = [(x,y) for x,y in zip(x,y)]
# u_shape_points = [(-5,-10),(-5,5),(10,5),(10,-2.5),(5,-5),(2.5,-10)]
# poly = u_shape_points
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=0, collapse=False, buffer=.1)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, show_constraints=True)

#%%
circle = vf.circle(0,0,10)
poly = [(x,y) for x,y,_ in circle]
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=0, collapse=False, buffer=.1)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, show_constraints=True)

#%%
u_shape_points = [(-5,-10),(-5,5),(10,5),(10,-2.5),(5,-5),(2.5,-10)]
poly = u_shape_points
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=0, collapse=False, buffer=.1)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, show_constraints=True)