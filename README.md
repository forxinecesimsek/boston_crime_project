# Boston Crime Analysis 

Exploratory Data Analysis and Prediction Models for Boston Crime Data Set using classification algorithms

# UPSchool

UP School is an ed-tech startup that boosts up women to become role models in technology. By helping women gain technical and collaborative success skills. This is a 4 months ed-tech program which provides you the best platform to improve soft skills and hard skills by involving students to variety projects . In this project term , I want to thank my mentors and Up School organization team for supporting me.

<img id="comp-k87qg1nu2imgimage" style="object-position:50% 50%;width:1200px;height:1200px;object-fit:contain" alt="Screen_Shot_2020-03-24_at_13-removebg-pr" data-type="image" itemprop="image" src="https://static.wixstatic.com/media/407b54_d4bd43ddf7e84c498d2d60eaba022f3f~mv2.png/v1/fill/w_158,h_100,al_c,q_85,usm_0.66_1.00_0.01/Screen_Shot_2020-03-24_at_13-removebg-pr.webp">


# Dataset

Crime incident reports are provided by Boston Police Department (BPD) to document the initial details surrounding an incident to which BPD officers respond. This is a dataset containing records from the new crime incident report system, which includes a reduced set of fields focused on capturing the type of incident as well as when and where it occurred. (Records begin in June 14, 2015 and continue to September 3, 2018.)

__BOSTON CRIME DATA__ includes 17 features that are:

__INCIDENT_NUMBER:__ It is a unique number given each case. (unique incident number is not equal total incident number because some cases include lots of crime type, some of them have been shown below) #data.INCIDENT_NUMBER.nunique() :282517 (As you can see above, just 88.5% is a unique number in this column.)

__OFFENSE_CODE:__ It shows type of crime, also we have another list explain of each of them. (Because of existing Offense Code Group, it will be not used in the analysis.)

__OFFENSE_CODE_GROUP:__ The general name of each crime type.

__OFFENSE_DESCRIPTION:__ Explanation of specific crime. (It can be useful for further investigation)

__DISTRICT:__ Code of zone that crime happened. (Because of code is meaningless, it will be changed with name of district)

__REPORTING_AREA:__ Area number that crime reported.

__SHOOTING:__ If the crime included shooting, it shows with 'Y'.

__OCCURRED_ON_DATE:__ It shows exact time of crime. (year, month, day and time)

__YEAR:__ 2015,2016,2017,2018

__MONTH:__ the month that crime happened.

__DAY_OF_WEEK:__ the week that crime happened.

__HOUR:__ the hour that crime happened.

__UCR_PART:__ Uniform Crime Reporting Offence types that is defined by The Federal Bureau of Investigation for reporting data on crimes.

__STREET:__ the street name that crime happened

__LAT:__ the location latitude that crime happened.

__LONG:__ the location longitude that crime happened.

__LOCATION:__ the location latitude and longitude together that crime happened.

# Prediction Models

I chose classification algorithms to predict whether a crime is a __important__ crime by providing location, month, day, time and district information. 

The important crimes (label) are listed below:

- Aggravated Assault 

- Harassment 

- Arson

- Homicide

- Criminal Harassment

- Biological Threat

- Manslaughter 

- Human Trafficking  

- Auto Theft 

- Larceny 

- Robbery

- Residential Burglary 

- Larceny From Motor Vehicle

- Other Burglary Commercial Burglary

# ML Algorithms Used

- __XGBoost__
- __LightGBM__
- Gradient Boosting
- ExtraTreeClassifier
- Random Forest
- GaussianNB
- AdaBoost

# Results (LGBM)


![Alt Text](https://github.com/forxinecesimsek/boston_crime_project/blob/master/AccuracyScore_LGBM.PNG)


# Streamlit Demo

![Alt Text](https://github.com/forxinecesimsek/boston_crime_project/blob/master/streamlit_demo/Ece-Simsek-streamlit-demovideo.gif)


[For More Detail, Please Go My Capstone Project Presentation](https://docs.google.com/presentation/d/1eubSge6yBwh2CxtIA_QKyClYNQGmiijrfpHY-nl8L2o/edit#slide=id.g9a79991ba5_0_92)
