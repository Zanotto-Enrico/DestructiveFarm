#!/usr/bin/env python3

import random
import string
import sys
import requests
import json
from pwn import *
from Crypto.Hash import SHA256
import sys


host = sys.argv[1]
print("I need to attack a team with host: {}".format(host))

service = 'SERVICE NAME'

# Server supplying the flag's ids
server = 'http://10.10.0.1:8081/flagIds?service='+service

# requesting flags ids

response = requests.get(server)
data = response.json();

# for every host the APIs returns 5 ids
# (runnin 5 exploit on the same host)
for i in range(5):
    id = data[service][host][i]
    print(id)
    #       ...      ...


    proc = remote(host, 1234)

    # ...

    proc.write(b""  + b"\n")
    proc.recvuntil(b"\n")

    # ...

    print(proc.recvuntil(b"="), flush=True)
