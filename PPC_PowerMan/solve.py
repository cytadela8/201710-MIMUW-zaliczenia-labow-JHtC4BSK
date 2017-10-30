#!/usr/bin/env python2

from pwn import *
import time

targ = remote('jhtc4bsk.jhtc.pl',42100)

time.sleep(0.5)
i=0
for i in range(120):
    #print (targ.readline())
    targ.readuntil("a =")
    a = int(targ.readuntil("\n"))
    targ.readuntil("b =")
    b = int(targ.readuntil("\n"))
    targ.readuntil("m =")
    m = int(targ.readuntil("\n"))
    i+=1
    print i,
    targ.writeline(str(pow(a,b,m)))
print targ.read()
targ.interactive()
