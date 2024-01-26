import cv2
import os

def reading(diretorio):
    """
        Lê e carrega imagens de um diretório.

        Parameters:
        ----------
        - diretorio: str, caminho do diretório contendo as imagens.

        Returns:
        -------
        - list, lista de arrays numpy representando as imagens lidas.
        Retorna None e exibe uma mensagem de erro se o diretório não for encontrado.
    """
    
    
    lista = []

    if not os.path.exists(diretorio):
        print(f"Diretório {diretorio} não encontrado.")
        return None

    arquivos = os.listdir(diretorio)

    for arquivo in arquivos:
        caminho_completo = os.path.join(diretorio, arquivo)
        if os.path.isfile(caminho_completo) and any(extensao in arquivo.lower() for extensao in ['.jpg', '.jpeg', '.png']):
            imagem = cv2.imread(caminho_completo)
            
            if imagem is not None:
                lista.append(imagem)
            else:
                print(f"Não foi possível ler a imagem: {caminho_completo}")

    return lista