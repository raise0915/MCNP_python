from matplotlib import pyplot as plt
import seaborn as sns
from path_holder import path_holder

PATH_INPUT,PATH_OUTPUT,PATH_MCNP = path_holder()

def plot_scatter(result,file_name,flag=0):
    r = result.loc[:,"rad"]
    r *= 100
    result["rad"] = r
    sns.set_theme(style="whitegrid")
    g = sns.relplot(
    data=result,
    x="x", y="y",
    hue="Total",palette="mako", sizes="rad")
    g.ax.xaxis.grid(True, "minor", linewidth=.25)
    g.ax.yaxis.grid(True, "minor", linewidth=.25)
    
    
    # flag 1:savefig 2:plot 
    if flag == 2:
        plt.show()
    if flag == 1:
        plt.savefig(f'{PATH_OUTPUT}{file_name}_scatter.png')
        
def plot_line(result,file_name,flag=0):

    result = result.drop(2)
    sns.relplot(x="x", y="Total", kind="line",data=result)

     # flag 1:plot 2:savefig
    if flag == 1:
        plt.show()
    if flag == 2:
        plt.savefig(f'{PATH_OUTPUT}{file_name}_line.png')   
    
# 確率密度変数
# ax = sns.kdeplot(data["Total"],shade=True) 
# plt.show()
