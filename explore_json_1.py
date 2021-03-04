import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)
    #the json.load() function converts the data into a
    # format python can work with: in this case, a giant dictionary

json.dump(eq_data,outfile,indent=4)
    #the json.dump() function takes a JSON data objectr and a file object,
    # file. the indent=4 argument tells dump() to format the data using indent
    #the data's structure

list_of_eqs = eq_data['features']

mags,lons,lats = [],[],[]

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lon = eq['geometry']['coordinates'][0]
    lat = eq['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags[:10])
print(lons[:10])
print(lats[:10])
    #the :10 means show everything from 0 to 10 (list splicing)
        #1:10 would show 1-10 and etc.

#print(eq_data['features'][0]['properties']['mag'])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline
    #the offline module helps us render the map in real-time on our computer so we can visualize it,
    # but we do need to make a data object that will allow us to combine the latitudes and longitudes together

data = [Scattergeo(lon = lons, lat = lats)]

my_layout = Layout(title = "Global Earthquakes")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename = 'global_earthquakes.html')

