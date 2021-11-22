from numpy.core.numeric import Inf, NaN
import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import timedelta

static_path = './dataset/csv/'


summary_md = str(open("README.md").read())


st.title('Marathon analysis')

st.markdown(summary_md)

st.sidebar.header('Select year')
selected_year = st.sidebar.selectbox('Év', list(reversed(range(2015,2021))))

@st.cache
def load_data(year):
    bszm = pd.read_csv(static_path + 'BSZM_' + str(year) + '.csv', encoding = "ISO-8859-1", 
                    sep=';', header=0)
    bszm['Hely.'] = bszm['Hely.'].replace(NaN, 9999)
    bszm['Hely.'] = bszm['Hely.'].astype(int)
    #bszm.drop(['Név/Csapatnév', 'Ország', 'Csapat', 'Város', 'rajtszám', 'Hely.', 'kat.h.'], axis = 1, inplace=True)
    #bszm.drop(['1.nap/1.idõ', '1.nap/2.idõ', '1.nap/3.idõ', '2.nap/1.idõ', '2.nap/2.idõ', '2.nap/3.idõ', '3.nap /1.idõ', '3.nap/2.idõ', '3.nap/3.idõ', '4.nap/1.idõ', '4.nap/2.idõ', '4.nap/3.idõ'], axis = 1, inplace=True)
    bszm["befejezte"] = np.where(bszm['Megtett táv (km)'] < 196, False, True)
    #bszm = bszm.replace('99:59:59', np.nan)
    #bszm['eredmény'] = pd.to_timedelta(bszm['eredmény'])
    #bszm['1.nap összidõ'] = pd.to_timedelta(bszm['1.nap összidõ'])
    #bszm['2.nap összidõ'] = pd.to_timedelta(bszm['2.nap összidõ'])
    #bszm['3.nap összidõ'] = pd.to_timedelta(bszm['3.nap összidõ'])
    #bszm['4.nap összidõ'] = pd.to_timedelta(bszm['4.nap összidõ'])
    #eredmény = ['1.nap összidõ', '2.nap összidõ', '3.nap összidõ', '4.nap összidõ']
    #bszm['eredmény'] = bszm[eredmény].sum(axis=1, skipna=True)
    #bszm['eredmény'] = bszm['eredmény'] - pd.to_timedelta(bszm['eredmény'].dt.days, unit='h')
    #bszm["eredmény(perc)"] = bszm['eredmény'].astype('timedelta64[m]')
    #bszm["átlagos tempó (perc/km)"] = bszm['eredmény'].astype('timedelta64[m]')/bszm['Megtett táv (km)']
    #bszm['sebesség kategória'] = pd.qcut(bszm['átlagos tempó (perc/km)'], 5, labels=['gyors', 'közepesen gyors', 'közepes', 'közepesen lassú', 'lassú'])
    bszm.drop_duplicates(inplace=True)
    #bszm.loc[bszm['eredmény(perc)'] == 0.0] = np.nan
    bszm.dropna(axis=0, how='all', inplace=True)
    return bszm

df = load_data(selected_year)

st.header('Résztvevők eredményei')
st.write('Dimenziók: ' + str(df.shape[0]) + ' sor és ' + str(df.shape[1]) + ' oszlop')
st.dataframe(df)
    