#######################################################################
# Gravitational Wave Memory from Chimera's D-Series Tappering and ASD
#######################################################################
#######################################################################
## House Keeping
#######################################################################
#######################################################################
### Math, Science, and Computing Modules
#######################################################################
import scipy as sp
from scipy import interpolate, fftpack
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
#### Plotting Definitions
#######################################################################
def draw_grid(ax):
   ax.grid(which = "both")
   ax.minorticks_on()
   ax.grid(visible =True, which='minor', color='#999999', 
           linestyle='-', alpha=0.2) 
   return
def draw_prelim(ax):
   ax.text(0.5, 0.5, 'Preliminary', transform=ax.transAxes, 
           fontsize=60, color='gray', alpha=0.5, ha='center', 
           va='center', rotation=30)
   return
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
def sn_fft_wave(t,h):
    """
    Fourier transform of the h array.
    Time array need to be evenly spaced
    
    Input:
        t - time array
        h - strain array
    Output:
        f - frequency array
        H - one-sided FFT with doubled amplitudes
    """
    dt = t[1] - t[0]
    
    # Fourier Transform
    H = dt*fftpack.fft(h)
    f = fftpack.fftfreq(len(t),dt)
    
    # shift frequencies and data into normal order
    f = fftpack.fftshift(f)
    H = fftpack.fftshift(H)
    
    # use only real data from n/2+1 (freq>0) to n-1
    # double- to one-sided
    n = len(f)
    f =     f[int(n/2)+1:n-1]
    H = 2.0*H[int(n/2)+1:n-1]
    
    return f, H
def sn_snr_wave(f,H,fasd,asd):
    """
    Calculate signal-to-noise ratio for a given waveform and Amplitude Spectral Density (ASD)
    General equation for two-sided fft:
    
    SNR^2 = 4 * int_0^infty ( |h(f)|^2 / Sn(f) df)
    
    Below we drop factor of '4' because sn_fft() function already calculates one-sided fft.
    
    Input:
        t - time array
        h - strain array
        fasd - frequency array for noise ASD
        asd  - array of noise ASD
    Output:
        snr - signal-to-noise ratio
    """
    
    # Do fft of a waveform
    FFT = abs(H)
    
    # Adjust fft array to asd array
    tck = interpolate.splrep(fasd,asd,s=0)
    asd = interpolate.splev(f,tck,der=0) 

    df = f[2]-f[1]
    psd = asd**2
    
    # Calculate SNR
    snrsq = sum(FFT**2/psd)*df
    snr = np.sqrt(snrsq)

    return snr
#######################################################################
## Tapering and Power Spectral Density
#######################################################################      
def plot_ASD(time_09, 
             hp_t_09, hc_t_09,
             time_15, 
             hp_t_15, hc_t_15,
             time_25, 
             hp_t_25, hc_t_25,
             phi_ind = 0,
             theta_ind = 0,
             tmax = 3, 
             frequency = 16384,
             f_tail = 1/2,
             output_distance = 1,
             debug = False):      
#######################################################################        
### D9.6-3D
#######################################################################
    dt = 1 / frequency
    if debug :
        print("Extending D9.6-3D")

    hp = hp_t_09[:,phi_ind, theta_ind]
    hc = hc_t_09[:,phi_ind, theta_ind]

    time_new = np.arange(0,tmax,dt) 

    hp_ext      = np.zeros(len(time_new))
    hc_ext      = np.zeros(len(time_new))
    hp_ext_fit  = np.zeros(len(time_new))
    hc_ext_fit  = np.zeros(len(time_new))

    ti, hpp = sn_resample_wave(time_09 / 1000, hp, frequency)
    ti, hcp = sn_resample_wave(time_09 / 1000, hc, frequency)

    hp_mem = hp[-1]
    hc_mem = hc[-1]
 
    hp_ext[:len(hpp)] = hpp
    hc_ext[:len(hcp)] = hcp

    hp_ext[len(hpp):] = 1.0 / 2.0 * (hp_mem + hp_mem * np.cos(2 * np.pi * f_tail * (time_new[len(hpp):]-time_09[-1] / 1000)))
    hc_ext[len(hcp):] = 1.0 / 2.0 * (hc_mem + hc_mem * np.cos(2 * np.pi * f_tail * (time_new[len(hcp):]-time_09[-1] / 1000)))
    
    for t in range(len(ti), len(time_new)):
        if abs(hp_ext[t]) < 0.00001:
            hp_ext[t:] = 0
            hc_ext[t:] = 0
            break
    f_09, Hp_09 = sn_fft_wave(time_new, hp_ext)
    f_09, Hc_09 = sn_fft_wave(time_new, hc_ext)

