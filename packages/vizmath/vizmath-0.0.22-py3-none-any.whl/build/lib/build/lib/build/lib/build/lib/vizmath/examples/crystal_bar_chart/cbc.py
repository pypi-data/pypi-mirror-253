#%%
from . import crystal_bar_chart as cbc

#%%
data = {'building' : ['One World Trade Center','Central Park Tower','Willis Tower',
    '111 West 57th Street','One Vanderbilt','432 Park Avenue',
    'Trump International Hotel and Tower','30 Hudson Yards',
    'Empire State Building','Bank of America Tower','St. Regis Chicago'],
    'height' : [1776,1550,1450,1428,1401,1397,1388,1270,1250,1200,1191],
    'age' : [8.5,1.5,48.5,1.5,2.5,7.5,13.5,3.5,91.5,13.5,2.5]}

df = pd.DataFrame(data=data)
df['width'] = (df['age']+5)*5.

o_cbc = cbc(df, 'building', 'height', 50, 'width', offset=-1000, rotation=90)
o_cbc.cbc_plot()