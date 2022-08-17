from path_holder import path_holder

import numpy as np
from mcnp_run import mcnp_run
from make_result import make_result
import numpy as np
import time
from make_elements import add_elements

PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()
file_name = "square_cf06"
area = np.pi*(10**2)

def main(file_name):
    t1 = time.time()
    add_elements(file_name,0.5,5,0.01)
    
    # mcnp_run 
    mcnp_run(file_name)
    mcnp_run(f'{file_name}_exN')
    
    # 第4因数を1にするとcsvが出力される
    result = make_result(PATH_INPUT,f"{PATH_OUTPUT}{file_name}/",file_name,area,1)
    
    t2 = time.time()
    print((t2-t1)/60) #分


if __name__ =='__main__':
    main("square_temp")
    
    