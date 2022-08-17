def change_rate_d2o(rate):
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