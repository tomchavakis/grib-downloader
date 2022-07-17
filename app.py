'''
Editor: Thomas Chavakis
Year: 2022
Tools:
Description: Service of downloading pressure, wind and temperature.
Output folder structure
/tmp/weather/(wind,pressure,temp)
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
'''

import threading
import weather_downloader


def download_pressure(levelOfDetail):
  weather_downloader.download_gfs(levelOfDetail, "PRES", "lev_80_m_above_ground", "/tmp/weather/pressure/")
  threading.Timer(20.0, updateGribFiles, [levelOfDetail]).start()

def download_wind(levelOfDetail):
  weather_downloader.download_gfs(levelOfDetail, "UGRD,VGRD", "lev_10_m_above_ground", "/tmp/weather/wind/")
  threading.Timer(20.0, updateGribFiles, [levelOfDetail]).start()

def download_temperature(levelOfDetail):
  weather_downloader.download_gfs(levelOfDetail, "TMP", "lev_surface", "/tmp/weather/temp/")
  threading.Timer(20.0, updateGribFiles, [levelOfDetail]).start()



def updateGribFiles(levelOfDetail):
  print("Checking For Updates")
  download_pressure(levelOfDetail)
  download_wind(levelOfDetail)
  download_temperature(levelOfDetail)


print ("Update Started...")
# level of detail p25 --> 0.25 Degree, p1 --> 1 Degree
updateGribFiles('p25')