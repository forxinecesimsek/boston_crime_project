import streamlit as st
import datetime

from demo import *




titles = ("Welcome",
          "Exploratory Data Analysis",
          "Clustering for Police Stations"
          )


callable_dict = {'Welcome': welcome,
                 'Exploratory Data Analysis': eda,
                 'Clustering for Police Stations':cluster}

st.sidebar.title("Content")

st.sidebar.subheader("Today's Agenda")

part = st.sidebar.radio("", titles)

callable_dict.get(part, lambda: None)()