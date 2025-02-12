# Matti - A QGIS plugin for estimating soybean maturity
Soybean maturity is an important trait but manual phenotyping is time-consuming and error prone. Matti is unique among other comparable solutions in that it provides maturity estimates on an ongoing basis as plots mature by tracking the average green leaf index (GLI) of each plot during the senescence period. Regression models are used to monitor the senescence curve and provide maturity estimates when GLI values are near or below a user-specified threshold. Maturity estimates are added directly to the attribute table associated with the experiment/field shapefile. A summary graph will be displayed indicating the proportion of plots in each experiment rated as mature. This feature helps breeders better plan for note taking and harvest logistics.

<p align="center">
<img src="https://github.com/user-attachments/assets/12861b64-9390-4487-bba8-2d72e4b03f75" height="300">
  
  <em>Plugin icon created with BioRender.com</em>
</p>

## Citation
*Pending publication*

## Installation
Matti requires the Python package [piecewise-regression](https://github.com/chasmani/piecewise-regression). To install, navigate to *Plugins > Python Console* and type the following commands:
```
import pip
pip.main(['install','piecewise-regression'])
```
Matti itself available on the QGIS plugin repository. Navigate to ```Plugins > Manage and Install Plugins... > All``` and search for ```Matti``` 

## Tutorial

### Maturity rating types

*By Date:* Maturity estimates expressed as a date and days after a specified date (day zero). Typically used for advanced yield trials when a precise maturity estimate is desired.

*By Date Block:* Maturity estimates expressed as groupings of dates after a specified date. This is used when a lower resolution of maturity ratings is desired, for example with early generation materials.

### When to fly

Flights should capture the change in greenness during senescence of plots. For best results, begin flights no later than when the earliest maturing plots begin senescing. For By Date ratings, fly every 2-3 days. For By Date Block, fly at least once per week.

### Workflow
1. Create a shapefile for the experiment(s) of interest. Shapefiles for common serpentine plot layouts can be quickly generated with [SHP Buddy](https://github.com/nburner96/shp_buddy). For soybean fields, it is recommended to generate a field orthomosaic prior to full canopy coverage to ease shapefile alignment. Multiple shapefiles within the same field can be merged by going to ```Vector > Data Management Tools > Merge Vector Layers...```. Save to a ```.shp``` file. Select input layers and click ```Run```. 
2. Load orthomosaic from most recent flight date into QGIS project
3. Open Matti




