#######################################################################
# Gravitational Wave Memory from Chimera's D-Series Plotting 
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
## Individual Waveform Plots
#######################################################################
#######################################################################        
### D9.6-3D
#######################################################################
def plot_D96(time_09, 
             hp_f_09, hc_f_09, 
             hp_n_09, hc_n_09, 
             hp_t_09, hc_t_09, 
             ap_09, ac_09, LN_09, 
             theta_09, phi_09, 
             D96 = True, 
             Flow = True, Neutrino = True, Total = True, Anisotropy = True, 
             debug = False):
    if D96:
        if debug :
            print("Plotting D9.6-3D")
        count = 0
        size_arr = (len(theta_09) * len(phi_09))
        for t in range(len(theta_09)):
            for p in range(len(phi_09)):
                count += 1
                ###########################################################
                if debug:
                    print("Plotting D9.6-3D: {:.2f} %".format(count/size_arr * 100))
                ###########################################################
                theta_str = str(int(theta_09[t])).zfill(3)
                phi_str = str(int(phi_09[p])).zfill(4)
#######################################################################
#### Flow Plot
#######################################################################
                if Flow:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_09, hp_f_09[:,p,t], label = r"$h_{+}$")
                    ax.plot(time_09, hc_f_09[:,p,t], label = r"$h_{\times}$")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{flow} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D9.6-3D}$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")
                    plt.legend()

                    plt.savefig("Images/Waveforms/D9.6-3D/Flow/D9.6-3D_h_flow_theta_" + 
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Neutrino Plot
#######################################################################
                if Neutrino:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_09, hp_n_09[:,p,t,0], ls = "-", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_09, hp_n_09[:,p,t,1], ls = "-", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_09, hp_n_09[:,p,t,2], ls = "-", color = "tab:red", alpha = 0.5)
                    ax.plot(time_09, hp_n_09[:,p,t,3], ls = "-", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_09, hc_n_09[:,p,t,0], ls = "--", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_09, hc_n_09[:,p,t,1], ls = "--", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_09, hc_n_09[:,p,t,2], ls = "--", color = "tab:red", alpha = 0.5)
                    ax.plot(time_09, hc_n_09[:,p,t,3], ls = "--", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_09, hp_n_09[:,p,t,4], ls = "-", color = "Black")
                    ax.plot(time_09, hc_n_09[:,p,t,4], ls = "--", color = "Black")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{\nu} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D9.6-3D}$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")

                    legend1 = plt.legend(custom_lines, [r"$\nu_{e}$", r"$\bar{\nu}_{e}$",
                                                        r"$\nu_{x}$", r"$\bar{\nu}_{x}$", 
                                                        r"$\sum_{i} \nu_{i}$"], 
                                        fontsize = "x-small", loc = "center", ncol = 1, 
                                        bbox_to_anchor = (0.1,0.8), frameon = False)
                    legend2 = plt.legend(custom_lines_style, [r"$h_{+}$", r"$h_{\times}$"], 
                                        fontsize = "x-small", loc = "center", ncol = 1, 
                                        bbox_to_anchor = (0.25,0.8), frameon = False)

                    ax.add_artist(legend1)

                    plt.savefig("Images/Waveforms/D9.6-3D/Neutrino/D9.6-3D_h_neutrino_theta_" +
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Total Plot
#######################################################################
                if Total:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_09, hp_t_09[:,p,t], label = r"$h_{+}$")
                    ax.plot(time_09, hc_t_09[:,p,t], label = r"$h_{\times}$")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{total} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D9.6-3D}$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")
                    plt.legend()

                    plt.savefig("Images/Waveforms/D9.6-3D/Total/D9.6-3D_h_total_theta_" 
                                + theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Anisotropy Plot
#######################################################################
                if Anisotropy:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_09, ap_09[:,p,t,0], ls = "-", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_09, ap_09[:,p,t,1], ls = "-", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_09, ap_09[:,p,t,2], ls = "-", color = "tab:red", alpha = 0.5)
                    ax.plot(time_09, ap_09[:,p,t,3], ls = "-", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_09, ac_09[:,p,t,0]+0.05, ls = "--", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_09, ac_09[:,p,t,1]+0.05, ls = "--", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_09, ac_09[:,p,t,2]+0.05, ls = "--", color = "tab:red", alpha = 0.5)
                    ax.plot(time_09, ac_09[:,p,t,3]+0.05, ls = "--", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_09, ap_09[:,p,t,4], ls = "-", color = "Black")
                    ax.plot(time_09, ac_09[:,p,t,4]+0.05, ls = "--", color = "Black")


                    ax.set_xlabel(r"Time Post Bounce ($ms$)")
                    ax.set_ylabel(r"$\alpha_{+/\times}$")
                    ax.set_title(r"$\mathrm{D9.6-3D}$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")

                    legend1 = plt.legend(custom_lines, 
                                         [r"$\nu_{e}$", r"$\bar{\nu}_e$", r"$\nu_{x}$", r"$\nu_{e}$", r"$\sum_{i} \nu_{i}$"],
                                           fontsize = "x-small", loc = "lower left", ncol = 5, 
                                           bbox_to_anchor = (0.1,0.08), frameon = False)
                    legend2 = plt.legend(custom_lines_style, 
                                         [r"$\alpha_{+}$", r"$\alpha_{\times}$+0.05"], 
                                         fontsize = "x-small", loc = "lower left", ncol = 2, 
                                         bbox_to_anchor = (0.3,0.05), frameon = False)

                    ax.add_artist(legend1)

                    plt.savefig("Images/Waveforms/D9.6-3D/Anisotropy/D9.6-3D_alpha_theta_" 
                                + theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()

        ap_09_max = np.zeros((len(time_09), 5))
        ap_09_min = np.zeros((len(time_09), 5))
        ac_09_max = np.zeros((len(time_09), 5))
        ac_09_min = np.zeros((len(time_09), 5))
        if debug :
            print("Begin D9.6-3D Min-Max Anisotropy Plots")
        for t in range(len(time_09)):
            for i in range(5):
                ap_09_max[t,i] = np.max(ap_09[t,:,:,i])
                ap_09_min[t,i] = np.min(ap_09[t,:,:,i]) 
                ac_09_max[t,i] = np.max(ac_09[t,:,:,i]) 
                ac_09_min[t,i] = np.min(ac_09[t,:,:,i]) 

        fig, ax = plt.subplots(2,1,figsize = (10,14), sharex = True)

        ax[0].plot(time_09, ap_09_max[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_min[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_max[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_min[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_max[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_min[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_max[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_min[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_max[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_09, ap_09_min[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")

        ax[1].plot(time_09, ac_09_max[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_min[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_max[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_min[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_max[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_min[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_max[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_min[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_max[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_09, ac_09_min[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")

        ax[1].set_xlabel(r"$\mathrm{ Time \ Post \ Bounce \ (ms)}$")
        ax[0].set_ylabel(r"$\mathrm{\alpha_{+}}$")
        ax[1].set_ylabel(r"$\mathrm{\alpha_{\times}}$")

        legend1 = ax[0].legend(custom_lines, [r"$\mathrm{\nu_{e}}$", r"$\mathrm{\bar{\nu}_{e}}$", 
                                              r"$\mathrm{\nu_{x}}$", r"$\mathrm{\bar{\nu}_{x}}$", 
                                              r"$\mathrm{\sum_{i} \nu_{i}}$"], 
                            fontsize = "x-small", loc = "center", ncol = 1, 
                            bbox_to_anchor = (0.1,0.8), frameon = False)
        
        plt.subplots_adjust(hspace = 0.0)

        plt.savefig("Images/Waveforms/D9.6-3D_anisotropy.png", 
                    dpi = 200, bbox_inches = "tight")
        plt.close()
    
    return None

#######################################################################        
### D15-3D
#######################################################################
def plot_D15(time_15, 
             hp_f_15, hc_f_15, 
             hp_n_15, hc_n_15, 
             hp_t_15, hc_t_15, 
             ap_15, ac_15, LN_15, 
             theta_15, phi_15, 
             D15 = True, 
             Flow = True, Neutrino = True, Total = True, Anisotropy = True, 
             debug = False):
    if D15:
        count = 0
        size_arr = (len(theta_15) * len(phi_15))
        for t in range(len(theta_15)):
            for p in range(len(phi_15)):
                count += 1
                ###########################################################
                if debug:
                    print("Plotting D15-3D: {:.2f} %".format(count/size_arr * 100))
                ###########################################################

                theta_str = str(int(theta_15[t])).zfill(3)
                phi_str = str(int(phi_15[p])).zfill(4)
#######################################################################
#### Flow Plot
#######################################################################
                if Flow:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_15, hp_f_15[:,p,t], label = r"$h_{+}$")
                    ax.plot(time_15, hc_f_15[:,p,t], label = r"$h_{\times}$")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{flow} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D \ } 15$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")
                    plt.legend()

                    plt.savefig("Images/Waveforms/D15-3D/Flow/D15-3D_h_flow_theta_" + 
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Neutrino Plot
#######################################################################
                if Neutrino:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_15, hp_n_15[:,p,t,0], ls = "-", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_15, hp_n_15[:,p,t,1], ls = "-", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_15, hp_n_15[:,p,t,2], ls = "-", color = "tab:red", alpha = 0.5)
                    ax.plot(time_15, hp_n_15[:,p,t,3], ls = "-", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_15, hc_n_15[:,p,t,0], ls = "--", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_15, hc_n_15[:,p,t,1], ls = "--", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_15, hc_n_15[:,p,t,2], ls = "--", color = "tab:red", alpha = 0.5)
                    ax.plot(time_15, hc_n_15[:,p,t,3], ls = "--", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_15, hp_n_15[:,p,t,4], ls = "-", color = "Black")
                    ax.plot(time_15, hc_n_15[:,p,t,4], ls = "--", color = "Black")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{\nu} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D \ } 15$ $\theta \ =$ " + theta_str[1:] +
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")

                    legend1 = plt.legend(custom_lines, [r"$\nu_{e}$", r"$\bar{\nu}_{e}$", 
                                                        r"$\nu_{x}$", r"$\bar{\nu}_{x}$", 
                                                        r"$\sum_{i} \nu_{i}$"], 
                                        fontsize = "x-small", loc = "center", ncol = 1, 
                                        bbox_to_anchor = (0.1,0.8), frameon = False)
                    legend2 = plt.legend(custom_lines_style, [r"$h_{+}$", r"$h_{\times}$"], 
                                        fontsize = "x-small", loc = "center", ncol = 1, 
                                        bbox_to_anchor = (0.25,0.8), frameon = False)

                    ax.add_artist(legend1)

                    plt.savefig("Images/Waveforms/D15-3D/Neutrino/D15-3D_h_neutrino_theta_" + 
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Total Plot
#######################################################################
                if Total:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_15, hp_t_15[:,p,t], label = r"$h_{+}$")
                    ax.plot(time_15, hc_t_15[:,p,t], label = r"$h_{\times}$")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{total} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D \ } 15$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")
                    plt.legend()

                    plt.savefig("Images/Waveforms/D15-3D/Total/D15-3D_h_total_theta_" + 
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Anisotropy Plot
#######################################################################
                if Anisotropy:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_15, ap_15[:,p,t,0], ls = "-", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_15, ap_15[:,p,t,1], ls = "-", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_15, ap_15[:,p,t,2], ls = "-", color = "tab:red", alpha = 0.5)
                    ax.plot(time_15, ap_15[:,p,t,3], ls = "-", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_15, ac_15[:,p,t,0]+0.1, ls = "--", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_15, ac_15[:,p,t,1]+0.1, ls = "--", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_15, ac_15[:,p,t,2]+0.1, ls = "--", color = "tab:red", alpha = 0.5)
                    ax.plot(time_15, ac_15[:,p,t,3]+0.1, ls = "--", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_15, ap_15[:,p,t,4], ls = "-", color = "Black")
                    ax.plot(time_15, ac_15[:,p,t,4]+0.1, ls = "--", color = "Black")


                    ax.set_xlabel(r"Time Post Bounce ($ms$)")
                    ax.set_ylabel(r"$\alpha_{+/\times}$")
                    ax.set_title(r"$\mathrm{D15-3D}$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")

                    legend1 = plt.legend(custom_lines, 
                                         [r"$\nu_{e}$", r"$\bar{\nu}_e$", r"$\nu_{x}$", r"$\nu_{e}$", r"$\sum_{i} \nu_{i}$"],
                                           fontsize = "x-small", loc = "lower left", ncol = 5, 
                                           bbox_to_anchor = (0.1,0.08), frameon = False)
                    legend2 = plt.legend(custom_lines_style, 
                                         [r"$\alpha_{+}$", r"$\alpha_{\times}$+0.1"], 
                                         fontsize = "x-small", loc = "lower left", ncol = 2, 
                                         bbox_to_anchor = (0.3,0.05), frameon = False)

                    ax.add_artist(legend1)

                    plt.savefig("Images/Waveforms/D15-3D/Anisotropy/D15-3D_alpha_theta_" 
                                + theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()

        ap_15_max = np.zeros((len(time_15), 5))
        ap_15_min = np.zeros((len(time_15), 5))
        ac_15_max = np.zeros((len(time_15), 5))
        ac_15_min = np.zeros((len(time_15), 5))
        if debug :
            print("Begin D9.6-3D Min-Max Anisotropy Plots")
        for t in range(len(time_15)):
            for i in range(5):
                ap_15_max[t,i] = np.max(ap_15[t,:,:,i])
                ap_15_min[t,i] = np.min(ap_15[t,:,:,i]) 
                ac_15_max[t,i] = np.max(ac_15[t,:,:,i]) 
                ac_15_min[t,i] = np.min(ac_15[t,:,:,i]) 

        fig, ax = plt.subplots(2,1,figsize = (10,14), sharex = True)

        ax[0].plot(time_15, ap_15_max[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_min[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_max[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_min[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_max[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_min[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_max[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_min[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_max[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_15, ap_15_min[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")

        ax[1].plot(time_15, ac_15_max[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_min[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_max[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_min[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_max[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_min[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_max[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_min[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_max[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_15, ac_15_min[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")

        ax[1].set_xlabel(r"$\mathrm{ Time \ Post \ Bounce \ (ms)}$")
        ax[0].set_ylabel(r"$\mathrm{\alpha_{+}}$")
        ax[1].set_ylabel(r"$\mathrm{\alpha_{\times}}$")

        legend1 = ax[0].legend(custom_lines, [r"$\mathrm{\nu_{e}}$", r"$\mathrm{\bar{\nu}_{e}}$", 
                                              r"$\mathrm{\nu_{x}}$", r"$\mathrm{\bar{\nu}_{x}}$", 
                                              r"$\mathrm{\sum_{i} \nu_{i}}$"], 
                            fontsize = "x-small", loc = "center", ncol = 1, 
                            bbox_to_anchor = (0.1,0.8), frameon = False)
        
        plt.subplots_adjust(hspace = 0.0)

        plt.savefig("Images/Waveforms/D15-3D_anisotropy.png", 
                    dpi = 200, bbox_inches = "tight")
        plt.close()
    
    return None

#######################################################################        
### D25-3D
#######################################################################
def plot_D25(time_25, 
             hp_f_25, hc_f_25, 
             hp_n_25, hc_n_25, 
             hp_t_25, hc_t_25, 
             ap_25, ac_25, LN_25, 
             theta_25, phi_25, 
             D25 = True, 
             Flow = True, Neutrino = True, Total = True, Anisotropy = True, 
             debug = False):
    if D25:
        count = 0
        size_arr = (len(theta_25) * len(phi_25))
        for t in range(len(theta_25)):
            for p in range(len(phi_25)):
                count += 1
                ###########################################################
                if debug:
                    print("Plotting D25-3D: {:.2f} %".format(count/size_arr * 100))
                ###########################################################

                theta_str = str(int(theta_25[t])).zfill(3)
                phi_str = str(int(phi_25[p])).zfill(4)
#######################################################################
#### Flow Plot
#######################################################################
                if Flow:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_25, hp_f_25[:,p,t], label = r"$h_{+}$")
                    ax.plot(time_25, hc_f_25[:,p,t], label = r"$h_{\times}$")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{flow} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D \ } 25$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")
                    plt.legend()

                    plt.savefig("Images/Waveforms/D25-3D/Flow/D25-3D_h_flow_theta_" + 
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Neutrino Plot
#######################################################################
                if Neutrino:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_25, hp_n_25[:,p,t,0], ls = "-", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_25, hp_n_25[:,p,t,1], ls = "-", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_25, hp_n_25[:,p,t,2], ls = "-", color = "tab:red", alpha = 0.5)
                    ax.plot(time_25, hp_n_25[:,p,t,3], ls = "-", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_25, hc_n_25[:,p,t,0], ls = "--", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_25, hc_n_25[:,p,t,1], ls = "--", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_25, hc_n_25[:,p,t,2], ls = "--", color = "tab:red", alpha = 0.5)
                    ax.plot(time_25, hc_n_25[:,p,t,3], ls = "--", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_25, hp_n_25[:,p,t,4], ls = "-", color = "Black")
                    ax.plot(time_25, hc_n_25[:,p,t,4], ls = "--", color = "Black")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{\nu} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D \ } 25$ $\theta \ =$ " + theta_str[1:] +
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")

                    legend1 = plt.legend(custom_lines, [r"$\nu_{e}$", r"$\bar{\nu}_{e}$", 
                                                        r"$\nu_{x}$", r"$\bar{\nu}_{x}$", 
                                                        r"$\sum_{i} \nu_{i}$"], 
                                        fontsize = "x-small", loc = "center", ncol = 1, 
                                        bbox_to_anchor = (0.1,0.8), frameon = False)
                    legend2 = plt.legend(custom_lines_style, [r"$h_{+}$", r"$h_{\times}$"], 
                                        fontsize = "x-small", loc = "center", ncol = 1, 
                                        bbox_to_anchor = (0.25,0.8), frameon = False)

                    ax.add_artist(legend1)

                    plt.savefig("Images/Waveforms/D25-3D/Neutrino/D25-3D_h_neutrino_theta_" + 
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Total Plot
#######################################################################
                if Total:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_25, hp_t_25[:,p,t], label = r"$h_{+}$")
                    ax.plot(time_25, hc_t_25[:,p,t], label = r"$h_{\times}$")

                    ax.set_xlabel(r"$\mathrm{Time \  (ms)}$")
                    ax.set_ylabel(r"$\mathrm{D \ h_{total} \ (cm)}$")
                    ax.set_title(r"$\mathrm{D \ } 25$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")
                    plt.legend()

                    plt.savefig("Images/Waveforms/D25-3D/Total/D25-3D_h_total_theta_" + 
                                theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()
#######################################################################
#### Anisotropy Plot
#######################################################################
                if Anisotropy:
                    fig, ax = plt.subplots(figsize = (10,7))

                    ax.plot(time_25, ap_25[:,p,t,0], ls = "-", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_25, ap_25[:,p,t,1], ls = "-", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_25, ap_25[:,p,t,2], ls = "-", color = "tab:red", alpha = 0.5)
                    ax.plot(time_25, ap_25[:,p,t,3], ls = "-", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_25, ac_25[:,p,t,0]+0.1, ls = "--", color = "tab:blue", alpha = 0.5)
                    ax.plot(time_25, ac_25[:,p,t,1]+0.1, ls = "--", color = "tab:orange", alpha = 0.5)
                    ax.plot(time_25, ac_25[:,p,t,2]+0.1, ls = "--", color = "tab:red", alpha = 0.5)
                    ax.plot(time_25, ac_25[:,p,t,3]+0.1, ls = "--", color = "tab:purple", alpha = 0.5)

                    ax.plot(time_25, ap_25[:,p,t,4], ls = "-", color = "Black")
                    ax.plot(time_25, ac_25[:,p,t,4]+0.1, ls = "--", color = "Black")


                    ax.set_xlabel(r"Time Post Bounce ($ms$)")
                    ax.set_ylabel(r"$\alpha_{+/\times}$")
                    ax.set_title(r"$\mathrm{D25-3D}$ $\theta \ =$ " + theta_str[1:] + 
                                r"$^{\circ}$ $\phi \ =$ " + phi_str[1:] + r"$^{\circ}$")

                    legend1 = plt.legend(custom_lines, 
                                         [r"$\nu_{e}$", r"$\bar{\nu}_e$", r"$\nu_{x}$", r"$\nu_{e}$", r"$\sum_{i} \nu_{i}$"],
                                           fontsize = "x-small", loc = "lower left", ncol = 5, 
                                           bbox_to_anchor = (0.1,0.08), frameon = False)
                    legend2 = plt.legend(custom_lines_style, 
                                         [r"$\alpha_{+}$", r"$\alpha_{\times}$+0.1"], 
                                         fontsize = "x-small", loc = "lower left", ncol = 2, 
                                         bbox_to_anchor = (0.3,0.05), frameon = False)

                    ax.add_artist(legend1)

                    plt.savefig("Images/Waveforms/D25-3D/Anisotropy/D25-3D_alpha_theta_" 
                                + theta_str + "_phi_" + phi_str+ ".png", 
                                dpi = 200, bbox_inches = "tight")
                    plt.close()

        ap_25_max = np.zeros((len(time_25), 5))
        ap_25_min = np.zeros((len(time_25), 5))
        ac_25_max = np.zeros((len(time_25), 5))
        ac_25_min = np.zeros((len(time_25), 5))
        if debug :
            print("Begin D9.6-3D Min-Max Anisotropy Plots")
        for t in range(len(time_25)):
            for i in range(5):
                ap_25_max[t,i] = np.max(ap_25[t,:,:,i])
                ap_25_min[t,i] = np.min(ap_25[t,:,:,i]) 
                ac_25_max[t,i] = np.max(ac_25[t,:,:,i]) 
                ac_25_min[t,i] = np.min(ac_25[t,:,:,i]) 

        fig, ax = plt.subplots(2,1,figsize = (10,14), sharex = True)

        ax[0].plot(time_25, ap_25_max[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_min[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_max[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_min[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_max[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_min[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_max[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_min[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_max[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")
        ax[0].plot(time_25, ap_25_min[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")

        ax[1].plot(time_25, ac_25_max[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_min[:,0], color = "tab:blue", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_max[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_min[:,1], color = "tab:orange", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_max[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_min[:,2], color = "tab:red", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_max[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_min[:,3], color = "tab:purple", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_max[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")
        ax[1].plot(time_25, ac_25_min[:,4], color = "Black", alpha = 0.5, ls = "", marker = ".")

        ax[1].set_xlabel(r"$\mathrm{ Time \ Post \ Bounce \ (ms)}$")
        ax[0].set_ylabel(r"$\mathrm{\alpha_{+}}$")
        ax[1].set_ylabel(r"$\mathrm{\alpha_{\times}}$")

        legend1 = ax[0].legend(custom_lines, [r"$\mathrm{\nu_{e}}$", r"$\mathrm{\bar{\nu}_{e}}$", 
                                              r"$\mathrm{\nu_{x}}$", r"$\mathrm{\bar{\nu}_{x}}$", 
                                              r"$\mathrm{\sum_{i} \nu_{i}}$"], 
                            fontsize = "x-small", loc = "center", ncol = 1, 
                            bbox_to_anchor = (0.1,0.8), frameon = False)
        
        plt.subplots_adjust(hspace = 0.0)

        plt.savefig("Images/Waveforms/D25-3D_anisotropy.png", 
                    dpi = 200, bbox_inches = "tight")
        plt.close()
    
    return None
#######################################################################
## Paper Total Waveform Plots
#######################################################################
def plot_all(time_09, 
             hp_f_09, hc_f_09, 
             hp_n_09, hc_n_09, 
             hp_t_09, hc_t_09,
             theta_09, phi_09,
             time_15, 
             hp_f_15, hc_f_15, 
             hp_n_15, hc_n_15, 
             hp_t_15, hc_t_15, 
             theta_15, phi_15,
             time_25, 
             hp_f_25, hc_f_25, 
             hp_n_25, hc_n_25, 
             hp_t_25, hc_t_25,
             theta_25, phi_25,  
             Flow = True, Neutrino = True, Total = True, 
             debug = False):
    if debug:
        print("Plotting Example Plots")
#######################################################################
### Flow
#######################################################################
    if Flow:
        fig, ax = plt.subplots(2,3, figsize = (21, 14), 
                            sharey = "all", sharex = "all")

        ax[0,0].plot(time_25, hp_f_25[:,36,0], color = 'tab:blue')
        ax[1,0].plot(time_25, hc_f_25[:,36,0], color = 'tab:blue')
        ax[0,0].plot(time_15, hp_f_15[:,36,0], color = 'tab:orange')
        ax[1,0].plot(time_15, hc_f_15[:,36,0], color = 'tab:orange')
        ax[0,0].plot(time_09, hp_f_09[:,36,0] * 10, color = 'tab:green')
        ax[1,0].plot(time_09, hc_f_09[:,36,0] * 10, color = 'tab:green')

        legend1 = ax[0,0].legend([Line2D([0], [0], color="tab:blue", lw=4),
                                  Line2D([0], [0], color="tab:orange", lw=4),
                                  Line2D([0], [0], color="tab:green", lw=4)],
                                [r"$\mathrm{D \ 25}$", 
                                 r"$\mathrm{D \ 15}$", 
                                 r"$\mathrm{D \ 9.6} \times \ 10$"], 
                                fontsize = "xx-small", loc = "lower left",
                                ncol = 3, bbox_to_anchor = (0.10,0.9), 
                                frameon = False)

        ax[0,0].set_ylabel(r"$\mathrm{D \ h_{+} \ (cm)}$")
        ax[1,0].set_ylabel(r"$\mathrm{D \ h_{\times} \ (cm)}$")
        ax[1,0].set_xlabel(r"$\mathrm{Time \ (ms)}$")

        ax[0,0].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[0])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[36])) + r"$\mathrm{^{\circ}}$")

        ax[0,1].plot(time_25, hp_f_25[:,6,24], color = 'tab:blue')
        ax[1,1].plot(time_25, hc_f_25[:,6,24], color = 'tab:blue')
        ax[0,1].plot(time_15, hp_f_15[:,6,24], color = 'tab:orange')
        ax[1,1].plot(time_15, hc_f_15[:,6,24], color = 'tab:orange')
        ax[0,1].plot(time_09, hp_f_09[:,6,24] * 10, color = 'tab:green')
        ax[1,1].plot(time_09, hc_f_09[:,6,24] * 10, color = 'tab:green')

        ax[1,1].set_xlabel(r"$\mathrm{Time \ (ms)}$")
        ax[0,1].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[24])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[6])) + r"$\mathrm{^{\circ}}$")

        ax[0,2].plot(time_25, hp_f_25[:,45,9], color = 'tab:blue')
        ax[1,2].plot(time_25, hc_f_25[:,45,9], color = 'tab:blue')
        ax[0,2].plot(time_15, hp_f_15[:,45,9], color = 'tab:orange')
        ax[1,2].plot(time_15, hc_f_15[:,45,9], color = 'tab:orange')
        ax[0,2].plot(time_09, hp_f_09[:,45,9] * 10, color = 'tab:green')
        ax[1,2].plot(time_09, hc_f_09[:,45,9] * 10, color = 'tab:green')

        ax[1,2].set_xlabel(r"$\mathrm{Time \ (ms)}$")
        ax[0,2].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[9])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[45])) + r"$\mathrm{^{\circ}}$")

        plt.subplots_adjust(wspace=0.05,hspace=0.05)

        plt.savefig("Images/Waveforms/Waveform_Examples_Flow.png", 
                    dpi = 200, bbox_inches = "tight")
        plt.close()
#######################################################################
### Neutrino
#######################################################################
    if Neutrino:
        fig, ax = plt.subplots(2,3, figsize = (21, 14), sharey = "all", sharex = "all")

        ax[0,0].plot(time_25, hp_n_25[:,36,0,-1], color = 'tab:blue')
        ax[1,0].plot(time_25, hc_n_25[:,36,0,-1], color = 'tab:blue')
        ax[0,0].plot(time_15, hp_n_15[:,36,0,-1], color = 'tab:orange')
        ax[1,0].plot(time_15, hc_n_15[:,36,0,-1], color = 'tab:orange')
        ax[0,0].plot(time_09, hp_n_09[:,36,0,-1] * 10, color = 'tab:green')
        ax[1,0].plot(time_09, hc_n_09[:,36,0,-1] * 10, color = 'tab:green')

        legend1 = ax[0,0].legend([Line2D([0], [0], color="tab:blue", lw=4),
                                  Line2D([0], [0], color="tab:orange", lw=4),
                                  Line2D([0], [0], color="tab:green", lw=4)],
                                [r"$\mathrm{D \ 25}$", 
                                 r"$\mathrm{D \ 15}$", 
                                 r"$\mathrm{D \ 9.6} \times \ 10$"], 
                                fontsize = "xx-small", loc = "lower left",
                                ncol = 3, bbox_to_anchor = (0.10,0.9), 
                                frameon = False)

        ax[0,0].set_ylabel(r"$\mathrm{D \ h_{+} \ (cm)}$")
        ax[1,0].set_ylabel(r"$\mathrm{D \ h_{\times} \ (cm)}$")
        ax[1,0].set_xlabel(r"$\mathrm{Time \ (ms)}$")

        ax[0,0].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[0])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[36])) + r"$\mathrm{^{\circ}}$")

        ax[0,1].plot(time_25, hp_n_25[:,6,24,-1], color = 'tab:blue')
        ax[1,1].plot(time_25, hc_n_25[:,6,24,-1], color = 'tab:blue')
        ax[0,1].plot(time_15, hp_n_15[:,6,24,-1], color = 'tab:orange')
        ax[1,1].plot(time_15, hc_n_15[:,6,24,-1], color = 'tab:orange')
        ax[0,1].plot(time_09, hp_n_09[:,6,24,-1] * 10, color = 'tab:green')
        ax[1,1].plot(time_09, hc_n_09[:,6,24,-1] * 10, color = 'tab:green')

        ax[1,1].set_xlabel(r"$\mathrm{Time \ (ms)}$")
        ax[0,1].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[24])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[6])) + r"$\mathrm{^{\circ}}$")

        ax[0,2].plot(time_25, hp_n_25[:,45,9,-1], color = 'tab:blue')
        ax[1,2].plot(time_25, hc_n_25[:,45,9,-1], color = 'tab:blue')
        ax[0,2].plot(time_15, hp_n_15[:,45,9,-1], color = 'tab:orange')
        ax[1,2].plot(time_15, hc_n_15[:,45,9,-1], color = 'tab:orange')
        ax[0,2].plot(time_09, hp_n_09[:,45,9,-1] * 10, color = 'tab:green')
        ax[1,2].plot(time_09, hc_n_09[:,45,9,-1] * 10, color = 'tab:green')

        ax[1,2].set_xlabel(r"$\mathrm{Time \ (ms)}$")
        ax[0,2].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[9])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[45])) + r"$\mathrm{^{\circ}}$")

        plt.subplots_adjust(wspace=0.05,hspace=0.05)

        plt.savefig("Images/Waveforms/Waveform_Examples_Neutrino.png", 
                    dpi = 200, bbox_inches = "tight")
        plt.close()
#######################################################################
### Total
#######################################################################
    if Total:
        fig, ax = plt.subplots(2,3, figsize = (21, 14), sharey = "all", sharex = "all")

        ax[0,0].plot(time_25, hp_t_25[:,36,0], color = 'tab:blue')
        ax[1,0].plot(time_25, hc_t_25[:,36,0], color = 'tab:blue')
        ax[0,0].plot(time_15, hp_t_15[:,36,0], color = 'tab:orange')
        ax[1,0].plot(time_15, hc_t_15[:,36,0], color = 'tab:orange')
        ax[0,0].plot(time_09, hp_t_09[:,36,0] * 10, color = 'tab:green')
        ax[1,0].plot(time_09, hc_t_09[:,36,0] * 10, color = 'tab:green')

        legend1 = ax[0,0].legend([Line2D([0], [0], color="tab:blue", lw=4),
                                  Line2D([0], [0], color="tab:orange", lw=4),
                                  Line2D([0], [0], color="tab:green", lw=4)],
                                [r"$\mathrm{D \ 25}$", 
                                 r"$\mathrm{D \ 15}$", 
                                 r"$\mathrm{D \ 9.6} \times \ 10$"], 
                                fontsize = "xx-small", loc = "lower left",
                                ncol = 3, bbox_to_anchor = (0.10,0.9), 
                                frameon = False)

        ax[0,0].set_ylabel(r"$\mathrm{D \ h_{+} \ (cm)}$")
        ax[1,0].set_ylabel(r"$\mathrm{D \ h_{\times} \ (cm)}$")
        ax[1,0].set_xlabel(r"$\mathrm{Time \ (ms)}$")

        ax[0,0].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[0])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[36])) + r"$\mathrm{^{\circ}}$")

        ax[0,1].plot(time_25, hp_t_25[:,6,24], color = 'tab:blue')
        ax[1,1].plot(time_25, hc_t_25[:,6,24], color = 'tab:blue')
        ax[0,1].plot(time_15, hp_t_15[:,6,24], color = 'tab:orange')
        ax[1,1].plot(time_15, hc_t_15[:,6,24], color = 'tab:orange')
        ax[0,1].plot(time_09, hp_t_09[:,6,24] * 10, color = 'tab:green')
        ax[1,1].plot(time_09, hc_t_09[:,6,24] * 10, color = 'tab:green')

        ax[1,1].set_xlabel(r"$\mathrm{Time \ (ms)}$")
        ax[0,1].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[24])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[6])) + r"$\mathrm{^{\circ}}$")

        ax[0,2].plot(time_25, hp_t_25[:,45,9], color = 'tab:blue')
        ax[1,2].plot(time_25, hc_t_25[:,45,9], color = 'tab:blue')
        ax[0,2].plot(time_15, hp_t_15[:,45,9], color = 'tab:orange')
        ax[1,2].plot(time_15, hc_t_15[:,45,9], color = 'tab:orange')
        ax[0,2].plot(time_09, hp_t_09[:,45,9] * 10, color = 'tab:green')
        ax[1,2].plot(time_09, hc_t_09[:,45,9] * 10, color = 'tab:green')

        ax[1,2].set_xlabel(r"$\mathrm{Time \ (ms)}$")
        ax[0,2].set_title(r"$\mathrm{\theta \ = \ }$" + str(np.round(theta_25[9])) + 
                          r"$\mathrm{^{\circ} \ \phi = \ }$" + str(np.round(phi_25[45])) + r"$\mathrm{^{\circ}}$")

        plt.subplots_adjust(wspace=0.05,hspace=0.05)

        plt.savefig("Images/Waveforms/Waveform_Examples_Total.png", 
                    dpi = 200, bbox_inches = "tight")
        plt.close()
    return None