#!/bin/bash
#$ -M yxu6@nd.edu       # Email address for job notification
#$ -m abe               # Send mail when job begins, ends and aborts
#$ -q debug # Specify queue
#$ -pe smp 1            # Specify number of cores to use.
#$ -N UK-RA # Specify job name

module load python

python3 batch_pull.py
