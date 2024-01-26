import os
import cv2

def save_file(imagem, diretorio, nome_arquivo):
    """
        Salva uma imagem em um diretório específico com um nome de arquivo fornecido.

        Parameters:
        - imagem: array numpy, imagem a ser salva.
        - diretorio: str, caminho do diretório onde a imagem será salva.
        - nome_arquivo: str, nome do arquivo (sem extensão) a ser atribuído à imagem.
    """


    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    caminho_completo = os.path.join(diretorio, nome_arquivo)

    nome_arquivo = f'{nome_arquivo}.png'
    cv2.imwrite(nome_arquivo,imagem)
    print(f'Imagem salva em: {caminho_completo}')