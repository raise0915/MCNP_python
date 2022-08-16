import subprocess
import time
import os
import multiprocessing
import time

path = r"C:\Users\yuri1\Documents\MCNP"
def mcnp_run(path):
    # set path for input / output file 

    t1 = time.time()

    print()
    os.chdir(path)

    # シミュレーション用のMCNPファイル内に入っていればファイル名のみ、それ以外であれば絶対パスを指定する
    file_name = r"04-07-2021_Light.ip"
    #file_name = r"square"
    # run MCNP6
    subprocess.run(["mcnp6.exe", f"i=INPUT/{file_name}", f"o=OUTPUT/{file_name}.o"])
    # mcnp6.exe i=INPUT/square.i o=OUTPUT/square.o

    t2 = time.time()
    print((t2-t1)/60) #分

""""""
if __name__ == '__main__':
    s = multiprocessing.Process(mcnp_run(path))
    s.start()