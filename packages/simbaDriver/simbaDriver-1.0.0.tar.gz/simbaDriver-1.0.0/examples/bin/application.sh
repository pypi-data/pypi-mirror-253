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

STATUS=$(jq '.statusFile' $1 | tr -d '"')

OUT=$(dirname $1)/$(basename $1 .json).out

echo 'hostname:   ' $(hostname) > ${OUT}

echo 'mode:       ' $(jq '.mode' $1) >> ${OUT}
echo 'currentTick: ' $(jq '.currentTick' $1) >> ${OUT}
echo 'currentTime: ' $(jq '.currentTime' $1) >> ${OUT}

echo '{"status": "success"}' > ${STATUS}