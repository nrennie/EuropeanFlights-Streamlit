"""
European Flights Streamlit app
"""
# Imports
import streamlit as st
import pandas as pd
import plotnine as gg
from mizani.breaks import date_breaks
from mizani.formatters import date_format

# Read in data
flights = pd.read_csv('https://raw.githubusercontent.com/nrennie/EuropeanFlights-Streamlit/main/flights_data.csv')

# Function to make the plot
def create_plot(data):
  plot = (
    gg.ggplot(data = data, mapping = gg.aes(x = 'Date', y='Total', fill='Country')) +
      gg.geom_col() +
      gg.theme_minimal() +
      gg.labs(x = "", y = "Total number of flights per week", title="Total number of flights per week") +
      gg.scale_x_datetime(breaks=date_breaks('1 years'), labels=date_format('%Y')) +
      gg.scale_fill_manual(values = {'Belgium':'#F2C57C', 'France':'#DDAE7E', 'Ireland':'#7FB685', 'Luxembourg':'#426A5A', 'Netherlands':'#EF6F6C', 'United Kingdom':'#AC9FBB'}) +
      gg.theme(panel_grid_major_x = gg.element_blank(),
               panel_grid_minor_x = gg.element_blank())
  )
  return plot.draw()

# Write app code

st.title('European Flights')
st.markdown('The number of flights arriving or leaving from European airports saw a dramatic decrease with the onset of the Covid-19 pandemic in March 2020. Amsterdam - Schipol remains the busiest airport, averaging 1,150 flights per day since January 2016.')
st.markdown('Data: [Eurocontrol](https://ansperformance.eu/data/).')

st.header('Controls')
option = st.multiselect(' Use the selectors below to choose a set of countries to explore.',
["Belgium", "France", "Ireland", "Luxembourg", "Netherlands", "United Kingdom"],
default=["Belgium", "France", "Ireland", "Luxembourg", "Netherlands", "United Kingdom"])  

country = list(option)
new_data = flights[flights['Country'].isin(country)]
p = create_plot(new_data)

st.pyplot(gg.ggplot.draw(p))

