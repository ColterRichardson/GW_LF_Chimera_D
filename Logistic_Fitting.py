#######################################################################
# Gravitational Wave Memory from Chimera's D-Series Logistic Fitting
#######################################################################
#######################################################################
## House Keeping
#######################################################################
#######################################################################
### Math, Science, and Computing Modules
#######################################################################
import scipy as sp
import numpy as np
import warnings
warnings.filterwarnings("ignore")
#######################################################################
### Definitions
#######################################################################
def Logistic(x, x0, k, L):
    """
    Define template for the memory signal
    
    Input:
        x   - 
        x0  - center of ramp-up
        k   - ramp-up frequency
        L   - saturation value
    Output:
        y   - $\frac{L}{1 + e^{-k (x - x_{0})}}$
    """

    y = L / (1 + np.exp(-k * (x - x0)))

    return y
#######################################################################
## Logistic Fitting
#######################################################################
#######################################################################
### D9.6-3D
#######################################################################
def fit_D96(time_09, 
            hp_f_09, hc_f_09, 
            hp_n_09, hc_n_09, 
            hp_t_09, hc_t_09, 
            theta_09, phi_09, 
            D96 = True, 
            debug = False):

    t0_09_p_f    = np.empty((len(theta_09), len(phi_09)))
    k_09_p_f     = np.empty((len(theta_09), len(phi_09)))
    L_09_p_f     = np.empty((len(theta_09), len(phi_09)))

    t0_09_c_f    = np.empty((len(theta_09), len(phi_09)))
    k_09_c_f     = np.empty((len(theta_09), len(phi_09)))
    L_09_c_f     = np.empty((len(theta_09), len(phi_09)))

    t0_09_p_n    = np.empty((len(theta_09), len(phi_09)))
    k_09_p_n     = np.empty((len(theta_09), len(phi_09)))
    L_09_p_n     = np.empty((len(theta_09), len(phi_09)))

    t0_09_c_n    = np.empty((len(theta_09), len(phi_09)))
    k_09_c_n     = np.empty((len(theta_09), len(phi_09)))
    L_09_c_n     = np.empty((len(theta_09), len(phi_09)))

    t0_09_c_t    = np.empty((len(theta_09), len(phi_09)))
    k_09_c_t     = np.empty((len(theta_09), len(phi_09)))
    L_09_c_t     = np.empty((len(theta_09), len(phi_09)))

    t0_09_p_t    = np.empty((len(theta_09), len(phi_09)))
    k_09_p_t     = np.empty((len(theta_09), len(phi_09)))
    L_09_p_t     = np.empty((len(theta_09), len(phi_09)))

    if D96:

        Logistic_bounds_09 = ([0, 0, -10], [0.4, 200, 10])

        for t in range(len(theta_09)):
            for p in range(len(phi_09)):
                if debug:
                    print("theta_" + str(int(theta_09[t])) + "_phi_" + str(int(phi_09[p])))
                hpD_f = hp_f_09[:,p,t]
                hcD_f = hc_f_09[:,p,t]

                hpD_n = hp_n_09[:,p,t,4]
                hcD_n = hc_n_09[:,p,t,4]

                hpD_t = hpD_f + hpD_n
                hcD_t = hcD_f + hcD_n
#######################################################################
#### Flow Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic, 
                                        time_09 / 1000, 
                                        hpD_f, 
                                        bounds = Logistic_bounds_09, 
                                        p0 = [0.3, 30, 0.5])

                    t0_09_p_f[t,p]   = popt_plus[0]
                    k_09_p_f[t,p]    = popt_plus[1]
                    L_09_p_f[t,p]    = popt_plus[2]
                except:
                    t0_09_p_f[t,p]   = np.nan
                    k_09_p_f[t,p]    = np.nan
                    L_09_p_f[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_09 / 1000, 
                                            hcD_f, 
                                            bounds = Logistic_bounds_09, 
                                            p0 = [0.3, 30, 0.5])

                    t0_09_c_f[t,p]   = popt_cross[0]
                    k_09_c_f[t,p]    = popt_cross[1]
                    L_09_c_f[t,p]    = popt_cross[2]

                except:
                    t0_09_c_f[t,p]   = np.nan
                    k_09_c_f[t,p]    = np.nan
                    L_09_c_f[t,p]    = np.nan
