import matplotlib.pyplot as plt
import numpy as np
import servermanager.info as info
import time
import pkg_resources

cpu_ypoints = np.zeros(60)
cpu_xpoints = np.zeros(60)
cpu_xpoints[:] = np.nan
cpu_xpoints[0] = 0

memory_ypoints = np.zeros(60)
memory_xpoints = np.zeros(60)
memory_xpoints[:] = np.nan
memory_xpoints[0] = 0

swap_ypoints = np.zeros(60)
swap_xpoints = np.zeros(60)
swap_xpoints[:] = np.nan
swap_xpoints[0] = 0


def cpu_usage(path):
    COLOR = 'white'
    plt.rcParams['text.color'] = COLOR
    plt.rcParams['axes.labelcolor'] = COLOR


    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    ifn = info.system_dynamic()
    cpu_xpoints[1:] = cpu_xpoints[:-1] + 1
    cpu_ypoints[1:] = cpu_ypoints[:-1]
    cpu_ypoints[0] = ifn.cpu_usage

    swap_xpoints[1:] = swap_xpoints[:-1] + 1
    swap_ypoints[1:] = swap_ypoints[:-1]
    swap_ypoints[0] = ifn.used_swap_percent

    plt.cla()
    ax = plt.gca()
    ax.set_ylim([-1, 101])
    ax.set_xlim([60, 0])

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white') 
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.grid(True)

    plt.plot(cpu_xpoints, cpu_ypoints, color='#FF0000', label = "CPU %")
    plt.legend(labelcolor='black')
    plt.title("Usage %", loc = 'left')
    plt.xlabel("time s", loc = 'right')

    plt.savefig(path, transparent = True)

def memory_usage(path):
    COLOR = 'white'
    plt.rcParams['text.color'] = COLOR
    plt.rcParams['axes.labelcolor'] = COLOR

    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True

    ifn = info.system_dynamic()
    memory_xpoints[1:] = memory_xpoints[:-1] + 1
    memory_ypoints[1:] = memory_ypoints[:-1]
    memory_ypoints[0] = ifn.used_memory_percent

    plt.cla()
    ax = plt.gca()
    ax.set_ylim([-1, 101])
    ax.set_xlim([60, 0])

    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')

    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.grid(True)

    plt.plot(memory_xpoints, memory_ypoints, color='#FF0000', label = "Memory %")
    plt.plot(swap_xpoints, swap_ypoints, color='green', label = "Swap %")
    plt.legend(labelcolor='black')
    plt.title("Usage %", loc = 'left')
    plt.xlabel("time s", loc = 'right')

    plt.savefig(path, transparent = True)


def always_gen():
    cpupath = pkg_resources.resource_filename(__name__, 'graphs/cpu_usage_1.svg')
    mempath = pkg_resources.resource_filename(__name__, 'graphs/memory_usage_1.svg')

    while True:
        cpu_usage(cpupath)
        memory_usage(mempath)
        time.sleep(1)


#always_gen()