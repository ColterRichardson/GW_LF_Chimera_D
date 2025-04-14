#######################################################################
# Gravitational Wave Memory from Chimera's D-Series Anisotrpy Plotting 
#######################################################################
#######################################################################
## House Keeping
#######################################################################
#######################################################################
### Math, Science, and Computing Modules
#######################################################################
import numpy as np
import warnings
warnings.filterwarnings("ignore")
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
custom_lines = [Line2D([0], [0], color="tab:blue", lw=4),
                Line2D([0], [0], color="tab:orange", lw=4),
                Line2D([0], [0], color="tab:red", lw=4),
                Line2D([0], [0], color="tab:purple", lw=4),
                Line2D([0], [0], color="Black", lw=4)]

custom_lines_style = [Line2D([0], [0], ls = "-", color="Black", lw=4),
                      Line2D([0], [0], ls = "--", color="Black", lw=4)]
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
#######################################################################        
### User Definitions
#######################################################################
Bethe2Erg = 1.0e51                         # erg / Bethe
## Function Definitions
def erg2Bethe(x):
    return x / Bethe2Erg
def Bethe2erg(x):
    return x * Bethe2Erg
#######################################################################
## Individual Waveform Plots
#######################################################################
#######################################################################        
### D9.6-3D
#######################################################################
def plot_Ani_D96(time_09, 
             hp_n_09, hc_n_09, 
             ap_09, ac_09, LN_09, 
             theta_09, phi_09, 
             D96 = True, 
             Neutrino = True,Anisotropy = True, 
             debug = False):
    if D96:
        if debug :
            print("Plotting D9.6-3D")
        theta_str = str(int(theta_09[0])).zfill(3)
        phi_str = str(int(phi_09[36])).zfill(4)
