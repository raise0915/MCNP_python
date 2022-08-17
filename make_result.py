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


def make_result(input_env,output_env,file_name,area,out) :
        data = make_output(output_env,file_name,out)
        data_ex = make_output(output_env,f'{file_name}_exN',out)
        
        result = []
        
        items = ["Boron","Neutron","Nitrogen","Gamma","Total"]
        location = find_location(input_env,file_name)
        location = location.set_index(data.index)     
        
        for i in range(2,43):
            if i ==2:
                flag = 1
            else:
                flag = 2
            
            boron = dose_boron(data["Boron"][i],area,flag,0.5)
            nitro = dose_nitro(data["Nitrogen"][i],area,0.5)
            neutron = dose_neutron(data_ex["Neutron"][i],area,0.5)
            gamma = dose_gamma(data["Gamma"][i],area,0.5)
            total = boron+nitro+neutron+gamma
            result.append([boron,nitro,neutron,gamma,total])
 
        result = pd.DataFrame(result,columns=items,index=data.index)

        result = pd.merge(result,location,left_index=True,right_index=True)
        
        if out == 1:
            with pd.ExcelWriter(f"{output_env}{file_name}_output.xlsx") as writer:
                data.to_excel(writer, sheet_name='MCNP')
                data_ex.to_excel(writer, sheet_name='MCNP_exN')
                result.to_excel(writer, sheet_name=f'Result')
        
        return result
""" 
# test
from path_holder import path_holder
PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
file_name = "square_1e9"
area = np.pi*(10**2)
result = make_result(PATH_INPUT,PATH_OUTPUT,file_name,area,1)

plot_scatter(result,file_name,2)
# plot_line(result,file_name,1)

# data = result[["x","y","Total","rad"]]
""" 



