## Grib Downloader

This tool can be used to download the daily latest grib data from the [NOMADS-NOAA](https://nomads.ncep.noaa.gov) Operational Model Archive and Distribution System.


### Features
You can download the following data

- GFS
  - Pressure
  - Temperature
  - Wind


### Docker Build
```
Development
docker build -f Dockerfile.remote -t grib-downloader-dev .

Production
docker build -t grib-downloader .
```

### Remote development 
```
Windows
docker run -it --name dev-grib -v "C:\Projects\grib-downloader":/app grib-downloader-dev

Linux
docker run -it --name dev-grib -v "$(pwd)"/target:/app grib-downloader-dev

# install dependencies
root@e276c0662796: pip3 install -r requirements.txt
$python3 app.py
```

### Run Docker Production

```
docker run -d grib-downloader
```


In the output folder (default: /tmp/grib/)

### Output:
```
/tmp/grib/(wind,pressure,temp)
  - 20220202 (date)
    - 12 (run 0,6,12,18)
      - gfs.f000.grb2
      - gfs.f003.grb2
      - gfs.f006.grb2
      - gfs.f012.grb2
      - gfs.f015.grb2
      - gfs.f018.grb2
      - gfs.f021.grb2
      - gfs.f024.grb2
```

```
Update Started...
Checking For Updates
hour >=12 and hour <18
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f000&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f003&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f006&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f009&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f012&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f015&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f018&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f021&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
200
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f000.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   400k      0 --:--:--  0:00:02 --:--:--  400k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f003.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   406k      0 --:--:--  0:00:02 --:--:--  406k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f006.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   421k      0 --:--:--  0:00:01 --:--:--  421k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f009.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   410k      0 --:--:--  0:00:01 --:--:--  410k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f012.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   418k      0 --:--:--  0:00:01 --:--:--  418k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f015.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   427k      0 --:--:--  0:00:01 --:--:--  427k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f018.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   404k      0 --:--:--  0:00:02 --:--:--  404k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f021.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   433k      0 --:--:--  0:00:01 --:--:--  433k
/home/geoserver/app/downloads/pressure/20220716/18/gfs.f024.grb2
https://nomads.ncep.noaa.gov/cgi-bin/filter_gfs_0p25.pl?file=gfs.t12z.pgrb2.0p25.f024&lev_80_m_above_ground=on&var_PRES=on&leftlon=0&rightlon=360&toplat=90&bottomlat=-90&dir=%2Fgfs.20220716/12/atmos
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  817k    0  817k    0     0   406k      0 --:--:--  0:00:02 --:--:--  406k

Checking For Updates
hour >=12 and hour <18
Total Files on run 12 = 9
files already downloaded
```


### Tools

You can use the [IDV](https://downloads.unidata.ucar.edu/idv/), Integrated Data Viewer (IDV) from Unidata to visualize the grib files