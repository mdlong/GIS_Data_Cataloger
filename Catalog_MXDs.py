import os, pyodbc, arcpy, time, binascii
from os import path
from arcpy import da

# Set up the SQL Server connection info
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=jeeves;DATABASE=CMTAGISStats;Trusted_Connection=yes;')
cursor = cnxn.cursor()

# Define a function to create a CRC for the file
# http://www.matteomattei.com/how-to-calculate-the-crc32-of-a-file-in-python/
def CRC32_from_file(filename):
    buf = open(filename,'rb').read()
    buf = (binascii.crc32(buf) & 0xFFFFFFFF)
    return "%08X" % buf

#arrMxd = [];

mxdPath = r"H:\\"
#mxdPath = r"H:\James\Rapid Bus"

print mxdPath

for root, dirs, files in os.walk(mxdPath, topdown=False):

    for name in files:
        if '.mxd' in name:
            print name
            x = os.path.join(root,name)
            print x

            info = os.stat(x)

            created = datetime.datetime.strptime(time.ctime(os.path.getctime(x)), "%a %b %d %H:%M:%S %Y")
            print created

            modified = datetime.datetime.strptime(time.ctime(os.path.getmtime(x)), "%a %b %d %H:%M:%S %Y")
            print modified

            crc = CRC32_from_file(x)
            print crc

            size =  info.st_size
            print size

            cursor.execute("insert into GDB.MXDs(Name, Path, Size, Created, Modified, CRC) values (?, ?, ?, ?, ?, ?)", name, x, size, created, modified, crc)
            cnxn.commit()
            cursor.execute("SELECT @@IDENTITY AS ID")
            rowid = cursor.fetchone()
            mxdid = rowid.ID
            print mxdid

            if size > 2048:
                mxd = arcpy.mapping.MapDocument(x)
                #print mxd
                for df in arcpy.mapping.ListDataFrames(mxd):
                    print df.name
                    for lyrs in arcpy.mapping.ListLayers(mxd, "", df):
                        if hasattr(lyrs, "dataSource"):
                            print lyrs.name
                            print lyrs.longName
                            print lyrs.datasetName
                            print lyrs.dataSource
                            lyrtype = "Feature"

                            cursor.execute("insert into Layers(MXD_Name, MXD_Path, LYR_Name, LYR_Path, MXD_ID, LYR_Type) values (?, ?, ?, ?, ?, ?)", name, x, lyrs.name, lyrs.dataSource, mxdid, lyrtype)
                            cnxn.commit()
                        elif hasattr(lyrs, "isGroupLayer"):
                            print lyrs.name + " is a group layer."
                            lyrtype = "Group"
                            cursor.execute("insert into Layers(MXD_Name, MXD_Path, LYR_Name, MXD_ID, LYR_Type) values (?, ?, ?, ?, ?)", name, x, lyrs.name, mxdid, lyrtype)
                            cnxn.commit()

                    print "---------Moving to next Layer----------"
                print "___------Moving to next MXD-------___"

#del rows



