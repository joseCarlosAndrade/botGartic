import cv2
from pyautogui import *
import time
import win32api, win32con
import keyboard

# funçoes para clique
def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    #time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
        

def clickD(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#classe de fato
class Desenhar:
    # Defina as ranges das cores e a posiçao delas aqui
    def __init__(self) :
        #definiçao das variaveis globais
        global max_black 
        global gray_dl 
        global white_min 

        global posPreto 
        global posCinzaE 
        global posCinzaC 
        global sX 
        global sY 
        global stop 
        global pixel_jump 

        


        max_black = 25
        gray_dl = 110
        white_min = 230

        posPreto = [308, 395]
        posCinzaE = [334, 395]
        posCinzaC = [334, 423]
        sX = 524
        sY = 227

        stop = []
        pixel_jump = 3 # Pulo por cada click


    
    def capImagem(self): # funçao membro que captura a imagem
        global img1
        global img_gray
        img1 = cv2.imread("imagens/image.JPG")

        # Converte para escala de cinza
        img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)


        
        h, w = img_gray.shape

        h2 = 85  # Nova altura a ser definida
        w2 = (w * h2) / h

        global img
        img = cv2.resize(img_gray, (round(w2), h2))
        cv2.imshow("Sua imagem!", img)

        # =========================================================

        # salba a imagem modificada para posterior comparaçao
        cv2.imwrite('MODIFI.png',img)
        cv2.waitKey(1000)

    # ==========================================================
    # Mostra o tamanho da imagem
    #print("Original size :" + str(img_gray.shape))
    
    

    ##########################################################################


    def magica(self):
        time.sleep(2)
        #cinzaEscuro = 0
        cabo2 = False
        while keyboard.is_pressed('q') == False and cabo2 == False:

            #PRETO
            clickD(posPreto[0], posPreto[1]) # clica na cor preta (vo mudar dps)
            clickD(posPreto[0], posPreto[1])
            click(posPreto[0], posPreto[1])
            click(posPreto[0], posPreto[1])

            x = sX
            y = sY
            contador = 0
            for altura in img:
                contador = contador + 1
                
                if contador == 40:
                    time.sleep(2)

                for largura in altura:
                    x = x + pixel_jump
                    
                    if largura <= max_black:

                        click(x, y)
                    
                y = y + pixel_jump
                x = sX

            time.sleep(3)

            #CINZA ESCURO
            clickD(posCinzaE[0], posCinzaE[1])
            clickD(posCinzaE[0], posCinzaE[1])
            click(posCinzaE[0], posCinzaE[1])
            click(posCinzaE[0], posCinzaE[1])

            x = sX
            y = sY

            contadord = 0
            for altura in img:
                contadord = contadord + 1
                
                if contadord == 40:
                    time.sleep(2)
                for largura in altura:
                    x = x + pixel_jump
                    
                    if max_black < largura <= gray_dl:
                        click(x, y)
                    
                    
                y = y + pixel_jump
                x = sX

            time.sleep(3)

            #CINZA CLARO
            clickD(posCinzaC[0], posCinzaC[1])
            clickD(posCinzaC[0], posCinzaC[1])
            click(posCinzaC[0], posCinzaC[1])
            click(posCinzaC[0], posCinzaC[1])

            x = sX
            y = sY

            contadorl = 0
            for altura in img:
                contadorl = contadorl + 1
                
                if contadorl == 40:
                    time.sleep(2) 
                for largura in altura:
                    x = x + pixel_jump
                    
                    if gray_dl < largura <= white_min:
                        click(x, y)
                    
                y = y + pixel_jump
                x = sX

            time.sleep(3)

            cabo2 = True

            
        cv2.waitKey(1000)




