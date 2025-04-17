
#######################################################################
# Gravitational Wave Memory from Chimera's D-Series Data Read
#######################################################################
#######################################################################
## House Keeping
#######################################################################
#######################################################################
### Math, Science, and Computing Modules
#######################################################################
import numpy as np
import h5py
#######################################################################
## Data Read and Array Allocation
#######################################################################
#######################################################################
### D9.6-3D
#######################################################################
def read_D96(D96 = True, Flow = True, Neutrino = True, Total = True, debug = True ):
    """
    Reads data for the GW Memory from Chimera's 
    D-Series Core-Collapse Supernovae simulations.

    Includes structure for 
        D9.6-3D

    For GWs sourced from 
        Fluid Flow
        Neutrino Anisotropy
        Linear Combination
    
    Input:
        D96         = True - Read D9.6-3D
        Flow        = True - Read Flow
        Neutrino    = True - Read Neutrino
        Total       = True - Combine Flow and Neutrino
        debug       = True - If True, print when starting
    Output:
        time_09     - Array of time values in miliseconds
        hp_f_09     - Array of h_{+} sourced from Flow
        hc_f_09     - Array of h_{\times} sourced from Flow
        hp_n_09     - Array of h_{+} sourced from Neutrino
        hc_n_09     - Array of h_{\times} sourced from Flow
        hp_t_09     - Array of h_{+} sourced form both
        hc_t_09     - Array of h_{\times} sourced from both
        ap_09       - Array of anisotropy for h_{+}
        ac_09       - Array of anisotropy for h_{\times}
        LN_09       - Array of neutrino number luminosity
        theta_09    - Array of observer angles theta
        phi_09      - Array of observer angles phi
    """
    if D96:
        if debug :
            print("Reading D9.6-3D")
        data_09 = h5py.File("/Users/colterrichardson/Desktop/Research/" + 
                            "Gravitational Waves/Memory_D/Data/" + 
                            "D9.6-3D" + "-Gw.h5", "r")
        
        time_09 = data_09["Time"][:]

        if Flow or Total:
            hp_f_09 = data_09["D hp Flow"][:]
            hc_f_09 = data_09["D hc Flow"][:]
        if Neutrino or Total:
            hp_n_09 = data_09["D hp Neutrino"][:]
            hc_n_09 = data_09["D hc Neutrino"][:]
        if Total:
            hp_t_09 = hp_f_09 + hp_n_09[:,:,:,-1]
            hc_t_09 = hc_f_09 + hc_n_09[:,:,:,-1]
        if Neutrino:
            ap_09 = data_09["alpha_p"][:]
            ac_09 = data_09["alpha_c"][:]

        theta_09    = data_09["Theta Degree"][:]
        phi_09      = data_09["Phi Degree"][:]

        LN_09   = data_09["Neutrino Energy Luminosity"][:]

        data_09.close()
    else:
        time_09 = None
        hp_f_09 = None
        hc_f_09 = None
        hp_n_09 = None
        hc_n_09 = None
        hp_t_09 = None
        hc_t_09 = None
        ap_09 = None
        ac_09 = None
        LN_09 = None
        theta_09 = None 
        phi_09 = None
    return time_09, hp_f_09, hc_f_09, hp_n_09, hc_n_09, hp_t_09, hc_t_09, ap_09, ac_09, LN_09, theta_09, phi_09
