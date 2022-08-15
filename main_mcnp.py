import numpy as np
from make_output import make_output
from calc_dose import dose_boron,dose_neutron,dose_nitro,dose_gamma
from mcnp_run import mcnp_run
from path_holder import path_holder
import multiprocessing
import numpy as np
import pandas as pd

PATH_OUTPUT,file_name,PATH_MCNP = path_holder()
area = np.pi*(10**2)

def main():
    # s = multiprocessing.Process(mcnp_run(PATH_MCNP,file_name))
    # s.start()
    data = make_output(PATH_OUTPUT,file_name)
    print(data)
    print(data["Boron"][2])
    # print(dose_boron(data["Boron"][0],area,1,0.5))
    
    
    
    

if __name__ =='__main__':
    main()
    
    