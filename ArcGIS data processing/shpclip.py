import arcpy

z_shp = "D:\TREESLab\TREES\S-A-T\dataset1\sea_level\NEUS"
arcpy.env.workspace = z_shp
shps = arcpy.ListFiles("*.shp")
output_shp = "D:\TREESLab\TREES\S-A-T\dataset1\sea_level\Patagonian"
archi_shp = "D:\TREESLab\TREES\S-A-T\dataset1\currents\Patagonian.shp"
for shp in shps:
    catchment_name = shp[:-1]
    # 输出文件名称
    out_feature_class = output_shp + catchment_name
    # 调用ArcGIS操作
    arcpy.Clip_analysis(shp, archi_shp, out_feature_class, "")
    print "finished"
