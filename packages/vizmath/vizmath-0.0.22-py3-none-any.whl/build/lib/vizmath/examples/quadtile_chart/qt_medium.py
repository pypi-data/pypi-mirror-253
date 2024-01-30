#%%
from vizmath.quadtile_chart import quadtile as qt
from vizmath.quadtile_chart import polyquadtile as pqt
import pandas as pd
from vizmath import functions as vf
import numpy as np

#%%
data = {
    'id' : [str(i) for i in range(1, 21)],
    'speed' : [242,200,105,100,100,95,92.5,88,80,79,
        75,67.85,61.06,60,56,55,55,55,50,50]
}
poly = [(-1000,-1000),(-1000,1000),(1000,1000),
    (1000,-1000)] # big enough container (for explainingg example output)
df = pd.DataFrame(data)
o_pq1 = pqt(df,'id','speed',buffer=5.0, collapse=True,
    constraints=poly, auto=False)
o_pq2 = pqt(df,'id','speed',buffer=5.0, collapse=True,
    constraints=poly, auto=False, size_by='width')
o_pq1.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)
o_pq2.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)
#%%
# o_pq1.o_polyquadtile_chart.df[['id','item','a','w','x','y','path']].head()
o_pq2.o_polyquadtile_chart.df[['id','item','a','w','x','y','path']].head()

#%%
# o_pq1.o_polysquares.df[['id','a','w','x','y']].head()
o_pq2.o_polysquares.df[['id','a','w','x','y']].head()

#%%
#region examples
##%%
data = {
    'id' : [str(i) for i in range(1, 21)],
    'speed' : [242,200,105,100,100,95,92.5,88,80,79,
        75,67.85,61.06,60,56,55,55,55,50,50]
}
df = pd.DataFrame(data)
qt_o_area = qt(df,'id','speed', size_by='area', buffer=0)
qt_o_width = qt(df,'id','speed', size_by='width', buffer=0)
qt_o_area.quadtile_plot(color='quad', cw=0.75, opacity=.9)
qt_o_width.quadtile_plot(color='quad', cw=0.75, opacity=.9)

##%%
data = {
    'id' : [str(i) for i in range(1, 21)],
    'speed' : [242,200,105,100,100,95,92.5,88,80,79,
        75,67.85,61.06,60,56,55,55,55,50,50]
}
df = pd.DataFrame(data)
pqt_o_area = pqt(df,'id','speed', size_by='area', buffer=0)
pqt_o_width = pqt(df,'id','speed', size_by='width', buffer=0)
pqt_o_area.polyquadtile_plot(color='quad', cw=0.75, opacity=.9)
pqt_o_width.polyquadtile_plot(color='quad', cw=0.75, opacity=.9)

#endregion

#%%
#region 1000 squares
##%%
qt_o1 = qt.random_quadtile(1000, rotate=45)
qt_o1.quadtile_plot(color='quad', cw=0.75, opacity=.9)

##%%
qt_o2 = qt.random_quadtile(1000, rotate=0)
qt_o2.quadtile_plot(color='quad', cw=0.75, opacity=.9)

##%%
# poly = [(-10,0),(0,10),(10,0),(0,-10)]
poly = [(-10,-10),(-10,10),(10,10),(10,-10)]
pqt_o1 = pqt.random_polyquadtile(1000, constraints=poly, buffer=0)
pqt_o1.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)

##%%
pqt_o2 = pqt.random_polyquadtile(1000, constraints=[(1,1)], buffer=0)
pqt_o2.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)

##%%
pqt_o3 = pqt.random_polyquadtile(1000, constraints=[(1,1)],
    buffer=0, rotate=0)
pqt_o3.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)
#endregion

#%%
pqt_o = pqt.random_polyquadtile(100, collapse=True)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True,
    show_constraints=True)

#%%
pqt_o.o_polyquadtile_chart.df[['id','item','a','w','x','y','path']].head()

#%%
pqt_o.o_polysquares.df[['id','a','w','x','y']].head()

#%%
poly = [(-200,-100),(-200,100),(200,100),(200,-100)]
qt_o = qt.random_quadtile(200, constraints=poly, packing='inc', rotate=0)
qt_o.quadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, show_constraints=True)

#%%
qt_o = qt.random_quadtile(100, constraints=poly, packing='auto', rotate=45)
qt_o.quadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, show_constraints=False)

#%%
qt_o = qt.random_quadtile(20, constraints=poly, packing='auto', rotate=45, buffer=2)
qt_o.quadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, show_constraints=False)

#%%
pqt_o = pqt(df,'id','speed', collapse=True, size_by='width', constraints=[(1,1)], buffer=0)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False)

#%%
t = np.linspace(0, 2 * np.pi, 50)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
poly = [(x,y) for x,y in zip(x,y)]
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=0, collapse=True, buffer=.1)
# pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, show_constraints=True)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, squares_off=False, show_constraints=True)

#%%
circle = vf.circle(0,0,10)
poly = [(x,y) for x,y,_ in circle]
pqt_o = pqt.random_polyquadtile(50, constraints=poly, rotate=0, collapse=True, buffer=.1)
# pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, show_constraints=True)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, squares_off=False, show_constraints=False)

#%%
u_shape_points = [(-5,-10),(-5,5),(10,5),(10,-2.5),(5,-5),(2.5,-10)]
poly = u_shape_points
pqt_o = pqt.random_polyquadtile(100, constraints=poly, rotate=45, collapse=True, buffer=.1)
# pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, show_constraints=True)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, squares_off=False, show_constraints=True)

#%%
pqt_o = pqt.random_polyquadtile(100, rotate=45, collapse=True, constraints=[(1,1)])
# pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=False, show_constraints=True)
pqt_o.polyquadtile_plot(color='quad', cw=0.75, opacity=.9, circles=True, squares_off=False, show_constraints=True)