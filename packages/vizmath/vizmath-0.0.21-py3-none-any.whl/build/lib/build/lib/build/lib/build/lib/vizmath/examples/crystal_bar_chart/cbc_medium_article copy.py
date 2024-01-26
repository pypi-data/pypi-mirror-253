
#%%
# vizmath crystal bar chart
import pandas as pd
from vizmath.crystal_bar_chart import crystals

#%%
diamonds = {
    'Name' : [
        '4 February Stone', 'Centenary Diamond', 'Cross of Asia',
        'DeBeers Diamond', 'Earth Star Diamond', 'Golden Jubilee Diamond',
        'Graff Lesedi La Rona', 'Great Mogul Diamond', 'Gruosi Diamond',
        'Incomparable Diamond', 'Jubilee Diamond', 'Koh-i-Noor',
        'Lesotho Brown', 'Lesotho Promise', 'Millennium Star',
        'Premier Rose Diamond', 'Regent Diamond', 'Taylor-Burton Diamond',
        'Tiffany Yellow Diamond'],
    'Uncut' : [
        404.2, 599, 280, 440, 248.9, 755.5, 1111, 780, 300.12, 
        890, 650.8, 793, 601, 603, 777, 353.9, 410, 241, 280],
    'Cut' : [
        163.41, 273.85, 79.12, 234.5, 111.59, 545.67, 302.37, 280, 115.34,
        407.48, 245.3, 105.6, 71.73, 75, 203.04, 137, 140.64, 68, 128.54],
    'Color' : [
        'white', 'colorless', 'yellow', '-', 'brown', 'yellow-brown',
        'colourless', '-', 'black', 'brownish-yellow', 'colorless',
        'colorless', 'pale brown', 'colorless', 'colorless',
        'colorless', 'white with pale blue', 'colorless', 'yellow'],
    'Origin' : [
        'Angola', 'South Africa', 'South Africa', 'South Africa',
        'South Africa', 'South Africa', 'Botswana', 'India', 'India',
        'Democratic Republic of Congo', 'South Africa', 'India', 'Lesotho',
        'Lesotho', 'Democratic Republic of Congo', 'South Africa', 'India',
        'South Africa', 'South Africa']
    }
df = pd.DataFrame(data=diamonds)

#%%
cbc = crystals(df, 'Name', 'Uncut', 100, width_field='Cut')
cbc.o_crystal_bar_chart.dataframe_rescale(
    0, 5000, -2500, 2500
)
cbc.o_crystal_bar_chart.df_plot_xy()

#%%
cbc.df.to_csv('data.csv')

#%%
# cbc.cbc_plot(legend=False, alternate_color=True, color=False)
cbc.to_csv('crystal_bar_chart')
