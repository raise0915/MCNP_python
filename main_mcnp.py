from path_holder import path_holder

import numpy as np
import os
import multiprocessing
import time

from make_result import make_result
from run_mcnp import run_mcnp
from add_elements import add_elements
from makefile_exN import makefile_exN, makefile_exN_D2O

filename = "square_temp"
area = np.pi*(10**2)

cf = 0.7
rad = 10 #[cm]
E = 0.01 # [MeV]

def main():
    PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
    t1 = time.time()
    
    # Version :D2O
    if ".ip" in file_name:  # type: ignore
        file_name = file_name.replace(".ip","")  # type: ignore
        makefile_exN_D2O(file_name)  # type: ignore
        flag = 2
                
    # Version: Deep seated Protocol
    else:    
        # add information - cf:Current/Flux ratio, rad:beam rad, E:beam energy
        file_name = add_elements(filename,cf,rad,E)
        # make file - exclude Nitrogenvc   in brain
        makefile_exN(PATH_INPUT,file_name)
        flag = 1
    
    # make dir
    if not os.path.exists(f'{PATH_OUTPUT}{file_name}'):
        os.mkdir(f'{PATH_OUTPUT}{file_name}') 
         
    # mcnp_run     
    run_mcnp(file_name,flag)
    
    if flag == 1:     
        # 第4因数を1にするとcsvが出力される
        result = make_result(PATH_INPUT,PATH_OUTPUT,file_name,area,1)
    else:
        result = make_result(PATH_INPUT,PATH_OUTPUT,file_name,area,1)
    
    if os.path.exists(PATH_MCNP+"/runtpe"):
        os.remove(PATH_MCNP+"/runtpe")
    
    t2 = time.time()
    print((t2-t1)/60) #分


if __name__ =='__main__':
    main()
    
    