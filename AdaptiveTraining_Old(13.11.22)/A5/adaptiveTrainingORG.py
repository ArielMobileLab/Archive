"""
@author: Raz Gavrieli, @date: july 2022, C mobileLab Ariel University
This program is used to run the cognata simulation with the SDK and mobileLab's scripts automatically. 
"""

from cognata_api.web_api.cognata_demo import CognataRequests as cog_api
import time
import os
import threading

import timeit

import signal
from contextlib import contextmanager

import sys

import json

@contextmanager
def timeout(time):
    signal.signal(signal.SIGALRM, raise_timeout)
    signal.alarm(time)
    try:
        yield
    except TimeoutError:
        pass
    finally:
        signal.signal(signal.SIGALRM, signal.SIG_IGN)

def raise_timeout(signum, frame):
    print("Loading timed out")
    sys.exit()

#### --- GLOBAL VARIABLES --- ####
company_id = "844cd963"
username = "arielandromeda21"
password = "ArielAnDrOmEdA21"
backendIP = "https://{}.cognata-studio.com/v1".format(company_id)
api = cog_api(backendIP, username, password)

# The following dicrionaries were created to quickly find the correct scenarioID\script\sensorPreset using a short keyword that we use in the lab. 
scenarioDict = json.loads(open('scenarios.json').read())
scriptDict =  json.loads(open('scripts.json').read())
sensorDict = json.loads(open('sensorPresets.json').read())
# IMPORTANTE NOTE - The three dictionaries above should be updated whenever new scenarios\scripts\sensor presets are added. 

class scenarioLaunch:
    def __init__(self, scenarioID="", scriptToRun="", sensorPreset="", queueID="lab_00:0e:c6:47:1f:31"):
        #### --- CONSTANTS --- ####
        self.MINTIME = 15

        #### --- VARIABLES --- ####
        try:
            self.scenarioID = scenarioDict[scenarioID]      # USE A DICTIONARY TO FIND THE CORRECT SCENARIOID BY ITS NAME
            self.scriptToRun = scriptDict[scriptToRun]      # USE A DICTIONARY TO FIND THE CORRECT SCRIPT TO RUN BY ITS NAME
            self.sensorPreset = sensorDict[sensorPreset]    # USE A DICTIONARY TO FIND THE CORRECT PRESET BY ITS NAME
        except:
            print("could not find what you were asking for..")
            raise "bad input"
            sys.exit()
        self.queueID = [queueID]
        # self.forceFeedback = THIS WILL BE THE FORCE FEED BACK VALUE
        # self.autoCenter = THIS WILL BE THE AUTO CETNER VALUE
        self.isRunning = False
        
        #### --- THREAD INITIALIZATION --- ####
        self.AO = threading.Thread(target=self.runAO) # AO = Active Object (design pattern)
        # self.AO.daemon = True - For this to be true the main loop should be running all the time
        self.runAliasThread = threading.Thread(target=self.run_alias_thread_func)
        self.runAliasThread.daemon = True
        self.scriptAliasThread = threading.Thread(target=self.script_alias_thread_func)
        self.scriptAliasThread.daemon = True
        self.speedThread = threading.Thread(target=self.speed_thread_func)
        self.speedThread.daemon = True


    def runAO(self):
        self.runAliasThread.start() 
        self.scriptAliasThread.start()
        self.speedThread.start()
        self.isRunning = True
        print("here")
        while self.isRunning:
            time.sleep(5)
        
        print("AO closed")
        os.system('kill -9 $(ps -e | grep SimCloud | head -c 6)') # find and kill simcloud window
        sys.exit()

    def run_scenarioLaunch_object(self):
        with timeout(5): # will wait 5 seconds to load the scenario
            scenario = api.find_scenario(scenario_id=self.scenarioID) # will hang if scenario is not found
        scenario['queues'] = self.queueID 
        scenario['ego_car']['ego_car_sku'] = self.sensorPreset
        api.generate_simulation(scenario_data=scenario)
        self.AO.start()
       

    def run_alias_thread_func(self):
        i = 0
        while i < 10: # Runs until the 'break' keyword or after 10 attempts
            start = timeit.default_timer()
            os.system('rosrun cognata_sdk ROSCognataSDK 10.20.0.1 5555 --optimize-rendering --gps > /dev/null')
            stop = timeit.default_timer()
            if (stop - start > self.MINTIME): # if the run function ran more than MINTIME secs, break the loop (meaning the run time was long enough and probably the simulation ran)
                break 
            print("could not connect to engine, trying again in 5 seconds.. attempt " + str(i) + "/10")
            i+=1
            time.sleep(5)

        self.isRunning = False
        if i>=9:
            print("failed to load the SDK")
        
        print("closing the program.. (5-10 seconds)")

    def script_alias_thread_func(self):
        os.system(self.scriptToRun) # Will die when run thread dies (daemon)

    def speed_thread_func(self):
        os.system('terminator --geometry=340x130-2700+1000 -T speed -p speed -x rosrun cognata_sdk speed.py') # Will die when run thread dies (daemon)
    # END OF LAUNCHSCENARIO CLASS

def roscore_thread():
    os.system('roscore') # Will die if used as daemon

if __name__ == '__main__':
    scenarioID = sys.argv[1]
    scriptToRun = sys.argv[2]
    sensorPreset = sys.argv[3]

    A = scenarioLaunch(scenarioID, scriptToRun, sensorPreset)
    A.run_scenarioLaunch_object()
