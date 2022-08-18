from CF_list import cf_list
from path_holder import path_holder
PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()

def add_beam(file_name,cf,rad,E,o):
    cf_val = list(map(str,cf_list(cf).split("\n")))
    with open(f'{PATH_INPUT}{file_name}.i','r+') as f:
        lines = f.readlines()
        lines_strip = [line.strip("\n") for line in lines ]
        flag = False
        
        for i,line in enumerate(lines_strip):
            if "source properties" in line:
                flag = True
            
            if flag and "C/F ratio" in line:
                for j,strings in enumerate(cf_val):
                    lines_strip.insert(i+1+j,strings)
            if flag and "@rad@" in line:
                lines_strip[i] = line.replace("@rad@",str(rad))
            if flag and "@energy@" in line:
                lines_strip[i] = line.replace("@energy@",str(E))
        
        o.write("\n".join(lines_strip))
 
 
def add_elements(file_name,cf,rad,E):
    save_file = f'{file_name}_cf{cf}_rad{rad}_e{E}'
    if "temp" in save_file:
        save_file = save_file.replace("_temp","")  
    with open(f'{PATH_INPUT}{save_file}.i','w') as o:
        add_beam(file_name,cf,rad,E,o)

    return save_file


        
