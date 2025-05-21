import os
import glob
import arcpy
import numpy as np
from arcpy.sa import *
arcpy.CheckOutExtension("ImageAnalyst")
arcpy.CheckOutExtension("spatial")
inws = r"D:\TREESLab\TREES\S-A-T\dataset1\temperature\Mexico_Gulf_clip"
OutputFile = open('Mexico_MEAN.csv', 'w')
rasters = glob.glob(os.path.join(inws, "*.tif"))
whereClause = "VALUE = 0"
for ras in rasters:
    array = arcpy.RasterToNumPyArray(ras)
    array[np.isnan(array)] = -100
    if np.max(array) <= -100:
        continue
    outSetNull = SetNull(ras, ras, whereClause)
    meanValueInfo = arcpy.GetRasterProperties_management(outSetNull, 'MEAN')
    meanValue = meanValueInfo.getOutput(0)
    print os.path.basename(ras).split('_')[0] + ',' + str(meanValue) + '\n'
    OutputFile.write(os.path.basename(ras).split('_')[0] + ',' + str(meanValue) + '\n')
OutputFile.close()
print("All project is OK£¡")
