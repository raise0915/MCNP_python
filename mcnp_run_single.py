import subprocess
import time
import os
import multiprocessing
import time

from path_holder import path_holder

def mcnp_run(file_name):
    PATH_INPUT,PATH_OUTPUT,PATH_MCNP  = path_holder()
    # set path for input / output file 

    t1 = time.time()

    print()
    os.chdir(PATH_MCNP)
    # file_name = r"04-07-2021_Light.ip"
    # run MCNP6
    if not os.path.exists(PATH_OUTPUT+file_name):
        os.mkdir(PATH_OUTPUT+file_name)
        
    # run mcnp 
    # ex:  mcnp6.exe i=INPUT/square.i o=OUTPUT/square.o
    if ".ip" in file_name:
        file_name = file_name.replace(".ip","")
        subprocess.run(["mcnp6.exe", f"i={PATH_INPUT}{file_name}.ip", f"o={PATH_OUTPUT}{file_name}/{file_name}.o"])
    else:    
        subprocess.run(["mcnp6.exe", f"i={PATH_INPUT}{file_name}.i", f"o={PATH_OUTPUT}{file_name}/{file_name}.o"])
    
    # remove runtpe
    if os.path.exists(PATH_MCNP+"/runtpe"):
        os.remove(PATH_MCNP+"/runtpe")
        
    t2 = time.time()
    print((t2-t1)/60) #分
    

if __name__ == '__main__':
    file_name = r"04-07-2021_Light_h20.ip"
    file_name = r"square_cf0.7_rad10_e0.01_exN"
    # mcnp_run(path,file_name)
    mcnp_run(file_name)