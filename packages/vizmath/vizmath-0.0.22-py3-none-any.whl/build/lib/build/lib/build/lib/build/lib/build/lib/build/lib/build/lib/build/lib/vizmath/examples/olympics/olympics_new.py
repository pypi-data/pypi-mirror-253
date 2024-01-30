#%%
import os
import pandas as pd
from vizmath import functions as fun
from vizmath.draw import points as pts
import matplotlib.pyplot as plt

#%%
#https://www.kaggle.com/datasets/nitishsharma01/olympics-124-years-datasettill-2020?select=Athletes_summer_games.csv
df_summ = pd.read_csv(os.path.dirname(__file__) + '/Athletes_summer_games.csv')

#%% explore
# df_summ.shape
# max(df_summ.groupby('Year')['NOC'].nunique().reset_index()['NOC']) # 207 Country Max
# df_summ['Year'].unique()

#%%
df_summ = df_summ.loc[df_summ['Year'] != 1906].copy(deep=True)
df_summ = df_summ.sort_values('Year', ascending=True)
df_summ['Gold'] = [1 if x == 'Gold' else 0 for x in df_summ['Medal']]
y = 100.
y_buff = 5.
y_max = y + (df_summ['Year'].nunique() + 3) * y_buff # add skipped years
list_xy = pts()
b_list_xy = pts()
year_counter = 1896
id = 1
idb = 1
scale = 6.1
for year, group in df_summ.groupby('Year'):
    # account for skipped years
    if year != year_counter:
        steps = (year - year_counter)/4
        y += y_buff * steps
        year_counter = year
    # background
    circle_point_list = fun.circle(0, 0, points=300, r=y, end_cap=True)
    for cp in circle_point_list:
        b_list_xy.append(id=idb, x=cp[0], y=cp[1], path=cp[2], year=year)
        idb += 1
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
    # setup
    country_count = df_year.shape[0]
    country_points = fun.concentric_spread(y, scale, country_count, style='gravity')
    # draw
    p = 0
    for r, row in df_year.sort_values(by=['Gold'], ascending=False).iterrows():
        cx = country_points[p][0]
        cy = country_points[p][1]
        list_xy.append(id=id, x=cx, y=cy, path=p+1, year=year, country=row['NOC'], golds=row['Gold'], events=row['Event'], events_total=row['Events_Total'])
        id += 1
        p += 1
    y += y_buff
    year_counter += 4

list_xy.to_dataframe()
b_list_xy.to_dataframe()
extent = max(list_xy.df['x']) + 10 # buffer
list_xy.dataframe_rescale(-extent, extent, -extent, extent)
b_list_xy.dataframe_rescale(-extent, extent, -extent, extent)

#%%
list_xy.plot_xy()

#%%
list_xy.df.head()

#%% test plot
x = [r['x'] for o, r in list_xy.df.iterrows()]
y = [r['y'] for o, r in list_xy.df.iterrows()]
plt.scatter(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#%%
list_xy.dataframe_to_csv('viz_chart')

#%%
b_list_xy.dataframe_to_csv('viz_background')