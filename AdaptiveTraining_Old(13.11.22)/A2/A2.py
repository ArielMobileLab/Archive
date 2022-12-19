#@Directed by A.W

from cognata_api.web_api.cognata_demo import CognataRequests as cog_api
import time
import os
import threading
import queue
import timeit
import signal
from contextlib import contextmanager
import sys
import json
import rospy
import tkinter
from geometry_msgs.msg import Point
from std_msgs.msg import Float64
from sensor_msgs.msg import NavSatFix

ParIdDict = json.loads(open("Adaptive_Ammo_A2.json").read())
os.system(ParIdDict["training"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L1CUBE_latency2"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L1_latency2"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L1CUBE_latency1"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L1_latency1"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["Allo"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["Ego"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L2TTCMatlabLATENCY100"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L2TTCMatlabLATENCY200"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L2TTC10LATENCY100"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L2TTC10LATENCY200"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L2TTC20LATENCY200"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict["L2TTC20LATENCY100"])





#OnLy GoD cAn judGe mE

