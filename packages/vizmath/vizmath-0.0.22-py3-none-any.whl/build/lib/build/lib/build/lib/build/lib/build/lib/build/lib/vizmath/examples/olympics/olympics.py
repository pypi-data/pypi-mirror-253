#%%
import sys
import os
import pandas as pd
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from viz_math import *
import matplotlib.pyplot as plt

#%%
class point:
    def __init__(self, year, country, x, y, path, golds, events, events_total): 
        self.year = year
        self.country = country
        self.x = x
        self.y = y
        self.path = path
        self.golds = golds
        self.events = events
        self.events_total = events_total
    def to_dict(self):
        return {
            'year' : self.year,
            'country' : self.country,
            'x' : self.x,
            'y' : self.y,
            'path' : self.path,
            'golds' : self.golds,
            'events' : self.events,
            'events_total' : self.events_total }

class background:
    def __init__(self, year, x, y, path): 
        self.year = year
        self.x = x
        self.y = y
        self.path = path
    def to_dict(self):
        return {
            'year' : self.year,
            'x' : self.x,
            'y' : self.y,
            'path' : self.path }

def position(x_max, span, xo=None):
    if xo is None:
        xo = -x_max/2
    x1 = (x_max - span)/2
    x2 = x1 + span
    return x1, x2
    
#%%
#https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020?select=Athletes_summer_games.csv
df_summ = pd.read_csv(os.path.dirname(__file__) + '/Athletes_summer_games.csv')
df_wint = pd.read_csv(os.path.dirname(__file__) + '/Athletes_winter_games.csv')

#%% explore
# max(df_summ.groupby('Year')['NOC'].nunique().reset_index()['NOC']) # 207 Country Max

#%% explore
# df_summ['Year'].unique()

#%%
df_summ = df_summ.loc[df_summ['Year'] != 1906].copy(deep=True)
df_summ = df_summ.sort_values('Year', ascending=True)
df_summ['Gold'] = [1 if x == 'Gold' else 0 for x in df_summ['Medal']]
y = 100.
y_buff = 5.
y_max = y + (df_summ['Year'].nunique() + 3) * y_buff # addedskipped years
extent = 300
list_xy = []
b_list_xy = []
scale = 2.75
year_counter = 1896
for year, group in df_summ.groupby('Year'):
    if year != year_counter:
        steps = (year - year_counter)/4
        y += y_buff * steps
        year_counter = year
    
    # background
    circle_point_list = circle(0, 0, points=300, r=y, end_cap=True)
    for cp in circle_point_list:
        b_list_xy.append(background(year, cp[0], cp[1], cp[2]))

    countries = group['NOC'].nunique()
    yp = 1-y/y_max
    ys = yp*scale
    x1, x2 = position(extent, countries*(1+ys))
    # golds
    nat_evt = group.reset_index().groupby(['NOC','Event'])['Gold'].max().reset_index()
    nat_gold = nat_evt.groupby(['NOC'])['Gold'].sum().reset_index()
    # athletes
    nat_ath = group.groupby(['NOC'])['Name'].nunique().reset_index()
    # events
    events = group.groupby(['NOC'])['Event'].nunique().reset_index()
    events_tot = group['Event'].nunique()
    # join
    df_year = nat_gold.merge(nat_ath, on='NOC', how='left')
    df_year = nat_gold.merge(events, on='NOC', how='left')
    df_year['Events_Total'] = events_tot
    for r, row in df_year.sort_values(by=['Gold'], ascending=False).iterrows():
        p = 1
        # linear space (test):
        # xp = x1
        # yp = y
        # polar space:
        xp, yp = polarize(x1, extent, y=y)
        list_xy.append(point(year, row['NOC'], xp, yp, p, row['Gold'], row['Event'], row['Events_Total']))
        p += 1
        next = (countries*(1+ys))/countries
        x1 += next
    y += y_buff
    year_counter += 4

#%% test plot
x = [o.x for o in list_xy]
y = [o.y for o in list_xy]
plt.scatter(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#%%
df_out = pd.DataFrame.from_records([s.to_dict() for s in list_xy])
df_out['x'] = [rescale(x, -y_max, y_max, -1., 1.) for x in df_out['x']]
df_out['y'] = [rescale(y, -y_max, y_max, -1., 1.) for y in df_out['y']]
df_out.to_csv(os.path.dirname(__file__) + '/olympics_viz.csv', encoding='utf-8', index=False)

#%%
df_out_b = pd.DataFrame.from_records([s.to_dict() for s in b_list_xy])
df_out_b['x'] = [rescale(x, -y_max, y_max, -1., 1.) for x in df_out_b['x']]
df_out_b['y'] = [rescale(y, -y_max, y_max, -1., 1.) for y in df_out_b['y']]
df_out_b.to_csv(os.path.dirname(__file__) + '/olympics_viz_background.csv', encoding='utf-8', index=False)