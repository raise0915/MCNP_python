
def makefile_exN(PATHINPUT,file_name):
    with open(f'{PATHINPUT}{file_name}_exN.i','w') as o:
        with open(f'{PATHINPUT}{file_name}.i','r+') as f:
            lines = f.readlines()
            lines_strip = [line.strip() for line in lines ]
            flag = False
            
            for i,line in enumerate(lines_strip):
                if "material card" in line:
                    flag = True
                
                if flag and "$N" in line:
                    lines_strip[i] = f'c {lines_strip[i]}'
            
            l = "\n".join(lines_strip)
            o.write(l)


