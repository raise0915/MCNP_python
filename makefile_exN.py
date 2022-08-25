
def makefile_exN(PATH_INPUT,file_name):
    with open(f'{PATH_INPUT}{file_name}_exN.i','w') as o:
        with open(f'{PATH_INPUT}{file_name}.i','r+') as f:
            lines = f.readlines()
            lines_strip = [line.strip("\n") for line in lines ]
            flag = False
            
            for i,line in enumerate(lines_strip):
                if "material card" in line:
                    flag = True
                
                if flag and "$N" in line:
                    print(lines_strip[i])
                    lines_strip[i] = f'c {lines_strip[i]}'
            
            l = "\n".join(lines_strip)
            o.write(l)


def makefile_exN_D2O(PATHINPUT,file_name):
    with open(f'{PATHINPUT}{file_name}_exN.ip','w') as o:
        with open(f'{PATHINPUT}{file_name}.ip','r+') as f:
            lines = f.readlines()
            lines_strip = [line.strip("\n") for line in lines ]
            flag = False
            
            for i,line in enumerate(lines_strip):
                if " DATA CARDS" in line:
                    flag = True
                
                if flag and "7014.60C -0.013280" in line:
                    lines_strip[i] = f'c {lines_strip[i]}'
            
            l = "\n".join(lines_strip)
            o.write(l)
