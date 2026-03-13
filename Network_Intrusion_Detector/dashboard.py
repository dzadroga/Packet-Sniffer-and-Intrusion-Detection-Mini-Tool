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

#Suspicious traffic
if "prediction" in df.columns:
    st.subheader("Traffic Classification")

    pred_counts = df["prediction"].value_counts()

    fig2, ax2 = plt.subplots()
    pred_counts.plot(kind="pie", autopct="%1.1f%%", ax=ax2)
    st.pyplot(fig2)

#SYN Flood Detection
st.subheader("Top SYN Senders")

syn = df.groupby("src")["syn_count"].max().sort_values(ascending=False).head(10)

fig3, ax3 = plt.subplots()
syn.plot(kind="bar", ax=ax3)
st.pyplot(fig3)