import struct
import numpy as np
fn = 'testdata.dat'
binary = open(fn,'rb').read()

#檔頭所占長度為170，170之後的資料都是QPE的網格數值。
#用len(binary[170:])會得到494802，因為有441*561=247401個網格，一個網格的數值是使用2個字元儲存。
ascii = struct.unpack('247401h',binary[170:]) # h代表一次用2個字元讀2進位數值，請參考https://docs.python.org/3/library/struct.html。

#讀出來的檔案為tuple，所以轉成array
ascii_arr = np.asarray(ascii)

#要轉成2維資料，這邊就交給你們了，到底是(441,561)還是(561,441)
#ascii_reshape = ascii_arr.reshape(441,561)
#ascii_reshape = ascii_arr.reshape(561,441)
