from logging import raiseExceptions
import subprocess
import os
import time

from path_holder import path_holder


def run_mcnp(file_name,flag):
    PATH_INPUT,PATH_OUTPUT,PATH_MCNP  = path_holder()
    # set path for input / output file 

    print()
    os.chdir(PATH_MCNP)
    
    # extention 1: .i 2: .ip
    if flag == 1:
        ext = ".i"
    elif flag == 2:
        ext = ".ip"
    else:
        raise Exception("Choose the extention 1: .i 2: .ip")
        exit(1)
        
    # run MCNP6  
    # mcnp6.exe i={path_input} o={path_output}        
    subprocess.run(["mcnp6.exe", f"i={PATH_INPUT}{file_name}{ext}", f"o={PATH_OUTPUT}{file_name}/{file_name}.o"])
    subprocess.run(["mcnp6.exe", f"i={PATH_INPUT}{file_name}{ext}", f"o={PATH_OUTPUT}{file_name}/{file_name}_exN.o"])

    print("mcnp FINISH")


    

