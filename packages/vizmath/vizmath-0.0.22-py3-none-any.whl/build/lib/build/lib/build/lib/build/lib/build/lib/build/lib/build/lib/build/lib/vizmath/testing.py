
# Testing

#region Nick's Radial Treemap
#%%
import radial_treemap as rtm
import pandas as pd
data = [
    ['a1', 'b1', 'c1', 12.3],
    ['a1', 'b2', 'c1', 4.5],
    ['a2', 'b1', 'c2', 32.3],
    ['a1', 'b2', 'c2', 2.1],
    ['a2', 'b1', 'c1', 5.9],
    ['a3', 'b1', 'c1', 3.5],
    ['a4', 'b2', 'c1', 3.1]]
df = pd.DataFrame(data, columns = ['a', 'b', 'c', 'value'])
o_rtm = rtm.rad_treemap(df, ['a','b','c'], 'value', 0.5, 1, 0, 180, 200,
    rotate_deg=-90, mode='alternate', default_sort_override_reversed=True, no_groups=False)
#%%
o_rtm.plot_levels(3, 0.5)
#%%
o_rtm.to_df().head()
#endregion

#region Nick's Crystal Bar Chart
#%%
from crystal_bar_chart import crystals as cbc
import pandas as pd

#%%
data = {'building' : ['One World Trade Center','Central Park Tower','Willis Tower',
    '111 West 57th Street','One Vanderbilt','432 Park Avenue',
    'Trump International Hotel and Tower','30 Hudson Yards',
    'Empire State Building','Bank of America Tower','St. Regis Chicago'],
    'height' : [1776,1550,1450,1428,1401,1397,1388,1270,1250,1200,1191],
    'age' : [8.5,1.5,48.5,1.5,2.5,7.5,13.5,3.5,91.5,13.5,2.5]}

df = pd.DataFrame(data=data)
df['width'] = (df['age']+5)*5.

o_cbc = cbc(df, 'building', 'height', 50, 'width', offset=1000, rotation=0)
o_cbc.cbc_plot(opacity=1)
#endregion

#region concentric circles

#%%
import functions as f
import matplotlib.pyplot as plt
from math import radians, cos, sin, pi

#%%

def concentric_spread(radius, arc_length, points, xo=0, yo=0, rotate=0, style=''):
    # Nick's concentric spread function
    rr = radians(rotate)
    angles =  [radians(90) - i * arc_length / radius for i in range(points)]
    avg_a = rr
    if style == 'gravity':
        avg_a += sum(angles) / points + pi/2
    elif style == 'antigravity':
        avg_a += sum(angles) / points - pi/2 
    xy_cs = [[xo + radius * cos(a-avg_a), yo + radius * sin(a-avg_a)] for a in angles]
    return xy_cs

radius = 1
arc_length = .18
angle = 90
points = 25

list_xy_1 = concentric_spread(radius, arc_length, points, xo=0, yo=0, style='', rotate=angle)
list_xy_2 = concentric_spread(radius+0.5, arc_length, points+20, xo=0, yo=0, style='', rotate=angle)
list_xy = []
list_xy.extend(list_xy_1)
list_xy.extend(list_xy_2)

x = [o[0] for o in list_xy]
y = [o[1] for o in list_xy]
plt.scatter(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#endregion