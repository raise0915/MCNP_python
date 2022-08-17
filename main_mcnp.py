from path_holder import path_holder
import numpy as np
from make_output import make_output
from mcnp_run import mcnp_run
from make_result import make_result
import multiprocessing
import numpy as np
import pandas as pd

PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
file_name = "square_1e9"
area = np.pi*(10**2)

def main():
    # s = multiprocessing.Process(mcnp_run(PATH_MCNP,file_name))
    # s.start()
    
    # 第4因数を1にするとcsvが出力される
    result = make_result(PATH_INPUT,PATH_OUTPUT,file_name,area,1)



if __name__ =='__main__':
    main()
    
    