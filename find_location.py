import pandas as pd


def find_location(PATH_INPUT,file_name,ver)->pd.DataFrame:
    flag = False
    x_list = []
    y_list = []
    z_list = []
    rad_list = []
    if ver == 1:
        ext = ".i"
    else:
        ext = ".ip"
        
    with open(PATH_INPUT+file_name+ext, "r+") as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines]
        for i,line in enumerate(lines_strip):
            if line == "c Test check cells":
                flag = True
                continue
            if flag and line == "c Test check cells end":
                flag = False
                break
            
            if flag and "s" in line:
                a = list(map(str,lines_strip[i].split()))
                
                if ver == 1:
                    if a[1] == "sx":
                        x = float(a[2])
                        y = 0
                        z = 0
                        rad = float(a[3])
                    else:
                        x = float(a[2])
                        y = float(a[3])
                        z = float(a[4])
                        rad = float(a[5])
                else:
                    if a[2] == "sx":
                        x = float(a[3])
                        y = 0
                        z = 0
                        rad = float(a[4])
                    else:
                        x = float(a[3])
                        y = float(a[4])
                        z = float(a[5])
                        rad = float(a[6])                    
                    
                x_list.append(x)
                y_list.append(y)
                z_list.append(z)
                rad_list.append(rad)

    
    location = pd.DataFrame({'x':x_list,'y':y_list,'z':z_list,'rad':rad_list})
    return location