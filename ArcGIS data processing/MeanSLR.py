import arcpy
import os
import numpy as np
arcpy.env.workspace = r'D:\TREESLab\TREES\S-A-T\dataset1\sea_level\Patagonian_clip'
OutputFile = open('Patagonian_MEAN_sealevel.csv', 'w')
for i in range(1952, 2017):
    filename = 'D:\TREESLab\TREES\S-A-T\dataset1\sea_level\Patagonian_clip\Patagonian%s_sealevel.shp'%i
    sealevel_value = []
    with arcpy.da.SearchCursor(filename,'mean_seale') as cursor:
        for row in cursor:
            sealevel_value.append(row[0])
    OutputFile.write('%s'%i + ',' + str(np.mean(sealevel_value)) + '\n')
    print i
OutputFile.close()
print("All project is OK")
