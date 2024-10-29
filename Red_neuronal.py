# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 11:30:01 2022

@author: jorge
"""
## MANERAS DE PROGRAMAR UNA RED NEURONAL
# 1.importamos librerias 
import numpy as np
import scipy as sc 
import matplotlib.pyplot as plt 

from sklearn.datasets import make_circles 

#2.creamos nuestros datos artificales, donde buscaremos clasificar 
#dos anillos concéntricos de datos 
X, Y = make_circles(n_samples = 500, factor = 0.5, noise= 0.05) 

#Resolulacion del mapa de prediccion 
res= 100

#Coordenadas del mapa de prediccion 
_x0 = np.linspace(-1.5, 1.5, res) #estas variables no se ven en el variable explorer 
_x1 = np.linspace(-1.5,1.5,res)

#Input con cada combo de coordenadas del mapa de prediccion 
_pX = np.array(np.meshgrid(_x0,_x1)).T.reshape(-1, 2)

#Objeto vacio a 0.5 del mapa de prediccion 
_pY = np.zeros((res,res)) + 0.5

#Visualizacion del mapa de prediccion sin datos 
plt.figure(figsize=(8,8))
plt.pcolormesh(_x0,_x1,_pY, cmap="coolwarm", vmin=0,vmax=1)

#visualizacion de la nube de datos 
plt.scatter(X[Y == 0,0], X[Y == 0,1], c="skyblue")
plt.scatter(X[Y == 1,0], X[Y == 1,1], c='salmon')

plt.tick_params(labelbottom = False, labelleft = False ) #False tiene que ir con mayuscula y sirve para no mostrar las madidas de los ejes 

" Uso de tensoroflow que sirve para resolver derivadas parciales, es decir gradientes"
import tensorflow as tf

from matplotlib import animation 
from IPython.core.display import display, HTML

# Definimos los puntos de entrada de la red, para la matriz X e Y 
iX = tf.placeholder('float', shape=[None,X.shape[1]])
iY = tf.placeholder('float', shape=[None])

lr = 0.01 #learning rate
nn = [2, 16, 8, 1] #numero de neuronas por capa. 

#capa 1 
W1 = tf.Variable(tf.random_normal([nn[0], nn[1]]), name ='Weights_1')
b1 = tf.Variable (tf.random_normal([nn[1]]), name = 'bias_1')

l1 = tf.nn.relu(tf.add(tf.matmul(iX,W1),b1)) #XW + b

#capa 2 
W2 = tf.Variable(tf.random_normal([nn[1], nn[2]]), name ='Weights_2')
b2 = tf.Variable (tf.random_normal([nn[2]]), name = 'bias_2')

l2 = tf.nn.relu(tf.add(tf.matmul(l1,W2),b2)) #XW + b

#Capa 3 
W3 = tf.Variable(tf.random_normal([nn[2], nn[3]]), name ='Weights_3')
b3 = tf.Variable (tf.random_normal([nn[3]]), name = 'bias_3')

#vector de predicciones de Y,  SALIDA
pY = tf.nn.sigmoid(tf.add(tf.matmul(l2,W3),b3))[:,0] #se acota de 0 a 1 

