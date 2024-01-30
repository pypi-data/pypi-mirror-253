
#%%
import pandas as pd
import os
import numpy as np
import random
import math
from math import cos, sin, pi
import matplotlib.pyplot as plt

class point:
    def __init__(self, id, side, x, y, path, value, group, height, width, parent=''): 
        self.id = id
        self.side = side
        self.x = x
        self.y = y
        self.path = path
        self.value = value
        self.group = group
        self.height = height
        self.width = width
        self.parent = parent
    def to_dict(self):
        return {
            'id' : self.id,
            'side' : self.side,
            'x' : self.x,
            'y' : self.y,
            'path' : self.path,
            'value' : self.value,
            'group' : self.group,
            'height' : self.height,
            'width' : self.width,
            'parent' : self.parent }

def delete_multiple_element(list_object, indices):
    indices = sorted(indices, reverse=True)
    for idx in indices:
        if idx < len(list_object):
            list_object.pop(idx)

def bubble_group(df):
    dfi = df[['item', 'Min', 'Max']]
    records = dfi.to_records(index=False)
    list_c = list(records)
    group = 0
    groups = {}
    groups[group] = [list_c[0]]
    pop_list = []
    minx = list_c[0][1]
    maxx = list_c[0][2]
    list_c.pop(0)
    while len(list_c) > 0:
        for i in range(len(list_c)):
            minx2 = list_c[i][1]
            maxx2 = list_c[i][2]
            c1 = minx <= minx2 and maxx >= minx2
            c2 = minx <= maxx2 and maxx >= maxx2
            c3 = minx2 <= minx and maxx2 >= minx
            c4 = minx2 <= maxx and maxx2 >= maxx
            if c1 or c2 or c3 or c4:
                if minx2 <= minx:
                    minx = minx2
                if maxx2 >= maxx:
                    maxx = maxx2
                groups[group].append(list_c[i])
                pop_list.append(i)
        if len(pop_list) == 0:
            group += 1
            minx = list_c[0][1]
            maxx = list_c[0][2]
            groups[group] = [list_c[0]]
            list_c.pop(0)
        else:
            delete_multiple_element(list_c, pop_list)
            pop_list = []

    rows = []
    for key in groups:
        for i in range(len(groups[key])):
            rows.append((key,groups[key][i][0]))

    df_join = pd.DataFrame(rows, columns=['group', 'item'])
    df_out = df.merge(df_join, on=['item'], how='left')
    return df_out

def place(side, width, level=0, count=1, middle_taken=False):
    if side == 'm':
        xl = -width/2.
        xr = width/2.
    elif side == 'r':
        if (count == 1 or middle_taken == False) and level == 0 :
            xl = width/2. - width/2.
            xr = width/2. + width/2.
        elif middle_taken:
            xl = level*width + width - width/2.
            xr = level*width + width + width/2.
        else:
            xl = level*width + width/2. - width/2.
            xr = level*width + width/2. + width/2.
    elif side == 'l':
        if (count == 1 or middle_taken == False) and level == 0:
            xl = -width/2. - width/2.
            xr = -width/2. + width/2.
        elif middle_taken:
            xl = -level*width + -width - width/2.
            xr = -level*width + -width + width/2.
        else:
            xl = -level*width -width/2. - width/2.
            xr = -level*width -width/2. + width/2.
    return xl, xr

def place_width(side, width, mw, rw, lw, level=0, count=1, middle_taken=False):
    if side == 'm':
        xl = -width/2.
        xr = width/2.
    elif side == 'r':
        if (count == 1 or middle_taken == False) and level == 0 :
            xl = width/2. - width/2.
            xr = width/2. + width/2.
        elif middle_taken:
            xl = rw + mw/2. + width/2. - width/2.
            xr = rw + mw/2. + width/2. + width/2.
        else:
            xl = rw + width/2. - width/2.
            xr = rw + width/2. + width/2.
    elif side == 'l':
        if (count == 1 or middle_taken == False) and level == 0:
            xl = -width/2. - width/2.
            xr = -width/2. + width/2.
        elif middle_taken:
            xl = -lw - mw/2. - width/2. - width/2.
            xr = -lw - mw/2. - width/2. + width/2.
        else:
            xl = -lw - width/2. - width/2.
            xr = -lw - width/2. + width/2.
    return xl, xr

def nextside(side, group_i=0, count=1):
    next_side = ''
    if side == 'm':
        next_side = 'r'
    elif side == 'r':
        next_side = 'l'
    elif side == 'l':
        if group_i == count-1:
            next_side = 'm'
        else:
            next_side = 'r'
    return next_side

def draw_top(list_xy, id, xmin, xmax, ymin, ymax, value, group, height, width):
    y = (ymax-ymin)/2.+ymin
    x = (xmax-xmin)/2.+xmin
    list_xy.append(point(id,0,xmin,y,0,value,group,height,width))
    list_xy.append(point(id,0,x,ymax,1,value,group,height,width))
    list_xy.append(point(id,0,xmax,y,2,value,group,height,width))
    list_xy.append(point(id,0,x,ymin,3,value,group,height,width))
    list_xy.append(point(id,0,xmin,y,4,value,group,height,width))

