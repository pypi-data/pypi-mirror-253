import numpy as np
import cv2

def gaussiano_noise(imagem, scala):
    """
        Adiciona ruído gaussiano a uma imagem em escala de cinza.

        Parameters
        ----------
        - imagem: array numpy, imagem de entrada.
        - scala: float, escala do ruído gaussiano.

        Returns
        -------
        - array numpy, imagem com ruído gaussiano adicionado.
    """

    imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
    ruido_gaussiano = np.random.normal(loc=0, scale=scala, size=imagem_cinza.shape).astype(np.uint8)
    return np.clip(imagem_cinza + ruido_gaussiano, 0, 255).astype(np.uint8)
