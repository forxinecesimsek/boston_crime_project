import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist
import pandas as pd
import numpy as np
import folium
from folium.features import DivIcon
from streamlit_folium import folium_static


def get_data() :
    df = pd.read_csv('crime.csv', encoding="ISO-8859-1")
    return df

def doKmeans(X, nclust) :
    model = KMeans(nclust)
    model.fit(X)
    clust_labels = model.predict(X)
    cent = model.cluster_centers_
    return (clust_labels, cent)





def content():

    st.title('What are the best locations for police stations? 👮🏻‍♂️')


    st.header('Clustering Analysis')

    df = get_data()
    df = df.dropna(subset=['Lat', 'Long'])
    df = df[df['Lat'] > 0]
    df_cluster = df.dropna()[['Lat', 'Long']]

    clust_labels, cent = doKmeans(df_cluster, 100)
    kmeans = pd.DataFrame(clust_labels)
    df_cluster.insert((df_cluster.shape[1]), 'kmeans', kmeans)
    arr = pd.DataFrame(data=cent, columns=['latitude', 'longitude'])



    # create a map
    this_map = folium.Map(width=1500,height=500, location=[42.361145,-71.057083])

    def plotDot(point) :
        '''input: series that contains a numeric named latitude and a numeric named longitude
        this function creates a CircleMarker and adds it to your this_map'''
        folium.Marker(location=[point.latitude, point.longitude],
                      radius=2,
                      weight=5, icon=DivIcon(
                html='<img alt="Police Icon of Colored Outline style - Available in SVG, PNG, EPS, AI &amp; Icon  fonts" class="n3VNCb" src="https://cdn.iconscout.com/icon/premium/png-256-thumb/police-1623568-1375513.png" data-noaft="1" jsname="HiaYvf" jsaction="load:XAeZkd;" style="width: 35px; height: 35px; margin: 0px;">',
                icon_size=(1, 1), icon_anchor=(0, 0), )).add_to(this_map)

    # use df.apply(,axis=1) to "iterate" through every row in your dataframe
    arr.apply(plotDot, axis=1)

    # Set the zoom to the maximum possible
    this_map.fit_bounds(this_map.get_bounds())

    # Save the map to an HTML file
    folium_static(this_map)


    st.markdown('On this map, latitude and longitude points\'re clustered into 100 points, then visualized the center points of these clusters to see best locations for police stations. '
                '\n\n\n Please note that the number of cluster depends on police force of Boston Police Department. It can be increase or decrease according to it.')



if __name__ == '__main__':
    content()