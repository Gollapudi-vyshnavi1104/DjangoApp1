
import geopandas as gpd

shppath = "/Users/gollapudi.vyshnavi/Downloads/Point_4888_UID_2/point_4888_UID_2.shp"

gdf = gpd.read_file(shppath)

df1 = gdf[['SyncID', 'FeatureNam','FeatureSta','UniqueID','RouteID','RouteName','RouteCla','MaintCnt','Division']]

print(df1.head(5))

import psycopg2


import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="1234",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="ShapeDB")
    cursor = connection.cursor()

    for i in range(10):
        postgres_insert_query= """ INSERT INTO  myapp_asset(asset_id, asset_name, asset_stat,segment_id,route_id,route_name,route_class,county_id,division_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

        record_to_insert = (str(df1.SyncID[i]), str(df1.FeatureNam[i]), str(df1.FeatureSta[i]),str(df1.UniqueID[i]),str(df1.RouteID[i]),str(df1.RouteName[i]),str(df1.RouteCla[i]),str(df1.MaintCnt[i]),str(df1.Division[i]))
        cursor.execute(postgres_insert_query, record_to_insert)

    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

