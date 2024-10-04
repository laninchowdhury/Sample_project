




import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
import os

print(os.getcwd())  # Prints the current working directory
print(os.path.exists(r"c:\users\nsuka\desktop\sample_project\vehicles_us.csv"))

# Read the dataset's csv file 
df = pd.read_csv(r"c:\users\nsuka\desktop\sample_project\vehicles_us.csv")
# Add a header
st.header("Car Analysis Dashboard")

# create a plotly express histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# st.write(fig_hist)

# Add a checkbox to filter data


fig_hist = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.write(fig_hist)

