import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np

# Read the dataset's csv file 
df = pd.read_csv("C:\\Users\\nsuka\\Desktop\\sample_project\\vehicles_us.csv")

# Add a header
st.header("Car Analysis Dashboard")

# create a plotly express histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# st.write(fig_hist)

# Add a checkbox to filter data


fig_hist = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.write(fig_hist)

if st.checkbox('Show Histogram'):
    st.plotly_chart(fig)
else:
    st.write("Histogram is hidden")