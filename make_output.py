import pandas as pd

cell_start = 2
cell_end = 42

def make_output(output_env,file_name,out) -> pd.DataFrame:
    data = pd.DataFrame()
    items = ["Boron","Neutron","Nitrogen","Gamma"] # four pattern -> add them according to 
    cell = [i for i in range(cell_start,cell_end+1)]
    data["cell"] = cell
    count = 0
    res = []
    error = []
    flag = True
    check = False
    with open(output_env+file_name+'.o', "r+") as f:
        lines = f.readlines()
        lines_strip = [line.strip() for line in lines ]
        for i,line in enumerate(lines_strip):
            if "nps =  1000000000" in line:
                check = True
            for j in range(cell_start,cell_end+1):
                if check:
                    if lines_strip[i] == f"cell  {j}":
                        if j == cell_start:
                            if "107" in lines_strip[i+1]:
                                pass
                            elif "103" in lines_strip[i+1]:
                                data[items[count]] = res
                                data[items[count]+str("_error")] = error
                                count += 1
                            else:
                                if flag:
                                    data[items[count]] = res
                                    data[items[count]+str("_error")] = error
                                    count += 1                            
                                    flag = False
                                else:
                                    data[items[count]] = res
                                    data[items[count]+str("_error")] = error
                                    count += 1    
                            res = []
                            error = []                        
                        
                        if "multiplier bin" in lines_strip[i+1]:
                            x,y = map(float,lines_strip[i+2].split())
                        else:
                            x,y = map(float,lines_strip[i+1].split())
                        res.append(x)
                        error.append(y)

        if res:
            data[items[count]] = res
            data[items[count]+str("_error")] = error

    data = data.set_index("cell")
    
    
     # save original_data to csv 
    if out == 1:
        data.to_csv(f"{output_env}{file_name}.csv")
    
    return data
    

    
    
        
    