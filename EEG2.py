import time
import numpy as np
import mne
from tkinter import *
from tkinter import filedialog

raiz= Tk()

# interfaz de apertura de datos 
def abrirArchivo(): 
	archivo = filedialog.askopenfilename(title = "Abrir", initialdir= "C:/", filetypes=("Archivos de EEG", ".CNT"),)
	print (archivo)
Button(raiz, text = "Abrir archivo", command=abrirArchivo).pack()
raiz.mainloop()


## 2 bloque accesamos a datos 

#cd \Users\Alumnos-Dell\Desktop\ej-python\CNTs Notebooks

##sample_data_folder = mne.datasets.sample.data_path()
#sample_data_folder = Desktop.ej-python.CNTs.data_path()
##print(sample_data_folder)
#C:\Users\Alumnos-Dell\Desktop\ej-python\CNTs