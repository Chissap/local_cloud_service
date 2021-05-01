# IMPORTS
############################################
from os import listdir

import os.path

from pathlib import Path

import os

import shutil

from filecmp import dircmp

import time

##############################################

# This part allows running the code automatically every X seconds
while True:
    time.sleep(2)

######################################################################################


# COMPARE FILES IN TWO DIRECTORIES

# Construct a new directory comparision object
# to compare the directories left and right
 
    dcmp = dircmp(r"C:/Users/Chissa/Desktop/asd",r"C:/Users/Chissa/Desktop/asd2")
 
# This directory from left side of dircmp method
    print("\nleft:",dcmp.left)

#Files and subdirectories in a directory from left side of dircmp method
    print("\nleft list:", dcmp.left_list)
 
#The directory from right side of dircmp method
    print("\nright:",dcmp.right)
 
 
#Files and subdirectories in a directory from right side of dircmp method
    print("\nright list:", dcmp.right_list)
 
#Files and subdirectories in both left and right
    print("\nCommon:",dcmp.common)
 
#Files in both left and right
    print("\nCommon files:", dcmp.common_files)
 
#files which are identical in both left and right, using the class's
# file comparision operator
    print("\nsame_files", dcmp.same_files)

#############################################################################

# SOURCE AND DESTINATION PATHS

# Set up path to copy from
    source = Path("C:/Users/Chissa/Desktop/asd")
# Set up path to copy
    destination = Path("C:/Users/Chissa/Desktop/asd2")

##############################################################################

# Copying the files from dest and src folders
# Able to add third folder -> copy code below and paste. Add new destination and source for it

    # list files from both folders
    files = listdir(source)
    dst_files = listdir(destination)
    print('\ndestination folder files\n', dst_files)
    print('\nsource folder files\n', files)

    # copy all the files that aren't in both fodlers
    src_files = os.listdir(source)
    for file_name in src_files:
        full_file_name = os.path.join(source, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, destination)

    # this does the same as above but destination and source are in reverse order
    dst_files = os.listdir(destination)
    for file_name in dst_files:
        full_file_name = os.path.join(destination, file_name)
        if os.path.isfile(full_file_name):
            shutil.copy(full_file_name, source)



#TODO:
# how to make it .exe so it would be easier to run it

# make user input that can be imported into gui to let user assign copy paths
# also dcmp dir comparison should be the same path as the copy path ^^