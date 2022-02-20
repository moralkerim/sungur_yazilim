# Import DroneKit-Python
from dronekit import connect, VehicleMode

# Connect to the Vehicle.

vehicle = connect('127.0.0.1:14550', wait_ready=True)

# Get some vehicle attributes (state)
print "Get some vehicle attribute values:"
print " GPS: %s" % vehicle.location.global_relative_frame

# Close vehicle object before exiting script
vehicle.close()

# Shut down simulator

print("Completed")
