import numpy as np

from IO_Infrastructure import dir_setup
from Data_Read import read_D96, read_D15, read_D25
from Plot_Individual_Waveforms import plot_D96, plot_D15, plot_D25, plot_all
from Anisotropy_Plot import plot_Ani_D96, plot_Ani_D15, plot_Ani_D25
from Memory_Extraction import extract_D96, extract_D15, extract_D25
from Data_Write import write_D96, write_D15, write_D25
from Tapering_ASD import plot_ASD
from Logistic_Fitting import fit_D96, fit_D15, fit_D25
from Logistic_Analysis import logistic_plot

dir_setup(debug = True)

time_09,  hp_f_09, hc_f_09, hp_n_09, hc_n_09, hp_t_09, hc_t_09, ap_09, ac_09, LN_09, theta_09, phi_09 = read_D96(D96 = True, 
                                                                                                                 Flow = True, 
                                                                                                                 Neutrino = True, 
                                                                                                                 Total = True, 
                                                                                                                 debug = True)

time_15, hp_f_15, hc_f_15, hp_n_15, hc_n_15, hp_t_15, hc_t_15, ap_15, ac_15, LN_15, theta_15, phi_15 = read_D15(D15 = True, 
                                                                                                                Flow = True, 
                                                                                                                Neutrino = True, 
                                                                                                                Total = True, 
                                                                                                                debug = True)

time_25, hp_f_25, hc_f_25, hp_n_25, hc_n_25, hp_t_25, hc_t_25, ap_25, ac_25, LN_25, theta_25, phi_25 = read_D25(D25 = True, 
                                                                                                                Flow = True, 
                                                                                                                Neutrino = True, 
                                                                                                                Total = True, 
                                                                                                                debug = True)

# plot_D96(time_09, 
#          hp_f_09, hc_f_09, 
#          hp_n_09, hc_n_09, 
#          hp_t_09, hc_t_09, 
#          ap_09, ac_09, LN_09, 
#          theta_09, phi_09, 
#          D96 = True, 
#          Flow = True, Neutrino = True, Total = True, Anisotropy = True, 
#          debug = True)

# plot_D15(time_15, 
#          hp_f_15, hc_f_15, 
#          hp_n_15, hc_n_15, 
#          hp_t_15, hc_t_15, 
#          ap_15, ac_15, LN_15, 
#          theta_15, phi_15, 
#          D15 = True,
#          Flow = True, Neutrino = True, Total = True, Anisotropy = True, 
#          debug = True)

# plot_D25(time_25, 
#          hp_f_25, hc_f_25, 
#          hp_n_25, hc_n_25, 
#          hp_t_25, hc_t_25, 
#          ap_25, ac_25, LN_25, 
#          theta_25, phi_25, 
#          D25 = True, 
#          Flow = True, Neutrino = True, Total = True, Anisotropy = True, 
#          debug = True)

# plot_all(time_09, 
#              hp_f_09, hc_f_09, 
#              hp_n_09, hc_n_09, 
#              hp_t_09, hc_t_09,
#              theta_09, phi_09,
#              time_15, 
#              hp_f_15, hc_f_15, 
#              hp_n_15, hc_n_15, 
#              hp_t_15, hc_t_15, 
#              theta_15, phi_15,
#              time_25, 
#              hp_f_25, hc_f_25, 
#              hp_n_25, hc_n_25, 
#              hp_t_25, hc_t_25,
#              theta_25, phi_25,  
#              Flow = True, Neutrino = True, Total = True, 
#              debug = True)

plot_Ani_D96(time_09, 
             hp_n_09, hc_n_09, 
             ap_09, ac_09, LN_09, 
             theta_09, phi_09, 
             D96 = True, 
             Neutrino = True,Anisotropy = True, 
             debug = False)

plot_Ani_D15(time_15, 
             hp_n_15, hc_n_15, 
             ap_15, ac_15, LN_15, 
             theta_15, phi_15, 
             D15 = True, 
             Neutrino = True,Anisotropy = True, 
             debug = False)

plot_Ani_D25(time_25, 
             hp_n_25, hc_n_25, 
             ap_25, ac_25, LN_25, 
             theta_25, phi_25, 
             D25 = True, 
             Neutrino = True,Anisotropy = True, 
             debug = False)

# extract_D96(hp_f_09, hc_f_09, 
#             hp_n_09, hc_n_09, 
#             hp_t_09, hc_t_09, 
#             D96 = True, 
#             Flow = True, Neutrino = True, Total = True, 
#             debug = True)

# extract_D15(hp_f_15, hc_f_15, 
#             hp_n_15, hc_n_15, 
#             hp_t_15, hc_t_15, 
#             D15 = True, 
#             Flow = True, Neutrino = True, Total = True, 
#             debug = True)

# extract_D25(hp_f_25, hc_f_25, 
#             hp_n_25, hc_n_25, 
#             hp_t_25, hc_t_25, 
#             D25 = True, 
#             Flow = True, Neutrino = True, Total = True, 
#             debug = True)

# write_D96(time_09,
#               hp_f_09, hc_f_09, 
#               hp_n_09, hc_n_09, 
#               hp_t_09, hc_t_09,
#               theta_09, phi_09,
#               output_frequency = 16384,
#               output_distance = 10, 
#               D96 = True, 
#               Flow = True, Neutrino = True, Total = True, 
#               debug = True)

# write_D15(time_15,
#               hp_f_15, hc_f_15, 
#               hp_n_15, hc_n_15, 
#               hp_t_15, hc_t_15,
#               theta_15, phi_15,
#               output_frequency = 16384,
#               output_distance = 10, 
#               D15 = True, 
#               Flow = True, Neutrino = True, Total = True, 
#               debug = True)

# write_D25(time_25,
#               hp_f_25, hc_f_25, 
#               hp_n_25, hc_n_25, 
#               hp_t_25, hc_t_25,
#               theta_25, phi_25,
#               output_frequency = 16384,
#               output_distance = 10, 
#               D25 = True, 
#               Flow = True, Neutrino = True, Total = True, 
#               debug = True)

# SNR = plot_ASD(time_09, 
#                hp_t_09, hc_t_09,
#                time_15, 
#                hp_t_15, hc_t_15,
#                time_25, 
#                hp_t_25, hc_t_25,
#                phi_ind = 0,
#                theta_ind = 0,
#                tmax = 500, 
#                frequency = 16384,
#                f_tail = 1/100,
#                output_distance = 1,
#                debug = True) 

# fit_D96(time_09, 
#         hp_f_09, hc_f_09, 
#         hp_n_09, hc_n_09, 
#         theta_09, phi_09, 
#         D96 = True, 
#         debug = True)

# fit_D15(time_15, 
#         hp_f_15, hc_f_15, 
#         hp_n_15, hc_n_15, 
#         theta_15, phi_15, 
#         D15 = True, 
#         debug = True)

# fit_D25(time_15, 
#         hp_f_15, hc_f_15, 
#         hp_n_15, hc_n_15, 
#         theta_15, phi_15, 
#         D25 = True, 
#         debug = True)


# logistic_plot(debug = True)