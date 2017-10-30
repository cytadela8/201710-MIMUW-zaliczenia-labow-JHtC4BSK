import socket
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.SocketType.settimeout(s, 10.0)
socket.SocketType.connect(s, ('jhtc4bsk.jhtc.pl', 31337))
s.send(b'H\n')
sleep(1)
data = s.recv(1024).decode()
print (data)
a = int(data.split("\n")[0])
b = int(data.split("\n")[1])
c = int(data.split("\n")[2])
d = int(data.split("\n")[3])
def operacja2(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        za, zc, zb = operacja2(b % a, a)
        return (za, zb - b // a * zc, zc)


def operacja(a, m):
    za, zb, zc = operacja2(a, m)
    if za != 1:
        raise Exception('This shouldnt happen...')
    else:
        return zb % m
A = 1007012107
B = 179426549
C = 1500450271
hostek = 'jhtc4bsk.jhtc.pl'
D = 31337
E = 450
F = 29
G = 130
w_ab = b ^ a ^ operacja(c, A)
w_cd = c ^ d ^ operacja(b, B)
s.send((str(min(w_ab, w_cd)) + '\n').encode())
s.send((str(max(w_ab, w_cd)) + '\n').encode())
print (s.recv(1024))
kod = w_ab ^ w_cd ^ B
for i in range(1000):
    msg = operacja(i + 2, C) ^ kod
    s.send('R'.encode())
    s.send(('C ' + str(msg) + "\n").encode())
    sleep(0.01)
    dat = s.recv(1024).decode()
    dat = dat.replace("0", ".")
    dat = dat.replace("1", "#")
    print (dat[::-1], end="")

