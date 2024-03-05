import streamlit as st
import plotly.express as px
import pandas as pd


df = pd.read_csv('/Users/limoges/Documents/Datascience/Bank_project/german_credit_data.csv')

unique_savings = df['Saving accounts'].unique()

# Create a color map from the 'rocket' color scale
rocket_cmap = px.colors.qualitative.rocket
color_discrete_map = {k: rocket_cmap[i % len(rocket_cmap)] for i, k in enumerate(unique_savings)}

# Create a simple bar chart using Plotly
fig = px.bar(df, x='Sex', y='Age', color='Saving accounts', color_discrete_map=color_discrete_map)

# Customize the Plotly theme to match the image
fig.update_layout(
    template='plotly_dark',
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font_color='blue'
)

# Display the chart in Streamlit
st.plotly_chart(fig)
