import os

from pip._vendor.distlib.compat import raw_input

def checkinput( param , ret ):
    if param == "1" :
        ret += "move_base:=true "

    if param == "2" :
        ret+="gmapping:=true "

    if param == "3" :
        ret+= "lidar:=true "

    return ret

ret=" "
param=" "
while param != "5":
    param = raw_input("What is your param for launch?:\n 1.move_base \n 2. gmapping \n 3. lidar \n 5. exit")
    ret = checkinput( param, ret)

TheCommand = 'roslaunch armadillo2 armadillo2.launch  {}'.format(ret)

#print(TheCommand)
#check if input is correct:

os.system(TheCommand)    #shell command

