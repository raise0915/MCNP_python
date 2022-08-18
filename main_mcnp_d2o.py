from path_holder import path_holder

import numpy as np
import os
import time

from make_result_d2o import make_result_d2o
from run_mcnp import run_mcnp
from makefile_exN import  makefile_exN_D2O
from change_rate_d2o import change_rate_d2o

area = np.pi*(10**2)

rate_list = [0.0,0.1,0.2] # hard water rate
def main():
    PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
    for rate in rate_list:
        filename = "d2o_tset"
        
        t1 = time.time()
        
        # add information - cf:Current/Flux ratio, rad:beam rad, E:beam energy
        file_name = change_rate_d2o(filename,rate)        
        # make file - exclude Nitrogenvc   in brain
        makefile_exN_D2O(PATH_INPUT,file_name)

        
        # make dir
        if not os.path.exists(f'{PATH_OUTPUT}{file_name}'):
            os.mkdir(f'{PATH_OUTPUT}{file_name}') 
            
        # mcnp_run     
        run_mcnp(file_name,2)
        
        try:
            result = make_result_d2o(PATH_INPUT,PATH_OUTPUT,file_name,area,1)
        except:
            pass
        
        # 不要なファイルの削除
        if os.path.exists(PATH_MCNP+"/runtpe"):
            os.remove(PATH_MCNP+"/runtpe")
        
        t2 = time.time()
        print((t2-t1)/60) #分


if __name__ =='__main__':
    main()
    
    