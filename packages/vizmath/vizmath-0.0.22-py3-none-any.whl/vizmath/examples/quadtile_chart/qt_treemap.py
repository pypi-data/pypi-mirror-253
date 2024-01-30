#%%
import pandas as pd
from vizmath.quadtile_chart import squaremap as sm
from vizmath.radial_treemap import rad_treemap as rt
from vizmath import functions as vf

#%%
circle = vf.circle(0,0,10)
poly = [(x,y) for x,y,_ in circle]
o_sm = sm.random_squaremap(num_levels=2, num_top_level_items=25, items_range=(2,4), 
    value_range=(1,1000), sig=0.8, constraints=poly, buffer=.4)
o_sm.o_squaremap.plot_levels(level=2, fill='w')

#%%
o_sm = sm.random_squaremap(num_levels=3, num_top_level_items=4, items_range=(2,4), 
    value_range=(1,1000), sig=0.8, constraints=[(1,1)], buffer=.2, sides=['top','right'])
o_sm.o_squaremap.plot_levels(level=3, fill='w')

#%%
rotate = 45
poly = vf.rectangle(4,1,-rotate, x_offset=0, y_offset=0)
o_sm = sm.random_squaremap(num_levels=2, num_top_level_items=25, items_range=(2,5), 
    value_range=(1,1000), sig=0.8, constraints=poly, buffer=.2, sides=['top'])
o_sm.o_squaremap.plot_levels(level=2, fill='w')

#%% NEW

o_sm1 = sm.random_squaremap(num_levels=3, items_range=(2,4), 
    value_range=(1,1000), sig=0.8)
o_sm1.o_squaremap.plot_levels(level=3, fill='w')

#%%
data = [
    ['a1', 'b1', 'c1', 9.3],
    ['a1', 'b1', 'c2', 6.7],
    ['a1', 'b1', 'c3', 2.4],
    ['a1', 'b2', 'c1', 4.5],
    ['a1', 'b2', 'c2', 3.1],

    ['a2', 'b1', 'c1', 5.9],
    ['a2', 'b1', 'c2', 32.3],
    ['a2', 'b1', 'c3', 12.3],
    ['a2', 'b1', 'c4', 2.3],
    ['a2', 'b2', 'c1', 9.1],
    ['a2', 'b2', 'c2', 17.3],
    ['a2', 'b2', 'c3', 6.7],
    ['a2', 'b2', 'c4', 4.4],
    ['a2', 'b2', 'c5', 11.3],

    ['a3', 'b1', 'c1', 7.5],
    ['a3', 'b1', 'c2', 9.5],
    ['a3', 'b2', 'c3', 17.1],

    ['a4', 'b2', 'c1', 5.1],
    ['a4', 'b2', 'c2', 2.1],
    ['a4', 'b2', 'c3', 11.1],
    ['a4', 'b2', 'c4', 1.5]]

df = pd.DataFrame(data, columns = ['a', 'b', 'c', 'value'])
o_sm2 = sm(df, ['a','b','c'], 'value', constraints=[(1,1)], buffer=.2)
o_sm2.o_squaremap.plot_levels(level=3, fill='w')

#%%
df = rt.random_rad_treemap(num_levels=3, value_range=(1,1000), sig=1, data_only=True)
df.head()