#######################################################################
#### Neutrino Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic, 
                                        time_09 / 1000, 
                                        hpD_n, 
                                        bounds = Logistic_bounds_09, 
                                        p0 = [0.3, 30, 0.5])

                    t0_09_p_n[t,p]   = popt_plus[0]
                    k_09_p_n[t,p]    = popt_plus[1]
                    L_09_p_n[t,p]    = popt_plus[2]
                except:
                    t0_09_p_n[t,p]   = np.nan
                    k_09_p_n[t,p]    = np.nan
                    L_09_p_n[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_09 / 1000, 
                                            hcD_n, 
                                            bounds = Logistic_bounds_09, 
                                            p0 = [0.3, 30, 0.5])

                    t0_09_c_n[t,p]   = popt_cross[0]
                    k_09_c_n[t,p]    = popt_cross[1]
                    L_09_c_n[t,p]    = popt_cross[2]

                except:
                    t0_09_c_n[t,p]   = np.nan
                    k_09_c_n[t,p]    = np.nan
                    L_09_c_n[t,p]    = np.nan
#######################################################################
#### Total Fit
#######################################################################
                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_09 / 1000, 
                                            hpD_t, 
                                            bounds = Logistic_bounds_09, 
                                            p0 = [0.3, 30, 0.5])

                    t0_09_p_t[t,p]   = popt_cross[0]
                    k_09_p_t[t,p]    = popt_cross[1]
                    L_09_p_t[t,p]    = popt_cross[2]

                except:
                    t0_09_p_t[t,p]   = np.nan
                    k_09_p_t[t,p]    = np.nan
                    L_09_p_t[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_09 / 1000, 
                                            hcD_t, 
                                            bounds = Logistic_bounds_09, 
                                            p0 = [0.3, 30, 0.5])

                    t0_09_c_t[t,p]   = popt_cross[0]
                    k_09_c_t[t,p]    = popt_cross[1]
                    L_09_c_t[t,p]    = popt_cross[2]

                except:
                    t0_09_c_t[t,p]   = np.nan
                    k_09_c_t[t,p]    = np.nan
                    L_09_c_t[t,p]    = np.nan
#######################################################################
#### Flow Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_t0_p_f.txt", t0_09_p_f )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_t0_c_f.txt", t0_09_c_f )

        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_L_p_f.txt", L_09_p_f )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_L_c_f.txt", L_09_c_f )

        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_p_f.txt", k_09_p_f )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_c_f.txt", k_09_c_f )
#######################################################################
#### Neutrino Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_t0_p_n.txt", t0_09_p_n )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_t0_c_n.txt", t0_09_c_n )

        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_L_p_n.txt", L_09_p_n )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_L_c_n.txt", L_09_c_n )

        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_p_n.txt", k_09_p_n )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_c_n.txt", k_09_c_n )
#######################################################################
#### Total Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_t0_p_t.txt", t0_09_p_t )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_t0_c_t.txt", t0_09_c_t )

        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_L_p_t.txt", L_09_p_t )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_L_c_t.txt", L_09_c_t )

        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_p_t.txt", k_09_p_t )
        np.savetxt("Data/Logistic_Fit/D9.6-3D/D9.6-3D_k_c_t.txt", k_09_c_t )

        print(f"{str("D9.6-3D"):11} {str("hp"):6} {str("hc"):6}")
        print(f"{str("Flow"):10} {np.round(np.nanmean(k_09_p_f),2):6} {np.round(np.nanmean(k_09_c_f),2):6}")
        print(f"{str("Neutrino"):10} {np.round(np.nanmean(k_09_p_n),2):6} {np.round(np.nanmean(k_09_c_n),2):6}")
        print(f"{str("Total"):10} {np.round(np.nanmean(k_09_p_t),2):6} {np.round(np.nanmean(k_09_c_t),2):6}")
    return None
