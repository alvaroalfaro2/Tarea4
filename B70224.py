import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal
import csv
import pandas as pd  #se usa el paquete panda para leer los datos del archivo csv 


datos=pd.read_csv('bits10k.csv')  #se lee el documento 


#Se crea una matriz con los registros del archivo para poder utilizar cada dato en los cálculos.  
archivo = 'bits10k.csv'
matriz_datos = []
with open(archivo) as csvfile:
    dato = csv.reader(csvfile) 
    for lista in dato: # Cada fila es una lista
        matriz_datos.append(lista)

df=pd.DataFrame(datos)

N=len(matriz_datos)    #Número de bits
bits = np.zeros((N))  #Matriz con los bits que se desea transmitir

for i in range (0, N):
  bits [i] = int (matriz_datos[i][0])

# Frecuencia de operación
f = 5000 # Hz

# Duración del período de cada símbolo (onda)
T = 1/f # 200 ms

# Número de puntos de muestreo por período
p = 50

# Puntos de muestreo para cada período
tp = np.linspace(0, T, p)

# Creación de la forma de onda de la portadora
sinus = np.sin(2*np.pi * f * tp)

# Visualización de la forma de onda de la portadora
plt.plot(tp, sinus)
plt.xlabel('Tiempo / s')
plt.savefig('senal.png')

# Frecuencia de muestreo
fs = p/T 

# Creación de la línea temporal para toda la señal Tx
t = np.linspace(0, N*T, N*p)

# Inicializar el vector de la señal modulada Tx
senal = np.zeros(t.shape)

'''
Para la modulación BPSK se definen las funciones:
sin (2*pi*f*t) si el bit es un 1
-sin(2*pi*f*t) si el bit es un 0
'''

# Creación de la señal modulada BPSK
for k, b in enumerate(bits):
    if b==1: 
      senal[k*p:(k+1)*p] = sinus
    
    if b==0:
      senal[k*p:(k+1)*p] = -sinus

# Visualización de los primeros bits modulados
pb = 5
plt.figure()
plt.plot(senal[0:pb*p])
plt.savefig('Tx.png')

# Potencia instantánea
Pinst = senal**2

# Potencia promedio a partir de la potencia instantánea (W)
Ps = integrate.trapz(Pinst, t) / (N * T)


# Relación señal-a-ruido deseada
SNR=[-2,-1,0,1,2,3]
BER = np.zeros(len(SNR))
for i in range (0,6):
  
  # Potencia del ruido para SNR y potencia de la señal dadas
  Pn = Ps / (10**(SNR[i] / 10))

  # Desviación estándar del ruido
  sigma = np.sqrt(Pn)

  # Crear ruido (Pn = sigma^2)
  ruido = np.random.normal(0, sigma, senal.shape)

  # Simular "el canal": señal recibida
  Rx = senal + ruido

  plt.figure()
  plt.plot(Rx[0:pb*p])
  plt.savefig('AWGN _SNR={}.png'.format(SNR[i]))
  

  # Antes del canal ruidoso
  fw, PSD = signal.welch(senal, fs, nperseg=1024)
  plt.figure()
  plt.semilogy(fw, PSD)
  plt.xlabel('Frecuencia / Hz')
  plt.ylabel('Densidad espectral de potencia / V**2/Hz')
  plt.savefig('Antes_SNR={}.png'.format(SNR[i]))

  # Después del canal ruidoso
  fw, PSD = signal.welch(Rx, fs, nperseg=1024)
  plt.figure()
  plt.semilogy(fw, PSD)
  plt.xlabel('Frecuencia / Hz')
  plt.ylabel('Densidad espectral de potencia / V**2/Hz')
  plt.savefig('Despues_SNR={}.png'.format(SNR[i]))

  # Pseudo-energía de la onda original (esta es suma, no integral)
  Es = np.sum(sinus**2)

  # Inicialización del vector de bits recibidos
  bitsRx = np.zeros(bits.shape)

  # Decodificación de la señal por detección de energía
  for k, b in enumerate(bits):
      Ep = np.sum(Rx[k*p:(k+1)*p] * sinus)
      if Ep > Es/2:
          bitsRx[k] = 1
      else:
          bitsRx[k] = 0

  err = np.sum(np.abs(bits - bitsRx))
  BER[i] = (err/N)

  print('Para un SNR de {}, hay un total de {} errores en {} bits para una tasa de error de {}.'.format(SNR[i], err, N, BER[i]))

plt.figure()
plt.plot(SNR,BER, marker="o", color="red")
plt.xlabel('SNR')
plt.ylabel('BER')
plt.savefig('BERversusSNR.png')