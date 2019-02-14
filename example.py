


import struct
fn = 'QPESUMS_18071515_q01_18071516.dat'
binary = open(fn,'rb').read()
acsii = struct.unpack('247401h',binary[170:])