#######################################################################
#### Neutrino Plot
#######################################################################
        if Neutrino and Anisotropy:
            fig, ax = plt.subplots(1, 2, figsize = (20,7))

            ax[1].plot(time_09, hp_n_09[:,36,0,0], ls = "-", color = "tab:blue", alpha = 0.5)
            ax[1].plot(time_09, hp_n_09[:,36,0,1], ls = "-", color = "tab:orange", alpha = 0.5)
            ax[1].plot(time_09, hp_n_09[:,36,0,2], ls = "-", color = "tab:red", alpha = 0.5)
            ax[1].plot(time_09, hp_n_09[:,36,0,3], ls = "-", color = "tab:purple", alpha = 0.5)

            ax[1].plot(time_09, hc_n_09[:,36,0,0], ls = "--", color = "tab:blue", alpha = 0.5)
            ax[1].plot(time_09, hc_n_09[:,36,0,1], ls = "--", color = "tab:orange", alpha = 0.5)
            ax[1].plot(time_09, hc_n_09[:,36,0,2], ls = "--", color = "tab:red", alpha = 0.5)
            ax[1].plot(time_09, hc_n_09[:,36,0,3], ls = "--", color = "tab:purple", alpha = 0.5)

            ax[1].plot(time_09, hp_n_09[:,36,0,4], ls = "-", color = "Black")
            ax[1].plot(time_09, hc_n_09[:,36,0,4], ls = "--", color = "Black")

            ax[1].set_xlabel(r"$\mathrm{Time \  (ms)}$")
            ax[1].set_ylabel(r"$\mathrm{D \ h_{\nu} \ (cm)}$")


            legend1 = ax[1].legend(custom_lines, [r"$\mathrm{\nu_{e}}$", r"$\mathrm{\bar{\nu}_{e}}$",
                                                r"$\mathrm{\nu_{x}}$", r"$\mathrm{\bar{\nu}_{x}}$", 
                                                r"$\mathrm{\sum_{i} \nu_{i}}$"], 
                                fontsize = "x-small", loc = "center", ncol = 1, 
                                bbox_to_anchor = (0.1,0.8), frameon = False)
            legend2 = ax[1].legend(custom_lines_style, [r"$h_{+}$", r"$h_{\times}$"], 
                                fontsize = "x-small", loc = "center", ncol = 1, 
                                bbox_to_anchor = (0.25,0.8), frameon = False)

            ax[1].add_artist(legend1)

            ax[0].plot(time_09, ap_09[:,36,0,0], ls = "-", color = "tab:blue", alpha = 0.5)
            ax[0].plot(time_09, ap_09[:,36,0,1], ls = "-", color = "tab:orange", alpha = 0.5)
            ax[0].plot(time_09, ap_09[:,36,0,2], ls = "-", color = "tab:red", alpha = 0.5)
            ax[0].plot(time_09, ap_09[:,36,0,3], ls = "-", color = "tab:purple", alpha = 0.5)

            ax[0].plot(time_09, ac_09[:,36,0,0]+0.05, ls = "--", color = "tab:blue", alpha = 0.5)
            ax[0].plot(time_09, ac_09[:,36,0,1]+0.05, ls = "--", color = "tab:orange", alpha = 0.5)
            ax[0].plot(time_09, ac_09[:,36,0,2]+0.05, ls = "--", color = "tab:red", alpha = 0.5)
            ax[0].plot(time_09, ac_09[:,36,0,3]+0.05, ls = "--", color = "tab:purple", alpha = 0.5)

            ax[0].plot(time_09, ap_09[:,36,0,4], ls = "-", color = "Black")
            ax[0].plot(time_09, ac_09[:,36,0,4]+0.05, ls = "--", color = "Black")


            ax[0].set_xlabel(r"$\mathrm{Time \ Post \ Bounce \ (ms)}$")
            ax[0].set_ylabel(r"$\mathrm{\alpha_{+/\times}}$")
            plt.savefig("Images/Waveforms/D9.6-3D_alpha_theta_" 
                        + theta_str + "_phi_" + phi_str+ ".png", 
                        dpi = 200, bbox_inches = "tight")
            plt.close()

        fig, ax = plt.subplots(figsize = (10,7))

        ax.plot(time_09, LN_09[:,0], ls = "-", color = "tab:blue", alpha = 0.5)
        ax.plot(time_09, LN_09[:,1], ls = "-", color = "tab:orange", alpha = 0.5)
        ax.plot(time_09, LN_09[:,2], ls = "-", color = "tab:red", alpha = 0.5)
        ax.plot(time_09, LN_09[:,3], ls = "-", color = "tab:purple", alpha = 0.5)

        ax.plot(time_09, LN_09[:,4], ls = "-", color = "Black")

        ax.set_ylabel(r"$\mathrm{L_{E} \ (erg \ s^{-1})}$")
        ax.set_xlabel(r"$\mathrm{Time \ Post \ Bounce \ (ms)}$")

        secax_y = ax.secondary_yaxis(
            'right', functions=(erg2Bethe, Bethe2erg))
        secax_y.set_ylabel(r"$\mathrm{L_{E} \ (B \ s^{-1})}$")
        fig.legend(frameon = False, loc = "upper right", bbox_to_anchor=(0.68, 0.85))

        legend1 = plt.legend(custom_lines, [r"$\nu_{e}$", r"$\bar{\nu}_e$", r"$\nu_{x}$", r"$\nu_{e}$", r"$\sum_{i}^{6} \nu_{i}$"], fontsize = "x-small", loc = "upper left", ncol = 1, bbox_to_anchor = (0.8,0.99), frameon = False)


        plt.savefig("Images/Waveforms/D9.6-3D-500km_luminosity.png", dpi = 300, bbox_inches = "tight")
        plt.close() 
 
    return None
#######################################################################        
### D15-3D
#######################################################################
def plot_Ani_D15(time_15, 
             hp_n_15, hc_n_15, 
             ap_15, ac_15, LN_15, 
             theta_15, phi_15, 
             D15 = True, 
             Neutrino = True,Anisotropy = True, 
             debug = False):
    if D15:
        if debug :
            print("Plotting D15-3D")
        theta_str = str(int(theta_15[0])).zfill(3)
        phi_str = str(int(phi_15[36])).zfill(4)
