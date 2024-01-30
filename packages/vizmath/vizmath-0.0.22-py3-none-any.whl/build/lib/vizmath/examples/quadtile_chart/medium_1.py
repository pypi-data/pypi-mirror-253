#%%
import pandas as pd
import matplotlib.pyplot as plt
from vizmath.quadtile_chart import polyquadtile as pq
from vizmath.crystal_bar_chart import crystals
from vizmath.beeswarm import swarm
from vizmath.radial_treemap import rad_treemap as rt
import circlify
import packcircles
from math import pi

#%%
data = {
    'id' : [str(i) for i in range(1, 21)],
    'speed' : [242,200,105,100,100,95,92.5,88,80,79,
        75,67.85,61.06,60,56,55,55,55,50,50]
}

#%%
import os
df = pd.DataFrame(data)
df.to_csv(os.path.dirname(__file__) + '/circles.csv',
    encoding='utf-8', index=False)

#%%
df = pd.DataFrame(data)
o_rt = rt(df, ['speed'], 'speed', r1=0)
o_rt.plot_levels()

#%%
df = pd.DataFrame(data)
o_rt = rt(df, ['speed'], 'speed')
o_rt.plot_levels()

#%%
df = pd.DataFrame(data)
o_rt = rt(df, ['speed'], 'speed', r1=0, r2=1,
    a1=0, a2=1, rectangular=True)
o_rt.plot_levels()

#%%
df = pd.DataFrame(data)
o_rt = rt(df, ['speed'], 'speed', r1=0, rectangular=True)
o_rt.plot_levels()

#%%
plt.figure(figsize=(7, 1.5))
bars = plt.bar(range(1, 21), data['speed'], edgecolor='black',
    color='white', linewidth=1)
plt.xticks([])
plt.grid(False)
plt.show()

#%%
o_pq = pq.random_polyquadtile(100, buffer=0.05, collapse=True) #, constraints=[(3,1)]) #, xc=0., yc=0.)
o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black')
# o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black', suqares_off=True, circles=True)

#%%
df = pd.DataFrame(data)
o_pq = pq(df,'id','speed',buffer=0.05, collapse=True, constraints=[(2,1)])
o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black')

#%%
df = pd.DataFrame(data)
df['speed'] = df['speed']**2 # width comparison instead of area
o_pq = pq(df,'id','speed',buffer=0.0, collapse=True, constraints=[(2,1)])
o_pq.polyquadtile_plot(show_constraints=True, poly_color='w', poly_line='black')

#%%
df = pd.DataFrame(data)
df['speed'] = df['speed']/df['speed'].max()*3.5
o_pq = pq(df,'id','speed',buffer=0.0, collapse=True,
    constraints=[(2,1)], auto=False)
o_pq.polyquadtile_plot(show_constraints=True, poly_color='w',
    poly_line='black', squares_off=True, circles=True)
print(o_pq.multiplier)

#%%
df = pd.DataFrame(data)
df['speed'] = df['speed']**2 # width comparison instead of area
df['speed'] = df['speed']/df['speed'].max()*3.5
o_pq = pq(df,'id','speed',buffer=0.0, collapse=True,
    constraints=[(2,1)], auto=False)
o_pq.polyquadtile_plot(show_constraints=True, poly_color='w',
    poly_line='black', squares_off=True, circles=True)

#%%
df = pd.DataFrame(data)
cbc = crystals(df, 'id', 'speed', height_range=5, width_override=5,
    rotation=90, offset=50, bottom_up=True) # new offset
cbc.cbc_plot(legend=False, alternate_color=True, color=False)

#%%
df = pd.DataFrame(data)
diameter = 5
bs = swarm(df, 'id', 'speed', None, size_override=pi*(diameter/2)**2)
bs.beeswarm_plot(color=False)

#%%
import numpy as np
def grid_bubbles(values, size_by='area', rows=2, cols=10, buffer=0.1):
    fig, ax = plt.subplots(rows, cols, figsize=(7, 1.5))
    sorted_values = np.sort(values)[::-1]
    if size_by == 'area':
        sizes = np.sqrt(sorted_values)
    elif size_by == 'diameter':
        sizes = sorted_values
    max_size = np.max(sizes)
    b = max_size*buffer
    max_size += b
    index = 0
    for i in range(rows):
        for j in range(cols):
            circle = plt.Circle((0.5, 0.5), sizes[index]/max_size/2,
                color='black', fill=False, linewidth=2)
            ax[i, j].add_artist(circle)
            ax[i, j].set_xlim(0, 1)
            ax[i, j].set_ylim(0, 1)
            ax[i, j].axis('off')
            index += 1
    fig.patch.set_edgecolor('black')
    fig.patch.set_linewidth(2)
    plt.tight_layout()
    plt.show()

#%%
# Plot corrected circles sized by diameter (actual area representation)
grid_bubbles(data['speed'], size_by='area')

#%%
# Plot corrected circles sized by radius (value representation)
grid_bubbles(data['speed'], size_by='diameter')

#%%
circles_circlify = circlify.circlify(data['speed'], show_enclosure=False)
circles = [c for c in circles_circlify]
max_radius = max(circle.r for circle in circles)
xlim = max(abs(circle.x) + max_radius for circle in circles)
ylim = max(abs(circle.y) + max_radius for circle in circles)
limit = max(xlim, ylim)
fig, axs = plt.subplots(figsize=(8, 8))
axs.axis('off')
plt.xlim(-limit, limit)
plt.ylim(-limit, limit)
for circle in circles:
    axs.add_patch(plt.Circle((circle.x, circle.y), circle.r,
        edgecolor='black', facecolor='white', linewidth=2))
plt.show()

#%%
circles_packcircles = packcircles.pack(data['speed'])
circles = [c for c in circles_packcircles]
# circles
max_radius = max(radius for (_, _, radius) in circles)
xlim = max(abs(x) + max_radius for (x, _, _) in circles)
ylim = max(abs(y) + max_radius for (_, y, _) in circles)
limit = max(xlim, ylim)
fig, axs = plt.subplots(figsize=(8, 8))
axs.axis('off')
plt.xlim(-limit, limit)
plt.ylim(-limit, limit)
for (x, y, radius) in circles:
    axs.add_patch(plt.Circle((x, y), radius,
        edgecolor='black', facecolor='white', linewidth=2))
plt.show()