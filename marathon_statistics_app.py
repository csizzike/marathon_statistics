from numpy.core.numeric import Inf, NaN
from pandas._libs.tslibs import NaT
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import timedelta
from datetime import date

static_path = './dataset/csv/'
st.set_page_config(page_title="Running analysis", page_icon="./static/images/running.png", menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None}    )

summary_md = str(open("README.md").read())


st.title('Running analysis')

st.markdown(summary_md)

#Év kiválasztása
st.sidebar.header('Select year')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(2015,2021))))


@st.cache
def load_data(year):
    bszm = pd.read_csv(static_path + 'BSZM_' + str(year) + '.csv', encoding = "ISO-8859-1", 
                    sep=';', header=0)
    bszm['Hely.'] = bszm['Hely.'].replace(NaN, 9999)
    bszm['Hely.'] = bszm['Hely.'].astype(int)
    bszm['sz.év.'] = bszm['sz.év.'].replace(NaN, 9999)
    bszm['sz.év.'] = bszm['sz.év.'].astype(int)
    bszm['curryear'] = date.today().year
    bszm['kor'] = bszm['curryear'] - bszm['sz.év.']
    bszm.drop(['rajtszám', 'kat.h.'], axis = 1, inplace=True)    
    bszm.drop(['1.nap/1.idõ', '1.nap/2.idõ', '1.nap/3.idõ', '2.nap/1.idõ', '2.nap/2.idõ', '2.nap/3.idõ', '3.nap /1.idõ', '3.nap/2.idõ', '3.nap/3.idõ', '4.nap/1.idõ', '4.nap/2.idõ', '4.nap/3.idõ'], axis = 1, inplace=True)
    bszm["befejezte"] = np.where(bszm['Megtett táv (km)'] < bszm['Megtett táv (km)'].max(), False, True)
    bszm = bszm.replace('99:59:59', np.nan)
    bszm['eredmény'] = pd.to_timedelta(bszm['eredmény'])
    bszm['1.nap összidõ'] = pd.to_timedelta(bszm['1.nap összidõ'])
    bszm['2.nap összidõ'] = pd.to_timedelta(bszm['2.nap összidõ'])
    bszm['3.nap összidõ'] = pd.to_timedelta(bszm['3.nap összidõ'])
    bszm['4.nap összidõ'] = pd.to_timedelta(bszm['4.nap összidõ'])
    eredmény = ['1.nap összidõ', '2.nap összidõ', '3.nap összidõ', '4.nap összidõ']
    bszm['eredmény'] = bszm[eredmény].sum(axis=1, skipna=True)
    bszm['eredmény'] = bszm['eredmény'] - pd.to_timedelta(bszm['eredmény'].dt.days, unit='h')
    bszm["eredmény(perc)"] = bszm['eredmény'].astype('timedelta64[m]')
    bszm["átlagos tempó (perc/km)"] = bszm['eredmény'].astype('timedelta64[m]')/bszm['Megtett táv (km)']
    bszm['sebesség kategória'] = pd.qcut(bszm['átlagos tempó (perc/km)'], 5, labels=['gyors', 'közepesen gyors', 'közepes', 'közepesen lassú', 'lassú'])
    bszm.loc[bszm['eredmény(perc)'] == 0.0] = np.nan
    bszm.drop_duplicates(inplace=True)
    bszm.loc[bszm['átlagos tempó (perc/km)'] < 3] = np.nan
    bszm.loc[bszm['átlagos tempó (perc/km)'] == np.inf] = np.nan
    bszm.dropna(axis=0, how='all', inplace=True)
    return bszm

df = load_data(selected_year)

st.header('Résztvevők eredményei')
st.write('Dimenziók: ' + str(df.shape[0]) + ' sor és ' + str(df.shape[1]) + ' oszlop')
st.dataframe(df.astype('object'))

