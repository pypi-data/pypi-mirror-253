#%%
import pandas as pd
import os
from vizmath.quadtile_chart import polyquadtile as pqt
from vizmath import functions as vf

#%%
data = {
    'river' : [str(i) for i in range(1, 51)],
    'length_km' : [
        6650,6400,6300,6275,5539,5464,5410,4880,4700,4444,4400,4350,4241,
        4200,3969,3672,3650,3645,3610,3596,3380,3211,3185,3180,3078,3060,
        3058,3057,2989,2888,2809,2740,2720,2704,2620,2615,2570,2549,2513,
        2500,2490,2450,2428,2410,2348,2333,2292,2287,2273,2270],
    'length_m' : [
        4130,3976,3917,3902,3445,3395,3364,3030,2922,2763,2736,2705,2637,
        2611,2466,2282,2270,2266,2250,2236,2100,1995,1980,1976,1913,1901,
        1900,1900,1857,1795,1745.8,1703,1700,1690,1628,1625,1597,1584,
        1562,1553,1547,1522,1509,1498,1459,1450,1424,1421,1412,1410],
    'drainage_area_km2' : [
        3254555,7000000,1800000,2980000,2580000,745000,2990000,2582672,
        3680000,1855000,2490000,810000,1790000,2090000,712035,1061000,
        950000,1380000,960000,884000,1485200,63166,850000,610000,219000,
        324000,1030000,570000,473000,817000,404200,1330000,454000,1024000,
        534739,242259,1093000,900000,644000,270000,1547,1522,1509,1498,
        1459,1450,1424,1421,1412,1410],
    'average_discharge_m3_s' : [
        2800,209000,30166,16792,18050,2571,12475,22000,41800,11400,15500,
        16000,10300,5589,19800,767,13598,8080,7160,856,31200,8400,6210,
        3300,703,3153,10100,82,3600,7130,13000,4880,1480,12037,1400,6000,
        2575,4300,3800,270000,1547,1522,1509,1498,1459,1450,1424,1421,
        1412,1410],
    'outflow' : [
        'Mediterranean','Atlantic Ocean','East China Sea','Gulf of Mexico',
        'Kara Sea','Bohai Sea','Gulf of Ob','Río de la Plata',
        'Atlantic Ocean','Sea of Okhotsk','Laptev Sea','South China Sea',
        'Beaufort Sea','Gulf of Guinea','Ganges','Southern Ocean',
        'Atlantic Ocean (Marajó Bay), Amazon Delta','Caspian Sea',
        'Arabian Sea','Persian Gulf','Amazon','Amazon','Bering Sea',
        'Atlantic Ocean','Aral Sea','Andaman Sea','Gulf of Saint Lawrence',
        'Gulf of Mexico','Yenisei','Black Sea','Andaman Sea',
        'Mozambique Channel','Lena','Bay of Bengal','Aral Sea','Amazon',
        'Hudson Bay','Paraná','East Siberian Sea','Paraguay','Ob','Irtysh',
        'Caspian Sea','Amazon','Mississippi','Gulf of California',
        'Laptev Sea','Black Sea','Lena','Congo'],
    'name': [
        'Nile–White Nile–Kagera–Nyabarongo–Mwogo–Rukarara',
        'Amazon–Ucayali–Tambo–Ene–Mantaro',
        'Yangtze–Jinsha–Tongtian–Dangqu (Chang Jiang)',
        'Mississippi–Missouri–Jefferson–Beaverhead–Red Rock–Hell Roaring',
        'Yenisey–Angara–Selenga–Ider','Yellow River (Huang He)','Ob–Irtysh',
        'Río de la Plata–Paraná–Rio Grande','Congo–Chambeshi (Zaïre)',
        'Amur–Argun–Kherlen (Heilong Jiang)','Lena','Mekong (Lancang Jiang)',
        'Mackenzie–Slave–Peace–Finlay','Niger','Brahmaputra–Yarlung Tsangpo',
        'Murray–Darling–Culgoa–Balonne–Condamine','Tocantins–Araguaia',
        'Volga','Indus–Sênggê Zangbo','Shatt al-Arab–Euphrates–Murat',
        'Madeira–Mamoré–Grande–Caine–Rocha','Purús','Yukon','São Francisco',
        'Syr Darya–Naryn','Salween (Nu Jiang)',
        'Saint Lawrence–Niagara–Detroit–Saint Clair–Saint \
        Marys–Saint Louis–North (Great Lakes)','Rio Grande','Lower Tunguska',
        f"Danube–Breg (Donau', Dunăre', Duna', Dunav', Dunaj)",
        f"Irrawaddy River–N'Mai River–Dulong River–Kelaoluo–Gada Qu",
        'Zambezi (Zambesi)','Vilyuy','Ganges–Hooghly–Padma (Ganga)',
        'Amu Darya–Panj','Japurá (Caquetá)','Nelson–Saskatchewan',
        'Paraguay (Rio Paraguay)','Kolyma','Pilcomayo','Upper Ob–Katun',
        'Ishim','Ural','Juruá','Arkansas','Colorado (western U.S.)',
        'Olenyok','Dnieper','Aldan','Ubangi–Uele']
}
df = pd.DataFrame(data)
df.to_csv(os.path.dirname(__file__) + '/river_systems.csv', encoding='utf-8', index=False)

