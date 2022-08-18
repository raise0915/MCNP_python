from path_holder import path_holder
PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()

def change_rate_d2o(file_name,rate):
    save_file = f'{file_name}_h{rate}'
    with open(f'{PATH_INPUT}{save_file}.ip','w') as o:
        with open(f'{PATH_INPUT}{file_name}.ip','r+') as f:
            lines = f.readlines()
            lines_strip = [line.strip("\n") for line in lines ]
            flag = False
            
            for i,line in enumerate(lines_strip):
                if "M13" in line:
                    flag = True
                
                if flag and "1002.60C" in line:
                    lines_strip[i] = f'     1002.60C -{0.66667*rate} 8016.60C -{0.33333*rate}'
                    break 
        
        o.write("\n".join(lines_strip))
    return save_file