#######################################################################
### D15-3D
#######################################################################
def fit_D15(time_15, 
            hp_f_15, hc_f_15, 
            hp_n_15, hc_n_15, 
            hp_t_15, hc_t_15, 
            theta_15, phi_15, 
            D15 = True, 
            debug = False):

    t0_15_p_f    = np.empty((len(theta_15), len(phi_15)))
    k_15_p_f     = np.empty((len(theta_15), len(phi_15)))
    L_15_p_f     = np.empty((len(theta_15), len(phi_15)))

    t0_15_c_f    = np.empty((len(theta_15), len(phi_15)))
    k_15_c_f     = np.empty((len(theta_15), len(phi_15)))
    L_15_c_f     = np.empty((len(theta_15), len(phi_15)))

    t0_15_p_n    = np.empty((len(theta_15), len(phi_15)))
    k_15_p_n     = np.empty((len(theta_15), len(phi_15)))
    L_15_p_n     = np.empty((len(theta_15), len(phi_15)))

    t0_15_c_n    = np.empty((len(theta_15), len(phi_15)))
    k_15_c_n     = np.empty((len(theta_15), len(phi_15)))
    L_15_c_n     = np.empty((len(theta_15), len(phi_15)))

    t0_15_p_t    = np.empty((len(theta_15), len(phi_15)))
    k_15_p_t     = np.empty((len(theta_15), len(phi_15)))
    L_15_p_t     = np.empty((len(theta_15), len(phi_15)))

    t0_15_c_t    = np.empty((len(theta_15), len(phi_15)))
    k_15_c_t     = np.empty((len(theta_15), len(phi_15)))
    L_15_c_t     = np.empty((len(theta_15), len(phi_15)))


    if D15:

        Logistic_bounds_15 = ([0, 0, -20], [0.8, 200, 20])

        for t in range(len(theta_15)):
            for p in range(len(phi_15)):
                if debug:
                    print("theta_" + str(int(theta_15[t])) + "_phi_" + str(int(phi_15[p])))

                hpD_f = hp_f_15[:,p,t]
                hcD_f = hc_f_15[:,p,t]

                hpD_n = hp_n_15[:,p,t,4]
                hcD_n = hc_n_15[:,p,t,4]

                hpD_t = hpD_f + hpD_n
                hcD_t = hcD_f + hcD_n
#######################################################################
#### Flow Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic, time_15 / 1000, 
                                        hpD_f, 
                                        bounds = Logistic_bounds_15, 
                                        p0 = [0.3, 30, 0.5])

                    t0_15_p_f[t,p]   = popt_plus[0]
                    k_15_p_f[t,p]    = popt_plus[1]
                    L_15_p_f[t,p]    = popt_plus[2]
                except:
                    t0_15_p_f[t,p]   = np.nan
                    k_15_p_f[t,p]    = np.nan
                    L_15_p_f[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_15 / 1000,
                                            hcD_f, 
                                            bounds = Logistic_bounds_15, 
                                            p0 = [0.3, 30, 0.5])

                    t0_15_c_f[t,p]   = popt_cross[0]
                    k_15_c_f[t,p]    = popt_cross[1]
                    L_15_c_f[t,p]    = popt_cross[2]

                except:
                    t0_15_c_f[t,p]   = np.nan
                    k_15_c_f[t,p]    = np.nan
                    L_15_c_f[t,p]    = np.nan
#######################################################################
#### Neutrino Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic, 
                                        time_15 / 1000,
                                        hpD_n, 
                                        bounds = Logistic_bounds_15,
                                        p0 = [0.3, 30, 0.5])

                    t0_15_p_n[t,p]   = popt_plus[0]
                    k_15_p_n[t,p]    = popt_plus[1]
                    L_15_p_n[t,p]    = popt_plus[2]
                except:
                    t0_15_p_n[t,p]   = np.nan
                    k_15_p_n[t,p]    = np.nan
                    L_15_p_n[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_15 / 1000,
                                            hcD_n, 
                                            bounds = Logistic_bounds_15, 
                                            p0 = [0.3, 30, 0.5])

                    t0_15_c_n[t,p]   = popt_cross[0]
                    k_15_c_n[t,p]    = popt_cross[1]
                    L_15_c_n[t,p]    = popt_cross[2]

                except:
                    t0_15_c_n[t,p]   = np.nan
                    k_15_c_n[t,p]    = np.nan
                    L_15_c_n[t,p]    = np.nan
#######################################################################
#### Total Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic, 
                                        time_15 / 1000, 
                                        hpD_t, 
                                        bounds = Logistic_bounds_15, 
                                        p0 = [0.3, 30, 0.5])

                    t0_15_p_t[t,p]   = popt_plus[0]
                    k_15_p_t[t,p]    = popt_plus[1]
                    L_15_p_t[t,p]    = popt_plus[2]
                except:
                    t0_15_p_t[t,p]   = np.nan
                    k_15_p_t[t,p]    = np.nan
                    L_15_p_t[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_15 / 1000, 
                                            hcD_t, 
                                            bounds = Logistic_bounds_15, 
                                            p0 = [0.3, 30, 0.5])

                    t0_15_c_t[t,p]   = popt_cross[0]
                    k_15_c_t[t,p]    = popt_cross[1]
                    L_15_c_t[t,p]    = popt_cross[2]

                except:
                    t0_15_c_t[t,p]   = np.nan
                    k_15_c_t[t,p]    = np.nan
                    L_15_c_t[t,p]    = np.nan
