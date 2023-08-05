import pandas as pd
import streamlit as sr
new_weather=pd.read_csv('目前天氣.csv')
sr.write('目前台灣天氣')
sr.write(new_weather)