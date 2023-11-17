from subprocess import call
import os
#call(["ls", "-l"])
base_path = "/home/wooyeah/Documents/DSS"
orbit_path = base_path + "/orbit9"
conv_path = base_path + "/conv9"
os.chdir(orbit_path)
#asteroids = ("20215", "661346", "15543")
call([orbit_path + "/orbit9"])
call(["mv", orbit_path + "/vast.fil", conv_path])
call(["mv", orbit_path + "/vpla.fil", conv_path])
os.chdir(conv_path)
call([conv_path + "/conv9<conv9.inp"], shell = True)