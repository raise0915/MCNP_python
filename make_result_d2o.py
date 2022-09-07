from find_location import find_location
from calc_dose_d2o import dose_boron,dose_neutron,dose_nitro,dose_gamma
from make_output_d2o import make_output_d2o

import numpy as np
import openpyxl
import pandas as pd
import os

cell_start = 300
cell_end = 340

def make_result_d2o(input_env,output_env,file_name,area,flag,out) :

        # make dir
        if not os.path.exists(output_env):
            os.mkdir(output_env)
        
        # create csv of output
        data = make_output_d2o(output_env,file_name,out)
        data_ex = make_output_d2o(output_env,f'{file_name}_exN',out)
        
        result = []
        # Columns 
        items = ["Boron","Neutron","Nitrogen","Gamma","Total"]
        
        # Obtain locations of cells
        location = find_location(input_env,file_name,2)
        location = location.set_index(data.index)     
        
        for i in range(cell_start,cell_end+1):    
            # Calculate Dose and Combine results
            boron = dose_boron(data["Boron"][i],area,flag,1)
            nitro = dose_nitro(data["Nitrogen"][i],area,1)
            neutron = dose_neutron(data_ex["Neutron"][i],area,1)
            gamma = dose_gamma(data["Gamma"][i],area,1)
            total = boron+nitro+gamma+neutron
            result.append([boron,neutron,nitro,gamma,total])

        # Make DataFrame of the result
        result = pd.DataFrame(result,columns=items,index=data.index)
        result = pd.merge(result,location,left_index=True,right_index=True)
        
        # Write Excel if out == 1
        if out == 1:
            with pd.ExcelWriter(f"{output_env}{file_name}_output.xlsx") as writer:
                data.to_excel(writer, sheet_name='MCNP')
                data_ex.to_excel(writer, sheet_name='MCNP_exN')
                result.to_excel(writer, sheet_name=f'Result')
        
        print(" FINISH ")
        return result

# """test
from path_holder import path_holder
PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
file_name = 'd2o_h0'
area = (0.125**2)*np.pi

# areaのあとflag 1:tumor 2:normal tissue (brain)
make_result_d2o(PATH_INPUT,f'{PATH_OUTPUT}{file_name}/',file_name,1,2,1)
# """

