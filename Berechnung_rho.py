# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:37:28 2025

@author: johan
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
import statistics as sta
import matplotlib.ticker as ticker
import os
import uncertainties as u
import fehlerrechnung as f # eigenes Paket

def func_rho_pb(Ny, eps_f, eps_d, R, V,
           lam_Po, lam_Pb, T_f, t1, t2):

    A = (
        1 / lam_Po
        + 1 / lam_Pb
        + lam_Pb / (lam_Po * (lam_Po - lam_Pb))
        + lam_Po * np.exp(-lam_Pb * T_f) / (lam_Pb * (lam_Pb - lam_Po))
    )

    B = (
        lam_Pb / (lam_Po * (lam_Pb - lam_Po))
        * (1 - np.exp(-lam_Po * T_f))
    )

    F = A * (np.exp(-lam_Pb * t1) - np.exp(-lam_Pb * t2)) \
        + B * (np.exp(-lam_Po * t1) - np.exp(-lam_Po * t2))

    return Ny / (eps_f * eps_d * R * V * F)

#sichere Daten
eps_f=1
t1=58.61
t2=13543.61
T_f=4212


#vorläufig, also nochmal zu überprüfende
lam_Pb=np.log(2)*1/1608
lam_Po=np.log(2)*5/933
lam_Rn=np.log(2)*1/330048
V=0.01331 #Luftumsatz des Filters


#Peak 1,2,3
eps_d=[0.06343,0.07180,0.07673] #Nachweiswahrscheinlichkeit
R=[0.0746,0.0192,0.371]
Ny=[2245.5,1935.4,2829.8]

rho_pb=[]
c_A_Rn=[]

for i in range(len(eps_d)):
   rho=func_rho_pb(Ny[i], eps_f, eps_d[i], R[i], V, lam_Po, lam_Pb, T_f, t1, t2)
   rho_pb.append(rho)
   c_A_Rn.append(rho*lam_Pb)
print("rho_{Pb}=",rho_pb)
print()
print("c_A(Rn)")

print(c_A_Rn)