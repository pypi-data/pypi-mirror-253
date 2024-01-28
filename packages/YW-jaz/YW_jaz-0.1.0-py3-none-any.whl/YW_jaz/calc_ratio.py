

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

from .read_jaz import *



def calc_ratio(file0,file1):
    
    np.seterr(divide='ignore', invalid='ignore')

    # Bands matching the two spectrometers 
    #file_bm = 'bands_matching.csv'
    
    # A list of bands in spec1 that match bands in spec0
    #bands_matching = pd.read_csv(file_bm).I2_matching_I1.tolist()
    
    bands_matching = 'bands_matching.csv'
    
    my_meta0, my_spec0 = read_jaz(file0,0,bands_matching)
    my_meta1, my_spec1 = read_jaz(file1,1,bands_matching) # radiance should be file 1 
    
    np0 = np.array(my_spec0.S, dtype=np.float32)
    np1 = np.array(my_spec1.S, dtype=np.float32)
    
    wave = np.array(my_spec0.W, dtype=np.float32)
    ratio10 = np1/np0
    
    return wave, ratio10
    



# test a single pair 

if __name__ == '__main__':
    
    # Irradiance 
    file0 = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz/spec0_0000/SPECTRUM0000.jaz'
    # Radiance 
    file1 = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz/spec1_0000/SPECTRUM0000.jaz'

    wave, Rrs = calc_ratio(file0,file1)

    plt.scatter(wave, Rrs)
    plt.ylim(0,1)
    plt.xlim(350,1000)
    plt.show()
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




