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

mxdPath = r"H:/"
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

            size =  info.st_size
            print size

            crc = CRC32_from_file(x)
            print crc

            mxd = arcpy.mapping.MapDocument(x)
            #print mxd
            for df in arcpy.mapping.ListDataFrames(mxd):
                print df.name
                for lyrs in arcpy.mapping.ListLayers(mxd, "", df):
                    if lyrs.isGroupLayer == "True":
                        print "Skipping Group LYR"
                    else:

                        print lyrs

##            cursor.execute("insert into MXDs(Name, Path, Size, Created, Modified, CRC) values (?, ?, ?, ?, ?, ?)", name, x, size, created, modified, crc)
##            cnxn.commit()

            print "-------------------"

##            arrMxd.append(x)

### Delete any existing rows in table on GISDB1 in Inventory user
#arcpy.DeleteRows_management(r"ADD PATH TO SDE CONNECTION FILE/DB TABLE YOU WANT TO WRITE TO HERE")

# Create insert cursor for table
#rows = arcpy.InsertCursor(r"ADD PATH TO SDE CONNECTION FILE/DB TABLE YOU WANT TO WRITE TO HERE")

##for i in arrMxd:
##    arrRecord = [];
##    mxd = arcpy.mapping.MapDocument(i)
##    df = arcpy.mapping.ListDataFrames(mxd)[0]
##
##    arrLyrs=arcpy.mapping.ListLayers(mxd, "", df)
##
##    print i

##    for x in range(len(arrLyrs)):
##
##        try:
##            ## These are all arcgis layer properties (built-in)
##            lyrName=arrLyrs[x].name
##            ## Added REPLACE because some of the path names had % signs in them. Could not see pattern though...
##            dSource=arrLyrs[x].dataSource.replace(r'%', '')
##            dName=arrLyrs[x].datasetName.replace(r'%', '')
##
##        except:
##            continue
##        ## Then this is not a group layer
##
##
##        ## Try to Insert row into table
##        try:
##            row = rows.newRow()
##            row.setValue("name",ServerName)
##            row.setValue("datasource", dSource)
##            row.setValue("layername", lyrName)
##            row.setValue("mxd", i)
##            row.setValue("table_name",dName)
##            rows.insertRow(row)
####              print x
##
##            del row
##        except:
##            arcpy.AddWarning("Error inserting row: " + dName )
# Delete cursor and row objects to remove locks on the data
del rows



