import cv2

# Captura vídeo de uma webcam
# capturaCamera = cv2.VideoCapture(0)

# Captura vídeo de uma câmera USB (Kinect)
# capturaCamera = cv2.VideoCapture(1)

# Captura vídeo de uma câmera IP
capturaCamera = cv2.VideoCapture('http://usuario:senha@192.168.1.112:80/cgi-bin/mjpg/video.cgi?channel=0&subtype=1')

# identifica a taxa de quadros por segundo
# fps = 60
fps = capturaCamera.get(cv2.CAP_PROP_FPS)
print('Quadros por segundo:', fps)

# identifica largura e altura dos quadros no fluxo de video
tamanho = (int(capturaCamera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capturaCamera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print('Tamanho da imagem:', tamanho)

# salva o arquivo de video no formato .avi, codificação YUV(para arquivos grandes), taxa de frames e tamanho

# AVI
codificacao = cv2.VideoWriter_fourcc('I', '4', '2', '0')

# MP4
# codificacao = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
salvaVideo = cv2.VideoWriter('bancoDados/CAM02.avi', codificacao, fps, tamanho)

rodavideo, quadros = capturaCamera.read()
# o loop acontece até que não tenha mais frames
while rodavideo:
    salvaVideo.write(quadros)
    

