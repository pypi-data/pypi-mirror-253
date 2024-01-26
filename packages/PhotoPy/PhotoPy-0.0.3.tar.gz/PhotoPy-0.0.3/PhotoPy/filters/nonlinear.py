import numpy as np
import cv2

def median(imagem,tamanho_kernel):
    """
        Aplica a operação de filtro da mediana a uma imagem.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - tamanho_kernel: int, tamanho do kernel para a operação de filtro da mediana.

        Retorna:
        - array numpy, imagem filtrada pela mediana.
    """
    
    return cv2.medianBlur(imagem, tamanho_kernel)


def moda(imagem,tamanho_kernel):
    """
        Aplica a operação de filtro da moda a uma imagem.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - tamanho_kernel: int, tamanho do kernel para a operação de filtro da moda.

        Returns
        -------
        - array numpy, imagem filtrada pela moda.
    """
    
    
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.uint8)
    return cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, kernel)

def maximum(imagem,tamanho_kernel):
    """
        Aplica a operação de dilatação máxima a uma imagem.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - tamanho_kernel: int, tamanho do kernel para a operação de dilatação máxima.

        Returns
        -------
        - array numpy, imagem após a operação de dilatação máxima.
    """
    
    
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.uint8)
    return cv2.dilate(imagem, kernel)

def minimum(imagem, tamanho_kernel):
    """
        Aplica a operação de erosão mínima a uma imagem.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - tamanho_kernel: int, tamanho do kernel para a operação de erosão mínima.

        Returns
        -------
        - array numpy, imagem após a operação de erosão mínima.
    """
    
    
    kernel = np.ones((tamanho_kernel, tamanho_kernel), np.uint8)
    return cv2.erode(imagem, kernel)