def draw_left(list_xy, id, xmin, xmax, ymin, ymax, value, group, height, width):
    y = (ymax-ymin)/2.+ymin
    x = (xmax-xmin)/2.+xmin

    if x >= 0:
        if y >= 0:
            list_xy.append(point(id,1,xmin,y,0,value,group,height,width))
            list_xy.append(point(id,1,x,ymin,1,value,group,height,width))
            list_xy.append(point(id,1,0.,0.,2,value,group,height,width))
            list_xy.append(point(id,1,xmin,y,3,value,group,height,width))
        else:
            list_xy.append(point(id,1,xmin,y,0,value,group,height,width))
            list_xy.append(point(id,1,x,ymax,1,value,group,height,width))
            list_xy.append(point(id,1,0.,0.,2,value,group,height,width))
            list_xy.append(point(id,1,xmin,y,3,value,group,height,width))
    else:
        if y >= 0:
            slope1 = math.inf
            if x != 0:
                slope1 = abs(ymin)/abs(x)
            slope2 = abs(y)/abs(xmin)
            if slope1 > slope2 and ymin > 0:
                list_xy.append(point(id,1,xmin,y,0,value,group,height,width))
                list_xy.append(point(id,1,x,ymin,1,value,group,height,width))
                list_xy.append(point(id,1,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,1,xmin,y,3,value,group,height,width))
            else:
                list_xy.append(point(id,1,x,ymax,0,value,group,height,width))
                list_xy.append(point(id,1,xmax,y,1,value,group,height,width))
                list_xy.append(point(id,1,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,1,x,ymax,3,value,group,height,width))
        else:
            slope1 = math.inf
            if x != 0:
                slope1 = abs(ymax)/abs(x)
            slope2 = abs(y)/abs(xmin)
            if slope1 > slope2 and ymax < 0:
                list_xy.append(point(id,1,xmin,y,0,value,group,height,width))
                list_xy.append(point(id,1,x,ymax,1,value,group,height,width))
                list_xy.append(point(id,1,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,1,xmin,y,3,value,group,height,width))
            else:
                list_xy.append(point(id,1,x,ymin,0,value,group,height,width))
                list_xy.append(point(id,1,xmax,y,1,value,group,height,width))
                list_xy.append(point(id,1,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,1,x,ymin,3,value,group,height,width))

def draw_right(list_xy, id, xmin, xmax, ymin, ymax, value, group, height, width):
    y = (ymax-ymin)/2.+ymin
    x = (xmax-xmin)/2.+xmin
    if x >= 0:
        if y >= 0:
            slope1 = math.inf
            if x != 0:
                slope1 = abs(ymin)/abs(x)
            slope2 = abs(y)/abs(xmax)
            if slope1 > slope2 and ymin > 0:
                list_xy.append(point(id,2,x,ymin,0,value,group,height,width))
                list_xy.append(point(id,2,xmax,y,1,value,group,height,width))
                list_xy.append(point(id,2,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,2,x,ymin,3,value,group,height,width))
            else:
                list_xy.append(point(id,2,x,ymax,0,value,group,height,width))
                list_xy.append(point(id,2,xmin,y,1,value,group,height,width))
                list_xy.append(point(id,2,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,2,x,ymax,3,value,group,height,width))
        else:
            slope1 = math.inf
            if x != 0:
                slope1 = abs(ymax)/abs(x)
            slope2 = abs(y)/abs(xmax)
            if slope1 > slope2 and ymax < 0:
                list_xy.append(point(id,2,x,ymax,0,value,group,height,width))
                list_xy.append(point(id,2,xmax,y,1,value,group,height,width))
                list_xy.append(point(id,2,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,2,x,ymax,3,value,group,height,width))
            else:
                list_xy.append(point(id,2,x,ymin,0,value,group,height,width))
                list_xy.append(point(id,2,xmin,y,1,value,group,height,width))
                list_xy.append(point(id,2,0.,0.,2,value,group,height,width))
                list_xy.append(point(id,2,x,ymin,3,value,group,height,width))
    else:
        if y >= 0:
            list_xy.append(point(id,2,x,ymin,0,value,group,height,width))
            list_xy.append(point(id,2,xmax,y,1,value,group,height,width))
            list_xy.append(point(id,2,0.,0.,2,value,group,height,width))
            list_xy.append(point(id,2,x,ymin,3,value,group,height,width))
        else:
            list_xy.append(point(id,2,x,ymax,0,value,group,height,width))
            list_xy.append(point(id,2,xmax,y,1,value,group,height,width))
            list_xy.append(point(id,2,0.,0.,2,value,group,height,width))
            list_xy.append(point(id,2,x,ymax,3,value,group,height,width))