#######################################################################
#### Flow Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_t0_p_f.txt", t0_15_p_f )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_t0_c_f.txt", t0_15_c_f )

        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_L_p_f.txt", L_15_p_f )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_L_c_f.txt", L_15_c_f )

        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_k_p_f.txt", k_15_p_f )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_k_c_f.txt", k_15_c_f )
#######################################################################
#### Neutrino Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_t0_p_n.txt", t0_15_p_n )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_t0_c_n.txt", t0_15_c_n )

        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_L_p_n.txt", L_15_p_n )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_L_c_n.txt", L_15_c_n )

        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_k_p_n.txt", k_15_p_n )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_k_c_n.txt", k_15_c_n )
#######################################################################
#### Total Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_t0_p_t.txt", t0_15_p_t )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_t0_c_t.txt", t0_15_c_t )

        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_L_p_t.txt", L_15_p_t )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_L_c_t.txt", L_15_c_t )

        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_k_p_t.txt", k_15_p_t )
        np.savetxt("Data/Logistic_Fit/D15-3D/D15-3D_k_c_t.txt", k_15_c_t )
        
        print(f"{str("D15-3D"):11} {str("hp"):6} {str("hc"):6}")
        print(f"{str("Flow"):10} {np.round(np.nanmean(k_15_p_f),2):6} {np.round(np.nanmean(k_15_c_f),2):6}")
        print(f"{str("Neutrino"):10} {np.round(np.nanmean(k_15_p_n),2):6} {np.round(np.nanmean(k_15_c_n),2):6}")
        print(f"{str("Total"):10} {np.round(np.nanmean(k_15_p_t),2):6} {np.round(np.nanmean(k_15_c_t),2):6}")
    return None
#######################################################################
### D25-3D
#######################################################################
def fit_D25(time_25, 
            hp_f_25, hc_f_25, 
            hp_n_25, hc_n_25, 
            hp_t_25, hc_t_25, 
            theta_25, phi_25, 
            D25 = True, 
            debug = False):
        
    t0_25_p_f    = np.empty((len(theta_25), len(phi_25)))
    k_25_p_f     = np.empty((len(theta_25), len(phi_25)))
    L_25_p_f     = np.empty((len(theta_25), len(phi_25)))

    t0_25_c_f    = np.empty((len(theta_25), len(phi_25)))
    k_25_c_f     = np.empty((len(theta_25), len(phi_25)))
    L_25_c_f     = np.empty((len(theta_25), len(phi_25)))

    t0_25_p_n    = np.empty((len(theta_25), len(phi_25)))
    k_25_p_n     = np.empty((len(theta_25), len(phi_25)))
    L_25_p_n     = np.empty((len(theta_25), len(phi_25)))

    t0_25_c_n    = np.empty((len(theta_25), len(phi_25)))
    k_25_c_n     = np.empty((len(theta_25), len(phi_25)))
    L_25_c_n     = np.empty((len(theta_25), len(phi_25)))

    t0_25_p_t    = np.empty((len(theta_25), len(phi_25)))
    k_25_p_t     = np.empty((len(theta_25), len(phi_25)))
    L_25_p_t     = np.empty((len(theta_25), len(phi_25)))

    t0_25_c_t    = np.empty((len(theta_25), len(phi_25)))
    k_25_c_t     = np.empty((len(theta_25), len(phi_25)))
    L_25_c_t     = np.empty((len(theta_25), len(phi_25)))

    if D25:

        Logistic_bounds_25 = ([0, 0, -20], [0.8, 200, 20])

        for t in range(len(theta_25)):
            for p in range(len(phi_25)):
                if debug:
                    print("theta_" + str(int(theta_25[t])) +
                        "_phi_" + str(int(phi_25[p])))

                hpD_f = hp_f_25[:,p,t]
                hcD_f = hc_f_25[:,p,t]

                hpD_n = hp_n_25[:,p,t,4]
                hcD_n = hc_n_25[:,p,t,4]

                hpD_t = hpD_f + hpD_n
                hcD_t = hcD_f + hcD_n
#######################################################################
#### Flow Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic, 
                                        time_25 / 1000, 
                                        hpD_f, 
                                        bounds = Logistic_bounds_25, 
                                        p0 = [0.3, 30, 0.5])

                    t0_25_p_f[t,p]   = popt_plus[0]
                    k_25_p_f[t,p]    = popt_plus[1]
                    L_25_p_f[t,p]    = popt_plus[2]
                except:
                    t0_25_p_f[t,p]   = np.nan
                    k_25_p_f[t,p]    = np.nan
                    L_25_p_f[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_25 / 1000, 
                                            hcD_f, 
                                            bounds = Logistic_bounds_25, 
                                            p0 = [0.3, 30, 0.5])

                    t0_25_c_f[t,p]   = popt_cross[0]
                    k_25_c_f[t,p]    = popt_cross[1]
                    L_25_c_f[t,p]    = popt_cross[2]

                except:
                    t0_25_c_f[t,p]   = np.nan
                    k_25_c_f[t,p]    = np.nan
                    L_25_c_f[t,p]    = np.nan
