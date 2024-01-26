# BEGIN: Copyright 
# Copyright (C) 2024 Rector and Visitors of the University of Virginia 
# All rights reserved 
# END: Copyright 

# BEGIN: License 
# Licensed under the Apache License, Version 2.0 (the "License"); 
# you may not use this file except in compliance with the License. 
# You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0 
# END: License 

from pathlib import Path
from abc import ABCMeta, abstractmethod

class Module():
    __metaclass__ = ABCMeta
    
    def __init__(self, SIMBA, scheduler, data):
        self.SIMBA = SIMBA
        self.scheduler = scheduler
        
        self.data = {}
        self.name = data['name']
        self.index = data['index']
        self.command = self.SIMBA.getConfiguration().resolveCmd(data['command'])
        
        if 'updateCommonData' in data:
            self.updateCommonData = data['updateCommonData']
        else:
            self.updateCommonData = False
            
        if "moduleData" in data:
            self.moduleData = data['moduleData']
        else :
            self.moduleData = None

        self.__lastRunTick = None
        self.__lastRunTime = None
    
        self._init(data)
        
    @abstractmethod   
    def _init(self, data):
        return False
    
    def start(self, startTick, startTime):
        mode = 'start'
        self.config = str(Path.cwd().joinpath(mode, 'module_{}.json'.format(self.index)))
        self.status = str(Path.cwd().joinpath(mode, 'status_{}.json'.format(self.index)))
        
        self.__lastRunTick = startTick
        self.__lastRunTime = startTime
        
        moduleConfig = self.scheduler.initConfigData()
        moduleConfig['mode'] = 'start'
        moduleConfig['statusFile'] = self.status
        moduleConfig['currentTick'] = startTick
        moduleConfig['currentTime'] = startTime.isoformat()
        
        if self.moduleData != None:
            moduleConfig['moduleData'] = self.moduleData

        self.SIMBA.getConfiguration().writeJsonFile(self.config, moduleConfig)
        success = self._start(startTick, startTime)
        
        if success:
            success &= self.readStatus()
        
        return success
        
    @abstractmethod   
    def _start(self, startTick, startTime):
        return False
        
    def step(self, currentTick, currentTime, deltaTick, deltaTime, skipExecution):
        mode = self.SIMBA.formatTick(currentTick)
        self.config = str(Path.cwd().joinpath(mode, 'module_{}.json'.format(self.index)))
        self.status = str(Path.cwd().joinpath(mode, 'status_{}.json'.format(self.index)))

        success = True
    
        moduleConfig = self.scheduler.initConfigData()
        moduleConfig['mode'] = 'step'
        moduleConfig['statusFile'] = self.status
        moduleConfig['lastRunTick'] = self.__lastRunTick
        moduleConfig['lastRunTime'] = self.__lastRunTime.isoformat()
        moduleConfig['currentTick'] = currentTick
        moduleConfig['currentTime'] = currentTime.isoformat()
        moduleConfig['targetTick'] = currentTick + deltaTick
        moduleConfig['targetTime'] = (currentTime + deltaTime).isoformat()
        
        if self.moduleData != None:
            moduleConfig['moduleData'] = self.moduleData

        self.SIMBA.getConfiguration().writeJsonFile(self.config, moduleConfig)
        
        if not skipExecution:
            success = self._step(self.__lastRunTick, self.__lastRunTime, currentTick, currentTime, currentTick + deltaTick, currentTime + deltaTime)

            if success:
                success &= self.readStatus()
        
        self.__lastRunTick = currentTick
        self.__lastRunTime = currentTime
        
        return success 

    @abstractmethod   
    def _step(self, lastRunTick, lastRunTime, currentTick, currentTime, targetTick, targetTime):
        return False
        
    def end(self, endTick, endTime):
        mode = 'end'
        self.config = str(Path.cwd().joinpath(mode, 'module_{}.json'.format(self.index)))
        self.status = str(Path.cwd().joinpath(mode, 'status_{}.json'.format(self.index)))
 
        moduleConfig = self.scheduler.initConfigData()
        moduleConfig['mode'] = mode
        moduleConfig['statusFile'] = self.status
        moduleConfig['lastRunTick'] = self.__lastRunTick
        moduleConfig['lastRunTime'] = self.__lastRunTime.isoformat()
        moduleConfig['currentTick'] = endTick
        moduleConfig['currentTime'] = endTime.isoformat()
        
        if self.moduleData != None:
            moduleConfig['moduleData'] = self.moduleData

        self.SIMBA.getConfiguration().writeJsonFile(self.config, moduleConfig)
        
        success = self._end(self.__lastRunTick, self.__lastRunTime, endTick, endTime)
        
        if success:
            success &= self.readStatus()

        self.__lastRunTick = None
        self.__lastRunTime = None
        
        return success 

    @abstractmethod   
    def _end(self, lastRunTick, lastRunTime, endTick, endTime):
        return False

    def readStatus(self):
        if not Path(self.status).exists():
            return False
        
        status = self.SIMBA.getConfiguration().loadJsonFile(self.status)
        
        if 'moduleData' in status:
            self.moduleData = status['moduleData']
            
        if self.updateCommonData and 'commonData' in status:
            self.scheduler.updateCommonData(status['commonData'])
            
        return status['status'] == 'success'