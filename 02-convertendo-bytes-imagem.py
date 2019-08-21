import cv2
import numpy
import os

# cria uma matriz de 240.000 bytes aleatórios
matrizByte = bytearray(os.urandom(240000))
matrizNumpy = numpy.array(matrizByte)

# converte a matriz para criar uma imagem em escala de cinza de 400 x 300
imagemCinza = matrizNumpy.reshape(300, 800)
cv2.imwrite('BancoDados\imagemCinza.png', imagemCinza)

# converte a matriz para criar uma imagem colorida de 400 x 100
imagemRGB = matrizNumpy.reshape(100, 800, 3)
cv2.imwrite('BancoDados\imagemRGB.png', imagemRGB)
