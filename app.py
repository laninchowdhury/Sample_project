import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import os
import matplotlib.pyplot as plt



df =pd.read_csv("C:\\Users\\nsuka\\Downloads\\vehicles_us.csv")

df.head()



df.head(10)
# Add a header
st.header("Car Listings Analysis")

# create a plotly express histogram
fig_hist = px.histogram(df, x='price', title='Price Distribution')
st.plotly_chart(fig_hist)

# st.write(fig_hist)

show_only_4wd = st.checkbox("Show only 4WD vehicles")

if show_only_4wd:
    df = df[df['is_4wd'] == 1.0]


fig_hist = px.scatter(df, x='odometer', y='price', color='condition', title='Price vs. Odometer by Condition')
st.write(fig_hist)

df.head(5)