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

import json
import sys
from pathlib import Path
from jsonschema import validate

class Configuration:
    
    def __init__(self, configurationDirectory):
        self.configurationDirectory = configurationDirectory
        
    def loadJsonFile(self, fileName, schema = None):
    
        try:
            jsonFile = open(Path(self.configurationDirectory).joinpath(fileName),"r")
        
        except:
            sys.exit("ERROR: File '" + Path(self.configurationDirectory).joinpath(fileName) + "' does not exist.")
        
        dictionary = json.load(jsonFile)
        
        if schema != None:
            validate(dictionary, schema)
            
        jsonFile.close()
        return dictionary

    def writeJsonFile(self, fileName, dictionary, schema = None):
        if schema != None:
            validate(dictionary, schema)

        file = open(fileName, 'w')            
        json.dump(dictionary, file, indent=2)
        
    def resolveCmd(self, cmd):
        if Path(cmd).is_absolute():
            return cmd
        
        if Path(self.configurationDirectory).joinpath(cmd).exists():
            return str(Path(self.configurationDirectory).joinpath(cmd))
            
        return cmd