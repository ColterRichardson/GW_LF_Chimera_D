# GW_LF_Chimera_D
Analysis and plotting scripts for the low frequency gravitational waves from Chimera's D-Series.

## Data
In order to perform the analysis here, please download the .h5 files from ________ and place them in the _Data_ directory.

## Data Analysis
To run the script simply run the main.py file with the flags desired. Everything is set to FALSE initially. 

### Modal Analysis
Specifically for the modal analysis figures, the authors have provided the following:
 Files needed to create Spectrograms with modal analysis overlaid.
    
    *_PSD.dat files contain the 1024 x T entries for the spectrogram, where T is the number of time windows. The Figures in the paper are the log() of these quantities
    
    *_time_bins.dat files contain the T time bin entries for each model. The width of the bins is 10 ms if that is needed.
    
    *_frequency_bins.dat files contain the 1024 frequency bins
    
    *_g2n.dat files contain the times and frequency values for the g_21 (or g_22, g_23, g_24) mode. The even numbered files contain time jumps.
