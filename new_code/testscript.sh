#!/bin/bash
#SBATCH -n 1                # Number of cores
#SBATCH -N 1                # Ensure that all cores are on one machine
#SBATCH -t 1-06:10          # Runtime in D-HH:MM, minimum of 10 minutes
#SBATCH -p requeue   # Partition to submit to
#SBATCH --mem=100           # Memory pool for all cores (see also --mem-per-cpu)
#SBATCH -o myoutput_%j.out  # File to which STDOUT will be written, %j inserts jobid
#SBATCH -e myerrors_%j.err  # File to which STDERR will be written, %j inserts jobid
#SBATCH --test-only

module load Anaconda3/5.0.1-fasrc02 #Load Perl module
source activate thesis_env2
python3 'short.py'