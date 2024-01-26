import numpy as np
from PhotoPy import texture_attributes as txa
from PhotoPy import histograma
import cv2


def descritor_histograma(imagem):
    """
        Calcula descritores estatísticos e de histograma para uma imagem em escala de cinza.

        Parameters:
        - imagem: array numpy, imagem de entrada.

        Returns:
        - list, lista de descritores contendo média, variância, assimetria, curtose, energia e entropia.
    """
    
    
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # hist, _ = np.histogram(imagem_cinza.flatten(), bins=256, range=[0, 256])
    hist = histograma.calcular_hist(imagem_cinza)
    
    hist_norm = hist / np.sum(hist)
    
    media = txa.mean(imagem)
    var = txa.variance(imagem)
    skewness = txa.skewness(imagem)
    kurtosis = txa.kurtosis(imagem)
    energia =  txa.energy(hist_norm)
    entropia = txa.entropy(hist_norm)
    
    return [media,var,skewness,kurtosis,energia,entropia]



def calcular_hist(imagem):
    """
        Calcula o histograma de uma imagem em escala de cinza.

        Parameters:
        - imagem: array numpy, imagem de entrada.

        Returns:
        - array numpy, histograma da imagem.
    """
    
    
    #Criar uma matriz
    hist = np.zeros((256,), dtype=np.int64)

    for linhas in range(imagem.shape[0]):
        for colunas in range(imagem.shape[1]):
            intesidade_pixel = imagem[linhas, colunas]  
            hist[intesidade_pixel] += 1

    return hist



def equalizar(imagem):
    """
        Equaliza uma imagem em escala de cinza.

        Parameters:
        - imagem: array numpy, imagem de entrada.

        Returns:
        - array numpy, imagem equalizada.
    """
    
    
    hist = calcular_hist(imagem)
    func_dist_comul = hist.cumsum()
    func_dist_comul_norm = func_dist_comul * float(hist.max()) / func_dist_comul.max()
    imagem_equalizada = func_dist_comul_norm[imagem]

    return imagem_equalizada