#%% chart plot
poly = [(-2.75,-1.33),(0,3.33),(2.75,-1.33)]
poly = vf.rotate_polygon(poly,45)
o_pqt = pqt(df,'river','length_km', constraints=poly, collapse=True,
    rotate=45, buffer=.04, xc=-.18, yc=.18, size_by='width')
o_pqt.polyquadtile_plot(show_constraints=True)

#%% chart data
o_pqt.o_polyquadtile_chart.dataframe_rescale(-3,3,-2,4)
o_pqt.o_polyquadtile_chart.df = pd.merge(
    o_pqt.o_polyquadtile_chart.df, df, left_on='item', right_on='river')
o_pqt.o_polyquadtile_chart.df = o_pqt.o_polyquadtile_chart.df[
    ['river','side','x','y','path','length_km','length_m',
    'drainage_area_km2','average_discharge_m3_s','outflow','name']]
o_pqt.o_polyquadtile_chart.dataframe_to_csv('quadtile')

o_pqt.o_polysquares.dataframe_rescale(-3,3,-2,4)
o_pqt.o_polysquares.df = pd.merge(
    o_pqt.o_polysquares.df, df, left_on='id', right_on='river')
o_pqt.o_polysquares.df = o_pqt.o_polysquares.df[
    ['river','side','x','y','length_km','length_m',
    'drainage_area_km2','average_discharge_m3_s','outflow','name']]
o_pqt.o_polysquares.dataframe_to_csv('quadtile_centroids')

#%% triangle data
poly = o_pqt.constraints
rs_poly_yx = [(vf.rescale(y, -2, 4, -1, 1),vf.rescale(x, -3, 3, -1, 1)) for x,y in poly]
print(rs_poly_yx)

#%% legend plot
df_legend = df.groupby('outflow')['name'].count().reset_index()
o_pqt_legend = pqt(df_legend,'outflow','name', constraints=[(4,1)], collapse=True,
    rotate=45, buffer=.1, size_by='width', sides=['top','right'])
o_pqt_legend.polyquadtile_plot(show_constraints=True)

#%% legend data
o_pqt_legend.o_polyquadtile_chart.dataframe_rescale(-2,6,-4,4)
o_pqt_legend.o_polyquadtile_chart.df = pd.merge(o_pqt_legend.o_polyquadtile_chart.df, df_legend, left_on='item', right_on='outflow')
o_pqt_legend.o_polyquadtile_chart.df = o_pqt_legend.o_polyquadtile_chart.df[
    ['outflow','side','x','y','path','name']]
o_pqt_legend.o_polyquadtile_chart.dataframe_to_csv('quadtile_legend')