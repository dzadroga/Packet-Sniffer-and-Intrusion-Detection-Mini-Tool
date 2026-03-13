import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Network Intrusion Detection Dashboard")

try:
    df = pd.read_csv("traffic_log.csv")
except: 
    st.warning("No traffic captured yet")
    st.stop()
