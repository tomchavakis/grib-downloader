'''
Editor: Thomas Chavakis
Year: 2022
Description: Download the grib files (wind,pressure,temperature) from the nomads NOAA site.
The forecasting runs every 6 hours 
The results of every run uploaded to nomads after 3,4 hours or even more.
'''
from __future__ import print_function
from datetime import datetime
import os
import subprocess
import errno
import requests

filters = ['filter_gfs_1p00.pl?file=', 'filter_gfs_0p25.pl?file=']
pgrb2s = ['z.pgrb2.1p00.f', 'z.pgrb2.0p25.f']
SERVER = "https://nomads.ncep.noaa.gov/cgi-bin/"

# every six hours the model generates new files.
timelist = ['00', '06', '12', '12'] 
DOWNLOADS_PATH = ""
VARIABLES = ""
LEVEL = ""

def createPgrb2(detail):
    if detail == 'p1':
        return pgrb2s[0]
    elif detail == 'p25':
        return pgrb2s[1]


def createServerByDetail(detail):
    if detail == 'p1':
        return SERVER + filters[0]
    elif detail == 'p25':
        return SERVER + filters[1]


def createServerByTime(time, detail):
    if time == 0:
        result = createServerByDetail(detail) + 'gfs.t' + timelist[0] + createPgrb2(detail)
        return result
    elif time == 1:
        result = createServerByDetail(detail) + 'gfs.t' + timelist[1] + createPgrb2(detail)
        return result
    elif time == 2:
        result = createServerByDetail(detail) + 'gfs.t' + timelist[2] + createPgrb2(detail)
        return result
    elif time == 3:
        result = createServerByDetail(detail) + 'gfs.t' + timelist[3] + createPgrb2(detail)
        return result


def fileExistInServer(url, hour, run):
    url_final = url + '{:03d}'.format(hour)
    result = create_url(url_final) + '/' + timelist[run] + '/atmos'
    print(result, end="\n")
    r = requests.get(result, stream=True)
    return r.status_code, result


def fileIsDownloaded(run):
    dateString = createDateFolder()
    datefolder = DOWNLOADS_PATH + dateString + '/' + str(run) + '/'
    if os.path.exists(os.path.dirname(datefolder)):
        path, dirs, files = next(os.walk(os.path.dirname(datefolder)))
        if len(files) == 9:
            print('Total Files on run ' + str(run) + ' = ' + str(len(files)))
            return True
        else:
            print('Total Files on run ' + str(run) + ' = ' + str(len(files)))
            return False
    else:
        return False

def check_and_download(hour, time, detail):
    print(f'hour >={hour} and hour < {hour + 6}', end="\n")
    if fileIsDownloaded(hour):
        print('files already downloaded', end="\n")
        return
    SERVER_URL = createServerByTime(time, detail)
    counter = 0
    for i in range(0, 25, 3):
        exist = fileExistInServer(SERVER_URL, i, time)
        print(exist[0], end="\n")
        if exist[0] == 404:
            break
        if exist[0] == 200:
            counter += 1
    if counter == 9:
        for i in range(0, 25, 3):
            download_file(exist[1], hour, i)    

def download_gfs(detail, variables, level, output):
    now = datetime.utcnow()
    global DOWNLOADS_PATH
    DOWNLOADS_PATH = output
    
    global VARIABLES
    VARIABLES = variables

    global LEVEL
    LEVEL = level

    if 0 <= now.hour < 6:
        check_and_download(0,0, detail)
    elif 6 <= now.hour < 12:
        check_and_download(6,1, detail)
    elif 12 <= now.hour < 18:
        check_and_download(12,2,detail)
    elif 18 <= now.hour < 24:
        check_and_download(18,3,detail)


def download_file(url, run, hour):
    dateString = createDateFolder()
    datefolder = DOWNLOADS_PATH + dateString + '/' + str(run) + '/'
    filename = 'gfs.f' + '{:03d}'.format(hour) + '.grb2'
    local_filename = datefolder + filename
    print(local_filename)
    r = requests.get(url, stream=True)
    if not os.path.exists(os.path.dirname(datefolder)):
        try:
            os.makedirs(os.path.dirname(datefolder))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    wrongTime = 'gfs.t' + '{:02d}'.format(run) + 'z.pgrb2.0p25.f024'
    filetoreplace = 'gfs.t' + '{:02d}'.format(run) + 'z.pgrb2.0p25.f' + '{:03d}'.format(hour)
    url = url.replace(wrongTime, filetoreplace)
    print(url)
    wgetcmd = "curl -o " + local_filename + " -L '" + url + "'"
    subprocess.call(wgetcmd, shell=True)
    return local_filename


def createDateFolder():
    u = datetime.utcnow()
    dateString = str(u.year) + '{:02d}'.format(u.month) + '{:02d}'.format(u.day)
    return dateString

def create_url(SERVER_URL):
    url = SERVER_URL + '&' + LEVEL + '=on'
    variables = VARIABLES.split(',')
    for item in variables:
        url = url + '&var_' + item + '=on'
    url = url + '&leftlon=0&rightlon=360&toplat=90&bottomlat=-90'
    dateString = createDateFolder()
    url = url + '&dir=%2Fgfs.' + dateString
    return url
