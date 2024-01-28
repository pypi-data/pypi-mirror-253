



def get_regression(df_all): 

    import pandas as pd
    import numpy as np
    import statsmodels.api as sm
    
    import copy

    # # Read the CSV file
    # df = pd.read_csv("/Users/yw/Desktop/230620 SBA Fieldwork 2023/230622 calibration/all.csv")
    
    df = copy.copy(df_all)
    
    
    # Filter rows where 'Others' is 'Labsphere'
    df = df[df['Others'] == 'Labsphere']
    
    # Normalize reflectance
    df['reflectance'] = df['reflectance'] / 100
    
    # Get unique wavelengths
    unique_WLs = df['wavelength'].unique()
    
    # Initialize output DataFrame
    df_output = pd.DataFrame()
    
    # Loop over each wavelength
    for WL in unique_WLs:
        # Filter DataFrame for the current wavelength
        df_WL = df[df['wavelength'] == WL]
    
        # Check for NA values in R column
        if df_WL['Ratio'].isna().any():
            a = np.nan
            rsquare = np.nan
        else:
            # Perform linear regression
            X = df_WL['reflectance']
            y = df_WL['Ratio']
            X = sm.add_constant(X, prepend=False)
            model = sm.OLS(y, X).fit()
            a = model.params['reflectance']
            rsquare = model.rsquared
    
        # Append results to the output DataFrame
        df_temp = pd.DataFrame({'WL': [WL], 'a': [a], 'rsquare': [rsquare]})
        df_output = pd.concat([df_output, df_temp], ignore_index=True)
    
    
    
    # Write output DataFrame to CSV
    # df_output.to_csv('calibration201023.csv', index=False)

    return df_output










