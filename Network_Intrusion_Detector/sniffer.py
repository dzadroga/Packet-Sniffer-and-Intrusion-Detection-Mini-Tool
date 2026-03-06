from scapy.all import sniff, IP, TCP, UDP
import pandas as pd
import time
from collections import defaultdict
import job lib

#Load the trained ML model
try: 
    model = joblib.load("traffic_model.pkl")
except:
    model = None

syn_counter - defaultdict(int)

data = []

def process_packet(packet)
