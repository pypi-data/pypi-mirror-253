
'''
This script takes in a directory of spec0 and spec1 folders 

Outputs a table matching the files 

Output build on spec1, find a spec0 file for every spec1 file, 


'''

import os
import pandas as pd
import numpy as np

# input: a directory, folder name starts with
# output: a pandas DF with file directory and date time 

def extract_jazDate(my_dir,folder_name_start):
    
    # list all directories 
    my_folders = os.listdir(my_dir) 
    
    # find the module of interest, usually just one 
    my_folders_filtered = [folder for folder in my_folders if folder.startswith(folder_name_start)]
    my_folders_filtered.sort()
    
    # data frame for output 
    results  = []
    
    # for every folder
    for folder in my_folders_filtered:
        
        print("reading folder: " + folder)
    
        my_folder_dir = os.path.join(my_dir,folder)
        
        # all jaz files under the folder 
        jazes = os.listdir(my_folder_dir) 
        
        try:
            jazes.remove('.DS_Store')
        except:
            pass
        
        jazes.sort()
        
        # for every jaz
        for jaz in jazes:
            
            jaz_path = os.path.join(my_dir, folder, jaz)
            
            df = pd.read_csv(jaz_path).iloc[:,0]
                
            my_metadata = df[0:20].reset_index(drop=True)
            my_metadata=my_metadata.str.split(": ",expand=True)
            
            # 现在选了前20行所以肯定包括了Date，这个可以用来extract spectral data in the future 
            # data_firstRow=my_metadata.iloc[:,0][my_metadata.iloc[:,0]== '>>>>>Begin Spectral Data<<<<<'].index.tolist()
            
            my_metadata.columns = ['Data','Value']
            my_date=my_metadata[my_metadata.Data=="Date"].Value.values[0]#.split(' ')
            
            results.append({folder_name_start+'file': jaz_path, 
                             folder_name_start+'date': my_date})
            
    df_output = pd.DataFrame(results)
    return df_output


def match_time(my_dir,append_metadata):
    '''
    append_metadata: add empty columns for me to fill out their relationship for calibration purposes 

    '''

    # spec0 spec1
    spec0 = extract_jazDate(my_dir,'spec0')
    spec1 = extract_jazDate(my_dir,'spec1')
    
    # match the files according to the date and time 
    spec0_date = pd.to_datetime(spec0.spec0date).to_numpy()
    spec1_date = pd.to_datetime(spec1.spec1date).to_numpy()
    
    # for every spec1, find the closest spec0
    indices_closest = [np.argmin(np.abs(x - spec0_date)) for x in spec1_date]
    
    spec0_reindex = spec0.iloc[indices_closest].reset_index(drop=True) 
    
    # main df, built on spec1
    spec = spec1
    
    # add the two columns from reindexed spec0
    spec['spec0file']=spec0_reindex['spec0file']
    spec['spec0date']=spec0_reindex['spec0date']
    
    if append_metadata:
        spec['Int_time']= None
        spec['Reflectance']= None
        spec['Others']= None
    
    
    
    
    
    return spec



if __name__ == '__main__':

    # mac 
    my_dir = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz'
        
    
    #my_dir = '/Users/Daniel/Desktop/200616 Fieldwork/Data/200819/jaz'
    
    
    my_dir = '/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/jaz'
    
    
    
    # windows 
    #my_dir= r'C:\Users\ywu146\Desktop\Jaz'
    
    time_matching = match_time(my_dir,append_metadata=False)
    
    
    time_matching.to_csv('matched.csv',index=False)





























