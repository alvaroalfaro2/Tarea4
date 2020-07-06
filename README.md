## Universidad de Costa Rica 
## Modelos Probabilísticos de Señales y Sistemas
# Tarea 4: Álvaro Alfaro Miranda - B70224

1. Modulación BPSK para los bits presentados.

![Tx](Tx.png)

2. Potencia promedio de la señal modulada generada.
3. Canal ruidoso del tipo AWGN (ruido aditivo blanco gaussiano) con una relación señal a ruido (SNR) desde -2 hasta 3 dB.

![AWGN_SNR-2](AWGN_SNR-2.png)
![AWGN_SNR-1](AWGN_SNR-1.png)
![AWGN_SNR0](AWGN_SNR0.png)
![AWGN_SNR1](AWGN_SNR1.png)
![AWGN_SNR2](AWGN_SNR2.png)
![AWGN_SNR3](AWGN_SNR3.png)

4. Gráfica de la densidad espectral de potencia de la señal con el método de Welch (SciPy), antes y después del canal ruidoso.
![Antes_SNR-2](Antes_SNR-2.png)
![Despues_SNR-2](Despues_SNR-2.png)
![Despues_SNR-1](Despues_SNR-1.png)
![Despues_SNR0](Despues_SNR0.png)
![Despues_SNR1](Despues_SNR1.png)
![Despues_SNR2](Despues_SNR2.png)
![Despues_SNR3](Despues_SNR3.png)

5. Demodulación y decodificación de la señal y conteo de la tasa de error de bits (BER, bit error rate) para cada nivel SNR.

| SNR | Cantidad de errores | Tasa de error de bits (BER) | 
| ------ | ---- | ---- |
| -2 | 11 | 0,0011  |
| -1 | 3 | 0,0003 |
| 0 | 1  | 0,0001  |
| 1 | 1  | 0,0001 |
| 2 | 0  | 0 |
| 3 | 0  | 0 |

6. Gráfica BER versus SNR.

![BERversusSNR](BERversusSNR.png)




