import matplotlib.pyplot as plt
import numpy as np
import info
import time

x = [1]
y = []

def cpu_usage(path, x, y):
    COLOR = 'white'
    plt.rcParams['text.color'] = COLOR
    plt.rcParams['axes.labelcolor'] = COLOR


    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    ifn = info.system_dynamic()

    y.insert(0, ifn.cpu_usage)
    x.append(x[len(x) -1] + 1)
    
    print(y)
    xpoints = np.array(x)
    ypoints = np.array(y)
    

    

    ax = plt.gca()
    ax.set_ylim([0, 100])
    ax.set_xlim([60, 0])

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')

    plt.plot(xpoints, ypoints, color='#FF0000')
    plt.title("Usage %", loc = 'left')
    plt.xlabel("time s", loc = 'right')

    plt.savefig(path, transparent = True)

def always_gen():
    for j in range(60):
        cpu_usage("./graphs/cpu_usage_1.svg", x, y)
        time.sleep(1)


always_gen()