
'''
This script takes in Jaz files at path 0 and path 1
returns the wavelength of file 0, and 


'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# takes in a file path, bands_matching file, and module number
# returns metadata and spectral data

def read_jaz(file,module,bands_matching='bands_matching.csv'):
    
    # Module 0: return as is 
    # Module 1: return the rows matching module 0

    # read and convert to series 
    df = pd.read_csv(file).iloc[:,0]
    
    try:
        data_firstRow =df[df== '>>>>>Begin Spectral Data<<<<<'].index.tolist()[0] + 1
    except:
        data_firstRow =df[df== '>>>>>Begin Processed Spectral Data<<<<<'].index.tolist()[0] + 2
        
    my_metadata = df[1:data_firstRow].reset_index(drop=True)
    my_metadata=my_metadata.str.split(": ",expand=True)
    my_metadata.columns = ['Data','Value']
    
    my_spec = df[data_firstRow:-1].reset_index(drop=True)
    
    my_spec = my_spec.str.split("\t",expand=True)
    my_spec.columns = ['W','S'] # wavelength and spectral intensity? 
    

    if module ==0:
        pass

    # if module is 1, then match its bands with module 0 
    elif module == 1:
        # A list of bands in spec1 that match bands in spec0
        
        path_bands_matching = os.path.join(os.path.dirname(__file__), bands_matching)
        
        bands_matching = pd.read_csv(path_bands_matching).index_m1_matching.tolist()
        
        # Matching bands of spec 1 with spec 0
        my_spec = my_spec.iloc[bands_matching].reset_index(drop=True)
        
    else:
        print('Module can only be 0 or 1')
        exit(1)
    
    return my_metadata, my_spec



    
    
    
    



