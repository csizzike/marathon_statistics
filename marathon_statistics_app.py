from numpy.core.numeric import Inf, NaN
from pandas._libs.tslibs import NaT
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import flag
import pycountry

from time import gmtime
from time import strftime

def calculate_time_column_back(row):
    return strftime("%H:%M:%S", gmtime(row))

local_path = 'dataset/csv/bszm_2008_2020/'

bszm = pd.read_csv(local_path + 'bszm_cleaned.csv', encoding = "utf8", 
                        sep=';', header=0)

def get_difference(df, selected_year):
    return df.shape[0] - bszm[bszm['event_year'] == selected_year-1].shape[0]

def get_difference_gender(df, selected_year, gender):
    return df.shape[0] - bszm[(bszm['event_year'] == selected_year-1) & (bszm['Gender'] == gender)].shape[0]

def get_difference_finishers(df, selected_year):
    return df.shape[0] - bszm[(bszm['event_year'] == selected_year-1) & (bszm['finished'] == True)].shape[0]

def get_difference_countries(df, selected_year):
    return df['Country'].unique().size - bszm[bszm['event_year'] == selected_year-1]['Country'].unique().size

def get_difference_cities(df, selected_year):
    return df['City'].unique().size - bszm[bszm['event_year'] == selected_year-1]['City'].unique().size
    

st.set_page_config(page_title="Running analysis", page_icon="./static/images/running.png", layout="wide", menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None})

event_list = list(reversed(range(2008,2021)))
day_list = list(range(1,5))
event_list.append('ALL')

@st.cache
def load_data(year):
    if year == 'ALL': 
        return bszm
    return bszm[bszm['event_year'] == year]


selected = option_menu(None, ["Statistics", "Models", "Prediction", "Upload", 'About'], 
    icons=['bar-chart', "cpu", "lightbulb", "upload", "info-circle"], default_index=0, orientation="horizontal")


if (selected == 'Dashboard'):
    with st.container():
        st.image("https://c.tenor.com/d8Nj1CVSRbQAAAAM/monki-flips-dies.gif")
        

