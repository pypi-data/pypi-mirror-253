import numpy as np
from PhotoPy.convolution import border_ignore

def alargamento_contraste(imagem, k, E):
    """
        Aplica o estiramento de contraste a uma imagem de entrada.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - k: float, fator de estiramento.
        - E: float, expoente para realce de contraste.

        Returns
        -------
        - array numpy, imagem com contraste estirado.
    """
    
    imagem = imagem.astype(float)
    return (1 / (1 + (k / (imagem + 1e-10)) ** E)) * 255.0


def negativo(imagem,L):
    """
        Calcula o negativo de uma imagem de entrada.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - L: int, valor máximo de intensidade.

        Returns
        -------
        - array numpy, negativo da imagem de entrada.
    """
    
    return L - 1 - imagem

def logaritmica(imagem, valor):
    """
        Aplica a transformação logarítmica a uma imagem de entrada.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - valor: float, constante para a transformação logarítmica.

        Returns
        -------
        - array numpy, imagem transformada logaritmicamente.
    """
    
    
    c = valor/(np.log (1 + np.max(imagem)))
    return  (np.log(1 + imagem))**c

def potencia(imagem, c, gamma):
    """
        Aplica a transformação de lei de potência a uma imagem de entrada.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - c: float, constante para a transformação de lei de potência.
        - gamma: float, expoente para a transformação de lei de potência.

        Returns
        -------
        - array numpy, imagem transformada pela lei de potência.
    """
    
    return c * (imagem ** gamma)

def laplaciano(imagem):
    """
        Aplica o filtro Laplaciano a uma imagem de entrada.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.

        Returns
        -------
        - array numpy, imagem filtrada pelo Laplaciano.
    """
    
    
    filtro = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    return border_ignore(imagem,filtro)