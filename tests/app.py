import streamlit as st
import requests
import pandas as pd
from streamlit_lottie import st_lottie
from streamlit_tags import st_tags
from utils import merge_data, clean_data
import joblib

model= joblib.load('model.joblib')

st.set_page_config(page_title="My Webpage",page_icon=":bar_chart:", layout="wide")
