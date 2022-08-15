from matplotlib import pyplot as plt

def check_location(PATH_INPUT,file_name):
    flag = False
    location = []
    with open(PATH_INPUT+file_name+'.i', "r+") as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        for i,line in enumerate(lines_strip):
            if line == "c Test check cells":
                flag = True
                continue
            if flag and "s" in line:
                a = list(map(str,lines_strip[i].split()))
                if a[1] == "sx":
                    x = float(a[2])
                    y = 0
                else:
                    x = float(a[2])
                    y = float(a[3])
                    
                location.append([x,y])
            if flag and "c" in line:
                flag = False
                
    return location

inp = r"C:\Users\yuri1\Documents\MCNP\INPUT/"
file = "square"
print(check_location(inp,file))
                    
                    
                    
                
    