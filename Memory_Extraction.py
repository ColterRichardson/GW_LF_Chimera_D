#######################################################################
# Gravitational Wave Memory from Chimera's D-Series Memory Extraction
#######################################################################
#######################################################################
## House Keeping
#######################################################################
#######################################################################
### Math, Science, and Computing Modules
#######################################################################
import numpy as np
#######################################################################
## Memory Extraction
#######################################################################
#######################################################################
### D9.6-3D
#######################################################################
def extract_D96(hp_f_09, hc_f_09, 
                hp_n_09, hc_n_09, 
                hp_t_09, hc_t_09, 
                D96 = True, 
                Flow = True, Neutrino = True, Total = True, 
                debug = False):
    if D96:
        if debug :
            print("Begin D9.6-3D Memory Array Save as .txt")
#######################################################################
#### Flow
#######################################################################
        if Flow:
            hpD9_memory = hp_f_09[-1,:,:] 
            hcD9_memory = hc_f_09[-1,:,:] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D9.6-3D/Flow/D9.6-3D_hp_flow_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D9.6-3D/Flow/D9.6-3D_hc_flow_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D9.6-3D/Flow/D9.6-3D_ht_flow_memory.txt", htD9_memory)
#######################################################################
#### Neutrino
#######################################################################
        if Neutrino:
            hpD9_memory = hp_n_09[-1,:,:,-1] 
            hcD9_memory = hc_n_09[-1,:,:,-1] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D9.6-3D/Neutrino/D9.6-3D_hp_neutrino_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D9.6-3D/Neutrino/D9.6-3D_hc_neutrino_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D9.6-3D/Neutrino/D9.6-3D_ht_neutrino_memory.txt", htD9_memory)
#######################################################################
#### Total
#######################################################################
        if Total:
            hpD9_memory = hp_t_09[-1,:,:] 
            hcD9_memory = hc_t_09[-1,:,:] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D9.6-3D/Total/D9.6-3D_hp_total_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D9.6-3D/Total/D9.6-3D_hc_total_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D9.6-3D/Total/D9.6-3D_ht_total_memory.txt", htD9_memory)

            if debug :
                print("End D9.6-3D Memory Array Save as .txt")
    return None
#######################################################################
### D15-3D
#######################################################################
def extract_D15(hp_f_15, hc_f_15, 
                hp_n_15, hc_n_15, 
                hp_t_15, hc_t_15, 
                D15 = True, 
                Flow = True, Neutrino = True, Total = True, 
                debug = False):
    if D15:
        if debug :
            print("Begin D15-3D Memory Array Save as .txt")
#######################################################################
#### Flow
#######################################################################
        if Flow:
            hpD9_memory = hp_f_15[-1,:,:] 
            hcD9_memory = hc_f_15[-1,:,:] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D15-3D/Flow/D15-3D_hp_flow_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D15-3D/Flow/D15-3D_hc_flow_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D15-3D/Flow/D15-3D_ht_flow_memory.txt", htD9_memory)
#######################################################################
#### Neutrino
#######################################################################
        if Neutrino:
            hpD9_memory = hp_n_15[-1,:,:,-1] 
            hcD9_memory = hc_n_15[-1,:,:,-1] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D15-3D/Neutrino/D15-3D_hp_neutrino_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D15-3D/Neutrino/D15-3D_hc_neutrino_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D15-3D/Neutrino/D15-3D_ht_neutrino_memory.txt", htD9_memory)
#######################################################################
#### Total
#######################################################################
        if Total:
            hpD9_memory = hp_t_15[-1,:,:] 
            hcD9_memory = hc_t_15[-1,:,:] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D15-3D/Total/D15-3D_hp_total_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D15-3D/Total/D15-3D_hc_total_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D15-3D/Total/D15-3D_ht_total_memory.txt", htD9_memory)

            if debug :
                print("End D15-3D Memory Array Save as .txt")
    return None
#######################################################################
### D25-3D
#######################################################################
def extract_D25(hp_f_25, hc_f_25, 
                hp_n_25, hc_n_25, 
                hp_t_25, hc_t_25, 
                D25 = True, 
                Flow = True, Neutrino = True, Total = True, 
                debug = False):
    if D25:
        if debug :
            print("Begin D25-3D Memory Array Save as .txt")
#######################################################################
#### Flow
#######################################################################
        if Flow:
            hpD9_memory = hp_f_25[-1,:,:] 
            hcD9_memory = hc_f_25[-1,:,:] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D25-3D/Flow/D25-3D_hp_flow_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D25-3D/Flow/D25-3D_hc_flow_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D25-3D/Flow/D25-3D_ht_flow_memory.txt", htD9_memory)
#######################################################################
#### Neutrino
#######################################################################
        if Neutrino:
            hpD9_memory = hp_n_25[-1,:,:,-1] 
            hcD9_memory = hc_n_25[-1,:,:,-1] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D25-3D/Neutrino/D25-3D_hp_neutrino_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D25-3D/Neutrino/D25-3D_hc_neutrino_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D25-3D/Neutrino/D25-3D_ht_neutrino_memory.txt", htD9_memory)
#######################################################################
#### Total
#######################################################################
        if Total:
            hpD9_memory = hp_t_25[-1,:,:] 
            hcD9_memory = hc_t_25[-1,:,:] 
            htD9_memory = np.sqrt(hpD9_memory**2 + hcD9_memory**2)
            np.savetxt("Data/Memory/D25-3D/Total/D25-3D_hp_total_memory.txt", hpD9_memory)
            np.savetxt("Data/Memory/D25-3D/Total/D25-3D_hc_total_memory.txt", hcD9_memory)
            np.savetxt("Data/Memory/D25-3D/Total/D25-3D_ht_total_memory.txt", htD9_memory)

            if debug :
                print("End D25-3D Memory Array Save as .txt")
    return None