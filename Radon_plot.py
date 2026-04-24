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

#gib den richtigen Pfad an
#pfad = "C:/Users/johan/Eigene Sachen/aJohannes/aStudium/2.Semester/Anfaengerpraktikum-3/INT"
pfad=""
dateiname = "Radon_Daten.csv"

dateipfad = os.path.join(pfad, dateiname)
df = pd.read_csv(dateipfad,sep=";", decimal=",")

print(df)
#gib die x/y Werte per df["Name Spalte"] an und ggf. die Unsicherheiten
x_werte = df["kanaele"]
y_werte = df["ba133"]
x_err = None
y_err = None

#plotten
#x_werte = x_werte.dropna() #evt. bei Fehlermeldungen nötig, wenn zu lange Listen mit None
#y_werte = y_werte.dropna()
plt.plot(x_werte,y_werte,label="",color="green",markersize=7)#label =name des Graphen
plt.grid()
plt.xlabel("Kanäle 400-1400") #Name x-Achse
plt.ylabel("gemessene Ereignisse") #Name y-Achse
#plt.yscale("log")
#plt.xscale("log")


#falls Fehlerbalken gewünscht sind
#plt.errorbar(x_werte,y_werte,y_err,x_err,".",capsize=5, color='lime',label="")

"""
#falls fitfunktion gewünscht ist
def func(x, a, b):
    return a * x + b #Art der Funktion
x_fit = np.linspace(np.min(x_werte), np.max(x_werte), 300)
popt, pcov = curve_fit(func, x_werte, y_werte)
plt.plot(x_fit, func(x_fit, *popt), color='orange',label="Fitfunktion")
print("die besten Parameter sind",[f.fehlerklammern(popt[i], np.sqrt(pcov[i][i])) for i in range(len(popt))])
print()
"""

# falls Peaks gefunden werden sollen
"""
peaks, properties = find_peaks(
    y_werte,
    height=500,      # minimale Peak-Höhe
    distance=20,    # minimaler Abstand zwischen Peaks
    prominence=200  # wie stark der Peak herausragen muss
)
print(peaks)
"""

plt.xlim(400,1400)

plt.legend()
#ausgeben als Datei
#Name der Grafik inkl. .png in "":
name_grafik = "test.png"
dateipfad = os.path.join(pfad, name_grafik)
plt.savefig(dateipfad)


#anzeigen
plt.show()