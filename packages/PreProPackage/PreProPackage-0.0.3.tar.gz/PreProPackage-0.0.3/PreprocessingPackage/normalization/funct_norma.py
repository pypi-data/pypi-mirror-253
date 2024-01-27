import numpy as np

def normalization (signal_raw):        
    #initialization:
    data = signal_raw

    #=====================================================
    # main
    #=====================================================
    maximum = np.max(data)
    minimum = abs(np.min(data))

    if maximum>= minimum:
        new_data = data/maximum
    else:
        new_data = data/minimum

    return new_data

def normalization_min_max(signal_raw,lower,upper ):

    #initialization:
    data = signal_raw
    limit_lower = lower
    limit_upper = upper 
    
    #=====================================================
    # main
    #=====================================================        

    #feature: 
    minimum = np.min(data)
    maximum = np.max(data)
    
    #equation:
    new_data = limit_lower + ((data - minimum)*(limit_upper-limit_lower))/(maximum-minimum)       


    return new_data
