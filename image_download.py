import urllib.request
import sys

for numero in range(1000): #aqui seleciona número de imagens, colocar o valor total, pois é sobrescrito a cada download;
    try:
        urllib.request.urlretrieve("http://www2.cemaden.gov.br/mapainterativo/download/securimage/securimage_show.php", "{}.jpg".format(numero))
        print("Imagem salva! =)")
    except:
        erro = sys.exc_info()
        print("Ocorreu um erro:", erro)