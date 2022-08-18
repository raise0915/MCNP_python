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

    # extention 1: .i 2: .ip
    if ".ip" in file_name:
        ext = ".ip"
    else:
        ext = ".i"

    file_name = file_name.replace(".ip","")
    
    if not os.path.exists(PATH_OUTPUT+file_name):
        os.mkdir(PATH_OUTPUT+file_name)
        
    # run mcnp 
    # ex:  mcnp6.exe i=INPUT/square.i o=OUTPUT/square.o
    subprocess.run(["mcnp6.exe", f"i={PATH_INPUT}{file_name}{ext}", f"o={PATH_OUTPUT}{file_name}/{file_name}.o"])
    
    # remove runtpe
    if os.path.exists(PATH_MCNP+"/runtpe"):
        os.remove(PATH_MCNP+"/runtpe")
        
    t2 = time.time()
    print((t2-t1)/60) #分
    

if __name__ == '__main__':
    file_name = r"04-07-2021_Light_h20.ip"
    file_name = r"d2o_tset.ip"
    # mcnp_run(path,file_name)
    mcnp_run(file_name)