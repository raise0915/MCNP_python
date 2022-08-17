import subprocess
import os
import time

from path_holder import path_holder


def run_mcnp(file_name):
    PATH_INPUT,PATH_OUTPUT,PATH_MCNP  = path_holder()
    # set path for input / output file 

    print()
    os.chdir(PATH_MCNP)
        
    # run MCNP6  
    # mcnp6.exe i={path_input} o={path_output}        
    run = subprocess.run(["mcnp6.exe", f"i={PATH_INPUT}{file_name}.i", f"o={PATH_OUTPUT}{file_name}/{file_name}.o"])
    run = subprocess.run(["mcnp6.exe", f"i={PATH_INPUT}{file_name}.i", f"o={PATH_OUTPUT}{file_name}/{file_name}_exN.o"])

    print("mcnp FINISH")


    