def crystal_bar(df_in, id_field, height_field, height, width_field = None, 
    bottom_up = False, width_override = None):
    if width_override is not None:
        df = df_in.rename({id_field: 'item', height_field: 'x'}, axis=1)
        df['width'] = width_override
    else:
        df = df_in.rename({id_field: 'item', height_field: 'x', width_field: 'width'}, axis=1)
    df = df[['item', 'x', 'width']]
    df = df.sort_values('x', ascending=bottom_up)
    df['Min'] = df['x'] - height/2.
    df['Max'] = df['x'] + height/2.
    df = bubble_group(df)
    df_groups = df.groupby('group')
    list_xy = []
    side = 'm'
    for group, rows in df_groups:
        ll = 0
        rl = 0
        mw = 0.
        lw = 0.
        rw = 0.
        xmin = 0.
        xmax = 0.
        count = len(rows)
        middle_first = False
        group_i = 0
        if group==8:
            test = 1
        for i, row in rows.sort_values('x', ascending=bottom_up).iterrows():
            width = row['width']
            id = row['item']
            ymin = row['Min']
            ymax = row['Max']
            value = row['x']
            if side == 'm':
                mw += width
                xmin,xmax = place_width(side, width, mw, rw, lw, count=count)
                side = nextside(side)
                if group_i == 0:
                    middle_first = True
            elif side == 'r':
                xmin,xmax = place_width(side, width, mw, rw, lw, level=rl, count=count, middle_taken=middle_first)
                side = nextside(side, group_i, count)
                rl += 1
                rw += width
            elif side == 'l':
                xmin,xmax = place_width(side, width, mw, rw, lw, level=ll, count=count, middle_taken=middle_first)
                side = nextside(side, group_i, count)
                ll += 1
                lw += width
            draw_top(list_xy, id, xmin, xmax, ymin, ymax, value, group, height, width)
            draw_left(list_xy, id, xmin, xmax, ymin, ymax, value, group, height, width)
            draw_right(list_xy, id, xmin, xmax, ymin, ymax, value, group, height, width)
            group_i += 1
    df_out = pd.DataFrame.from_records([s.to_dict() for s in list_xy])
    return df_out

def rotate(x, y, angledeg, x_offset=0, y_offset=0):
    xa = x*cos(angledeg*pi/180) + y*sin(angledeg*pi/180)
    ya = -x*sin(angledeg*pi/180) + y*cos(angledeg*pi/180)
    xa += x_offset
    ya += y_offset
    return xa, ya

def crystal_bar_chart(df_in, id_field, height_field, height, width_field = None, 
    bottom_up = False, width_override = None, offset=0., reset_origin=False, rotation=0.):
    df_in[height_field] -= offset
    df_out = crystal_bar(df_in, id_field, height_field, height, width_field=width_field, bottom_up=bottom_up, width_override=width_override)
    if not reset_origin:
        df_out['y'] += offset
    if rotate != 0:
        df_out[['x', 'y']] = df_out.apply(lambda row: rotate(row['x'], row['y'], rotation), axis=1, result_type='expand')
    return df_out

def cbc_plot(df_cbc):
    fig, axs = plt.subplots()
    axs.set_aspect('equal', adjustable='box')
    df_lvl_group = df_cbc.groupby(['id','side'])
    colors = []
    for i in range(df_cbc['group'].max()+1):
        r = random.random()
        b = random.random()
        g = random.random()
        color = (r, g, b)
        axs.plot([], [], color=color, label=i+1)
        colors.append(color)
    nested_values = {name: group['group'].iloc[0] for name, group in df_lvl_group}
    sorted_group_names = sorted(nested_values, key=nested_values.get, reverse=False)
    axs.legend(bbox_to_anchor=(1, 1))
    for name in sorted_group_names:
        rows = df_lvl_group.get_group(name)
        x = rows['x'].values
        y = rows['y'].values
        i = rows['group'].values[0]
        axs.fill(x, y, alpha=0.8, fc=colors[i], linewidth=0.5, edgecolor='black')
    axs.legend()
    plt.show()

#%%
df = pd.read_csv(os.path.dirname(__file__) + '/buildings.csv')

#%%
df.head()

#%%

df['Age_2'] = (df['Age']+5)*5.
height_field = 'Height ft'
id_field = 'Name'
width_field = 'Age_2'
group_field = 'Country'
height = 50
# df['height'] = df[height_field]-1000

# df['Country'].unique()
df_in = df.loc[df['Country']=='United States'].copy(deep=True)
df_in
#%%
# df_in = df
df_out = crystal_bar_chart(df_in, id_field, height_field, height, width_field = width_field, 
    offset=1000, rotation=0)
cbc_plot(df_out)


#%%
df_out.to_csv(os.path.dirname(__file__) + '/dragonball2.csv', encoding='utf-8', index=False)

print('finished')