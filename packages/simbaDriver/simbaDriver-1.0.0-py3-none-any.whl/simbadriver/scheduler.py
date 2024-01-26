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

# from SIMBA.SIMBA import SIMBA
import sys
import os
import numbers
from pathlib import Path
from functools import cmp_to_key
from simbadriver.parslModule import ParslModule
from numpy import log10
from math import ceil

class Scheduler:
    @staticmethod
    def compare(A, B):
        if A["tick"] != B["tick"]:
            return A["tick"] - B["tick"]
        
        delta = B["priority"] - A["priority"]
        
        return -1 if delta < 0 else 1 if delta > 0 else 0
    
    def __init__(self, SIMBA):
        self.SIMBA = SIMBA

        self.schema = self.SIMBA.getConfiguration().loadJsonFile(SIMBA.getInstallDir().joinpath("schema", "schedule.json"))
        self.data = self.SIMBA.getConfiguration().loadJsonFile("schedule.json", self.schema)

        self.commonData = None
        if 'commonData' in self.data:
            self.commonData = self.data['commonData']
            
        self.schedule = list()
        priorities = set()
        
        index = '{{:0{}d}}'.format(ceil(log10(len(self.data['schedule']))))
        
        for item in self.data['schedule']:
            item['index'] = index.format(len(priorities) + 1)
            self.__addModule(item)
            
            """ Priorities must be unique """
            if item["priority"] in priorities:
                sys.exit("ERROR: Module '" + item["name"] + "' conflicting priority = '" + str(item["priority"]) + "'.")
                
            priorities.add(item["priority"])
            
        self.currentTick = None
        self.currentTime = None

        return
            
        
    def start(self, startTick, startTime):
        self.currentTick = startTick
        self.currentTime = startTime
        
        success = True
        
        if not os.path.exists('start'):
            os.mkdir('start')
        
        for item in self.data['schedule']:
            success &= item["instance"].start(startTick, startTime)
            
            if not success:
                break
            
        if not success:
            sys.exit("ERROR: Module '" + item["name"] + "' failed to start.")
            
        for item in self.data['schedule']:
            self.schedule.append({"tick" : item["startTick"], "priority" : item["priority"], "moduleData" : item})

        self.schedule.sort(key=cmp_to_key(Scheduler.compare))
         
        return success
        
    def step(self, continueFromTick, endTick, deltaTime):
        success = True
        startTime = self.currentTime
        startTick = self.currentTick
        
        while self.currentTick < endTick:
            if not os.path.exists(self.SIMBA.formatTick(self.currentTick)):
                os.mkdir(self.SIMBA.formatTick(self.currentTick))
        
            success &= self.__internalStep(deltaTime, self.currentTick < continueFromTick)
            self.currentTick += 1
            self.currentTime = startTime + (self.currentTick - startTick) * deltaTime

        return success
    
    def __internalStep(self, deltaTime, skipExecution):
        success = True
        toBeRemoved = list()
        
        for item in self.schedule:
            if item["tick"] != self.currentTick:
                break
            
            moduleData = item["moduleData"]
            
            success &= moduleData["instance"].step(self.currentTick, self.currentTime, 1, deltaTime, skipExecution)
            
            """ Reschedule the item if required otherwise prepare for removal """
            if self.currentTick + moduleData["tickIncrement"] <= moduleData["endTick"] and moduleData["tickIncrement"] > 0:
                item["tick"] += moduleData["tickIncrement"]
            else:
                toBeRemoved.append(item)
            
        """ Remove items which have not been rescheduled """
        for item in toBeRemoved:
            self.schedule.remove(item)
        
        self.schedule.sort(key=cmp_to_key(Scheduler.compare))
        
        return success
        
    def end(self):
        success = True
        
        if not os.path.exists('end'):
            os.mkdir('end')
        
        for item in self.data['schedule']:
            try:
                success &= item["instance"].end(self.currentTick, self.currentTime)
                
            except:
                success = False
                
            if not success:
                break
        
        if not success:
            sys.exit("ERROR: Module '" + item["name"] + "' failed to end.")
            
        self.schedule = list()
        self.currentTick = None
        self.currentTime = None
        
        return success

    def __addModule(self, module):
        if not module['type'] in [ 'parsl' ]:
            sys.exit("ERROR: Module '" + module["type"] + "' is not supported.")

        module['instance'] = ParslModule(self.SIMBA, self, module)

        if not isinstance(module["priority"], numbers.Real):
            if module["priority"] == "-Infinity":
                module["priority"] = -float("inf")
            elif module["priority"] == "Infinity":
                module["priority"] = float("inf")

        if not "startTick" in module:
            module ["startTick"] = -float("inf")

        if not "tickIncrement" in module:
            module ["tickIncrement"] = 1
            
        if not "endTick" in module:
            module["endTick"] = float("inf")
                
        if module["endTick"] < module["startTick"]:
            sys.exit("ERROR: Module '" + module["name"] + "' invalid endTick = '" + str(module["endTick"]) + "'.")
            
        return True

    def initConfigData(self):
        config = {
            '$schema': 'https://raw.githubusercontent.com/NSSAC/SIMBA_driver/master/schema/module.json'
            }
        
        if self.commonData != None:
            config['commonData'] = self.commonData

        return config
    
    def updateCommonData(self, commonData):
        if self.commonData == None:
            return
        
        for key in self.commonData:
            if key in commonData:
                self.commonData[key] = commonData[key]
