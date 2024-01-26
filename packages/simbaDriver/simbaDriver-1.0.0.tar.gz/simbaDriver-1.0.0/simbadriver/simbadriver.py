# BEGIN: Copyright 
# Copyright (C) 2019 - 2024 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

import sys
from pathlib import Path
from simbadriver.configuration import Configuration
from simbadriver.scheduler import Scheduler
from simbadriver.rfc3339Duration import rfc3339Duration
from numpy import inf
import os, logging, math
from datetime import datetime
from datetime import timedelta
from numpy import log10
from math import ceil

class SIMBA:
    def __init__(self, configurationDirectory):
        self.Configuration = Configuration(configurationDirectory)
        self.InstallDir = Path(__file__).parent.parent.resolve()
        self.pwd = Path.cwd()
        
        self.schema = self.Configuration.loadJsonFile(self.InstallDir.joinpath("schema", "driver.json"))
        self.data = self.Configuration.loadJsonFile("driver.json", self.schema)

        self.data['initialTime'] = datetime.fromisoformat(self.data['initialTime'])        
        self.data['endTime'] = datetime.fromisoformat(self.data['endTime'])        

        if self.data["endTime"] < self.data['initialTime']:
            sys.exit("ERROR: SIMBA invalid endTime: '" + str(self.data["endTime"]) + "'.")

        if not "runId" in self.data:
            #TODO CRITICAL Implement me
            self.data["runId"] = datetime.now().strftime("%Y%m%d%H%M%S.") + str(os.getpid())

        if not "cellId" in self.data:
            self.data["cellId"] = 0
            
        if not "initialTick" in self.data:
            self.data["initialTick"] = 0
            
        if not "continueFromTick" in self.data:
            self.data["continueFromTick"] = self.data["initialTick"]
        
        if self.data["continueFromTick"] < self.data["initialTick"]:
            sys.exit("ERROR: SIMBA invalid continueFromTick: '" + str(self.data["continueFromTick"]) + "'.")

        
        currentTime = self.data["initialTime"]
        currentTick = -1
        ToBeRemoved = list()
        
        for item in self.data["scheduleIntervals"]:
            if currentTime >= self.data["endTime"]:
                ToBeRemoved.append(item)
                continue
                
            if not "startTick" in item:
                item["startTick"] = currentTick + 1
                
            if  item["startTick"] <= currentTick:
                sys.exit("ERROR: SIMBA overlapping schedule interval with startTick:  '" + str(item["startTick"]) + "'.")
                
            if not "endTick" in item:
                item["endTick"] = float(inf)
            elif not isinstance(item["endTick"], int):
                item["endTick"] = float("inf")
                
            if item["endTick"] < item["startTick"]:
                sys.exit("ERROR: SIMBA invalid schedule interval: ['" + str(item["startTick"]) + "', '" + str(item["endTick"]) + "'].")
            
            tickDuration = rfc3339Duration.toTimeDelta(item["tickDuration"])

            if tickDuration <= timedelta(seconds=0):
                sys.exit("ERROR: SIMBA invalid schedule interval tickDuration: '" + item["tickDuration"] + "'.")

            item["tickDuration"] = tickDuration

            if currentTick < 0:
                correction = 0
            else: 
                correction = 1
            
            if isinstance(item["endTick"], int):
                maxTime = currentTime + (item["endTick"] - item["startTick"] + correction) * item["tickDuration"]
            else:
                maxTime = datetime.fromisoformat("9999-01-01T00:00:00Z")

            if maxTime > self.data["endTime"]:
                item["endTick"] = item["startTick"] + math.ceil((self.data["endTime"] - currentTime) / item["tickDuration"]) - 1
                maxTime = currentTime + (item["endTick"] - item["startTick"] + correction) * item["tickDuration"]
                
            currentTime = maxTime
            currentTick += item["endTick"] - item["startTick"] + 1

        self.tick = '{{:0{}d}}'.format(ceil(log10(currentTick)))
                         
        for item in ToBeRemoved:
            self.data["scheduleIntervals"].remove(item)
            
        if currentTime < self.data["endTime"]:
            sys.exit("ERROR: SIMBA endTime: '" + str(self.data["endTime"]) + "' will never be reached (max time: '" + str(currentTime) + "').")
            
        if currentTick < self.data["continueFromTick"]:
            sys.exit("ERROR: SIMBA continueFromTick: '" + str(self.data["continueFromTick"]) + "' will never be reached (max tick: '" + str(currentTick) + "').")

        self.Scheduler = Scheduler(self)

        logging.basicConfig(filename = __name__ + ".log")
        
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(10)
            
        return
    
    def run(self):
        self.Scheduler.start(self.data["initialTick"], self.data["initialTime"])
        
        for item in self.data["scheduleIntervals"]:
            self.Scheduler.step(max(item["startTick"], self.data["continueFromTick"]), item["endTick"], item["tickDuration"])
        
        self.Scheduler.end()
        return
    
    def getConfiguration(self):
        return self.Configuration
    
    def getDatabase(self):
        return self.Database
    
    def getRunId(self):
        return self.data["runId"]
    
    def getCellId(self):
        return self.data["cellId"]
    
    def getInstallDir(self):
        return self.InstallDir
    
    def getPwd(self):
        return self.pwd

    def formatTick(self, tick):
        return self.tick.format(tick)