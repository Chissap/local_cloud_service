# IMPORTS
############################################
from os import listdir

import os.path

from pathlib import Path

import os

import shutil

from filecmp import dircmp

import time

import datetime
##############################################

# This part allows running the code automatically every X seconds

while True:
    time.sleep(0)

######################################################################################

# SOURCE AND DESTINATION PATHS
    x = datetime.datetime.now()

    day = x.day
    month = x.month
    year = x.year

    destination_name = day, month, year

# Set up path to copy from
    source = Path("C:/Users/Chissa/Desktop/asd")
# Set up path to copy
    destination = Path(f"C:/Users/Chissa/Desktop/asd2/{destination_name}")

##############################################################################

    # copy all the files that aren't in both fodlers
    src_files = os.listdir(source)
    for file_name in src_files:
        full_file_name = os.path.join(source, file_name)
        if os.path.isdir(full_file_name):
            shutil.copytree(full_file_name, destination)

"""
    # this does the same as above but destination and source are in reverse order
    dst_files = os.listdir(destination)
    for file_name in dst_files:
        full_file_name = os.path.join(destination, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, source)
"""