#######################################################################
### D15-3D
#######################################################################
def read_D15(D15 = True, Flow = True, Neutrino = True, Total = True, debug = True ):
    """
    Reads data for the GW Memory from Chimera's 
    D-Series Core-Collapse Supernovae simulations.

    Includes structure for 
        D15-3D

    For GWs sourced from 
        Fluid Flow
        Neutrino Anisotropy
        Linear Combination
    
    Input:
        D15         = True - Read D15-3D
        Flow        = True - Read Flow
        Neutrino    = True - Read Neutrino
        Total       = True - Combine Flow and Neutrino
        debug       = True - If True, print when starting
    Output:
        time_15     - Array of time values in miliseconds
        hp_f_15     - Array of h_{+} sourced from Flow
        hc_f_15     - Array of h_{\times} sourced from Flow
        hp_n_15     - Array of h_{+} sourced from Neutrino
        hc_n_15     - Array of h_{\times} sourced from Flow
        hp_t_15     - Array of h_{+} sourced form both
        hc_t_15     - Array of h_{\times} sourced from both
        ap_15       - Array of anisotropy for h_{+}
        ac_15       - Array of anisotropy for h_{\times}
        LN_15       - Array of neutrino number luminosity
        theta_15    - Array of observer angles theta
        phi_15      - Array of observer angles phi
    """
    if D15:
        if debug :
            print("Reading D15-3D")
        data_15 = h5py.File("/Users/colterrichardson/Desktop/Research/" + 
                            "Gravitational Waves/Memory_D/Data/" + 
                            "D15-3D" + "-Gw.h5", "r")

        time_15 = data_15["Time"][:]

        if Flow or Total:
            hp_f_15 = data_15["D hp Flow"][:]
            hc_f_15 = data_15["D hc Flow"][:]
        if Neutrino or Total:
            hp_n_15 = data_15["D hp Neutrino"][:]
            hc_n_15 = data_15["D hc Neutrino"][:]
        if Total:
            hp_t_15 = hp_f_15 + hp_n_15[:,:,:,-1]
            hc_t_15 = hc_f_15 + hc_n_15[:,:,:,-1]
        if Neutrino:
            ap_15 = data_15["alpha_p"][:]
            ac_15 = data_15["alpha_c"][:]

        theta_15    = data_15["Theta Degree"][:]
        phi_15      = data_15["Phi Degree"][:]

        LN_15   = data_15["Neutrino Energy Luminosity"][:]

        data_15.close()
    else:
        time_15 = None
        hp_f_15 = None
        hc_f_15 = None
        hp_n_15 = None
        hc_n_15 = None
        hp_t_15 = None
        hc_t_15 = None
        ap_15 = None
        ac_15 = None
        LN_15 = None
        theta_15 = None 
        phi_15 = None
    return time_15, hp_f_15, hc_f_15, hp_n_15, hc_n_15, hp_t_15, hc_t_15, ap_15, ac_15, LN_15, theta_15, phi_15
#######################################################################
### D25-3D
#######################################################################
def read_D25(D25 = True, Flow = True, Neutrino = True, Total = True, debug = True ):
    """
    Reads data for the GW Memory from Chimera's 
    D-Series Core-Collapse Supernovae simulations.

    Includes structure for 
        D25-3D

    For GWs sourced from 
        Fluid Flow
        Neutrino Anisotropy
        Linear Combination
    
    Input:
        D25         = True - Read D25-3D
        Flow        = True - Read Flow
        Neutrino    = True - Read Neutrino
        Total       = True - Combine Flow and Neutrino
        debug       = True - If True, print when starting
    Output:
        time_25     - Array of time values in miliseconds
        hp_f_25     - Array of h_{+} sourced from Flow
        hc_f_25     - Array of h_{\times} sourced from Flow
        hp_n_25     - Array of h_{+} sourced from Neutrino
        hc_n_25     - Array of h_{\times} sourced from Flow
        hp_t_25     - Array of h_{+} sourced form both
        hc_t_25     - Array of h_{\times} sourced from both
        ap_25       - Array of anisotropy for h_{+}
        ac_25       - Array of anisotropy for h_{\times}
        LN_25       - Array of neutrino number luminosity
        theta_25    - Array of observer angles theta
        phi_25      - Array of observer angles phi
    """
    if D25:
        if debug :
            print("Reading D25-3D")
        data_25 = h5py.File("/Users/colterrichardson/Desktop/Research/" + 
                            "Gravitational Waves/Memory_D/Data/" + 
                            "D25-3D" + "-Gw.h5", "r")

        time_25 = data_25["Time"][:]

        if Flow or Total:
            hp_f_25 = data_25["D hp Flow"][:]
            hc_f_25 = data_25["D hc Flow"][:]
        if Neutrino or Total:
            hp_n_25 = data_25["D hp Neutrino"][:]
            hc_n_25 = data_25["D hc Neutrino"][:]
        if Total:
            hp_t_25 = hp_f_25 + hp_n_25[:,:,:,-1]
            hc_t_25 = hc_f_25 + hc_n_25[:,:,:,-1]
        if Neutrino:
            ap_25 = data_25["alpha_p"][:]
            ac_25 = data_25["alpha_c"][:]

        theta_25    = data_25["Theta Degree"][:]
        phi_25      = data_25["Phi Degree"][:]

        LN_25   = data_25["Neutrino Energy Luminosity"][:]

        data_25.close()
    else:
        time_25 = None
        hp_f_25 = None
        hc_f_25 = None
        hp_n_25 = None
        hc_n_25 = None
        hp_t_25 = None
        hc_t_25 = None
        ap_25 = None
        ac_25 = None
        LN_25 = None
        theta_25 = None 
        phi_25 = None
    return time_25, hp_f_25, hc_f_25, hp_n_25, hc_n_25, hp_t_25, hc_t_25, ap_25, ac_25, LN_25, theta_25, phi_25