#!/usr/bin/env python3

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

import argparse
from simbadriver.simbadriver import SIMBA

parser = argparse.ArgumentParser(description="SIMBA multi-scale simulation framework.")
parser.add_argument("directory", nargs=1, help='The directory where configuration files are located.')

arguments = parser.parse_args()
SIMBA(arguments.directory[0]).run()

exit
