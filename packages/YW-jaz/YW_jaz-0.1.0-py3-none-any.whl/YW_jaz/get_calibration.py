
### overall control for calibration 


from .match_time import match_time
from .calc_ratio import calc_ratio
from .get_all import get_all
from .get_regression import get_regression

import matplotlib.pyplot as plt
import os
import pandas as pd
import numpy as np


# input: jaz folder with 
# output: calibration file for each wavelength


### Steps: add _filled, and check plots

def get_calibration(jaz_dir, plot = False):
    
    ### Time matching
    time_matching = get_calibration_match_time(jaz_dir)


    ### Manually add int_time, reflectance and others to the output 
    ### Rename it to time_matching_filled.csv

    # add '_filled'
    base, extension = os.path.splitext(time_matching)
    time_matching_filled = base + '_filled' + extension
    
    if not os.path.isfile(time_matching_filled):
        os.exit('Please fill the time matching file and add _filled to the file name')
        
        
    ### Plot the calibration files 
        
    # parent directory 
    jaz_dir_up = os.path.dirname(jaz_dir) 
    dir_plot = os.path.join(jaz_dir_up,'plot')
    
    if not os.path.exists(dir_plot):
        os.makedirs(dir_plot)
        print(f"\nDirectory '{dir_plot}' was created.")


    df_tm = pd.read_csv(time_matching_filled)
    
    
    
    # Plot all pairs
    if plot: 
        for i in range(0,len(df_tm)):
            
            print('Processing: {}'.format(i))
    
            ### metadata
            
            i_int_time = df_tm.Int_time[i]
            i_reflectance = df_tm.Reflectance[i]
            i_others = df_tm.Others[i]
            
            tilte = "{} {} {} {}".format(i, i_int_time, i_reflectance, i_others)
            i_path = os.path.join(dir_plot,str(i) + '.png')
            
            ### files and plot 
            
            file0 = os.path.normpath(df_tm.spec0file[i])
            file1 = os.path.normpath(df_tm.spec1file[i])
            
            wave, ratio = calc_ratio(file0,file1)
            
            ratio_98percentile = np.nanpercentile(ratio,98)
            
            plt.scatter(wave, ratio)
            plt.ylim(0,ratio_98percentile)
            plt.xlim(350,1100)
            plt.title(tilte)
            # plt.show()
            
            plt.savefig(i_path)
            plt.close()
 
        print('\nPlots created in {}'.format(dir_plot))

    # all mean values at each reflectance at each wavelength 
    df_all = get_all(df_tm, jaz_dir_up)
    
    # regression 
    df_regression = get_regression(df_all)



    return df_regression




# match time 
def get_calibration_match_time(jaz_dir):
    
    # match the time 
    df_time_matching = match_time(jaz_dir, append_metadata=True)
    
    # path to export to 
    jaz_dir_up = os.path.dirname(jaz_dir) # parent directory 
    path_time_matching = os.path.join(jaz_dir_up,'time_matching.csv')
    
    # export it 
    df_time_matching.to_csv(path_time_matching,index=False)
    
    print('\nTime matching exported to {}'.format(path_time_matching))
    
    return path_time_matching
    
    
    




































