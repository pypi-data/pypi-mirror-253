from matplotlib import pyplot as plt
from ..simulationParameters import SimulationParameters
from ..Types import T1_COLORMAP, T2_COLORMAP, T1_COLORMAP_MIN, T1_COLORMAP_MAX, T2_COLORMAP_MIN, T2_COLORMAP_MAX
from ..Types import WHITE_MATTER_3T, GREY_MATTER_3T, CSF_3T, FAT_3T, MUSCLE_3T
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable

def PlotSimulationTimeseries(simulation:SimulationParameters, tissuesToPlot=[], tissueLabelsToPlot=[]):

    if (len(tissuesToPlot) != len(tissueLabelsToPlot)):
        print("Length of tissues and tissue labels must match")
        return

    if(len(tissuesToPlot)==0):
        tissuesToPlot=[WHITE_MATTER_3T, GREY_MATTER_3T, CSF_3T, FAT_3T, MUSCLE_3T]
        tissueLabelsToPlot=["White Matter", "Grey Matter", "CSF", "Fat", "Muscle"]
    
    tissuesIndicesToPlot = []
    for tissue in tissuesToPlot:
        index, entry = simulation.dictionaryParameters.GetNearestEntry(tissue['T1'], tissue['T2'])
        tissuesIndicesToPlot.append(index)

    # Plot the timecourses in time domain and readout domain
    plt.figure(figsize=(20,10))
    plt.subplot(211);plt.plot(simulation.times, np.abs(simulation.timeDomainResults[:,tissuesIndicesToPlot]))
    plt.legend(tissueLabelsToPlot, loc='upper right'); 
    plt.title('Magnetization vs Time (s)')
    plt.subplot(212);plt.plot(np.abs(simulation.results[:,tissuesIndicesToPlot]))
    plt.legend(tissueLabelsToPlot, loc='upper right'); 
    plt.title('Magnetization vs Readout')

    # Plot the inner product differences of the tissues of interest
    plt.figure()
    innerProductMatrix = SimulationParameters.GetInnerProducts(simulation.results[:,tissuesIndicesToPlot], simulation.results[:,tissuesIndicesToPlot])
    fig, ax = plt.subplots()
    divider = make_axes_locatable(ax)
    cax = divider.append_axes('right', size='5%', pad=0.05)
    im = ax.imshow(np.abs(innerProductMatrix)**10, 'gray')
    ax.set_xticks(np.arange(-1,len(tissueLabelsToPlot)))
    ax.set_xticklabels([""]+tissueLabelsToPlot,rotation='vertical')
    ax.xaxis.tick_top()
    ax.set_xlim(-0.5,len(tissueLabelsToPlot)-0.5)
    ax.set_yticks(np.arange(-1,len(tissueLabelsToPlot)))
    ax.set_yticklabels([""]+tissueLabelsToPlot)
    ax.set_ylim(len(tissueLabelsToPlot)-0.5, -0.5)

    fig.colorbar(im, cax=cax, orientation='vertical')
    plt.show()


def DisplayMRFSlice(input, slice, showM0=False):
    plt.figure(dpi=200)
    if(showM0):
        plt.subplot(131); plt.imshow(np.abs(input.data[:,:,slice]['T1']), cmap=T1_COLORMAP, vmin=T1_COLORMAP_MIN, vmax=T1_COLORMAP_MAX); plt.axis('off')
        plt.subplot(132); plt.imshow(np.abs(input.data[:,:,slice]['T2']), cmap=T2_COLORMAP, vmin=T2_COLORMAP_MIN, vmax=T2_COLORMAP_MAX); plt.axis('off')
        plt.subplot(133); plt.imshow(np.nan_to_num(input.data[:,:,slice]['M0']), cmap='gray', vmin=0, vmax=0.000001); plt.axis('off')
    else:
        plt.subplot(121); plt.imshow(np.abs(input.data[:,:,slice]['T1']), cmap=T1_COLORMAP, vmin=T1_COLORMAP_MIN, vmax=T1_COLORMAP_MAX); plt.axis('off')
        plt.subplot(122); plt.imshow(np.abs(input.data[:,:,slice]['T2']), cmap=T2_COLORMAP, vmin=T2_COLORMAP_MIN, vmax=T2_COLORMAP_MAX); plt.axis('off')
