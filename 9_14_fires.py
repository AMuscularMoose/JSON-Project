import json

infile = open('US_fires_9_14.json', 'r')

eq_data = json.load(infile)

lats,lons,brites = [],[],[]

for eq in eq_data:
    lat = eq['latitude']
    lon = eq['longitude']
    brt = eq['brightness']

    lats.append(lat)
    lons.append(lon)
    brites.append(brt)

print(lats[:10])
print(lons[:10])
print(brites[:10])

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        'type': 'scattergeo',
        'lon': lons,
        'lat': lats,
        'marker': {
            'size':[5*brt for brt in brites],
            'color':brites,
            'colorscale': 'Viridis',
            'reversescale': True,
            'colorbar':{'title':'Magnitude'},
        },
    }
]

my_layout = Layout(title = "US Fires - 9/14/2020 through 9/20/2020")

fig = {'data':data, 'layout':my_layout}

offline.plot(fig,filename = 'US_fires_9_14.html')