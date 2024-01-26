
#region test

#%%
from vizmath.crystal_bar_chart import crystals as cbc
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

#%%

df = pd.read_csv(os.path.dirname(__file__) + '/buildings.csv')
df['Age_2'] = (df['Age']+5)*5.
height_field = 'Height ft'
id_field = 'Name'
width_field = 'Age_2'
group_field = 'Country'
height = 50

o_cbc = cbc(df, 'Name', 'Height ft', 50, 'Age_2', offset=0, rotation=0)
o_cbc.cbc_plot(opacity=1)

#%%
o_cbc.o_crystal_bar_chart.dataframe_to_csv('new_cbc')

#endregion

#region article

#%%
# vizmath beeswarm
from vizmath.beeswarm import swarm
import pandas as pd
from math import pi
data = {
    'id' : [str(i) for i in range(1, 14)],
    'value' : [0,1,1,2,3,5,8,13,21,34,55,89,144]
}
df = pd.DataFrame(data=data)
bs = swarm(df, 'id', 'value', None, size_override=pi*(5/2)**2) #15
bs.beeswarm_plot(color=False)

#%%
# pandas histogram
import pandas as pd
import numpy as np
data = {'value' : [0,1,1,2,3,5,8,13,21,34,55,89,144]}
data_range = df['value'].max() - df['value'].min()
num_bins = np.ceil(data_range/5).astype(int)
print(num_bins)
df['value'].hist(bins=num_bins, color='w', edgecolor='black', 
  linewidth=1.2, grid=False, figsize=(7,1.5))

#%%
# vizmath crystal bar chart
import pandas as pd
from vizmath.crystal_bar_chart import crystals
data = {
    'id' : [str(i) for i in range(1, 14)],
    'value' : [0,1,1,2,3,5,8,13,21,34,55,89,144]
}
df = pd.DataFrame(data=data)
cbc = crystals(df, 'id', 'value', 5, width_override=5, rotation=90)
cbc.cbc_plot(legend=False, alternate_color=True, color=False)

#%%
# vizmath crystal bar chart
import pandas as pd
from vizmath.crystal_bar_chart import crystals
data = {
    'id' : [str(i) for i in range(1, 14)],
    'value' : [0,1,1,2,3,5,8,13,21,34,55,89,144],
    'size' : [5,13,8,7,6,8,13,5,11,4,9,12,6] # added size
}
df = pd.DataFrame(data=data)
cbc = crystals(df, 'id', 'value', 5, width_field='size', rotation=90)
cbc.cbc_plot(legend=False, alternate_color=True, color=False)

#%%
# vizmath crystal bar chart
import pandas as pd
from vizmath.crystal_bar_chart import crystals
data = {
    'id' : [str(i) for i in range(1, 14)],
    'value' : [0,1,1,2,3,5,8,13,21,34,55,89,144]
}
df = pd.DataFrame(data=data)
df['value'] += 50 # new center
cbc = crystals(df, 'id', 'value', 5, width_override=5, rotation=90)
cbc.cbc_plot(legend=False, alternate_color=True, color=False)

#%%
# vizmath crystal bar chart
import pandas as pd
from vizmath.crystal_bar_chart import crystals
data = {
    'id' : [str(i) for i in range(1, 14)],
    'value' : [0,1,1,2,3,5,8,13,21,34,55,89,144]
}
df = pd.DataFrame(data=data)
cbc = crystals(df, 'id', 'value', 5, width_override=5,
    rotation=90, offset=21, bottom_up=True) # new offset
cbc.cbc_plot(legend=False, alternate_color=True, color=False)


#%%
# def __init__(self, df, id_field, height_field, height_range, width_field = None, 
#     bottom_up = False, width_override = None, offset=0., reset_origin=False, rotation=0.):
    
import pandas as pd
from vizmath.crystal_bar_chart import crystals
data = {
    'id' : [str(i) for i in range(1, 14)],
    'value' : [0,1,1,2,3,5,8,13,21,34,55,89,144],
    'size' : [5,13,8,7,6,8,13,5,11,4,9,12,6]
}
df = pd.DataFrame(data=data)
cbc = crystals(df, 'id', 'value', 5, width_field='size', 
    bottom_up = True, width_override = None, offset=21, reset_origin=False, rotation=90)

#endregion