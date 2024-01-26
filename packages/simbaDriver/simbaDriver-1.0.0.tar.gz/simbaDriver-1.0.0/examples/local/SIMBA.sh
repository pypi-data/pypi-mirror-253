#!/usr/bin/env bash

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

# set -o xtrace

SIMBA_PATH=$(realpath $(dirname $(dirname $(dirname $0))))

export PYTHONPATH=${SIMBA_PATH}:${PYTHONPATH}
${SIMBA_PATH}/bin/SIMBA.py ${SIMBA_PATH}/example/local