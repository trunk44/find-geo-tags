#!/usr/bin/python3
# -*- coding: utf-8 -*-
# find-geo-tags
# Поиск и вывод на экран GPS геотэгов из изображений в текущей директории.
# 


from PIL import Image
import glob, os
from getch import pause
from GPSPhoto import gpsphoto

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
                data = gpsphoto.getGPSData(file)
                print('in file', file, 'GPS tag was founded: ', data['Latitude'], data['Longitude']) 
            except:
                pass


def main():
    cls()
    print('\n find from exif \n and print GPS tags \n from directory photos \n ')
    pause('Press Any Key To continue')
    search()

main()