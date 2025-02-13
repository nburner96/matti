# Matti: A QGIS plugin for estimating soybean maturity
Soybean maturity is an important trait but manual phenotyping is time-consuming and error prone. Matti is unique among other comparable solutions in that it provides maturity estimates on an ongoing basis as plots mature by tracking the average green leaf index (GLI) of each plot during the senescence period. Regression models are used to monitor the senescence curve and provide maturity estimates when GLI values are near or below a user-specified threshold. Maturity estimates are added directly to the attribute table associated with the experiment/field shapefile. A summary graph will be displayed indicating the proportion of plots in each experiment rated as mature. This feature helps breeders better plan for note taking and harvest logistics.

<p align="center">
<img src="https://github.com/user-attachments/assets/12861b64-9390-4487-bba8-2d72e4b03f75" height="300">
  <br>
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

Flights should capture the change in greenness during senescence of plots. For best results, begin flights no later than when the earliest maturing plots begin senescing. For By Date ratings, fly every 2-3 days. For By Date Block, fly at least once per week. The best time to fly is under uniform lighting conditions near solar noon.

### Workflow
1. Create a shapefile for the experiment(s) of interest. Shapefiles for common serpentine plot layouts can be quickly generated with [SHP Buddy](https://github.com/nburner96/shp_buddy). For soybean fields, it is recommended to generate a field orthomosaic prior to full canopy coverage to ease shapefile alignment. Multiple shapefiles within the same field can be merged by going to ```Vector > Data Management Tools > Merge Vector Layers...```. Save to a ```.shp``` file. Select input layers and click ```Run```. It is also recommended to use ground control points to align orthomosaics from different flight dates.

![image](https://github.com/user-attachments/assets/7edcf69c-7f3a-4e39-9a88-61bc83c7fdc7)
<p align="center">
  <em>Field with a shapefile colored by experiment</em>
</p>


3. Load orthomosaic from most recent flight date into QGIS project
4. Open Matti by clicking the icon in the plugins bar

### Matti
![image](https://github.com/user-attachments/assets/c79a861d-674d-4bcc-884f-f2a82b89ce40)
<p align="center">
  <em>Matti dialog with By Date (left) and By Date Block (right) options</em>
</p>

1. Orthomosaic layer. Orthomosaics need to be run through Matti in chronological order.
2. Shapefile layer
3. Path corresponding to CSV file containing GLI timeseries data for each plot. Select file location and name if running for first time, Matti will automatically generate a file. Select file path for subsequent runs.
4. Columns in shapefile attribute table corresponding to Experiment and Plot number. Each plot should have a unique Experiment x Plot number combination.
5. Image date
6. Date from which maturity estimates are expressed relative to. For example, if Aug 31 is specified, a Oct 5 estimated maturity date would be expressed as 35.
7. First date of the first date block in the maturity schedule
8. The days of the week corresponding to the start of new date blocks. ```Skip first break``` will skip the first occurrence of a break. This can be used to avoid date blocks with a small number of days at the beginning of the maturity schedule. This could happen if new date blocks begin on Sundays and Thursdays and the first day specified is on a Wednesday.
9. Length of maturity schedule in months. Should be long enough to encompass at least the typical length of time between the earliest maturing lines beginning to senesce and the latest maturing lines reaching maturity.
10. Preview of maturity schedule based on inputs
11. Default GLI threshold is 0.01. This value doesn't typically need to be changed, but can be if you wish to experiment
12. Various options
    - Last flight: check if it is the last flight of the season. Matti will try as best it can to give maturity estimates to all outstanding plots
    - Record estimate dates: will add a column indicating the image date that resulted in a plot's maturity being estimated
    - Keep GLI raster: check to prevent Matti from automatically deleting GLI raster
    - Summary graph: after running, will display bar chart indicating proportion of plots in each experiment with maturity estimates. Useful for tracking maturity progression throughout breeding program
13. Path to where you want Matti to store temporary files

### Output
After Matti finishes running, right-clicking the shapefile layer in the layers panel and selecting ```Open Attribute Table``` will display the maturity estimates made so far in the season.

<p align="center">
<img src="https://github.com/user-attachments/assets/8da06c69-afe7-4966-832a-a4da4220fdc0">
</p>

