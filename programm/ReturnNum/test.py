# below is a extract from a sample exploit that
# interfaces with a tcp socket
from netcat import Netcat
import re
import time

r = re.compile(r'^[0-9]+$')
# start a new Netcat() instance
nc = Netcat('35.157.111.68', 10145)

def wait(n):
    time.sleep(n)

# get to the prompt
#nc.read_until('>')

while 1:
    if 1==2:
        break

    wait(.5)
    ncString1 = nc.read()
    print(ncString1)
    wait(.5)
    ncString2 = ncString1.decode("utf-8")
   # wait(.5)
    num = re.sub(r'\D', "", ncString2)
    #wait(.5)
    num2 = str.encode(num)
    #wait(.5)
    nc.write(num2)
    print(num2)
    wait(.5)
    nc.read()



'''
filter(r.match, out)
out2 = out.decode("utf-8")
num = re.sub(r'\D', "", out2)

# start a new note
nc.write('num'+'\n')
nc.read_until('>')

# set note 0 with the payload
nc.write('set' + '\n')
nc.read_until('id:')
'''
