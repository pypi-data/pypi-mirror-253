#!/bin/bash

#SBATCH --job-name test
#SBATCH --time 1:00:00
#SBATCH --partition bii
#SBATCH --qos bii-half
#SBATCH --account nssac_covid19
#SBATCH --nodes 1
#SBATCH --tasks-per-node 1

export PYTHONPATH=${SIMBA_PATH}:${PYTHONPATH}
${SIMBA_PATH}/bin/SIMBA.py ${SIMBA_PATH}/example/slurm