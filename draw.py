import struct
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import cm

fn = '/the/path to your/file' #ex: windows- D:\QPSUMS\QPESUMS_18082323_q01_18082400.dat or linux- /home/john/datapool/PESUMS_18082323_q01_18082400.dat
source = open(fn,'rb').read() 
source_data = struct.unpack('247401h',source[170:])
data_resh = np.asarray(source_data).reshape(561,441)

x_lim = 118 + 440*0.0125
y_lim = 27 - 560*0.0125
xi = np.linspace(118, x_lim, 441)
yi = np.linspace(y_lim, 27, 561)
Xi, Yi = np.meshgrid(xi, yi)

plt.figure(figsize=(8,12))
#plt.contourf(Xi, Yi, data_Trasform,levels=[0,1,2,6,10,15,20,30,40,50,60,70,90,110,130,150,200,300],cmap=cm.s3pcpn)
plt.contourf(Xi, Yi, data_Trasform,levels=[0,1,2,6,10,15,20,30,40,50,60,70,90,110,130,150,200,300],cmap='YlGnBu')
plt.colorbar()
plt.show()
