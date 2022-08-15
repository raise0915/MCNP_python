
def make_output(output_env,file_name):
    output_env = r"C:\Users\yuri1\Documents\MCNP\OUTPUT/"
    res = []
    flag = True
    with open(output_env+file_name, "r+") as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines ]
        for i,line in enumerate(lines_strip):
            for j in range(2,43):

                if lines_strip[i] == f"cell  {j}":
                    if j==2:
                        res.append(" ")
                        if "107" in lines_strip[i+1]:
                            res.append("Boron")
                        elif "103" in lines_strip[i+1]:
                            res.append("Nitrogen")
                        else:
                            if flag:
                                flag = False
                                res.append("Neutron")
                            else:
                                res.append("Gamma")
                        
                    if "multiplier bin" in lines_strip[i+1]:
                        res.append(lines_strip[i+2])
                    else:
                        res.append(lines_strip[i+1])


    with open(output_env+file_name+str("_dose.txt"), "w") as f:
        for data in res:
            f.write(data+'\n')
    
    return output_env+file_name+str("_dose.txt")

