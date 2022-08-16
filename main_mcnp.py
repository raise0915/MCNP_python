import numpy as np
from make_output import make_output
from calc_dose import dose_boron,dose_neutron,dose_nitro,dose_gamma
from mcnp_run import mcnp_run
from path_holder import path_holder
import multiprocessing
import numpy as np
import pandas as pd

PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
file_name = "square_1e9"
area = np.pi*(10**2)

def main():
    # s = multiprocessing.Process(mcnp_run(PATH_MCNP,file_name))
    # s.start()
    data = make_output(PATH_OUTPUT,file_name)
    data_ex = make_output(PATH_OUTPUT,f'{file_name}_exN')
    

    for i in range(2,43):
        boron = dose_boron(data["Boron"][i],area,1,0.5)
        nitro = dose_nitro(data["Nitrogen"][i],area,0.5)
        neutron = dose_neutron(data_ex["Neutron"][i],area,0.5)
        gamma = dose_gamma(data["Gamma"][i],area,0.5)
        total = boron+nitro+neutron+gamma
        print(boron,nitro,neutron,gamma,total)

    
    
    

if __name__ =='__main__':
    main()
    
    