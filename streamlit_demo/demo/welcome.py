import streamlit as st

def content():
    st.title('Crime Analysis of Boston City  👮🏻')

    st.markdown("In recent days, data science and machine learning plays a key role for detection, analysis and forecasting of crimes.The goal of this work is to propose methods for predicting crimes classified into different categories of severity. We implemented visualization and analysis of crime data statistics in recent years in the city of Boston. "
                "\n\n\n We then carried out a comparative study between seven supervised learning algorithms, which are xgboost,  lightGBM, adaboost, gradientboosting, extratreeclassifier, random forest and GaussianNB based on the accuracy and processing time of the models to make predictions using geographical information provided by splitting the data into training and test sets. The result shows that XGBoost, LightGBM and adaboost as expected gives a better result with more accuracy in comparison to others. "
                "\n\n\n However, in this web application some important data visualisations and clustering map for best locations to determine the police stations."
                )

    st.markdown("![Alt Text](https://media1.tenor.com/images/11f9cf6582175ebe1fa8cc00c71431fa/tenor.gif?itemid=16367094)")
    st.title("Content of Web App")
    st.markdown('* Welcoming')
    st.markdown('* Exploratory Data Analysis')
    st.markdown('* Clustering for Police Stations')




if __name__ == '__main__':
    content()