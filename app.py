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

# Sidebar filters
time_range = st.sidebar.selectbox("Time Range", ["Last 24 hours", "Last week", "Last month"])
topic = st.sidebar.selectbox("Topic", ["AI", "Machine Learning", "Deep Learning"])

# Dummy data
scores = {
    "Overall": np.random.randint(0, 11),
    "Sentiment": np.random.randint(0, 11),
    "Relevance": np.random.randint(0, 11),
}
feedbacks = ["Mala gestión", "Caro", "Tiempo de llegada", "Atención al cliente"]
topic_scores = np.random.rand(4)
number_of_appearance = np.random.randint(0, 100, 4)
recommendations = "Based on the analysis, here are some recommendations:\n\n- Improve the user interface.\n- Focus on the most relevant topics.\n- Address the negative feedback."

# Charts
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Overall Score")
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = scores["Overall"],
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [0, 10]},
                'bar': {'color': "green"}}
    ))
    st.plotly_chart(fig)

with col2:
    st.subheader("Sentiment Score")
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = scores["Sentiment"],
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [0, 10]},
                'bar': {'color': "blue"}}
    ))
    st.plotly_chart(fig)

with col3:
    st.subheader("Relevance Score")
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = scores["Relevance"],
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {'axis': {'range': [0, 10]},
                'bar': {'color': "purple"}}
    ))
    st.plotly_chart(fig)

# Ranking of main feedback
st.subheader("Ranking of main feedback")
topic_df = pd.DataFrame({"Feedback": feedbacks, "Nº of Appearance": number_of_appearance, "Score": topic_scores}, index=None)
topic_df = topic_df.sort_values(by="Nº of Appearance", ascending=False)
st.table(topic_df.set_index("Feedback"))

# Text section for recommendations
st.subheader("Action plan")
st.text(recommendations)
