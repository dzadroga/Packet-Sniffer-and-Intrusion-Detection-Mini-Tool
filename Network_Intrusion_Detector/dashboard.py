import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Network Intrusion Detection Dashboard")

try:
    df = pd.read_csv("traffic_log.csv")
except: 
    st.warning("No traffic captured yet")
    st.stop()

st.subheader("Recent Traffic")
st.datafram(df.tail(50))

#Protocol Distribution
st.subheader("Protocol Distribution")

proto_counts = df["protocol"].value_counts()

fig, ax = plt.subplots()
proto_counts.plot(kind="bar", ax=ax)
st.pyplot(fig)

