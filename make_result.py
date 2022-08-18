from operator import index
from matplotlib import pyplot as plt
import pandas as pd
from calc_dose import dose_boron,dose_nitro,dose_neutron,dose_gamma
from make_output import make_output
import openpyxl
import seaborn as sns
import numpy as np
from find_location import find_location
from make_output_d2o import make_output_d2o
from plot_result import plot_scatter,plot_line
import os

def make_result(input_env,output_env,file_name,area,cf,out) :
        # make dir
        if not os.path.exists(output_env):
            os.mkdir(output_env)
        
        # create csv of output
        data = make_output(output_env,file_name,out)
        data_ex = make_output(output_env,f'{file_name}_exN',out)
        
        result = []
        # Columns 
        items = ["Boron","Neutron","Nitrogen","Gamma","Total"]
        
        # Obtain locations of cells
        location = find_location(input_env,file_name,1)
        location = location.set_index(data.index)     
        
        for i in range(2,43):
            if i ==2:
                flag = 1
            else:
                flag = 2
            
            # Calculate Dose and Combine results
            boron = dose_boron(data["Boron"][i],area,flag,cf)
            nitro = dose_nitro(data["Nitrogen"][i],area,cf)
            neutron = dose_neutron(data_ex["Neutron"][i],area,cf)
            gamma = dose_gamma(data["Gamma"][i],area,cf)
            total = boron+nitro+neutron+gamma
            result.append([boron,nitro,neutron,gamma,total])

        # Make DataFrame of the result
        result = pd.DataFrame(result,columns=items,index=data.index)
        result = pd.merge(result,location,left_index=True,right_index=True)
        
        # Write Excel if out == 1
        if out == 1:
            with pd.ExcelWriter(f"{output_env}{file_name}_output.xlsx") as writer:
                data.to_excel(writer, sheet_name='MCNP')
                data_ex.to_excel(writer, sheet_name='MCNP_exN')
                result.to_excel(writer, sheet_name=f'Result')
        
        return result
    




