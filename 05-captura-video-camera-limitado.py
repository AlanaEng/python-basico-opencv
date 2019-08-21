import cv2

# Captura vídeo de uma câmera IP
capturaCamera = cv2.VideoCapture('http://usuario:senha@192.168.1.150:80/cgi-bin/mjpg/video.cgi?channel=0&subtype=1')

# identifica a taxa de quadros por segundo
# fps = 60
fps = capturaCamera.get(cv2.CAP_PROP_FPS)
print('Quadros por segundo:', fps)

# identifica largura e altura dos quadros no fluxo de video
tamanho = (int(capturaCamera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capturaCamera.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# salva o arquivo de video no formato .avi, codificação YUV(para arquivos grandes), taxa de frames e tamanho

# AVI
codificacao = cv2.VideoWriter_fourcc('I', '4', '2', '0')

# MP4
# codificacao = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
salvaVideo = cv2.VideoWriter('bancoDados/CAM02.avi', codificacao, fps, tamanho)

rodavideo, quadros = capturaCamera.read()
# o loop acontece por 10 segundos de vídeo
numQuadros = 10 * fps - 1
while rodavideo and numQuadros > 0:
    salvaVideo.write(quadros)
    rodavideo, quadros = capturaCamera.read()
    numQuadros -= 1
