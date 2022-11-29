
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.write("""
# Social media usage

""")
st.sidebar.header("What would you like to display")
st.sidebar.selectbox(
    ' Choose ',
    ('Mobile', 'Web-Based', 'Male', 'Female')
)
data=pd.read_csv(r'C:\Users\sote\Downloads\WhatsgoodlyData-10.csv')


chart_female = data.loc[(data["Segment Type"]=="Gender") & (data["Segment Description"]=="Female respondents")].groupby("Answer")["Count"].sum()
#labels = chart_female.index
#sizes = chart_female.values
#explode = (0, 0.1, 0, 0)

#fig1, ax1 = plt.subplots()
#ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
 #       shadow=True, startangle=90)
#ax1.axis('equal')
#st.pyplot(fig1)*/