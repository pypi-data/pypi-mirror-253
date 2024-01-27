from hydronet import wmm

modem = wmm.wmm(10, bufsize=100, port=52001)
modem.send(0)
data = modem.recv()
print(data)