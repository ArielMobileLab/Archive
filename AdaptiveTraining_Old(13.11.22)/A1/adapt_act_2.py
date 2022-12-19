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

ParIdDict = json.loads(open('Adaptive_Ammo.json').read())
os.system(ParIdDict["spatial_ego"])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    os.system(ParIdDict['training'])
    if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
    	os.system(ParIdDict['allo'])
if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
        os.system(ParIdDict['L1ttc2'])
        if 'kill -9 $(ps -e | grep SimCloud | head -c 6)':
            os.system(ParIdDict['L1ttc1'])




#OnLy GoD cAn judGe mE