if (selected == 'Statistics'):
    selected_year = st.selectbox('Year', event_list)
    df = load_data(selected_year)
    
    stat1, empty, stat2, stat3 = st.columns([4, 0.5, 1, 1])
    
    with stat1:
        st.dataframe(df[['Placement', 'Name', 'Born', 'Category', 'Country', 'Team', 'City', 'Gender', 'Result_normal', 'finished']].astype('object'))
    with stat2:
        st.metric(label='Competitor', value=str(df.shape[0]) + ' 🏃🏻', delta = get_difference(df, selected_year) if selected_year != 'ALL' else None)
    with stat2:
        st.metric(label='Male', value=str(df[df['Gender'] == 'M'].shape[0]) + ' 🧔🏻‍♂️', delta= get_difference_gender(df[df['Gender'] == 'M'], selected_year, 'M') if selected_year != 'ALL' else None)
    with stat3:
        st.metric(label='Finisher', value=str(df[df['finished'] == True].shape[0]) + ' 🏅', delta = get_difference_finishers(df, selected_year) if selected_year != 'ALL' else None)
    with stat3:
        st.metric(label='Female', value=str(df[df['Gender'] == 'F'].shape[0]) + ' 👩🏻', delta = get_difference_gender(df[df['Gender'] == 'F'], selected_year, 'F') if selected_year != 'ALL' else None)
    with stat2:
        st.metric(label='Country', value=str(df['Country'].unique().size) + ' 🏳️', delta = get_difference_countries(df, selected_year) if selected_year != 'ALL' else None)
    with stat3:
        st.metric(label='City', value=str(df['City'].unique().size) + ' 🏘', delta = get_difference_cities(df, selected_year) if selected_year != 'ALL' else None)
        
    s1, s2, s3, s4, s5 = st.columns([1,1,1,2,2])
    topCLub = str(df[df['Team'] != '-'].value_counts().idxmax()[5])
    topClubCount = df[df['Team'] == topCLub].shape[0]
    maleCountry= pycountry.countries.get(alpha_3=str(df[(df['Gender'] == 'M') & df['Placement'] == 1].values[0][4]))
    femaleCountry= pycountry.countries.get(alpha_3=str(df[(df['Gender'] == 'F') & df['Placement'] == 1].values[0][4]))
    
    with s1:
      st.metric(label='Average tempo', value=str(df['average_tempo(minutes/km)'].mean().round(2)) + " m/km")  
    with s2:
        st.metric(label='Average result', value=str(calculate_time_column_back(df['Result'].mean())))  
    with s3:
        st.metric(label='Club Members', value=str(df[df['Team'] != '-'].shape[0]))
    with s4:
        st.metric(label='First Male', value=flag.flag(":" + maleCountry.alpha_2 + ":") + ' ' + str(df[(df['Gender'] == 'M') & df['Placement'] == 1].values[0][1]))
    with s5:
        st.metric(label='First Female', value=flag.flag(":" + femaleCountry.alpha_2 + ":") + ' ' + str(df[(df['Gender'] == 'F') & df['Placement'] == 1].values[0][1]))


    c1, c2 =  st.columns(2)
    with c1:
        fig = plt.figure(figsize=(10, 4))
        sns.distplot(df['average_tempo(minutes/km)'])
        st.pyplot(fig)
    with c1:
        fig = plt.figure(figsize=(10, 4))
        sns.distplot(df['Result'], label='Result in seconds')
        st.pyplot(fig)
    with c2:
        fig = plt.figure(figsize=(10, 4))
        sns.distplot(bszm['age'])
        st.pyplot(fig)
    with c2:
        topAgeCategory = bszm.groupby('Category').agg({
            'finished' : 'sum'
        }).sort_values('finished', ascending=False)[:10]
        fig = plt.figure(figsize=(10, 4))        
        sns.barplot(y='finished', x='Category', data=topAgeCategory.reset_index())
        st.pyplot(fig)


    selected_day = st.selectbox('Day', day_list)
    data = df[['Name', str(selected_day)+'.day/1.time_normal', str(selected_day)+'/1_tempo', str(selected_day)+'.day/2.time_normal', str(selected_day)+'/2_tempo', str(selected_day)+'.day/3.time_normal', str(selected_day)+'/3_tempo', str(selected_day)+'.day/sum_normal', str(selected_day)+'_tempo']]
    weather_data = df [[ str(selected_day)+'_weather_temp', str(selected_day)+'_weather_rain', str(selected_day)+'_weather_cloud',  str(selected_day)+'_weather_press',  str(selected_day)+'_weather_wind',  str(selected_day)+'_weather_gust']]

    
    daily1, daily2, daily3, daily4 = st.columns([4, 0.5, 1, 1])
    
    with daily1:
        st.dataframe(data.astype('object'))
    with daily2:
        st.empty()
    with daily3:
        st.metric(label='Temperature', value=str(weather_data.iloc[:1].values[0][0]) + ' °C ' + ('🥶' if weather_data.iloc[:1].values[0][0] < 8 else '😎' if weather_data.iloc[:1].values[0][0] < 20 else '🥵'))
    with daily4:
        st.metric(label='Rain', value=str(weather_data.iloc[:2].values[0][1]) + ' mm ' + '💧')
    with daily3:
        st.metric(label='Clouds', value=str(weather_data.iloc[:3].values[0][2]) + ' % ' + ('☀️' if weather_data.iloc[:3].values[0][2] < 1 else '🌤' if weather_data.iloc[:3].values[0][2] < 50 else  '⛅️' if weather_data.iloc[:3].values[0][2] < 80 else '☁️'       ))
    with daily4:
        st.metric(label='Pressure', value=str(weather_data.iloc[:3].values[0][3]) + ' atm ' + '')
    with daily3:
        st.metric(label='Wind', value=str(weather_data.iloc[:3].values[0][4]) + ' km/h')
    with daily4:
        st.metric(label='Gusts', value=str(weather_data.iloc[:3].values[0][5]) + ' km/h')
        
      
if (selected == 'Models'):
    modelc1, modelc2 = st.columns(2)
    
    st.header("Classification approaches")
    
    with modelc1:
        st.header("Decision tree")
        st.image('https://c.tenor.com/7kzP_bmlzccAAAAM/monkiflip-monki.gif')
    with modelc2:
        st.header("Support Vector Machine")
        st.image('https://c.tenor.com/7kzP_bmlzccAAAAM/monkiflip-monki.gif')
    with modelc1:
        st.header("Random Forest")
        st.image('https://c.tenor.com/7kzP_bmlzccAAAAM/monkiflip-monki.gif')
    with modelc2:
        st.header("Neural Network")
        st.image('https://c.tenor.com/7kzP_bmlzccAAAAM/monkiflip-monki.gif')

    
if (selected == 'Prediction'):
    st.title("Predict your future event outcome")
    st.write('Using the best performing machine learning model, we can give you a prediction on the outcome of your future performance')
    st.image('https://c.tenor.com/7kzP_bmlzccAAAAM/monkiflip-monki.gif')
    age = st.number_input(label='Age')
    club_member = st.radio('Are you a club member?', ('Yes', 'No'))
    st.button(label="Predict")
    
    st.balloons()
    
    
if (selected == "Upload"):
    st.header("Upload")
    st.write("You can upload fresh ultramarathon results from BSZM, and you can analyze it in the statistics tab.")
    st.write("Try it out")
    files = st.file_uploader(label="Upload new dataset", accept_multiple_files=True)
    st.button(label='Submit')
    
if (selected == "About"):
    st.image('https://c.tenor.com/7kzP_bmlzccAAAAM/monkiflip-monki.gif')