#######################################################################        
### D15-3D
#######################################################################
    if debug :
        print("Extending D15-3D")

    hp = hp_t_15[:,phi_ind, theta_ind]
    hc = hc_t_15[:,phi_ind, theta_ind]

    time_new = np.arange(0,tmax,dt) 

    hp_ext      = np.zeros(len(time_new))
    hc_ext      = np.zeros(len(time_new))
    hp_ext_fit  = np.zeros(len(time_new))
    hc_ext_fit  = np.zeros(len(time_new))

    ti, hpp = sn_resample_wave(time_15 / 1000, hp, frequency)
    ti, hcp = sn_resample_wave(time_15 / 1000, hc, frequency)

    hp_mem = hp[-1]
    hc_mem = hc[-1]
 
    hp_ext[:len(hpp)] = hpp
    hc_ext[:len(hcp)] = hcp

    hp_ext[len(hpp):] = 1.0 / 2.0 * (hp_mem + hp_mem * np.cos(2 * np.pi * f_tail * (time_new[len(hpp):]-time_15[-1] / 1000)))
    hc_ext[len(hcp):] = 1.0 / 2.0 * (hc_mem + hc_mem * np.cos(2 * np.pi * f_tail * (time_new[len(hcp):]-time_15[-1] / 1000)))
    
    for t in range(len(ti), len(time_new)):
        if abs(hp_ext[t]) < 0.00001:
            hp_ext[t:] = 0
            hc_ext[t:] = 0
            break

    f_15, Hp_15 = sn_fft_wave(time_new, hp_ext)
    f_15, Hc_15 = sn_fft_wave(time_new, hc_ext)
#######################################################################        
### D25-3D
#######################################################################
#######################################################################        
#### Total
#######################################################################
    if debug :
        print("Extending D25-3D")

    hp = hp_t_25[:,phi_ind, theta_ind]
    hc = hc_t_25[:,phi_ind, theta_ind]

    time_new = np.arange(0,tmax,dt) 

    hp_ext      = np.zeros(len(time_new))
    hc_ext      = np.zeros(len(time_new))
    hp_ext_fit  = np.zeros(len(time_new))
    hc_ext_fit  = np.zeros(len(time_new))

    ti, hpp = sn_resample_wave(time_25 / 1000, hp, frequency)
    ti, hcp = sn_resample_wave(time_25 / 1000, hc, frequency)

    hp_mem = hp[-1]
    hc_mem = hc[-1]
 
    hp_ext[:len(hpp)] = hpp
    hc_ext[:len(hcp)] = hcp

    hp_ext[len(hpp):] = 1.0 / 2.0 * (hp_mem + hp_mem * np.cos(2 * np.pi * f_tail * (time_new[len(hpp):]-time_25[-1] / 1000)))
    hc_ext[len(hcp):] = 1.0 / 2.0 * (hc_mem + hc_mem * np.cos(2 * np.pi * f_tail * (time_new[len(hcp):]-time_25[-1] / 1000)))
    
    for t in range(len(ti), len(time_new)):
        if abs(hp_ext[t]) < 0.00001:
            hp_ext[t:] = 0
            hc_ext[t:] = 0
            break
    
    f_25, Hp_25 = sn_fft_wave(time_new, hp_ext)
    f_25, Hc_25 = sn_fft_wave(time_new, hc_ext)
