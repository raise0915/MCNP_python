from path_holder import path_holder

import numpy as np
import os
import time
import itertools

from make_result import make_result
from run_mcnp import run_mcnp
from add_elements import add_elements
from makefile_exN import makefile_exN

area = np.pi*(10**2)



def main():
    cf = [0.5,0.6,0.7,0.8,0.9]
    rad = [5,10,15,20] #[cm]
    E = [0.0005,0.001,0.01,0.1,1] # [MeV] -> 0.5,1,10,100,1000 keV
    elements = list(itertools.product(rad,cf,E))
    print(elements) 
    filename = "square_temp"
    PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
    
    

    for rad,cf,E in elements:
        if cf == 0.5 and E == 0.01 and rad == 5:
            continue
        print(cf,rad,E)
        
        t1 = time.time()
                    
        # Version: Deep seated Protocol  
        # add information - cf:Current/Flux ratio, rad:beam rad, E:beam energy
        file_name = add_elements(filename,cf,rad,E)
        # make file - exclude Nitrogenvc   in brain
        makefile_exN(PATH_INPUT,file_name)
        
        # make dir
        if not os.path.exists(f'{PATH_OUTPUT}{file_name}'):
            os.mkdir(f'{PATH_OUTPUT}{file_name}') 
            
        # mcnp_run     
        run_mcnp(file_name,1)
        
        try:
            result = make_result(PATH_INPUT,f'{PATH_OUTPUT}{file_name}/',file_name,area,cf,1)
        except:
            pass
        
        if os.path.exists(PATH_MCNP+"/runtpe"):
            os.remove(PATH_MCNP+"/runtpe")
        
        t2 = time.time()
        print((t2-t1)/60) #分


if __name__ =='__main__':
    main()
    
    