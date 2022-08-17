from path_holder import path_holder

import numpy as np
from run_mcnp import run_mcnp
import os

from make_result import make_result
import time
from add_elements import add_elements
from makefile_exN import makefile_exN

PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
filename = "square_temp"
area = np.pi*(10**2)

cf = 0.5
rad = 10
E = 0.01

def main():
    t1 = time.time()
    # add information - cf:Current/Flux ratio, rad:beam rad, E:beam energy
    file_name = add_elements(filename,cf,rad,E)
    
    # make file - exclude Nitrogen in brain
    makefile_exN(PATH_INPUT,file_name)
    
    # make dir
    if not os.path.exists(PATH_OUTPUT+file_name):
        os.mkdir(PATH_OUTPUT+file_name)  
          
    # mcnp_run 
    run_mcnp(file_name)
    run_mcnp(f'{file_name}_exN')
    
    # 第4因数を1にするとcsvが出力される
    result = make_result(PATH_INPUT,f"{PATH_OUTPUT}{file_name}/",file_name,area,1)
    
    t2 = time.time()
    print((t2-t1)/60) #分


if __name__ =='__main__':
    main()
    
    