#######################################################################
#### Neutrino Plot
#######################################################################
        if Neutrino and Anisotropy:
            fig, ax = plt.subplots(1, 2, figsize = (20,7))

            ax[1].plot(time_15, hp_n_15[:,36,0,0], ls = "-", color = "tab:blue", alpha = 0.5)
            ax[1].plot(time_15, hp_n_15[:,36,0,1], ls = "-", color = "tab:orange", alpha = 0.5)
            ax[1].plot(time_15, hp_n_15[:,36,0,2], ls = "-", color = "tab:red", alpha = 0.5)
            ax[1].plot(time_15, hp_n_15[:,36,0,3], ls = "-", color = "tab:purple", alpha = 0.5)

            ax[1].plot(time_15, hc_n_15[:,36,0,0], ls = "--", color = "tab:blue", alpha = 0.5)
            ax[1].plot(time_15, hc_n_15[:,36,0,1], ls = "--", color = "tab:orange", alpha = 0.5)
            ax[1].plot(time_15, hc_n_15[:,36,0,2], ls = "--", color = "tab:red", alpha = 0.5)
            ax[1].plot(time_15, hc_n_15[:,36,0,3], ls = "--", color = "tab:purple", alpha = 0.5)

            ax[1].plot(time_15, hp_n_15[:,36,0,4], ls = "-", color = "Black")
            ax[1].plot(time_15, hc_n_15[:,36,0,4], ls = "--", color = "Black")

            ax[1].set_xlabel(r"$\mathrm{Time \  (ms)}$")
            ax[1].set_ylabel(r"$\mathrm{D \ h_{\nu} \ (cm)}$")


            legend1 = ax[1].legend(custom_lines, [r"$\mathrm{\nu_{e}}$", r"$\mathrm{\bar{\nu}_{e}}$",
                                                r"$\mathrm{\nu_{x}}$", r"$\mathrm{\bar{\nu}_{x}}$", 
                                                r"$\mathrm{\sum_{i} \nu_{i}}$"], 
                                fontsize = "x-small", loc = "center", ncol = 1, 
                                bbox_to_anchor = (0.1,0.2), frameon = False)
            legend2 = ax[1].legend(custom_lines_style, [r"$h_{+}$", r"$h_{\times}$"], 
                                fontsize = "x-small", loc = "center", ncol = 1, 
                                bbox_to_anchor = (0.25,0.2), frameon = False)

            ax[1].add_artist(legend1)

            ax[0].plot(time_15, ap_15[:,36,0,0], ls = "-", color = "tab:blue", alpha = 0.5)
            ax[0].plot(time_15, ap_15[:,36,0,1], ls = "-", color = "tab:orange", alpha = 0.5)
            ax[0].plot(time_15, ap_15[:,36,0,2], ls = "-", color = "tab:red", alpha = 0.5)
            ax[0].plot(time_15, ap_15[:,36,0,3], ls = "-", color = "tab:purple", alpha = 0.5)

            ax[0].plot(time_15, ac_15[:,36,0,0]+0.1, ls = "--", color = "tab:blue", alpha = 0.5)
            ax[0].plot(time_15, ac_15[:,36,0,1]+0.1, ls = "--", color = "tab:orange", alpha = 0.5)
            ax[0].plot(time_15, ac_15[:,36,0,2]+0.1, ls = "--", color = "tab:red", alpha = 0.5)
            ax[0].plot(time_15, ac_15[:,36,0,3]+0.1, ls = "--", color = "tab:purple", alpha = 0.5)

            ax[0].plot(time_15, ap_15[:,36,0,4], ls = "-", color = "Black")
            ax[0].plot(time_15, ac_15[:,36,0,4]+0.1, ls = "--", color = "Black")


            ax[0].set_xlabel(r"$\mathrm{Time \ Post \ Bounce \ (ms)}$")
            ax[0].set_ylabel(r"$\mathrm{\alpha_{+/\times}}$")
            plt.savefig("Images/Waveforms/D15-3D_alpha_theta_" 
                        + theta_str + "_phi_" + phi_str+ ".png", 
                        dpi = 200, bbox_inches = "tight")
            plt.close()

        fig, ax = plt.subplots(figsize = (10,7))

        ax.plot(time_15, LN_15[:,0], ls = "-", color = "tab:blue", alpha = 0.5)
        ax.plot(time_15, LN_15[:,1], ls = "-", color = "tab:orange", alpha = 0.5)
        ax.plot(time_15, LN_15[:,2], ls = "-", color = "tab:red", alpha = 0.5)
        ax.plot(time_15, LN_15[:,3], ls = "-", color = "tab:purple", alpha = 0.5)

        ax.plot(time_15, LN_15[:,4], ls = "-", color = "Black")

        ax.set_ylabel(r"$\mathrm{L_{E} \ (erg \ s^{-1})}$")
        ax.set_xlabel(r"$\mathrm{Time \ Post \ Bounce \ (ms)}$")

        secax_y = ax.secondary_yaxis(
            'right', functions=(erg2Bethe, Bethe2erg))
        secax_y.set_ylabel(r"$\mathrm{L_{E} \ (B \ s^{-1})}$")
        fig.legend(frameon = False, loc = "upper right", bbox_to_anchor=(0.68, 0.85))

        legend1 = plt.legend(custom_lines, [r"$\nu_{e}$", r"$\bar{\nu}_e$", r"$\nu_{x}$", r"$\nu_{e}$", r"$\sum_{i}^{6} \nu_{i}$"], fontsize = "x-small", loc = "upper left", ncol = 1, bbox_to_anchor = (0.8,0.99), frameon = False)


        plt.savefig("Images/Waveforms/D15-3D-500km_luminosity.png", dpi = 300, bbox_inches = "tight")
        plt.close() 
 
    return None
