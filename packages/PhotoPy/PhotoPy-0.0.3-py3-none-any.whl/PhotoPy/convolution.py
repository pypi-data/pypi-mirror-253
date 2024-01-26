import cv2

def border_ignore(imagem,filtro):
    """
        Aplica um filtro à imagem sem considerar as bordas.

        Parameters:
        - imagem: array numpy, imagem de entrada.
        - filtro: array numpy, filtro a ser aplicado.

        Returns:
        - array numpy, imagem resultante após a aplicação do filtro sem considerar as bordas.
    """
    
    
    return cv2.filter2D(imagem, -1, filtro)
    
def border_reflect(imagem,filtro):
    """
        Aplica um filtro à imagem utilizando reflexão nas bordas.

        Parameters:
        - imagem: array numpy, imagem de entrada.
        - filtro: array numpy, filtro a ser aplicado.

        Returns:
        - array numpy, imagem resultante após a aplicação do filtro com reflexão nas bordas.
    """

    m, n = filtro.shape
    return cv2.copyMakeBorder(imagem, m // 2, m // 2, n // 2, n // 2, cv2.BORDER_REFLECT)

def border_zero(imagem, filtro):
    """
        Aplica um filtro à imagem com bordas preenchidas com zeros.

        Parameters:
        - imagem: array numpy, imagem de entrada.
        - filtro: array numpy, filtro a ser aplicado.

        Returns:
        - array numpy, imagem resultante após a aplicação do filtro com bordas preenchidas com zeros.
    """
    
    
    m, n = filtro.shape
    imagem_bordar = cv2.copyMakeBorder(imagem, m // 2, m // 2, n // 2, n // 2, cv2.BORDER_CONSTANT)
    return cv2.filter2D(imagem_bordar, -1, filtro)    

def border_replicate(imagem,filtro):
    """
        Aplica um filtro à imagem utilizando replicação nas bordas.

        Parameters:
        - imagem: array numpy, imagem de entrada.
        - filtro: array numpy, filtro a ser aplicado.

        Returns:
        - array numpy, imagem resultante após a aplicação do filtro com replicação nas bordas.
    """
    
    
    m, n = filtro.shape
    imagem_bordar =  cv2.copyMakeBorder(imagem, m // 2, m // 2, n // 2, n // 2, cv2.BORDER_REPLICATE)
    return cv2.filter2D(imagem_bordar, -1, filtro)