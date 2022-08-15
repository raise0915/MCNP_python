import subprocess
import time
import os
import time


def mcnp_run(path,file_name):
    # set path for input / output file 

    t1 = time.time()

    print()
    os.chdir(path)

    # run MCNP6
    subprocess.run(["mcnp6.exe", f"i=INPUT/{file_name}.i", f"o=OUTPUT/{file_name}_incN_1e9.o"])
    # mcnp6.exe i=INPUT/square.i o=OUTPUT/square.o

    t2 = time.time()
    print((t2-t1)/60) #分

