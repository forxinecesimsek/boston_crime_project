import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px
import plotly
import altair as alt
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static




def get_data() :
    df = pd.read_csv('crime.csv', encoding = "ISO-8859-1")
    return df

    '# World GDP'




def content():
    st.title('Exploratory Data Analysis 🤔')

    df = get_data()
    if st.checkbox("Show first rows  & shape of the data"):
        st.write(df.head())
        st.write(df.shape)
    years = df['YEAR'].sort_values(ascending=True).unique()
    months = df['MONTH'].sort_values(ascending=True).unique()
    days = df['DAY_OF_WEEK'].sort_values(ascending=True).unique()
    hours = df['HOUR'].sort_values(ascending=True).unique()

    if st.button('Click Here to See Chart '):

        plt.figure(figsize=(10, 6))
        st.subheader("How has crime changed over the years?")
        sns.countplot(data=df, x='YEAR', palette="coolwarm")
        st.pyplot()

    st.markdown('As you can see at the chart above, although the highest crime rates seem to be in 2016 and in 2017, the fact that the data set is from the 6th month of 2015 and till 10th of 2018 does not make such an inference possible. (See: Number of Crimes by Month, Day and Hour for Each Years) In this context, considering that the dataset contains only 6 months of 2015 and only 9 months of 2018, we can conclude that the number of crimes has not changed significantly according to years.')

    st.subheader("Total Number of Crimes by Month, Day and Hour")
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 12))

    month_year = sns.countplot(x='MONTH',
                          data=df,
                          color="firebrick",
                          order=None,
                          ax=axes[0])

    day_year = sns.countplot(x='DAY_OF_WEEK',
                        data=df,
                        color="steelblue",
                        order=None,
                        ax=axes[1])

    hours_year = sns.countplot(x='HOUR',
                          data=df,
                          color="mediumseagreen",
                          order=None,
                          ax=axes[2])
    st.pyplot()
    st.markdown('When we look at the general picture for all years, we can conclude that crimes are mostly committed in summer. Although the crime density on the days of the week seem almost equal, we can say that they are committed at a higher level on Fridays. On the other hand, contrary to the perception that crimes are usually committed at night, when we examine the above chart, we can say that it is surprisingly more intense between 5 and 7 o clock in the evening.Considering that the most common crime type is a motor vehicle accident response, I think that the high traffic and motor vehicle density at the specified time intervals may explain the reason for the high crime rate in this hour interval.')

    st.subheader("Number of Crimes by Month, Day and Hour (Year by Year)")

    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(7, 12))

    year_selecting = st.selectbox('YEAR', years)
    # month_selecting = st.selectbox('MONTH', months)
    # day_selecting = st.selectbox('DAY', days)
    # hour_selecting = st.selectbox('HOUR', hours)


    month = sns.countplot(x='MONTH',
                          data=df[df['YEAR']==year_selecting],
                          color="firebrick",
                          order=None,
                          ax=axes[0])

    day = sns.countplot(x='DAY_OF_WEEK',
                        data=df[df['YEAR']==year_selecting],
                        color="steelblue",
                        order=None,
                        ax=axes[1])

    hours = sns.countplot(x='HOUR',
                          data=df[df['YEAR']==year_selecting],
                          color="mediumseagreen",
                          order=None,
                          ax=axes[2])
    st.pyplot()


    st.subheader("What can we say about the distribution of different offenses over the city?")

    nr_crimes = df['OFFENSE_CODE_GROUP'].value_counts()
    counts = nr_crimes.values
    categories = pd.DataFrame(data=nr_crimes.index, columns=["OFFENSE_CODE_GROUP"])
    categories['counts'] = counts

    fig = px.treemap(categories, path=['OFFENSE_CODE_GROUP'], values=counts, height= 800, width=1000,
                     title='Top Crimes in Boston', color_discrete_sequence=px.colors.sequential.Brwnyl)
    fig.data[0].textinfo = 'label+value'
    st.plotly_chart(fig)

    st.subheader("Heatmaps")

    offensecodegroups = df.OFFENSE_CODE_GROUP.sort_values(ascending=True).unique()
    OCG_selecting = st.selectbox('OFFENSE GROUPS', offensecodegroups)


    df_drop = df.dropna(subset=['Lat', 'Long', 'DISTRICT'])

    df_heatmap_mvar = df_drop[df_drop["OFFENSE_CODE_GROUP"] == OCG_selecting]

    map_mvar = folium.Map(location=[42.361145, -71.057083], tiles='cartodbpositron', zoom_start=12)

    # Add a heatmap to the base map
    heatmap= HeatMap(data=df_heatmap_mvar[['Lat', 'Long']], radius=10).add_to(map_mvar)

    folium_static(map_mvar)


if __name__ == '__main__':
    content()