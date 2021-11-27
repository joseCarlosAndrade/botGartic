from pesquisa import Imagens
from desenha_aiGarticPesquisa import Desenhar
import os


# =========== PESQUISA DA IMAGEM =========
# define obj que pesquisa a imagem a ser baixada
obj1 = Imagens()

# chama a funçao que pesquisa e baixa de fato
obj1.pesquisar(input("digita ai vai duvido: "))

# =========== DESENHO ==============
obj2 = Desenhar()
obj2.capImagem()
input("Pressione enter para continuar!")

obj2.magica()
# ===============================
# final do codigo (remove para nao deixar arquivos duplicados)
os.remove("imagens/image.jpg")