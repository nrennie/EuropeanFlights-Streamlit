"""
European Flights Streamlit app
"""
# Imports
import streamlit as st
import pandas as pd
import plotly.express as px

# Read in data
flights = pd.read_csv('https://raw.githubusercontent.com/nrennie/EuropeanFlights-Streamlit/main/flights_data.csv')

# use full page
st.set_page_config(layout="wide")

# App description
st.title('European Flights')
st.markdown('The number of flights arriving or leaving from European airports saw a dramatic decrease with the onset of the Covid-19 pandemic in March 2020. Amsterdam - Schipol remains the busiest airport, averaging 1,150 flights per day since January 2016.')
st.markdown('Data: [Eurocontrol](https://ansperformance.eu/data/).')

col1, col2 = st.columns([1, 2])

with col1:
  st.header('Controls')
  st.markdown('Use the selectors below to choose a set of countries to explore.')
  Belgium = st.checkbox("Belgium", value=True)
  France = st.checkbox("France", value=True)
  Ireland = st.checkbox("Ireland", value=True)
  Luxembourg = st.checkbox("Luxembourg", value=True)
  Netherlands = st.checkbox("Netherlands", value=True)
  UnitedKingdom = st.checkbox("United Kingdom", value=True)

d = {'country': ["Belgium", "France", "Ireland", "Luxembourg", "Netherlands", "United Kingdom"], 
'bools': [Belgium, France, Ireland, Luxembourg, Netherlands, UnitedKingdom]}
df = pd.DataFrame(data=d)
chosen = df[df['bools']]
country = list(chosen['country'])
country.reverse()
new_data = flights[flights['Country'].isin(country)]

fig = px.bar(new_data,
  x="Date",
  y="Total",
  color="Country",
  title="Total number of flights per week",
  color_discrete_map={
    'Belgium':'#F2C57C',
    'France':'#DDAE7E',
    'Ireland':'#7FB685',
    'Luxembourg':'#426A5A',
    'Netherlands':'#EF6F6C',
    'United Kingdom':'#AC9FBB'
    })
fig.update_layout(xaxis_title='', yaxis_title='Total number of flights per week')

with col2:
  st.plotly_chart(fig, use_container_width=True)
