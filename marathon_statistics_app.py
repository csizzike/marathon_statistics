from numpy.core.numeric import Inf, NaN
from pandas._libs.tslibs import NaT
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

local_path = '/Users/csizi/Development/marathon_statistics/dataset/csv/bszm_2008_2020/'

bszm = pd.read_csv(local_path + 'bszm_cleaned.csv', encoding = "utf8", 
                        sep=';', header=0)

st.set_page_config(page_title="Running analysis", page_icon="./static/images/running.png", layout="wide", menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None})

event_list = list(reversed(range(2008,2021)))
event_list.append('ALL')

@st.cache
def load_data(year):
    if year == 'ALL': 
        return bszm
    return bszm[bszm['event_year'] == year]


selected = option_menu(None, ["Dashboard", "Statistics", "Models", "Prediction", "Upload", 'About'], 
    icons=['bi-speedometer', 'bar-chart', "cpu", "lightbulb", "upload", "info-circle"], default_index=0, orientation="horizontal")


if (selected == 'Dashboard'):
    selected_year = st.selectbox('Year', event_list)
    df = load_data(selected_year)
    with st.expander("Individual results dataset"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.dataframe(df.astype('object'))
     
     
    c1, c2, c3 =  st.columns(3)
    with c1:
        yearly = {
            'Attendants': [296, 310, 277, 260, 216, 209, 190, 169, 162, 148, 114, 101, 54],
            'Year': [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008],
        }
        data = pd.DataFrame(yearly)
        
        fig, ax = plt.subplots()
        ax.plot(yearly['Year'], yearly['Attendants'])
        st.pyplot(fig)
    with c2:
        yearly = {
            'Attendants': [296, 310, 277, 260, 216, 209, 190, 169, 162, 148, 114, 101, 54],
            'Year': [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008],
        }
        data = pd.DataFrame(yearly)
        
        fig, ax = plt.subplots()
        ax.plot(yearly['Year'], yearly['Attendants'])
        st.pyplot(fig)
    with c3:
        yearly = {
            'Attendants': [296, 310, 277, 260, 216, 209, 190, 169, 162, 148, 114, 101, 54],
            'Year': [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008],
        }
        data = pd.DataFrame(yearly)
        
        fig, ax = plt.subplots()
        ax.hist(yearly['Year'], yearly['Attendants'])
        st.pyplot(fig)
     
     
    col2, col3, col4 = st.columns(3)

    with col2:
        st.caption("Competitors sex")
        my_labels = 'Male', 'Female'
        fig1, ax1 = plt.subplots()
        ax1.pie(df['Gender'].value_counts(), labels=my_labels)
        st.pyplot(fig1)

    with col3:
        st.caption("Finished race")
        df['finished'].value_counts()
        my_labels = 'Finished', 'Failed'
        fig1, ax1 = plt.subplots()
        ax1.pie(df['finished'].value_counts(), labels=my_labels)
        st.pyplot(fig1)
    with col4:
        st.caption("Competitors age category")
        my_labels = 'Male 18-27', 'Male 28-39', 'Male 40-50', 'Male 51-59', 'Male 60+', 'Female 18-27', 'Female 28-39', 'Female 40-55', 'Female 55+'
        fig1, ax1 = plt.subplots()
        ax1.pie(df['Category'].value_counts(), labels=my_labels)
        st.pyplot(fig1)
        

if (selected == 'Statistics'):
    selected_year = st.selectbox('Year', event_list)
    df = load_data(selected_year)
    with st.expander("Individual results dataset"):
     st.write("""
         The chart above shows some numbers I picked for you.
         I rolled actual dice for these, so they're *guaranteed* to
         be random.
     """)
     st.dataframe(df.astype('object'))
     
     
    c1, c2, c3 =  st.columns(3)
    with c1:
        yearly = {
            'Attendants': [296, 310, 277, 260, 216, 209, 190, 169, 162, 148, 114, 101, 54],
            'Year': [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008],
        }
        data = pd.DataFrame(yearly)
        
        fig, ax = plt.subplots()
        ax.plot(yearly['Year'], yearly['Attendants'])
        st.pyplot(fig)
    with c2:
        yearly = {
            'Attendants': [296, 310, 277, 260, 216, 209, 190, 169, 162, 148, 114, 101, 54],
            'Year': [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008],
        }
        data = pd.DataFrame(yearly)
        
        fig, ax = plt.subplots()
        ax.plot(yearly['Year'], yearly['Attendants'])
        st.pyplot(fig)
    with c3:
        yearly = {
            'Attendants': [296, 310, 277, 260, 216, 209, 190, 169, 162, 148, 114, 101, 54],
            'Year': [2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008],
        }
        data = pd.DataFrame(yearly)
        
        fig, ax = plt.subplots()
        ax.plot(yearly['Year'], yearly['Attendants'])
        st.pyplot(fig)
     
     
    col2, col3, col4 = st.columns(3)

    with col2:
        st.caption("Competitors sex")
        my_labels = 'Male', 'Female'
        fig1, ax1 = plt.subplots()
        ax1.pie(df['Gender'].value_counts(), labels=my_labels)
        st.pyplot(fig1)

    with col3:
        st.caption("Finished race")
        df['finished'].value_counts()
        my_labels = 'Finished', 'Failed'
        fig1, ax1 = plt.subplots()
        ax1.pie(df['finished'].value_counts(), labels=my_labels)
        st.pyplot(fig1)
    with col4:
        st.caption("Competitors age category")
        my_labels = 'Male 18-27', 'Male 28-39', 'Male 40-50', 'Male 51-59', 'Male 60+', 'Female 18-27', 'Female 28-39', 'Female 40-55', 'Female 55+'
        fig1, ax1 = plt.subplots()
        ax1.pie(df['Category'].value_counts(), labels=my_labels)
        st.pyplot(fig1)
