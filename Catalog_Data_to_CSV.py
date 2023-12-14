import os
import arcpy
import time
import datetime
import csv

# Set up the path and the writer to the CSV file
csvfile = r"F:\Repositories\gis_data_cataloger\gis_data.csv"
# csvfile = r"F:\Repositories\gis_data_cataloger\g_production_data.csv"

# Set the path of the data to ba scanned
workspace = r"Z:\GIS_Stuff\GIS_Data"
# workspace = r"G:\Production"

def get_file_info(path):
    info = os.stat(path)
    size = info.st_size
    created = datetime.datetime.strptime(time.ctime(os.path.getctime(path)), "%a %b %d %H:%M:%S %Y")
    modified = datetime.datetime.strptime(time.ctime(os.path.getmtime(path)), "%a %b %d %H:%M:%S %Y")
    accessed = datetime.datetime.strptime(time.ctime(os.path.getatime(path)), "%a %b %d %H:%M:%S %Y")
    return size, created, modified, accessed

def get_feature_count(path, nocountlist):
    if path in nocountlist:
        return ""
    try:
        print("Counting features...")
        return arcpy.GetCount_management(path).getOutput(0)
    except arcpy.ExecuteError as e:
        print(f"Error counting features for {path}: {e}")
        return "-1"

def process_file(x, skiplist, writer):
    if x in skiplist or os.path.normpath(x) in skiplist:
        return

    if arcpy.Exists(x):
        try:
            desc = arcpy.Describe(x)
            name = getattr(desc, "name", "")
            path = getattr(desc, "catalogPath", "")
            ext = getattr(desc, "extension", "")
            datatype = getattr(desc, "dataType", "")

            if datatype in ["ShapeFile", "DbaseTable", "TextFile"]:
                fileinfo = get_file_info(path)
                count = get_feature_count(path, nocountlist)
                data_writer(name, path, ext, datatype, count, size=fileinfo[0], created=fileinfo[1],
                            modified=fileinfo[2], accessed=fileinfo[3], writer=writer)

            # Handle other cases similarly...

        except arcpy.ExecuteError as e:
            print(f"Error processing file {x}: {e}")

def data_writer(name, path, ext, datatype, count="", created="", modified="", accessed="", size="", writer=None):
    print("Writing " + name + "...")
    writer.writerow({'name': name, 'path': path, 'extension': ext, 'created': created, 'modified': modified,
                     'accessed': accessed, 'size': size, 'datatype': datatype, 'count': count})

skiplist = [r"Z:\GIS_Stuff\GIS_Data\Austin\Austin.gdb\Transportation\ND_151_Connectors_Stops2Streets_SAI"]
nocountlist = []

with open(csvfile, "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'path', 'extension', 'datatype', 'count',
                                              'created', 'modified', 'accessed', 'size'])
    writer.writeheader()

    for dirpath, dirnames, filenames in arcpy.da.Walk(workspace, datatype="Any", type="All", onerror=None):
        for filename in filenames:
            x = os.path.join(dirpath, filename)
            print("Processing", os.path.normpath(x), "...")
            process_file(x, skiplist, writer)
            print("-------------------")
