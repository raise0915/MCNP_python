from find_location import find_location
from calc_dose_d2o import dose_boron,dose_neutron,dose_nitro,dose_gamma
from make_output_d2o import make_output_d2o

import numpy as np
import openpyxl
import pandas as pd
import os

cell_start = 300
cell_end = 340

def make_result_d2o(input_env,output_env,file_name,area,out) :

        # make dir
        if not os.path.exists(output_env):
            os.mkdir(output_env)
        
        # create csv of output
        data = make_output_d2o(output_env,file_name,out)
        data_ex = make_output_d2o(output_env,f'{file_name}_exN',out)
        
        result_normal = []
        result_tumor = []
        # Columns 
        items = ["Boron","Neutron","Nitrogen","Gamma","Total"]
        
        # Obtain locations of cells
        location = find_location(input_env,file_name,2)
        location = location.set_index(data.index)     
        
        for i in range(cell_start,cell_end+1):    
            # Calculate Dose and Combine results
            boron_tumor = dose_boron(data["Boron"][i],area,1,1)
            boron_normal = dose_boron(data["Boron"][i],area,2,1)
            nitro = dose_nitro(data["Nitrogen"][i],area,1)
            neutron = dose_neutron(data_ex["Neutron"][i],area,1)
            gamma = dose_gamma(data["Gamma"][i],area,1)
            total_normal = boron_normal+nitro+gamma+neutron
            total_tumor = boron_tumor+nitro+gamma+neutron
            result_normal.append([boron_normal,neutron,nitro,gamma,total_normal])
            result_tumor.append([boron_tumor,neutron,nitro,gamma,total_tumor])

        # Make DataFrame of the result
        result_normal = pd.DataFrame(result_normal,columns=items,index=data.index)
        result_normal = pd.merge(result_normal,location,left_index=True,right_index=True)

        result_tumor = pd.DataFrame(result_tumor,columns=items,index=data.index)
        result_tumor = pd.merge(result_tumor,location,left_index=True,right_index=True)
                
        # Write Excel if out == 1
        if out == 1:
            with pd.ExcelWriter(f"{output_env}{file_name}_output.xlsx") as writer:
                data.to_excel(writer, sheet_name='MCNP')
                data_ex.to_excel(writer, sheet_name='MCNP_exN')
                result_normal.to_excel(writer, sheet_name=f'Result_Normal')
                result_tumor.to_excel(writer, sheet_name=f'Result_Tumor')
        
        print(" FINISH ")
        return 0