#######################################################################
## Paper Total PSD Plots
#######################################################################   
    LIGO = np.genfromtxt("Data/Noise/aligo_O4high.txt")
    LISA = np.genfromtxt("Data/Noise/lisa_noise_curve.dat")
    ESTS = np.genfromtxt("Data/Noise/ET_D.txt")
    COEX = np.genfromtxt("Data/Noise/CE1.txt")


    fig, ax = plt.subplots(figsize = (10, 7))

    ax.loglog(f_25, abs(Hc_25 * cm2kpc / output_distance) * np.sqrt(f_25))
    ax.loglog(f_15, abs(Hc_15 * cm2kpc / output_distance) * np.sqrt(f_15))
    ax.loglog(f_09, abs(Hc_09 * cm2kpc / output_distance) * np.sqrt(f_09))

    ax.loglog(LIGO[:,0], LIGO[:,1], color = "Black")
    ax.loglog(LISA[:,0], LISA[:,1], color = "Gray")
    ax.loglog(ESTS[:,0], ESTS[:,1], color = "Red")
    ax.loglog(COEX[:,0], COEX[:,1], color = "Purple")


    ax.set_ylabel(r"$\mathrm{ASD \ (Hz^{-1/2})}$")
    ax.set_xlabel(r"$\mathrm{Freqhency \ (Hz)}$")

    ax.tick_params(axis='x', which='major', pad=10)

    legend1 = plt.legend([Line2D([0], [0], color="Black", lw=4),
                          Line2D([0], [0], color="Gray", lw=4),
                          Line2D([0], [0], color="Red", lw=4),
                          Line2D([0], [0], color="Purple", lw=4)], 
                          ["LIGO", "LISA", "Einstein Telescope", "Cosmic Explorer"], 
                          fontsize = "x-small", 
                          loc = "lower left", 
                          ncol = 1, 
                          bbox_to_anchor = (0.1,0.08), 
                          frameon = False)
    legend2 = plt.legend([Line2D([0], [0], color="tab:blue", lw=4),
                          Line2D([0], [0], color="tab:orange", lw=4),
                          Line2D([0], [0], color="tab:green", lw=4)], 
                         ["D25-3D", "D15-3D", "D9.6-3D"], 
                         fontsize = "x-small", 
                         loc = "lower left", 
                         ncol = 1, 
                         bbox_to_anchor = (0.4,0.1), 
                         frameon = False)

    ax.add_artist(legend1)

    plt.savefig("Images/ASD_paper.png", dpi = 200, bbox_inches = "tight")
    plt.close()

    snr_LIGO_09 = sn_snr_wave(f_09, Hc_09 * cm2kpc / output_distance, LIGO[:,0], LIGO[:,1])
    snr_LISA_09 = sn_snr_wave(f_09, Hc_09 * cm2kpc / output_distance, LISA[:,0], LISA[:,1])
    snr_ESTS_09 = sn_snr_wave(f_09, Hc_09 * cm2kpc / output_distance, ESTS[:,0], ESTS[:,1])
    snr_COEX_09 = sn_snr_wave(f_09, Hc_09 * cm2kpc / output_distance, COEX[:,0], COEX[:,1])

    snr_LIGO_15 = sn_snr_wave(f_15, Hc_15 * cm2kpc / output_distance, LIGO[:,0], LIGO[:,1])
    snr_LISA_15 = sn_snr_wave(f_15, Hc_15 * cm2kpc / output_distance, LISA[:,0], LISA[:,1])
    snr_ESTS_15 = sn_snr_wave(f_15, Hc_15 * cm2kpc / output_distance, ESTS[:,0], ESTS[:,1])
    snr_COEX_15 = sn_snr_wave(f_15, Hc_15 * cm2kpc / output_distance, COEX[:,0], COEX[:,1])

    snr_LIGO_25 = sn_snr_wave(f_25, Hc_25 * cm2kpc / output_distance, LIGO[:,0], LIGO[:,1])
    snr_LISA_25 = sn_snr_wave(f_25, Hc_25 * cm2kpc / output_distance, LISA[:,0], LISA[:,1])
    snr_ESTS_25 = sn_snr_wave(f_25, Hc_25 * cm2kpc / output_distance, ESTS[:,0], ESTS[:,1])
    snr_COEX_25 = sn_snr_wave(f_25, Hc_25 * cm2kpc / output_distance, COEX[:,0], COEX[:,1])

    print("SNR")
    print("LIGOo4", "LISA", "ET", "CE")
    print(np.round(snr_LIGO_09,2), np.round(snr_LISA_09,2), np.round(snr_ESTS_09,2), np.round(snr_COEX_09,2))
    print(np.round(snr_LIGO_15,2), np.round(snr_LISA_15,2), np.round(snr_ESTS_15,2), np.round(snr_COEX_15,2))
    print(np.round(snr_LIGO_25,2), np.round(snr_LISA_25,2), np.round(snr_ESTS_25,2), np.round(snr_COEX_25,2))

    return [[np.round(snr_LIGO_09,2), np.round(snr_LISA_09,2), np.round(snr_ESTS_09,2), np.round(snr_COEX_09,2)],
            [np.round(snr_LIGO_15,2), np.round(snr_LISA_15,2), np.round(snr_ESTS_15,2), np.round(snr_COEX_15,2)],
            [np.round(snr_LIGO_25,2), np.round(snr_LISA_25,2), np.round(snr_ESTS_25,2), np.round(snr_COEX_25,2)]]
