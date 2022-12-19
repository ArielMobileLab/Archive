# HOW TO INSTALL:
git clone the project to your machine.


# HOW TO USE:
Navigate to the folder and run the follwoing script: <br>
python3 adaptiveTraining.py 'scenario' 'script' 'sensor preset' <br>

### EXAMPLES
## training:
python3 adaptiveTraining.py train train allocentric-rear <br>

## acc:
#### TTC1 -
python3 adaptiveTraining.py load-1 ttc1 allocentric-rear <br>
python3 adaptiveTraining.py load-2 ttc1 allocentric-rear <br>
python3 adaptiveTraining.py load-3 ttc1 allocentric-rear <br>
#### TTC2 -
python3 adaptiveTraining.py load-1 ttc2 allocentric-rear <br>
python3 adaptiveTraining.py load-2 ttc2 allocentric-rear <br>
python3 adaptiveTraining.py load-3 ttc2 allocentric-rear <br>

## spatial:
python3 adaptiveTraining.py spatial spatial allocentric <br>
python3 adaptiveTraining.py spatial spatial egocentric <br>

## slallum:
#### far -
python3 adaptiveTraining.py latency0 far allocentric <br>
python3 adaptiveTraining.py latency1 far allocentric <br>
python3 adaptiveTraining.py latency2 far allocentric <br>
python3 adaptiveTraining.py latency3 far allocentric <br>
#### close -
python3 adaptiveTraining.py latency0 close allocentric <br>
python3 adaptiveTraining.py latency1 close allocentric <br>
python3 adaptiveTraining.py latency2 close allocentric <br>
python3 adaptiveTraining.py latency3 close allocentric <br>

# PROJECT INFORMATION
This project uses an Active Object design pattern. The class 'launchScenario' is an Active Object that gets (in the constructor) information about the simulation that it should run, and once the 'runAO()' function is called the object operates itself and launches the simulation with the relevant scripts. 

#### Class launchScenario:
    Variables
    scenarioID - String that represents the scenario that will be launched.
    scriptToRun - String that represents the code that will be run. (i.e latency, ttc, ect'..)
    sensorPreset - String that represents the ego car preset that will be used in the scenario.
    queueID - String that represents the Simulation Queue ID (to launch through Cognata)
    Running flag - Boolean that is true as long as the simCloud window is launched. 
    Functions
    A standard __init__ function is used for object construction. 
    runAO() - This function will run the scenario using the settings set in the object’s variables.
    This function will create threads to run each needed process. 
    Thread functions that Run() will call for each thread.

