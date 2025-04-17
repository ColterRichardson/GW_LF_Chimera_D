#######################################################################
# Gravitational Wave Memory from Chimera's D-Series Logistic Analysis
#######################################################################
#######################################################################
## House Keeping
#######################################################################
#######################################################################
### Math, Science, and Computing Modules
#######################################################################
import numpy as np
#######################################################################
### Plotting Modules and Definitions
#######################################################################
#######################################################################
#### Modules
#######################################################################
import matplotlib   
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
#######################################################################
#### Custom Line styles
#######################################################################
custom_lines = [Line2D([0], [0], color="Black", lw=4),
                Line2D([0], [0], color="tab:blue", lw=4),
                Line2D([0], [0], color="tab:orange", lw=4),]
#######################################################################
#### Graphical Properties                                              
####################################################################### 
matplotlib.rcParams["font.family"] = "Times New Roman"                         

matplotlib.rcParams.update({'font.size': 24})#,'family':'monospace'})
               
matplotlib.rcParams['xtick.direction'] = 'in'
matplotlib.rcParams['ytick.direction'] = 'in'
matplotlib.rcParams['xtick.top'] = True
matplotlib.rcParams['ytick.right'] = True

matplotlib.rcParams['pgf.texsystem'] = 'pdflatex'
matplotlib.rcParams.update({'pgf.rcfonts' : False})

matplotlib.rcParams['lines.linewidth'] = 3

matplotlib.rcParams['axes.linewidth'] = 3
matplotlib.rcParams['xtick.major.size'] = 9
matplotlib.rcParams['xtick.major.width'] = 3
matplotlib.rcParams['xtick.minor.size'] = 6
matplotlib.rcParams['xtick.minor.width'] = 2

matplotlib.rcParams['ytick.major.size'] = 9
matplotlib.rcParams['ytick.major.width'] = 3
matplotlib.rcParams['ytick.minor.size'] = 6
matplotlib.rcParams['ytick.minor.width'] = 2
#########################################################
#######################################################################
## Logistic_Fit Analysis
#######################################################################
def logistic_plot(LOG_Analysis = False, debug = False):
    if LOG_Analysis:
#######################################################################
### Read D9.6-3D
#######################################################################
        if debug :
            print("Reading D9.6-3D")
        k_c_f_09 = np.genfromtxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_c_f.txt")
        k_p_f_09 = np.genfromtxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_p_f.txt")

        k_c_n_09 = np.genfromtxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_c_n.txt")
        k_p_n_09 = np.genfromtxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_p_n.txt")

        k_c_t_09 = np.genfromtxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_c_t.txt")
        k_p_t_09 = np.genfromtxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_p_t.txt")

#######################################################################
### Read D15-3D
#######################################################################
        if debug:
            print("Reading D15-3D")
        k_c_f_15 = np.genfromtxt("Data/Logistic_Fit/D15-3D/D15-3D_k_c_f.txt")
        k_p_f_15 = np.genfromtxt("Data/Logistic_Fit/D15-3D/D15-3D_k_p_f.txt")

        k_c_n_15 = np.genfromtxt("Data/Logistic_Fit/D15-3D/D15-3D_k_c_n.txt")
        k_p_n_15 = np.genfromtxt("Data/Logistic_Fit/D15-3D/D15-3D_k_p_n.txt")

        k_c_t_15 = np.genfromtxt("Data/Logistic_Fit/D15-3D/D15-3D_k_c_t.txt")
        k_p_t_15 = np.genfromtxt("Data/Logistic_Fit/D15-3D/D15-3D_k_p_t.txt")
