from path_holder import path_holder

import numpy as np
import os
import time

from make_result_d2o import make_result_d2o
from run_mcnp import run_mcnp
from makefile_exN import  makefile_exN_D2O
from change_rate_d2o import change_rate_d2o

rate_list = [0.0,0.1,0.2] # hard water rate
def main():
    PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
    for rate in rate_list:
        # template
        filename= "d2o_temp"
        
        t1 = time.time()
        
        # add information - cf:Current/Flux ratio, rad:beam rad, E:beam energy
        file_name = change_rate_d2o(filename,rate)        
        # make file - exclude Nitrogen in brain
        makefile_exN_D2O(PATH_INPUT,file_name)

        
        # make dir
        if not os.path.exists(f'{PATH_OUTPUT}{file_name}'):
            os.mkdir(f'{PATH_OUTPUT}{file_name}') 
            
        # mcnp_run - d2o version
        run_mcnp(file_name,2)
        
        try:
            make_result_d2o(PATH_INPUT,f'{PATH_OUTPUT}{file_name}/',file_name,1,1)
        except:
            pass
        
        # 不要なファイルの削除
        try:
            os.remove(PATH_MCNP+"/runtpe")
        except:
            pass
        
        try:
            os.remove(PATH_MCNP+"/runtpf")
        except:
            pass
        
        t2 = time.time()
        print((t2-t1)/60) # minitues


if __name__ =='__main__':
    main()
    
    