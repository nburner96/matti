import fiona
import rasterio
import matplotlib.pyplot as plt
import geopandas as gpd
import rasterstats
from rasterio.plot import show
import rasterio.mask
from osgeo import gdal
import numpy as np
from pprint import pprint
import pandas as pd
import os
import time
import concurrent.futures
from functools import reduce
import glob2


def date_enter():
    date = input('Enter date of orthomosaic (mm-dd-yy): ')

    return(date)


def crop_to_shp(ortho, shp):
    print('\nCropping orthomosaic...')
    with fiona.open(shp, 'r') as shapefile:
        shapes = [feature['geometry'] for feature in shapefile]

    with rasterio.open(ortho) as src:
        out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
        out_meta = src.meta

    out_meta.update({'driver': 'GTiff',
                     'height': out_image.shape[1],
                     'width': out_image.shape[2],
                     'transform': out_transform})

    with rasterio.open('clip.tif', 'w', **out_meta) as dest:
        dest.write(out_image)

# Check that shapefile and raster projections are the same, and optionally plot
def projection(raster, shp, to_show=False):
    shp = gpd.read_file(shp)
    raster = rasterio.open(raster)
    assert raster.crs == shp.crs    # Assert that CRS is same
    print(f'\nRaster and shapefile projections are both {raster.crs}')
    if to_show == True:
        fig, ax = plt.subplots(1,1)
        show(raster, ax = ax, title = raster.crs)
        shp.plot(ax = ax, facecolor = 'None', edgecolor = 'red')
        plt.show()

def zonal_stats(rst, shp, date, output):
    ds = gdal.Open(rst)
    gt = ds.GetGeoTransform()
    proj = ds.GetProjection()

    # Convert shapefile to geopandas dataframe
    data = gpd.read_file(shp)

    # Read bands
    r = ds.GetRasterBand(1).ReadAsArray().astype(np.float32)
    g = ds.GetRasterBand(2).ReadAsArray().astype(np.float32)
    b = ds.GetRasterBand(3).ReadAsArray().astype(np.float32)

    print("Calculating GLI...")
    np.seterr(divide='ignore', invalid='ignore')

    vi_array = np.where(2 * g + r + b != 0, (2 * g - r - b) / (2 * g + r + b), np.nan)

    # Export VI array to GeoTIFF
    print("Exporting GLI orthomosaic...")
    gtiff_export(vi_array, gt, proj, date)

    # Calculate zonal statistics
    print("Calculating mean plot GLI...")
    result = rasterstats.zonal_stats(data, f'{date} GLI.tif', stats='mean', geojson_out=True)

    print("Writing zonal statistics...")
    geostats = gpd.GeoDataFrame.from_features(result, crs=data.crs)

    date_index = geostats.columns.get_loc(
        'geometry') + 1  # Index that the date column wil be added, one column to right of geometry

    geostats.insert(date_index, 'DATE', pd.Series([date for x in range(len(geostats.index))]))

    if os.path.isfile(f"{output}.csv"):
        prev_out = pd.read_csv(f"{output}.csv")

        if not prev_out.columns.equals(geostats.columns):
            raise ValueError("Previous output column names do not match desired output.")
        out = pd.concat([prev_out, geostats])
        out.to_csv(f'{output}.csv', index=False)
    else:
        geostats.to_csv(f'{output}.csv', index=False)


def gtiff_export(vi_array, affine, proj, date):
    driver = gdal.GetDriverByName('GTiff')
    driver.Register()
    outds = driver.Create(f'{date} GLI.tif',
                          xsize=vi_array.shape[1],
                          ysize=vi_array.shape[0],
                          bands=1,
                          eType=gdal.GDT_Float32)
    outds.SetGeoTransform(affine)
    outds.SetProjection(proj)
    outband = outds.GetRasterBand(1)
    outband.WriteArray(vi_array)
    outband.SetNoDataValue(np.nan)
    outband.FlushCache()
    outband = None
    outds = None

def main():
    rst = r"E:\Maturity Drone Images-Nathaniel\2023\2023 Orthomosaics\Area A\10-02-23 Area A_transparent_mosaic_group1.tif"
    shp = r"C:\Users\nb47899\OneDrive - University of Georgia\Documents\#Li Lab\#Projects\Maturity\QGIS Projects\2023 Area A.shp"
    output_name = "2023 Area A - GLI"
    date = date_enter()

    t1 = time.perf_counter()


    projection(rst, shp, False)
    crop_to_shp(rst, shp)
    zonal_stats("clip.tif", shp, date, output_name)

    t2 = time.perf_counter()
    print(f'\nFinished in {round(t2 - t1, 2)} seconds')

if __name__ == '__main__':
    main()