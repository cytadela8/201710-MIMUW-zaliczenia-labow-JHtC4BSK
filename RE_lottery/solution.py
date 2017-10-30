#!/usr/bin/env python2

from pwn import *
from github_f5x_not_random.rebuild_random import * 
from contextlib import closing
import gzip

print "Loading Magic"
with closing(gzip.GzipFile("github_f5x_not_random/magic_data")) as f:
    magic = pickle.load(f)
print "Done."

need_bytes = max(len(d) for d in magic)

targ = process("./lottery")

data_len = need_bytes
data = ""

for i in range(data_len):
    targ.writeline("grp")
    targ.readuntil("0x")
    char = targ.read()
    data += chr(int(char,16))

my_random = rebuild_random(magic, data)
expected_string = random_string(16, my_random)

test = ""
for i in range(16):
    targ.writeline("grp")
    targ.readuntil("0x")
    char = targ.read()
    test += chr(int(char,16))

print test.encode('hex')
print expected_string.encode('hex')
print test==expected_string