#######################################################################
### Read D25-3D
#######################################################################
        if debug:
            print("Reading D25-3D")
        k_c_f_25 = np.genfromtxt("Data/Logistic_Fit/D25-3D/D25-3D_k_c_f.txt")
        k_p_f_25 = np.genfromtxt("Data/Logistic_Fit/D25-3D/D25-3D_k_p_f.txt")

        k_c_n_25 = np.genfromtxt("Data/Logistic_Fit/D25-3D/D25-3D_k_c_n.txt")
        k_p_n_25 = np.genfromtxt("Data/Logistic_Fit/D25-3D/D25-3D_k_p_n.txt")

        k_c_t_25 = np.genfromtxt("Data/Logistic_Fit/D25-3D/D25-3D_k_c_t.txt")
        k_p_t_25 = np.genfromtxt("Data/Logistic_Fit/D25-3D/D25-3D_k_p_t.txt")


        bins_k = np.arange(0, 100, 1)

        fig, ax = plt.subplots(3,2,figsize = (14,21), sharex=True, sharey=True)
        ax[0,0].hist(k_p_t_09.flatten(), bins = bins_k, density=True, color = "Black")
        ax[0,0].hist(k_p_f_09.flatten(), bins = bins_k, density=True, color = "tab:blue", alpha = 0.75)
        ax[0,0].hist(k_p_n_09.flatten(), bins = bins_k, density=True, color = "tab:orange", alpha = 0.75)

        ax[0,1].hist(k_c_t_09.flatten(), bins = bins_k, density=True, color = "Black")
        ax[0,1].hist(k_c_f_09.flatten(), bins = bins_k, density=True, color = "tab:blue", alpha = 0.75)
        ax[0,1].hist(k_c_n_09.flatten(), bins = bins_k, density=True, color = "tab:orange", alpha = 0.75)

        ax[1,0].hist(k_p_t_15.flatten(), bins = bins_k, density=True, color = "Black")
        ax[1,0].hist(k_p_f_15.flatten(), bins = bins_k, density=True, color = "tab:blue", alpha = 0.75)
        ax[1,0].hist(k_p_n_15.flatten(), bins = bins_k, density=True, color = "tab:orange", alpha = 0.75)

        ax[1,1].hist(k_c_t_15.flatten(), bins = bins_k, density=True, color = "Black")
        ax[1,1].hist(k_c_f_15.flatten(), bins = bins_k, density=True, color = "tab:blue", alpha = 0.75)
        ax[1,1].hist(k_c_n_15.flatten(), bins = bins_k, density=True, color = "tab:orange", alpha = 0.75)

        ax[2,0].hist(k_p_t_25.flatten(), bins = bins_k, density=True, color = "Black")
        ax[2,0].hist(k_p_f_25.flatten(), bins = bins_k, density=True, color = "tab:blue", alpha = 0.75)
        ax[2,0].hist(k_p_n_25.flatten(), bins = bins_k, density=True, color = "tab:orange", alpha = 0.75)

        ax[2,1].hist(k_c_t_25.flatten(), bins = bins_k, density=True, color = "Black")
        ax[2,1].hist(k_c_f_25.flatten(), bins = bins_k, density=True, color = "tab:blue", alpha = 0.75)
        ax[2,1].hist(k_c_n_25.flatten(), bins = bins_k, density=True, color = "tab:orange", alpha = 0.75)

        ax[0,0].set_title(r"$\mathrm{h_{+}}$")
        ax[0,1].set_title(r"$\mathrm{h_{\times}}$")

        ax[0,0].set_ylabel("D9.6-3D")
        ax[1,0].set_ylabel("D15-3D")
        ax[2,0].set_ylabel("D25-3D")
        for i in range(2):
            ax[2,i].set_xlabel(r"$\mathrm{k \ (Hz)}$")
        for i in range(3):
            ax[i,0].set_yticks([0,0.05, 0.1, 0.15])

        ax[0,0].legend(custom_lines, [r"$\mathrm{Total}$", r"$\mathrm{Flow}$", r"$\mathrm{\nu}$"],loc = "upper left", fontsize = "x-small", frameon = False)

        plt.subplots_adjust(wspace=0.0,hspace=0.0)

        plt.savefig("Images/Logistic_Fit/histogram.png", dpi = 200, bbox_inches = "tight")

        print("D9.6-3D Plus Flow", np.nanmean(k_p_f_09), "pm", np.nanstd(k_p_f_09))
        print("D9.6-3D Plus Neutrino", np.nanmean(k_p_n_09), "pm", np.nanstd(k_p_n_09))
        print("D9.6-3D Plus Total", np.nanmean(k_p_t_09), "pm", np.nanstd(k_p_t_09))
        print("D9.6-3D Cross Flow", np.nanmean(k_c_f_09), "pm", np.nanstd(k_c_f_09))
        print("D9.6-3D Cross Neutrino", np.nanmean(k_c_n_09), "pm", np.nanstd(k_c_n_09))
        print("D9.6-3D Cross Total", np.nanmean(k_c_t_09), "pm", np.nanstd(k_c_t_09))

        print("D15-3D Plus Flow", np.nanmean(k_p_f_15), "pm", np.nanstd(k_p_f_15))
        print("D15-3D Plus Neutrino", np.nanmean(k_p_n_15), "pm", np.nanstd(k_p_n_15))
        print("D15-3D Plus Total", np.nanmean(k_p_t_15), "pm", np.nanstd(k_p_t_15))
        print("D15-3D Cross Flow", np.nanmean(k_c_f_15), "pm", np.nanstd(k_c_f_15))
        print("D15-3D Cross Neutrino", np.nanmean(k_c_n_15), "pm", np.nanstd(k_c_n_15))
        print("D15-3D Cross Total", np.nanmean(k_c_t_15), "pm", np.nanstd(k_c_t_15))

        print("D25-3D Plus Flow", np.nanmean(k_p_f_25), "pm", np.nanstd(k_p_f_25))
        print("D25-3D Plus Neutrino", np.nanmean(k_p_n_25), "pm", np.nanstd(k_p_n_25))
        print("D25-3D Plus Total", np.nanmean(k_p_t_25), "pm", np.nanstd(k_p_t_25))
        print("D25-3D Cross Flow", np.nanmean(k_c_f_25), "pm", np.nanstd(k_c_f_25))
        print("D25-3D Cross Neutrino", np.nanmean(k_c_n_25), "pm", np.nanstd(k_c_n_25))
        print("D25-3D Cross Total", np.nanmean(k_c_t_25), "pm", np.nanstd(k_c_t_25))

    return None