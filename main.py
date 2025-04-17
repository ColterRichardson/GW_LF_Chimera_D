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

D96 = False
D15 = False
D25 = False

Flow = False
Neutrino = False
Total = False

Anisotropy = False

debug = False

output_frequency = 16384
output_distance = 1

ASD = False
phi_ind = 0
theta_ind = 0
tmax = 500 
frequency = 16384
f_tail = 1/100

LOG_Analysis = False

dir_setup(debug)

time_09,  hp_f_09, hc_f_09, hp_n_09, hc_n_09, hp_t_09, hc_t_09, ap_09, ac_09, LN_09, theta_09, phi_09 = read_D96(D96, 
                                                                                                                 Flow, 
                                                                                                                 Neutrino, 
                                                                                                                 Total, 
                                                                                                                 debug)

time_15, hp_f_15, hc_f_15, hp_n_15, hc_n_15, hp_t_15, hc_t_15, ap_15, ac_15, LN_15, theta_15, phi_15 = read_D15(D15, 
                                                                                                                Flow, 
                                                                                                                Neutrino, 
                                                                                                                Total, 
                                                                                                                debug)

time_25, hp_f_25, hc_f_25, hp_n_25, hc_n_25, hp_t_25, hc_t_25, ap_25, ac_25, LN_25, theta_25, phi_25 = read_D25(D25, 
                                                                                                                Flow, 
                                                                                                                Neutrino, 
                                                                                                                Total, 
                                                                                                                debug)

plot_D96(time_09, 
         hp_f_09, hc_f_09, 
         hp_n_09, hc_n_09, 
         hp_t_09, hc_t_09, 
         ap_09, ac_09, LN_09, 
         theta_09, phi_09, 
         D96, 
         Flow, Neutrino, Total, Anisotropy, 
         debug)

plot_D15(time_15, 
         hp_f_15, hc_f_15, 
         hp_n_15, hc_n_15, 
         hp_t_15, hc_t_15, 
         ap_15, ac_15, LN_15, 
         theta_15, phi_15, 
         D15,
         Flow, Neutrino, Total, Anisotropy, 
         debug)

plot_D25(time_25, 
         hp_f_25, hc_f_25, 
         hp_n_25, hc_n_25, 
         hp_t_25, hc_t_25, 
         ap_25, ac_25, LN_25, 
         theta_25, phi_25, 
         D25, 
         Flow, Neutrino, Total, Anisotropy, 
         debug)

plot_all(time_09, 
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
             Flow, Neutrino, Total, 
             debug)

plot_Ani_D96(time_09, 
             hp_n_09, hc_n_09, 
             ap_09, ac_09, LN_09, 
             theta_09, phi_09, 
             D96, 
             Neutrino,Anisotropy, 
             debug)

plot_Ani_D15(time_15, 
             hp_n_15, hc_n_15, 
             ap_15, ac_15, LN_15, 
             theta_15, phi_15, 
             D15, 
             Neutrino,Anisotropy, 
             debug)

plot_Ani_D25(time_25, 
             hp_n_25, hc_n_25, 
             ap_25, ac_25, LN_25, 
             theta_25, phi_25, 
             D25, 
             Neutrino,Anisotropy, 
             debug)

extract_D96(hp_f_09, hc_f_09, 
            hp_n_09, hc_n_09, 
            hp_t_09, hc_t_09, 
            D96, 
            Flow, Neutrino, Total, 
            debug)

extract_D15(hp_f_15, hc_f_15, 
            hp_n_15, hc_n_15, 
            hp_t_15, hc_t_15, 
            D15, 
            Flow, Neutrino, Total, 
            debug)

extract_D25(hp_f_25, hc_f_25, 
            hp_n_25, hc_n_25, 
            hp_t_25, hc_t_25, 
            D25, 
            Flow, Neutrino, Total, 
            debug)

write_D96(time_09,
              hp_f_09, hc_f_09, 
              hp_n_09, hc_n_09, 
              hp_t_09, hc_t_09,
              theta_09, phi_09,
              output_frequency,
              output_distance, 
              D96, 
              Flow, Neutrino, Total, 
              debug)

write_D15(time_15,
              hp_f_15, hc_f_15, 
              hp_n_15, hc_n_15, 
              hp_t_15, hc_t_15,
              theta_15, phi_15,
              output_frequency,
              output_distance, 
              D15, 
              Flow, Neutrino, Total, 
              debug)

write_D25(time_25,
              hp_f_25, hc_f_25, 
              hp_n_25, hc_n_25, 
              hp_t_25, hc_t_25,
              theta_25, phi_25,
              output_frequency,
              output_distance, 
              D25, 
              Flow, Neutrino, Total, 
              debug)

SNR = plot_ASD(time_09, 
               hp_t_09, hc_t_09,
               time_15, 
               hp_t_15, hc_t_15,
               time_25, 
               hp_t_25, hc_t_25,
               phi_ind,
               theta_ind,
               tmax, 
               frequency,
               f_tail,
               output_distance,
               ASD,
               debug) 

fit_D96(time_09, 
        hp_f_09, hc_f_09, 
        hp_n_09, hc_n_09, 
        theta_09, phi_09, 
        D96, 
        debug)

fit_D15(time_15, 
        hp_f_15, hc_f_15, 
        hp_n_15, hc_n_15, 
        theta_15, phi_15, 
        D15, 
        debug)

fit_D25(time_15, 
        hp_f_15, hc_f_15, 
        hp_n_15, hc_n_15, 
        theta_15, phi_15, 
        D25, 
        debug)


logistic_plot(LOG_Analysis, debug)