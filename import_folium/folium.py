import folium

map = folium.Map(location=[55.599896, 38.122336], zoom_start= 14, tiles='openStreetmap')
#folium.Marker(location=[55.584393, 38.117546], popup="Лес", icon=folium.Icon(color = 'green')).add_to(map)

lst_markers = [[55.584393, 38.117546], [55.588453, 38.158481]]
for coordinate in lst_markers:
    folium.Marker(location=coordinate, icon=folium.Icon(color='green')).add_to(map)

map.save("map1.html")
