# Matti
Matti is a QGIS plugin that provides an intuitive method for providing same day estimates of soybean maturity in breeding programs. Matti tracks the average green leaf index (GLI) of each plot during the senescence period. Regression models are used to monitor the senescence curve and provide maturity estimates when GLI values are near or below a user-specified threshold. Maturity estimates are added directly to the attribute table associated with the experiment/field shapefile. A summary graph will be displayed indicating the proportion of plots in each experiment rated as mature. This feature helps breeders better plan for note taking and harvest logistics.

## Citation
Plugin icon created with BioRender.com

# Installation
Matti requires the Python package [piecewise-regression](https://github.com/chasmani/piecewise-regression). To install, navigate to *Plugins > Python Console* and type the folloiwng commands:
```
import pip
pip.main(['install','piecewise-regression'])
```
Matti itself available on the QGIS plugin repository. Navigate to *Plugins > Manage and Install Plugins... > All* and search for ```Matti``` 



