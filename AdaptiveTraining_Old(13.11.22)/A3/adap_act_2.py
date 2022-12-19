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
#def automation(ParIdDict):
os.system(ParIdDict['A1']['training'])
if os.system('kill -9 $(ps -e | grep SimCloud | head -c 6)'):
    os.system(ParIdDict['A1']['spatial_ego'])

