from __future__ import print_function

from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import time
import math
from pymavlink import mavutil
import numpy as np
import random

point_1 = [-35.36103886, 149.16196021]
point_2 = [-35.36526068, 149.16843215]
precision = 100

def get_distance_metres(aLocation1, aLocation2):
    """
    Returns the ground distance in metres between two LocationGlobal objects.
    This method is an approximation, and will not be accurate over large distances and close to the 
    earth's poles. It comes from the ArduPilot test code: 
    https://github.com/diydrones/ardupilot/blob/master/Tools/autotest/common.py
    """
    dlat = aLocation2.lat - aLocation1.lat
    dlong = aLocation2.lon - aLocation1.lon
    return math.sqrt((dlat*dlat) + (dlong*dlong)) * 1.113195e5


def generate_random_area():
    #Enlem noktalari arasinda rastgele bir nokta olustur.
    x_array = np.linspace(point_1[0],point_2[0],num=precision)
    #Boylam noktalari arasinda rastgele bir nokta olustur.
    y_array = np.linspace(point_1[1],point_2[1],num=precision)
    x_coord = random.choice(x_array)
    y_coord = random.choice(y_array)
    return LocationGlobal(x_coord,y_coord,100)


def check_area(vehicle, area_loc):
    #Platform ile arac arasindaki mesafeyi kontrol et.
    dx = get_distance_metres(vehicle.location.global_frame,area_loc)
    print(dx)

    if(dx < 30.0):
        return True

    else:
        return False

