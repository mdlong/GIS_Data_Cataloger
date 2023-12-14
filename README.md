# GIS Data Cataloger
The GIS Data Cataloger is a Python script designed for cataloging and documenting Geographic Information System (GIS) data within a specified workspace. This tool is built using the ArcPy library, providing a comprehensive inventory of GIS datasets.

## Key Features:
Data Exploration: Traverses through GIS workspaces using arcpy.da.Walk.

File Information Retrieval: Gathers details like file size, creation time, modification time, and last access time using os and datetime modules.

Feature Counting: Attempts to count features in geodatabase feature classes using arcpy.GetCount_management.

Data Categorization: Classifies GIS data types (e.g., shapefile, feature class, raster dataset) and extracts metadata using arcpy.Describe.

CSV Output: Organizes information systematically and exports to a CSV file for easy review and sharing.

Error Handling: Gracefully manages potential issues such as missing files or inaccessible geodatabase feature classes.

Skip List: Allows exclusion of specific files or directories from the cataloging process using a skip list.

Logging: Provides detailed logs for progress monitoring and issue identification.

## Usage:
Clone the repository.
Set the workspace and configure any skip lists.
Run the script to generate a detailed catalog in CSV format.
This tool is ideal for GIS professionals and data managers seeking an automated and systematic approach to cataloging spatial datasets. It streamlines data organization, facilitating subsequent analysis and decision-making within a GIS environment.
 
