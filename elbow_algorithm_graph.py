from matplotlib import pyplot as plt
import numpy as np
def line_graph(errors):
    #fig = plt.figure(figsize = (8, 5)) cái nì công dụng giống
    figure,axis = plt.subplots(figsize = (10,5))
    #x_axes = np.arange(len(subjects))
    K = [1,2,3,4,5,6,7,8,9,10]

    # creating the line graph
    plt.plot(K,errors, color ='r',marker='o')

    limit = 0
    if (limit !=0):
        axis.set_ylim (0,limit)
    plt.grid(True)
    plt.xlabel("K")
    plt.ylabel("Errors")
    plt.title("ELBOW ALGORITHM")

    plt.show()