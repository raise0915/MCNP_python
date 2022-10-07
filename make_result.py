from operator import index
from matplotlib import pyplot as plt
import pandas as pd
from calc_dose import dose_boron,dose_nitro,dose_neutron,dose_gamma
from make_output import make_output
import openpyxl
import seaborn as sns
import numpy as np
from find_location import find_location
from plot_result import plot_scatter,plot_line
import os

start_cell = 2
end_cell = 45
def make_result(input_env,output_env,file_name,area,cf,out) :
        # make dir
        
        # create csv of output
        data = make_output(output_env,file_name,out)
        data_ex = make_output(output_env,f'{file_name}_exN',out)
        
        result_normal = []
        result_tumor = []
        # Columns 
        items = ["Boron","Neutron","Nitrogen","Gamma","Total"]
        
        # Obtain locations of cells
        location = find_location(input_env,file_name,1)
        location = location.set_index(data.index)     
        
        for i in range(start_cell,end_cell):
            if i==2:
                flag = 1
            else:
                flag = 2
            
            # Calculate Dose and Combine results
            boron_tumor = dose_boron(data["Boron"][i],area,flag,cf)
            boron_normal = dose_boron(data["Boron"][i],area,flag,cf)
            nitro = dose_nitro(data["Nitrogen"][i],area,cf)
            neutron = dose_neutron(data_ex["Neutron"][i],area,cf)
            gamma = dose_gamma(data["Gamma"][i],area,cf)
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
        
        return 0
    

"""test
from path_holder import path_holder
PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
file_name = 'square_1e9'
data = make_result(PATH_INPUT,f'{PATH_OUTPUT}{file_name}/',file_name,10*10*np.pi,0.5,1)
plot_scatter(data,file_name,1)
"""