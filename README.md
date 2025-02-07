# Matti - A QGIS plugin for estimating soybean maturity
Soybean maturity is an important trait but manual phenotyping is time-consuming and error prone. Matti is unique among other comparable solutions in that it provides maturity estimates on an ongoing basis as plots mature by tracking the average green leaf index (GLI) of each plot during the senescence period. Regression models are used to monitor the senescence curve and provide maturity estimates when GLI values are near or below a user-specified threshold. Maturity estimates are added directly to the attribute table associated with the experiment/field shapefile. A summary graph will be displayed indicating the proportion of plots in each experiment rated as mature. This feature helps breeders better plan for note taking and harvest logistics.

## Citation
*Pending publication*

## Installation
Matti requires the Python package [piecewise-regression](https://github.com/chasmani/piecewise-regression). To install, navigate to *Plugins > Python Console* and type the folloiwng commands:
```
import pip
pip.main(['install','piecewise-regression'])
```
Matti itself available on the QGIS plugin repository. Navigate to *Plugins > Manage and Install Plugins... > All* and search for ```Matti``` 

## Tutorial
### Rating Types
Matti allows for two types of maturity ratings:

*By Date:* Maturity estimates expressed as a date and days after a specified date (day zero). Typically used for advanced yield trials when a precise maturity estimate is desired.

*By Date Block:* Maturity estimates expressed as groupings of dates after a specified date. This is used when a lower resolution of maturity ratings is desired, for example with early generation materials.


