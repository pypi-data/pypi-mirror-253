# Go up by 2 directory and import 

import sys
import os.path as path
two_up =  path.abspath(path.join(__file__ ,"../.."))
sys.path.append(two_up)

import YW_jaz
import matplotlib.pyplot as plt


### 必须 Step by step... 不能 run all 




jaz_dir = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz'

test = YW_jaz.get_calibration(jaz_dir)








# file = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz/spec1_0000/SPECTRUM0000.jaz'
# module = 1


# test1,test2 = YW_jaz.read_jaz(file, module)







# # Irradiance 
# file0 = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz/spec0_0000/SPECTRUM0000.jaz'
# # Radiance 
# file1 = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz/spec1_0000/SPECTRUM0000.jaz'

# wave, Rrs = YW_jaz.calc_ratio(file0,file1)

# plt.scatter(wave, Rrs)
# plt.ylim(0,1)
# plt.xlim(350,1000)
# plt.show()

