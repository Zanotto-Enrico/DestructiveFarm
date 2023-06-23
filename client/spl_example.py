#!/usr/bin/env python3

import random
import string
import sys
import requests
import json
from pwn import *

host = sys.argv[1]
print("I need to attack a team with host: {}".format(host))

# Server supplying the flag's ids
server = 'http://10.10.0.1:8081/flagIds'


# requesting flags ids 
response = requests.get(server)
data = response.json();
    
# for every host the APIs returns 5 ids 
# (runnin 5 exploit on the same host)
for i in range(5):
    data2 = json.loads(data['TiCCket'][host][i])
    print(data2)
    var1 = data2['var1 name']
    var2 = data2['var2 name']
    #       ...      ...



    r = remote(host, 1337)
    r.sendafter(b"> ", b"1\n")
    #       ...      ...
    



    print(r.recv(), flush=True)

