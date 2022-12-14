from path_holder import path_holder

import numpy as np
import os
import time
import itertools

from make_result import make_result
from run_mcnp import run_mcnp
from add_elements import add_elements
from makefile_exN import makefile_exN

# This is for deep-seated cancer protocol system on BNCT

area = np.pi*(10**2) # whole brain area estimated the brain
cf = [0.5,0.6,0.7,0.8,0.9] # current flux
rad = [5,10,15,20] #[cm] - beam diameter
E = [0.0005,0.001,0.01,0.1,1] # [MeV] -> beam energy 0.5,1,10,100,1000 keV
elements = list(itertools.product(rad,cf,E))
PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()

# ----------template file
filename = "square_temp"
# ----------
    
def main():

    for rad,cf,E in elements:
        print("==========SET CONDITION==========")
        
        print("Condition")
        print(f"CF : {cf}")
        print(f"Beam Radius : {rad}")
        print(f"Beam Energy : {E}")
        
        print("==========START SIMULATION==========")

        
        t1 = time.time()
                    
        # Version: MCNP run for Deep seated Protocol  
        # add information - cf:Current/Flux ratio, rad:beam radius, E:beam energy
        file_name = add_elements(filename,cf,rad,E)
        
        # make file - exclude Nitrogen
        makefile_exN(PATH_INPUT,file_name)
        
        # make dir
        if not os.path.exists(f'{PATH_OUTPUT}{file_name}'):
            os.mkdir(f'{PATH_OUTPUT}{file_name}') 
        else:
            continue
            
        # mcnp_run     
        run_mcnp(file_name,1)
        
        try:
            make_result(PATH_INPUT,f'{PATH_OUTPUT}{file_name}/',file_name,area,cf,1)
            
        except:
            pass
        
        if os.path.exists(PATH_MCNP+"/runtpe"):
            os.remove(PATH_MCNP+"/runtpe")
        
        t2 = time.time()
        print(f"TIME : {(t2-t1)/60} min") #分
        print("==========END SIMULATION==========")
        


if __name__ =='__main__':
    main()
    
            