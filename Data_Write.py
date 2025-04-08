#######################################################################
# Gravitational Wave Memory from Chimera's D-Series txt Output
#######################################################################
#######################################################################
## House Keeping
#######################################################################
#######################################################################
### Math, Science, and Computing Modules
#######################################################################
from scipy import interpolate
import numpy as np
#######################################################################
### Constants
#######################################################################
cm2kpc = 3.24078e-22
#######################################################################
### Definitions
#######################################################################
def sn_resample_wave(t,h,fs):
    """
    Interpolate array h to the fs sampling frequency.
    
    Input:
        t  - time array, in seconds
        h  - strain array to be interpolated
        fs - sampling frequency
    Output:
        t1 - time array, after resampling
        h1 - new strain array
    """
    
    # Quick check
    if len(t)!=len(h):
        print("Error: t and h need to have equal sizes")
        return 0
    
    # Define new time with fs
    t1 = np.arange(t[0],t[-1],1.0/fs)
    
    # Interpolation
    tck = interpolate.splrep(t,h,s=0)
    h1  = interpolate.splev(t1,tck,der=0)
    
    return t1, h1
#######################################################################        
## D9.6-3D
#######################################################################
def write_D96(time_09,
              hp_f_09, hc_f_09, 
              hp_n_09, hc_n_09, 
              hp_t_09, hc_t_09,
              theta_09, phi_09,
              output_frequency = 16384,
              output_distance = 10, 
              D96 = True, 
              Flow = True, Neutrino = True, Total = True, 
              debug = False):
    if D96:
        if debug :
            print("Writting D9.6-3D")
        count = 0
        size_arr = (len(theta_09) * len(phi_09))
        for t in range(len(theta_09)):
            for p in range(len(phi_09)):
                count += 1
                ###########################################################
                if debug:
                    print("Writting D9.6-3D: {:.2f} %".format(count/size_arr * 100))
                ###########################################################
                theta_str = str(int(theta_09[t])).zfill(3)
                phi_str = str(int(phi_09[p])).zfill(4)
