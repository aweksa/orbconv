from subprocess import call
import os


base_path = "/home/wooyeah/Documents/DSS"
orbit_path = base_path + "/orbit9"
conv_path = base_path + "/conv9"
output_path = base_path + "/4"
yark = False
yark_roc = 0.001
asteroids = ("20215", "661346", "15543", "11111", "55555", "12576")


output = []
with open("header.txt") as f:
    header = f.read().splitlines()
    
with open("options.txt") as f:
    options = f.read().splitlines()
    
for el in header:
    output.append(el)

output.append(f'nvz= {len(asteroids)} ; no. Lyapounov exponents')
for el in asteroids:
    output.append(el)
   
if(yark):
    options[-2] = "iyark=3; Yarkovsky effect as secular drift in a 0=no 3=yes 1,2=not in use"
    with open("yarkovsky.dat", "w") as f:
        f.write(f'{len(asteroids)} {yark_roc}')
    call(["mv", "yarkovsky.dat", orbit_path])
    
for el in options:
    output.append(el)
    
with open("orb9.opt", 'w') as f:
    for el in output:
        f.write(el + '\n')

call(["mv", "orb9.opt", orbit_path])    
    
os.chdir(orbit_path)
call([orbit_path + "/orbit9"])
call(["mv", orbit_path + "/vast.fil", conv_path])
call(["mv", orbit_path + "/vpla.fil", conv_path])
os.chdir(conv_path)
call([conv_path + "/conv9<conv9.inp"], shell = True)

for el in asteroids:
    call(["mv", output_path, f"v{el}.fil"])

