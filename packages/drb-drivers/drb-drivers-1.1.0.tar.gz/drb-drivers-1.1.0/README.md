# drivers

# DRB Drivers
**_drb-drivers_** is a Python plugin for **DRB**, to help the installations
of drb drivers.

## Installation
```shell
pip install drb-drivers[OPTIONAL]
```

## Driver
Here the list of all the drivers downloadable with this project.

| name      | category   | package              |
|:----------|:-----------|:---------------------|
| java      | NONE       | drb-driver-java      |
| grib      | FORMATTING | drb-driver-grib      |
| zarr      | FORMATTING | drb-driver-zarr      |
| yaml      | FORMATTING | drb-driver-yaml      |
| json      | FORMATTING | drb-driver-json      |
| netcdf    | FORMATTING | drb-driver-netcdf    |
| litto3d   | FORMATTING | drb-driver-litto3d   |
| image     | FORMATTING | drb-driver-image     |
| csv       | FORMATTING | drb-driver-csv       |
| zip       | CONTAINER  | drb-driver-zip       |
| tar       | CONTAINER  | drb-driver-tar       |
| wxs       | PROTOCOL   | drb-driver-wxs       |
| wcs       | PROTOCOL   | drb-driver-wcs       |
| wmts      | PROTOCOL   | drb-driver-wmts      |
| wms       | PROTOCOL   | drb-driver-wms       |
| webdav    | PROTOCOL   | drb-driver-webdav    |
| odata     | PROTOCOL   | drb-driver-odata     |
| swift     | PROTOCOL   | drb-driver-swift     |
| http      | PROTOCOL   | drb-driver-http      |
| eurostat  | PROTOCOL   | drb-driver-eurostat  |
| era5      | PROTOCOL   | drb-driver-era5      |
| discodata | PROTOCOL   | drb-driver-discodata |
| s3        | PROTOCOL   | drb-driver-s3        |
| ftp       | PROTOCOL   | drb-driver-ftp       |

You can download a driver with his name like:
```shell
pip install drb-drivers[http]
```
to only download the driver http

To download all the formatting drivers:
```shell
pip install drb-drivers[formatting]
```

To download all the drivers:
```shell
pip install drb-drivers[all]
```