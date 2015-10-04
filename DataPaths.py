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

import os, arcpy, time, binascii
from os import path
from arcpy import da
import sqlite3 as lite

# Set up a connection to a sqlite database
cnxn = lite.connect(r"G:\Internal\Tools\Python\GIS_Data_Cataloger\DataCatalog.sqlite")
cur = cnxn.cursor()



# Truncate the table before running the script.
cur.execute("DELETE FROM Data;")
cur.execute("DELETE FROM sqlite_sequence;")

# Define a function to create a CRC for the file
# http://www.matteomattei.com/how-to-calculate-the-crc32-of-a-file-in-python/
def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

workspace = r"H:/"
#workspace = r"Z:\RAID\GIS_Stuff\GIS_Data"


try:
    walk = arcpy.da.Walk(workspace, datatype="Any", type="All")

    for dirpath, dirnames, filenames in walk:
        for filename in filenames:
            x = os.path.join(dirpath,filename)
            print x

            if dirpath.endswith('.xlsx' or '.xls'):
                print "Excel File..."

                # Set the type, file extension, and path
                type = "Excel"
                ext = "xlsx"
                path = dirpath

                # Grab the filename from the path
                name = x.split("\\")[-1]

                created = datetime.datetime.strptime(time.ctime(os.path.getctime(dirpath)), "%a %b %d %H:%M:%S %Y")
                print created

                modified = datetime.datetime.strptime(time.ctime(os.path.getmtime(dirpath)), "%a %b %d %H:%M:%S %Y")
                print modified

                info = os.stat(dirpath)
                size =  info.st_size
                print size

                crc = CRC32_from_file(dirpath)
                print crc


                # Write the values into the database
                cur.execute("insert into Data VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (name, path, type, ext, size, created, modified, crc))
                cnxn.commit()
##                cur.execute ("insert into MXDs VALUES (NULL, ?, ?, ?, ?, ?, ?)",  (name, x, size, created, modified, crc))
##                cnxn.commit()
            elif '.gdb' in dirpath:
                print "GDB...will do stuff later"
                break

            elif dirpath.endswith('.DWG' or '.dwg' or '.dxf' or '.DXF'):
                print "DWG...will do stuff later"


##            elif 'arc' in filename:
##                print "arc...will do stuff later?"

            else:

                info = os.stat(x)

                created = datetime.datetime.strptime(time.ctime(os.path.getctime(x)), "%a %b %d %H:%M:%S %Y")
                print created

                modified = datetime.datetime.strptime(time.ctime(os.path.getmtime(x)), "%a %b %d %H:%M:%S %Y")
                print modified

                size =  info.st_size
                print size

                crc = CRC32_from_file(x)
                print crc

                desc = arcpy.Describe(x)
                if hasattr(desc, "name"):
                    name = desc.name
                    print name

                if hasattr(desc, "dataType"):
                    type = desc.dataType
                    print type
                if hasattr(desc, "catalogPath"):
                    path = desc.catalogPath
                    print path
                if hasattr(desc, "extension"):
                    ext = desc.extension
                    print ext


    ##            print "Children:"
    ##                for child in desc.children:
    ##                print "\t%s = %s" % (child.name, child.dataType)

                cur.execute("insert into Data VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (name, path, type, ext, size, created, modified, crc))
                cnxn.commit()

            print "-------------------"

except:
    # Close any left over connections
    cnxn.close()