#######################################################################        
### D25-3D
#######################################################################
def plot_Ani_D25(time_25, 
             hp_n_25, hc_n_25, 
             ap_25, ac_25, LN_25, 
             theta_25, phi_25, 
             D25 = True, 
             Neutrino = True,Anisotropy = True, 
             debug = False):
    if D25:
        if debug :
            print("Plotting D25-3D")
        theta_str = str(int(theta_25[0])).zfill(3)
        phi_str = str(int(phi_25[36])).zfill(4)
#######################################################################
#### Neutrino Plot
#######################################################################
        if Neutrino and Anisotropy:
            fig, ax = plt.subplots(1, 2, figsize = (20,7))

            ax[1].plot(time_25, hp_n_25[:,36,0,0], ls = "-", color = "tab:blue", alpha = 0.5)
            ax[1].plot(time_25, hp_n_25[:,36,0,1], ls = "-", color = "tab:orange", alpha = 0.5)
            ax[1].plot(time_25, hp_n_25[:,36,0,2], ls = "-", color = "tab:red", alpha = 0.5)
            ax[1].plot(time_25, hp_n_25[:,36,0,3], ls = "-", color = "tab:purple", alpha = 0.5)

            ax[1].plot(time_25, hc_n_25[:,36,0,0], ls = "--", color = "tab:blue", alpha = 0.5)
            ax[1].plot(time_25, hc_n_25[:,36,0,1], ls = "--", color = "tab:orange", alpha = 0.5)
            ax[1].plot(time_25, hc_n_25[:,36,0,2], ls = "--", color = "tab:red", alpha = 0.5)
            ax[1].plot(time_25, hc_n_25[:,36,0,3], ls = "--", color = "tab:purple", alpha = 0.5)

            ax[1].plot(time_25, hp_n_25[:,36,0,4], ls = "-", color = "Black")
            ax[1].plot(time_25, hc_n_25[:,36,0,4], ls = "--", color = "Black")

            ax[1].set_xlabel(r"$\mathrm{Time \  (ms)}$")
            ax[1].set_ylabel(r"$\mathrm{D \ h_{\nu} \ (cm)}$")


            legend1 = ax[1].legend(custom_lines, [r"$\mathrm{\nu_{e}}$", r"$\mathrm{\bar{\nu}_{e}}$",
                                                r"$\mathrm{\nu_{x}}$", r"$\mathrm{\bar{\nu}_{x}}$", 
                                                r"$\mathrm{\sum_{i} \nu_{i}}$"], 
                                fontsize = "x-small", loc = "center", ncol = 1, 
                                bbox_to_anchor = (0.1,0.2), frameon = False)
            legend2 = ax[1].legend(custom_lines_style, [r"$h_{+}$", r"$h_{\times}$"], 
                                fontsize = "x-small", loc = "center", ncol = 1, 
                                bbox_to_anchor = (0.25,0.2), frameon = False)

            ax[1].add_artist(legend1)

            ax[0].plot(time_25, ap_25[:,36,0,0], ls = "-", color = "tab:blue", alpha = 0.5)
            ax[0].plot(time_25, ap_25[:,36,0,1], ls = "-", color = "tab:orange", alpha = 0.5)
            ax[0].plot(time_25, ap_25[:,36,0,2], ls = "-", color = "tab:red", alpha = 0.5)
            ax[0].plot(time_25, ap_25[:,36,0,3], ls = "-", color = "tab:purple", alpha = 0.5)

            ax[0].plot(time_25, ac_25[:,36,0,0]+0.1, ls = "--", color = "tab:blue", alpha = 0.5)
            ax[0].plot(time_25, ac_25[:,36,0,1]+0.1, ls = "--", color = "tab:orange", alpha = 0.5)
            ax[0].plot(time_25, ac_25[:,36,0,2]+0.1, ls = "--", color = "tab:red", alpha = 0.5)
            ax[0].plot(time_25, ac_25[:,36,0,3]+0.1, ls = "--", color = "tab:purple", alpha = 0.5)

            ax[0].plot(time_25, ap_25[:,36,0,4], ls = "-", color = "Black")
            ax[0].plot(time_25, ac_25[:,36,0,4]+0.1, ls = "--", color = "Black")


            ax[0].set_xlabel(r"$\mathrm{Time \ Post \ Bounce \ (ms)}$")
            ax[0].set_ylabel(r"$\mathrm{\alpha_{+/\times}}$")
            plt.savefig("Images/Waveforms/D25-3D_alpha_theta_" 
                        + theta_str + "_phi_" + phi_str+ ".png", 
                        dpi = 200, bbox_inches = "tight")
            plt.close()

        fig, ax = plt.subplots(figsize = (10,7))

        ax.plot(time_25, LN_25[:,0], ls = "-", color = "tab:blue", alpha = 0.5)
        ax.plot(time_25, LN_25[:,1], ls = "-", color = "tab:orange", alpha = 0.5)
        ax.plot(time_25, LN_25[:,2], ls = "-", color = "tab:red", alpha = 0.5)
        ax.plot(time_25, LN_25[:,3], ls = "-", color = "tab:purple", alpha = 0.5)

        ax.plot(time_25, LN_25[:,4], ls = "-", color = "Black")

        ax.set_ylabel(r"$\mathrm{L_{E} \ (erg \ s^{-1})}$")
        ax.set_xlabel(r"$\mathrm{Time \ Post \ Bounce \ (ms)}$")

        secax_y = ax.secondary_yaxis(
            'right', functions=(erg2Bethe, Bethe2erg))
        secax_y.set_ylabel(r"$\mathrm{L_{E} \ (B \ s^{-1})}$")
        fig.legend(frameon = False, loc = "upper right", bbox_to_anchor=(0.68, 0.85))

        legend1 = plt.legend(custom_lines, [r"$\nu_{e}$", r"$\bar{\nu}_e$", r"$\nu_{x}$", r"$\nu_{e}$", r"$\sum_{i}^{6} \nu_{i}$"], fontsize = "x-small", loc = "upper left", ncol = 1, bbox_to_anchor = (0.8,0.99), frameon = False)


        plt.savefig("Images/Waveforms/D25-3D-500km_luminosity.png", dpi = 300, bbox_inches = "tight")
        plt.close() 
 
    return None