import numpy as np
#=============================================================================================
# 2) Background removal
#==============================================================================================

class BackgroundRemoval:

    def __init__(self,signal_raw):

        self.data = np.copy(signal_raw)

    def background_removal_row(self):
        #initialization:
        data = self.data
        #=======================================================
        # main
        #========================================================
         
        num_rows = data.shape[0]   
        mean_column = np.mean(data,axis=1)        
        mean = mean_column.reshape(num_rows,1)
        new_data = data-mean

        return  new_data
    
    def background_removal_column(self):
        #initialization:
        data = self.data
        #=======================================================
        # main
        #========================================================         
          
        mean_rows = np.mean(data,axis=0)        
        new_data = data-mean_rows

        return  new_data
    