import cv2

# pasta onde esta o arquivo de video
meuVideo = 'bancoDados/video01.mp4'

# importa o arquivo de video
capturaVideo = cv2.VideoCapture(meuVideo)

# identifica a taxa de quadros por segundo
fps = capturaVideo.get(cv2.CAP_PROP_FPS)
print('Taxa de quadros por segundo:', fps)

# identifica largura e altura dos quadros no fluxo de video
tamanho = (int(capturaVideo.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capturaVideo.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Largura e altura:", tamanho)

# salva o arquivo de video no formato .avi, codificação YUV(para arquivos grandes), taxa de frames e tamanho

# AVI
codificacao = cv2.VideoWriter_fourcc('I', '4', '2', '0')

# MP4
# codificacao = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

salvaVideo = cv2.VideoWriter('bancoDados/testeVideo01.avi', codificacao, fps, tamanho)

# inicializa a leitura do video.
rodavideo, quadros = capturaVideo.read()

# o arquivo é salvo sem audio, pois a OpenCV trabalha com Visão computacional e não com edição de vídeo.
while rodavideo:
    salvaVideo.write(quadros)
    rodavideo, quadros = capturaVideo.read()
