



    
# get all mean values at each reflectance at each wavelength 
def get_all(df_tm, jaz_dir_up):
    
    
    from .calc_ratio import calc_ratio
    import matplotlib.pyplot as plt
    import os
    
    import numpy as np
    import pandas as pd
    
    
        
    
    df_tm['uid'] = df_tm.Reflectance.astype(str) + df_tm.Others
    
    unique_uid = list(set(df_tm.uid))
    unique_uid.sort()
    
    df_output = pd.DataFrame()
    
    for uid in unique_uid:
        
        tm_temp =  df_tm[df_tm.uid == uid]
        tm_temp.reset_index(drop=True, inplace=True)
        
        # a dataframe of all ratio, 2048 rows, each column is a Rrs duplicate
        df_allDup = np.empty((2048,0))
        
        for i in range(0,len(tm_temp)):
        
            file0 = os.path.normpath(tm_temp.spec0file[i])
            file1 = os.path.normpath(tm_temp.spec1file[i])
            
            wave, ratio = calc_ratio(file0,file1)
            df_allDup = np.column_stack([df_allDup,ratio])
            
        
        # extract info, stack dfs 
        df_output_temp = pd.DataFrame({'reflectance':tm_temp.Reflectance[0],
                                       'wavelength':wave,
                                       'Ratio':df_allDup.mean(axis=1),
                                       'Others':tm_temp.Others[0]})

        df_output = pd.concat([df_output, df_output_temp])
        
        

    path_all = os.path.join(jaz_dir_up,'all.csv')
    
    df_output = df_output.reset_index(drop=True) 
    df_output.to_csv(path_all, index=True)
    
    print('\nAll reflectance values exported to {}'.format(path_all))
    
    return df_output
    







































