import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import datetime
import re
import pydeck as pdk
import base64

st.set_page_config(layout="wide")

# Main page title
st.title("V-Sentinel - AI Feedback Engine")

# Create the main sidebar section, useful for the filters
st.sidebar.header("V-Sentinel - AI Feedback Engine")