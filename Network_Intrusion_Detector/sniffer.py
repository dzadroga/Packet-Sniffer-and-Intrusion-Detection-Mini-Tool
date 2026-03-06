from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time
from collections import defaultdict
import joblib

#Load the trained ML model
try: 
    model = joblib.load("traffic_model.pkl")
except:
    model = None

syn_counter - defaultdict(int)

data = []

def process_packet(packet):
    if IP in packet: 
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet[IP].proto
        length = len(packet)
        syn_flag = 0

    if TCP in packet: 
        flags = packet[TCP].flags

        if flags == "S":
            syn_flag = 1
            syn_counter += 1

    feature = {
        "time":time.time(),
        "src":src,
        "dst":dst,
        "proto":proto,
        "length":length,
        "syn_flag":syn_flag,
        "syn_count":syn_counter[src]
    }

    #ML prediction 
    if model:
        df = pd.DataFrame([{
            "protocol":proto,
            "length":length, 
            "syn_flag":syn_flag,
            "syn_count":syn_counter[src]
        }])

        prediction = model.predict(df)[0]
        feature["prediction"] = prediction
    else:
        feature["prediction"] = "unknown"

    data.append(feature)

    print(feature)

    pd.DataFrame(data).to_csv("traffic_log.csv", index=False)

print("Starting Packet Capture")

sniff(prn = process_packet, store=False)