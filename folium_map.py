import folium 
import pandas as pd
import numpy as np
from IPython.display import display
import random

def all_launchSite(data):
    launchSites_feat = folium.map.FeatureGroup()

    for lat, lng in zip(data['Latitude'], data['Longitude']):
      launchSites_feat.add_child(
        folium.vector_layers.CircleMarker(
            [lat, lng],
            radius=5, # marker size
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
      )
    return launchSites_feat
      
def color_outcome(data):

    launchSites_feat = folium.map.FeatureGroup()
    label_color = ''
    for index, (lat, lng, outocme) in enumerate(zip(data['Latitude'], data['Longitude'], data['Outcome'])):
      # Color label
      if outocme == 'False ASDS': label_color = 'red'
      elif outocme == 'True Ocean': label_color = 'green'
      elif outocme == 'True ASDS': label_color = 'yellow'
      else: label_color = 'blue'
      #
      if index < 10 : add_rdm = 0.0001 + (0.0009 + 0.0001) * random.random()
      elif index > 10 : add_rdm = 0.0001 - (0.0009 - 0.0001) * random.random()
      lat = lat + add_rdm
      lng = lng + add_rdm

      launchSites_feat.add_child(
        folium.vector_layers.CircleMarker(
            [lat, lng],
            radius=10, # marker size
            color= label_color,
            fill=True,
            fill_color= label_color,
            fill_opacity=0.6
        )
      )
    return launchSites_feat

def main():
    # Read Data 
    data = pd.read_csv("dataset_collected.csv")
    df = pd.DataFrame(data)

    # Render initial MAP
    init_lat = 45.130
    init_long = -35.35
    show_map = folium.Map(location=[init_lat, init_long], zoom_start=2 )

    # Explore all launchSite
    #launchSite_feature = all_launchSite(df)
    
    # Color label depend value of outcome
    outcome_color_feature = color_outcome(df)

    show_map.add_child(outcome_color_feature)
    show_map.save("map.html")  # save HTML file to show the map 

if __name__ == '__main__':
  main()