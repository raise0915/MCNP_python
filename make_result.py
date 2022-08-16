import pandas as pd
from calc_dose import dose_boron,dose_nitro,dose_neutron,dose_gamma
from make_output import make_output
import openpyxl

def make_result(output_env,file_name,area,out) :
        data = make_output(output_env,file_name,out)
        data_ex = make_output(output_env,f'{file_name}_exN',out)
        
        result = []
        
        items = ["Boron","Neutron","Nitrogen","Gamma","Total"]
        cells = []
        
        for i in range(2,43):
            boron = dose_boron(data["Boron"][i],area,1,0.5)
            nitro = dose_nitro(data["Nitrogen"][i],area,0.5)
            neutron = dose_neutron(data_ex["Neutron"][i],area,0.5)
            gamma = dose_gamma(data["Gamma"][i],area,0.5)
            total = boron+nitro+neutron+gamma
            result.append([boron,nitro,neutron,gamma,total])
            cells.append(i)
            
        result = pd.DataFrame(result,columns=items,index=cells)
        
        if out == 1:
            with pd.ExcelWriter(f"{output_env}{file_name}_output.xlsx") as writer:
                data.to_excel(writer, sheet_name='MCNP')
                data_ex.to_excel(writer, sheet_name='MCNP_exN')
                result.to_excel(writer, sheet_name=f'Result')
        
        return result