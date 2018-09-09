# -------------------------------------------------------------------------------
# Name:       Create folder in D drive and then create file gdb in that folder
# Purpose:
#
# Author:      Vidya Sagar Gurung
#
# Created:     21/05/2015
# Copyright:   (c) Vidya Sagar Gurung 2015
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import os
import sys

import arcpy
from arcpy import env

# Getting user input for creating folder name
folder_name = raw_input('Please type in folder name')

# Checking if the folder exists.
if os.path.isdir(folder_name):
    print 'Folder name already exists.'
else:
    os.mkdir(folder_name)
    env.workspace = os.chdir(folder_name)

# Creating a file gdb

name = raw_input('Please choose a name for file geodatabase')
fgdb_name = name + '.gdb'

if os.path.isdir(fgdb_name):
    print 'File geodatabase with this name already exists.'
else:
    arcpy.CreateFileGDB_management(os.getcwd(), fgdb_name)

print 'Completed creating filegeodatabase.'
