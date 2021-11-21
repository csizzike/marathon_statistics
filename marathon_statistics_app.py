import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


summary_md = str(open("README.md").read())

st.title('BSZM egyéni eredmény kiértékelés')

st.markdown(summary_md)

st.sidebar.header('Év kiválasztása')
selected_year = st.sidebar.selectbox('Év', list(reversed(range(2015,2020))))