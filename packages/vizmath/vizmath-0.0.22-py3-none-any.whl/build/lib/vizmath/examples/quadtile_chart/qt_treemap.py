#%%
import pandas as pd
from vizmath.quadtile_chart import polyquadtile as pqt
from vizmath.radial_treemap import rad_treemap as rt
from vizmath import functions as vf
import random
import math

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

def polyquadtile_treemap(df, groupers, value_field, buffer=0, ar=[(1,1)], sides=['top','right','bottom','left'], rotate=0, origin=(0,0)):
    top_field = groupers[0]
    bottom_fields = groupers[1:]
    top_level = df.groupby(top_field).sum().reset_index()
    o_pqt = pqt(top_level,top_field,value_field, rotate=0, sides=sides, buffer=buffer, constraints=ar)
    o_pqt.o_polysquares.df['width'] = o_pqt.o_polysquares.df['w'] - 2*o_pqt.buffer
    polyquadtile = o_pqt.o_polyquadtile_chart.df[['item','side','x','y','path']].copy(deep=True)
    polyquadtile.rename({'item': 'group'}, axis=1, inplace=True)
    treemaps = [polyquadtile]
    for i in range(len(o_pqt.o_polysquares.viz)):
        id = o_pqt.o_polysquares.viz[i].id
        w = o_pqt.o_polysquares.viz[i].w
        x = o_pqt.o_polysquares.viz[i].x
        y = o_pqt.o_polysquares.viz[i].y
        side = o_pqt.o_polysquares.viz[i].side
        sw = w-2*o_pqt.buffer
        x1, x2 = x-sw/2, x+sw/2
        y1, y2 = y-sw/2, y+sw/2
        df_tm = df.loc[df[top_field]==id].copy(deep=True)
        o_rt = rt(df_tm, bottom_fields, value_field, r1=y1, r2=y2,
            a1=x1, a2=x2, rectangular=True)
        o_rt.o_rad_treemap.df['side'] = side
        o_rt.o_rad_treemap.df['group'] = o_rt.o_rad_treemap.df['group'].apply(
            lambda x: (id,) + tuple(x.split(',')) if isinstance(x, str) else (id,) + x)
        treemaps.append(o_rt.o_rad_treemap.df[['group','side','x','y','path']])
    pqt_tm = pd.concat(treemaps, axis=0)
    
    # treemap attributes
    o_rt = rt(df, groupers, value_field, r1=0, r2=1, a1=0, a2=1, rectangular=True)
    o_rt.o_rad_treemap.df.drop_duplicates(subset=['count','group','level','level_rank','overall_rank','value'], inplace=True)
    tma = o_rt.o_rad_treemap.df[['count','group','level','level_rank','overall_rank','value']].copy(deep=True)
    pqt_tm_df = pd.merge(pqt_tm, tma, how ='left', on ='group')
    o_rt.df_rad_treemap = pqt_tm_df
    if rotate != 0:
        o_rt.df_rad_treemap[['x', 'y']] = o_rt.df_rad_treemap.apply(lambda row: 
            ((math.cos(math.radians(rotate)) * (row['x'] - origin[0]) - 
            math.sin(math.radians(rotate)) * (row['y'] - origin[1])) + origin[0],
            (math.sin(math.radians(rotate)) * (row['x'] - origin[0]) + 
            math.cos(math.radians(rotate)) * (row['y'] - origin[1])) + origin[1]), axis=1, result_type='expand')
    return o_rt

def generate_hierarchical_data(num_levels=3, num_top_level_items=10, items_range=(2,5), value_range=(1,100), 
        outlier_fraction=0.2, use_log=True, sig=100):
    
    data = []
    min_val, max_val = value_range
    min_items, max_items = items_range
    # adjust the value range for each top-level item to add more variability
    top_level_ranges = [(random.uniform(min_val, max_val/2), random.uniform(max_val/2, max_val)) for _ in range(num_top_level_items)]

    def generate_value(current_range):
        # decide if the value should be an outlier
        if random.random() < outlier_fraction:
            value_range = current_range
        else:
            value_range = (current_range[0], current_range[0] + (current_range[1] - current_range[0]) * (1 - outlier_fraction))
        # generate value based on specified distribution
        if use_log:
            mean = (math.log(value_range[0]) + math.log(value_range[1])) / 2
            sigma = (math.log(value_range[1]) - mean) / sig
            return random.lognormvariate(mean, sigma)
        else:
            return random.uniform(*value_range)

    def create_rows(prefix, level_idx):
        if level_idx == num_levels:
            # determine the value range based on the top level
            current_range = top_level_ranges[int(prefix[0][1:]) - 1] if level_idx > 1 else value_range
            value = generate_value(current_range)
            data.append(prefix + [value])
        else:
            for item in range(random.randint(min_items, max_items) if level_idx > 0 else num_top_level_items):
                create_rows(prefix + [f'{chr(97 + level_idx)}{item + 1}'], level_idx + 1)

    create_rows([], 0)
    headers = [chr(97 + i) for i in range(num_levels)] + ['value']
    df = pd.DataFrame(data, columns = headers)
    return df

#%%
df = generate_hierarchical_data(4, 25, (2,5), (1,100), .2, True, 100)
df.shape

#%%
circle = vf.circle(0,0,10)
poly = [(x,y) for x,y,_ in circle]
pqt_tm = polyquadtile_treemap(df,['a','b','c','d'],'value', buffer=.3, ar=poly, rotate=-45, sides=['top','right'])
pqt_tm.plot_levels(level=2, fill='w')

#%%
rotate = 45
poly = vf.rectangle(4,1,-rotate, x_offset=0, y_offset=0)
pqt_tm = polyquadtile_treemap(df,['a','b','c','d'],'value', buffer=.125, ar=poly, rotate=-rotate, sides=['top']) #,'right'])
pqt_tm.plot_levels(level=2, fill='w')

#%%
pqt_tm.plot_levels(level=3, fill='w')

#%%
pqt_tm.df_rad_treemap.head(10)

#%% NEW

o_sm1 = squaremap.random_squaremap(num_levels=3)
o_sm1.o_squaremap.plot_levels(level=3, fill='w')

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
o_sm2 = squaremap(df, ['a','b','c'], 'value', constraints=[(1,1)], buffer=.2)
o_sm2.o_squaremap.plot_levels(level=3, fill='w')