#######################################################################
#### Neutrino Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic,
                                        time_25 / 1000,
                                        hpD_n, 
                                        bounds = Logistic_bounds_25, 
                                        p0 = [0.3, 30, 0.5])

                    t0_25_p_n[t,p]   = popt_plus[0]
                    k_25_p_n[t,p]    = popt_plus[1]
                    L_25_p_n[t,p]    = popt_plus[2]
                except:
                    t0_25_p_n[t,p]   = np.nan
                    k_25_p_n[t,p]    = np.nan
                    L_25_p_n[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_25 / 1000, 
                                            hcD_n, 
                                            bounds = Logistic_bounds_25, 
                                            p0 = [0.3, 30, 0.5])

                    t0_25_c_n[t,p]   = popt_cross[0]
                    k_25_c_n[t,p]    = popt_cross[1]
                    L_25_c_n[t,p]    = popt_cross[2]

                except:
                    t0_25_c_n[t,p]   = np.nan
                    k_25_c_n[t,p]    = np.nan
                    L_25_c_n[t,p]    = np.nan
#######################################################################
#### Total Fit
#######################################################################
                try:
                    popt_plus, pcov_plus = sp.optimize.curve_fit(
                                        Logistic, 
                                        time_25 / 1000, 
                                        hpD_t,
                                        bounds = Logistic_bounds_25, 
                                        p0 = [0.3, 30, 0.5])

                    t0_25_p_t[t,p]   = popt_plus[0]
                    k_25_p_t[t,p]    = popt_plus[1]
                    L_25_p_t[t,p]    = popt_plus[2]
                except:
                    t0_25_p_t[t,p]   = np.nan
                    k_25_p_t[t,p]    = np.nan
                    L_25_p_t[t,p]    = np.nan

                try:
                    popt_cross, pcov_cross = sp.optimize.curve_fit(
                                            Logistic, 
                                            time_25 / 1000, 
                                            hcD_t, 
                                            bounds = Logistic_bounds_25, 
                                            p0 = [0.3, 30, 0.5])

                    t0_25_c_t[t,p]   = popt_cross[0]
                    k_25_c_t[t,p]    = popt_cross[1]
                    L_25_c_t[t,p]    = popt_cross[2]

                except:
                    t0_25_c_t[t,p]   = np.nan
                    k_25_c_t[t,p]    = np.nan
                    L_25_c_t[t,p]    = np.nan
#######################################################################
#### Flow Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_t0_p_f.txt", t0_25_p_f )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_t0_c_f.txt", t0_25_c_f )

        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_L_p_f.txt", L_25_p_f )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_L_c_f.txt", L_25_c_f )

        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_k_p_f.txt", k_25_p_f )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_k_c_f.txt", k_25_c_f )
#######################################################################
#### Neutrino Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_t0_p_n.txt", t0_25_p_n )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_t0_c_n.txt", t0_25_c_n )

        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_L_p_n.txt", L_25_p_n )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_L_c_n.txt", L_25_c_n )

        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_k_p_n.txt", k_25_p_n )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_k_c_n.txt", k_25_c_n )
#######################################################################
#### Total Write
#######################################################################
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_t0_p_t.txt", t0_25_p_t )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_t0_c_t.txt", t0_25_c_t )

        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_L_p_t.txt", L_25_p_t )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_L_c_t.txt", L_25_c_t )

        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_k_p_t.txt", k_25_p_t )
        np.savetxt("Data/Logistic_Fit/D25-3D/D25-3D_k_c_t.txt", k_25_c_t )

        print(f"{str("D25-3D"):11} {str("hp"):6} {str("hc"):6}")
        print(f"{str("Flow"):10} {np.round(np.nanmean(k_25_p_f),2):6} {np.round(np.nanmean(k_25_c_f),2):6}")
        print(f"{str("Neutrino"):10} {np.round(np.nanmean(k_25_p_n),2):6} {np.round(np.nanmean(k_25_c_n),2):6}")
        print(f"{str("Total"):10} {np.round(np.nanmean(k_25_p_t),2):6} {np.round(np.nanmean(k_25_c_t),2):6}")

    return None