#import google_images_download
from google_images_search import GoogleImagesSearch
#import cv2
import time

# api credential = AIzaSyA_K5B5GLp3sNKMaxPyxIscDzkRXsBIdnM
# search engine = 0980f3eff5753f0ab

#classe de fato
class Imagens:
    def __init__(self): #inicia as credenciais e o obj gis que conecta o api
        global gis
        gis = GoogleImagesSearch('AIzaSyA_K5B5GLp3sNKMaxPyxIscDzkRXsBIdnM', '0980f3eff5753f0ab')

    def defPalavra(self, palavra): # preguiça de tirar mas ela nao faz nada por enquanto
        #global palavra
        #palavra = input("Digite a imagem desejada")
        return palavra


    def pesquisar(self, palavra): # funçao membro que de fato pesquisa a palavra com os parametros definidos
        _search_params = {
        'q': 'elefante',
        'num': 1,
        
        'fileType': 'jpg',
        'imgDominantColor': 'white',

        #'imgType': 'lineart',
        'imgColorType': 'color',
    
        }
    
        _search_params['q'] = palavra



        gis.search(search_params=_search_params, path_to_dir='imagens', custom_image_name='image')
        print(gis.results())
        #time.sleep(4)
    
