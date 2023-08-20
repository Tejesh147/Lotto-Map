import pandas as pd
import folium
from folium.plugins import MiniMap
from folium.plugins import HeatMap
import branca.colormap as cm
import streamlit as st

@st.cache_data()
def create_map():
    df = pd.read_csv('lotto_data.csv')

    ontario_coords = [46.493919, -80.995415]
    map = folium.Map(location=ontario_coords, world_copy_jump=True, zoom_start=6, tiles=None)
    folium.TileLayer('openstreetmap', name='Lotto Map').add_to(map)

    style = {'fillColor': 'None', 'color': 'green', 'fillOpacity': '0.2'}

    ontario_boundary = 'ontario_boundary.geojson'
    ontario_geojson = folium.GeoJson(data=ontario_boundary, name='Ontario Boundary', style_function=lambda x: style)
    map.add_child(ontario_geojson)

    minimap = MiniMap()
    map.add_child(minimap)
    
    location_info = {}

    min_amount = 10000
    max_amount = 1000000
    colors = ['#3186CC', '#FFCC00', '#FF0000']
    color_scale = cm.LinearColormap(colors=colors, vmin=min_amount, vmax=max_amount)

    marker_group = folium.FeatureGroup(name='Winning Tickets', show=True)

    for index, row in df.iterrows():
        name, address, product, date, amount, lat, long = row.Name, row.Address, row.Product, row.Draw, row.Value, row.Latitude, row.Longitude
        
        
        if address in location_info:
            count, prev_product, prev_amount = location_info[address]
            prev_product.append(product)
            prev_amount.append(amount)
            location_info[address] = (count + 1, prev_product, prev_amount)
        else:
            location_info[address] = (1, [product], [amount])
        
        popup_msg = f"Store: {name}<br>" \
                    f"Address: {address}<br>" \
                    f"Product: {product}<br>" \
                    f"Date Sold: {date}<br>" \
                    f"Prize Amount: ${amount}"
                    
        popup_msg_multiple = f"Store: {name}<br>" \
                    f"Address: {address}<br>" \
                    f"Winning Tickets Sold: {location_info[address][0]}<br>" \
                    f"Products: {location_info[address][1]}<br>" \
                    f"Prize Amounts: {location_info[address][2]}<br>" \
                            
        
        marker = folium.CircleMarker(
            location = [lat, long],
            radius = 7 if amount < 1000000 else 8 + amount / 1000000,
            popup = folium.Popup(popup_msg, max_width=300) if location_info[address][0] == 1 else folium.Popup(popup_msg_multiple, max_width=400),
            color = '#FFD700',
            fill = True,
            fill_color = color_scale(amount),
            fill_opacity = 0.7
        )

        marker_group.add_child(marker)

    map.add_child(marker_group)

    heatmap = folium.FeatureGroup(name='Heat Map', show=False)
    locations = list(zip(df.Latitude, df.Longitude))
    heatmap.add_child(HeatMap(locations)) 
    map.add_child(heatmap)

    folium.LayerControl().add_to(map)
    
    map_html = map.get_root().render()

    return map_html


def main():
    
    st.set_page_config(
        page_title='Lotto Map - Where Winning Tickets Are Sold!', 
        page_icon=':world_map:', 
        layout='wide'
        )
    
    lotto_map_html = create_map()
    
    st.image('app_images/olg_banner.png', width=400)
    st.title(':world_map: :blue[Lotto Map] - Where :red[Winning] Tickets Are Sold!')
    st.write("---")
    
    st.write('_Source: Ontario Lottery and Gaming Corporation_')
    st.components.v1.html(lotto_map_html, width=1300, height=700)
    st.write("##")
    
    st.header("❓ What does this map show?")
    st.subheader(
        """
        Lotto Map shows information such as...
        - Store names and locations of where winning OLG tickets were sold
        - Precise number of tickets sold and prize amount
        - Scaling bubble size and colour depending on winning prize amount 
        - Heatmap of locations around Ontario where tickets were purchased

        Enjoy the visualization :)
        """
    )
    


if __name__ == '__main__':
    main()