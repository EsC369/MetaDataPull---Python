'''
This script requires metaDataPull.py, it will take the data Long. & lat. that was written to data.txt file created from
metaDataPull.py, and translates into a readable text

Instructions:
You will have to manually look at the GPSinfo from the data.txt file, and then run the script as below:
Each data list will consist of 3 sets of numbers for example:   First section will be your lat (31, 1) , (14, 1), (3077, 100), second section your long, (121, 1), (29, 1), (984, 100)
you will take the first segment of each set like below:
desired lat/long
 lat = 31, 14, 3077
 long  = 121, 29, 984

command to run script:
translateGPS.py 31,14,3077 121,29,984

Format: 
Run Scriptname,   Latitude,     Longitude   

From there you copy and paste the converted Lat and Long into google and find your location of where the picture was taken!
'''
# //translateGPS.py/
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("lat", help="Latitude values in D,M,S")
parser.add_argument("lon", help="Longitude values in D,M,S")
args = parser.parse_args()

if args.lat and args.lon:
	lat = args.lat.split(',')
	lon = args.lon.split(',')

	dlat = int(lat[0]) + (int(lat[1])/60.0) + (int(lat[2])/3600.0)
	dlon = int(lon[0]) + (int(lon[1])/60.0) + (int(lon[2])/3600.0)

	print(dlat, dlon)

else:
	print(parser.usage)

