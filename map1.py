import folium
import pandas as pd

data = pd.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
vol_name = list(data["NAME"])
elev = list(data["ELEV"])

def color_elevation(elev):
    if elev < 1000:
        return "green"
    elif 1000 <= elev < 3000:
        return "orange"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Cartodb Positron")

fgv = folium.FeatureGroup(name="Volcanes")

for lt, ln, name, elev in zip(lat, lon, vol_name, elev):
    iframe = folium.IFrame(html=f"Name:{name} Elevation:{int(elev)} mts", width=200, height=60)
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                     popup=folium.Popup(iframe),
                                     fill_color=color_elevation(elev),
                                     fill_opacity=0.6,
                                     stroke=False,
                                     radius=10,
                                     ))

fgp = folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(),
                     name="Population",
                     style_function=lambda x: {"fillColor": 'green' if x['properties']['POP2005'] < 1000000
                     else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                     else 'red'})

controllLayer = folium.LayerControl()

map.add_child(fgv)
map.add_child(fgp)
map.add_child(controllLayer)

map.save("Map1.html")