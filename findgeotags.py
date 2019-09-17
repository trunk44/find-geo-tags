#!/usr/bin/python3
# -*- coding: utf-8 -*-
# find-geo-tags
# Поиск и вывод на экран GPS геотэгов из изображений в текущей директории.
# 


from PIL import Image
import glob, os
from getch import pause
from GPSPhoto import gpsphoto
#import exifread

dir_path = os.path.dirname(os.path.realpath(__file__))

def cls():
    os.system('clear')
    
def search():
    i = 0
    n = 0

    cls()
    files = glob.glob(dir_path + '/**/*.*', recursive=True)
    print('\n please wait for searching ...\n')
    for file in files:
        if Image: 
            try:
                img = Image.open(file)
                
                # Get the data from image file and return a dictionary
                data = gpsphoto.getGPSData(file)
                print('in file', file, 'GPS tag was founded: ', data['Latitude'], data['Longitude'])
            
#                tags = exifread.process_file(open(file, 'rb'))                                              
#                geo = {i:tags[i] for i in tags.keys() if i.startswith('GPS')}  
#                print('in file', file, 'find GEO ', geo)
                
            except:
                pass


def main():
    cls()
    print('\nfind from exif \nand print GPS tags \nfrom directory photos\n ')
    pause('Press Any Key To continue')
    search()

main()