#######################################################################
### Flow Write
#######################################################################
                if Flow:
                    ti, hp = sn_resample_wave(time_09 / 1000, hp_f_09[:,p,t], output_frequency)
                    ti, hc = sn_resample_wave(time_09 / 1000, hc_f_09[:,p,t], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D9.6-3D/Flow/D9.6-3D_hp_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D9.6-3D/Flow/D9.6-3D_hc_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D9.6-3D/Flow/D9.6-3D_ht_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
#######################################################################
### Neutrino Write
#######################################################################
                if Neutrino:
                    ti, hp = sn_resample_wave(time_09 / 1000, hp_n_09[:,p,t,4], output_frequency)
                    ti, hc = sn_resample_wave(time_09 / 1000, hc_n_09[:,p,t,4], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D9.6-3D/Neutrino/D9.6-3D_hp_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D9.6-3D/Neutrino/D9.6-3D_hc_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D9.6-3D/Neutrino/D9.6-3D_ht_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
#######################################################################
### Total Write
#######################################################################
                if Total:
                    ti, hp = sn_resample_wave(time_09 / 1000, hp_t_09[:,p,t], output_frequency)
                    ti, hc = sn_resample_wave(time_09 / 1000, hc_t_09[:,p,t], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D9.6-3D/Total/D9.6-3D_hp_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D9.6-3D/Total/D9.6-3D_hc_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D9.6-3D/Total/D9.6-3D_ht_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
    return None
#######################################################################
## D15-3D
#######################################################################
def write_D15(time_15,
              hp_f_15, hc_f_15, 
              hp_n_15, hc_n_15, 
              hp_t_15, hc_t_15,
              theta_15, phi_15,
              output_frequency = 16384,
              output_distance = 10, 
              D15 = True, 
              Flow = True, Neutrino = True, Total = True, 
              debug = False):
    if D15:
        count = 0
        size_arr = (len(theta_15) * len(phi_15))
        for t in range(len(theta_15)):
            for p in range(len(phi_15)):
                count += 1
                ###########################################################
                if debug:
                    print("Writting D15-3D: {:.2f} %".format(count/size_arr * 100))
                ###########################################################

                theta_str = str(int(theta_15[t])).zfill(3)
                phi_str = str(int(phi_15[p])).zfill(4)
#######################################################################
### Flow Write
#######################################################################
                if Flow:
                    ti, hp = sn_resample_wave(time_15 / 1000, hp_f_15[:,p,t], output_frequency)
                    ti, hc = sn_resample_wave(time_15 / 1000, hc_f_15[:,p,t], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D15-3D/Flow/D15-3D_hp_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D15-3D/Flow/D15-3D_hc_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D15-3D/Flow/D15-3D_ht_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
#######################################################################
### Neutrino Write
#######################################################################
                if Neutrino:
                    ti, hp = sn_resample_wave(time_15 / 1000, hp_n_15[:,p,t,4], output_frequency)
                    ti, hc = sn_resample_wave(time_15 / 1000, hc_n_15[:,p,t,4], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D15-3D/Neutrino/D15-3D_hp_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D15-3D/Neutrino/D15-3D_hc_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D15-3D/Neutrino/D15-3D_ht_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
#######################################################################
### Total Write
#######################################################################
                if Total:
                    ti, hp = sn_resample_wave(time_15 / 1000, hp_t_15[:,p,t], output_frequency)
                    ti, hc = sn_resample_wave(time_15 / 1000, hc_t_15[:,p,t], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D15-3D/Total/D15-3D_hp_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D15-3D/Total/D15-3D_hc_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D15-3D/Total/D15-3D_ht_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
    return None
#######################################################################
## D25-3D
#######################################################################
def write_D25(time_25,
              hp_f_25, hc_f_25, 
              hp_n_25, hc_n_25, 
              hp_t_25, hc_t_25,
              theta_25, phi_25,
              output_frequency = 16384,
              output_distance = 10, 
              D25 = True, 
              Flow = True, Neutrino = True, Total = True, 
              debug = False):
    if D25:
        count = 0
        size_arr = (len(theta_25) * len(phi_25))
        for t in range(len(theta_25)):
            for p in range(len(phi_25)):
                count += 1
                ###########################################################
                if debug:
                    print("Writting D25-3D: {:.2f} %".format(count/size_arr * 100))
                ###########################################################

                theta_str = str(int(theta_25[t])).zfill(3)
                phi_str = str(int(phi_25[p])).zfill(4)
#######################################################################
### Flow Write
#######################################################################
                if Flow:
                    ti, hp = sn_resample_wave(time_25 / 1000, hp_f_25[:,p,t], output_frequency)
                    ti, hc = sn_resample_wave(time_25 / 1000, hc_f_25[:,p,t], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D25-3D/Flow/D25-3D_hp_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D25-3D/Flow/D25-3D_hc_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D25-3D/Flow/D25-3D_ht_flow_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
#######################################################################
### Neutrino Write
#######################################################################
                if Neutrino:
                    ti, hp = sn_resample_wave(time_25 / 1000, hp_n_25[:,p,t,4], output_frequency)
                    ti, hc = sn_resample_wave(time_25 / 1000, hc_n_25[:,p,t,4], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D25-3D/Neutrino/D25-3D_hp_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D25-3D/Neutrino/D25-3D_hc_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D25-3D/Neutrino/D25-3D_ht_neutrino_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)
#######################################################################
### Total Write
#######################################################################
                if Total:
                    ti, hp = sn_resample_wave(time_25 / 1000, hp_t_25[:,p,t], output_frequency)
                    ti, hc = sn_resample_wave(time_25 / 1000, hc_t_25[:,p,t], output_frequency)
                    ht = np.sqrt(hp**2 + hc**2)

                    hp *= cm2kpc / output_distance
                    hc *= cm2kpc / output_distance
                    ht *= cm2kpc / output_distance

                    np.savetxt("Data/Waveforms/D25-3D/Total/D25-3D_hp_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hp)
                    np.savetxt("Data/Waveforms/D25-3D/Total/D25-3D_hc_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            hc)
                    np.savetxt("Data/Waveforms/D25-3D/Total/D25-3D_ht_total_" 
                            + phi_str + "_" + theta_str + "_" + 
                            str(output_frequency) + "Hz_" + 
                            str(output_distance).zfill(3) + "kpc.txt",
                            ht)     
    return None