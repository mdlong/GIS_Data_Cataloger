#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Mike
#
# Created:     12/08/2015
# Copyright:   (c) Mike 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os, pyodbc, arcpy, time, binascii
from os import path
from arcpy import da

# Define a function to create a CRC for the file
# http://www.matteomattei.com/how-to-calculate-the-crc32-of-a-file-in-python/
def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

workspace = r"H:/"


walk = arcpy.da.Walk(workspace, datatype="Any", type="All")

for dirpath, dirnames, filenames in walk:
    for filename in filenames:
        x = os.path.join(dirpath,filename)
        print x

        info = os.stat(x)

        created = datetime.datetime.strptime(time.ctime(os.path.getctime(x)), "%a %b %d %H:%M:%S %Y")
        print created

        modified = datetime.datetime.strptime(time.ctime(os.path.getmtime(x)), "%a %b %d %H:%M:%S %Y")
        print modified

        size =  info.st_size
        print size

        crc = CRC32_from_file(x)
        print crc

        print "-------------------"