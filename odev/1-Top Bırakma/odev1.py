from library import *
from dronekit import connect, VehicleMode
import time

print("Araca baglaniyor...")
#Araca baglanma komutu
vehicle = connect('127.0.0.1:14550', wait_ready=True)
print("Araca baglandi.")

#rastgele platform konumu uret.
area_loc = generate_random_area()
print(area_loc)

while True:
    #platform tespit edildi mi, kontrol et.
    ball_detected = check_area(vehicle,area_loc)



