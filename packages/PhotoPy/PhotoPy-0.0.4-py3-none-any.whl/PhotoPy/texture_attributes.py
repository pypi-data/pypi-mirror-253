import numpy as np

def mean(image):
    """
        Calcula a média de uma imagem.

        Parameters:
        - image: array numpy, imagem de entrada.

        Returns:
        - float, valor da média da imagem.
    """
    
    return np.mean(image)

def variance(image):
    """
        Calcula a variância de uma imagem.

        Parameters:
        - image: array numpy, imagem de entrada.

        Returns:
        - float, valor da variância da imagem.
    """
    
    return np.var(image)

def skewness(image):
    """
        Calcula a assimetria (skewness) de uma imagem.

        Parameters:
        - image: array numpy, imagem de entrada.

        Returns:
        - float, valor da assimetria da imagem.
    """
    
    return np.sum((image - mean(image))**3) / (np.size(image)*(np.sqrt(variance(image)))**3)

def kurtosis (image):
    """
        Calcula a curtose de uma imagem.

        Parameters:
        - image: array numpy, imagem de entrada.

        Returns:
        - float, valor da curtose da imagem.
    """
    
    return np.sum((image - mean(image))**4)/(np.size(image)*(np.sqrt(variance(image)))**4) - 3

def energy(hist_norm):
    """
        Calcula a energia de um histograma normalizado.

        Parameters:
        - hist_norm: array numpy, histograma normalizado.

        Returns:
        - float, valor da energia do histograma.
    """
    
    return  np.sum(hist_norm**2)

def entropy(hist_norm):
    """
        Calcula a entropia de um histograma normalizado.

        Parameters:
        - hist_norm: array numpy, histograma normalizado.

        Returns:
        - float, valor da entropia do histograma.
    """
    
    return -np.sum((hist_norm / np.sum(hist_norm)) * np.log2((hist_norm / np.sum(hist_norm)) + 1e-10))