import cv2

# Captura vídeo de uma câmera IP
capturaVideo = cv2.VideoCapture('http://usuario:senha@192.168.1.150:80/cgi-bin/mjpg/video.cgi?channel=0&subtype=1')

# identifica a taxa de quadros por segundo
# fps = 60
fps = capturaVideo.get(cv2.CAP_PROP_FPS)
print('Taxa de quadros por segundo:', fps)

# identifica largura e altura dos quadros no fluxo de video
tamanho = (int(capturaVideo.get(cv2.CAP_PROP_FRAME_WIDTH)), int(capturaVideo.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print("Largura e altura:", tamanho)

# salva o arquivo de video no formato .avi, codificação YUV(para arquivos grandes), taxa de frames e tamanho
# AVI
codificacao = cv2.VideoWriter_fourcc('I', '4', '2', '0')
salvaVideo = cv2.VideoWriter('testeVideo01.avi', codificacao, fps, tamanho)

# loop acontece infinitamente até apertar a tecla a.
while True:
    # lê quadros de uma câmera
    # ret verifica o retorno em cada quadro
    ret, frame = capturaVideo.read()

    # converte vídeo em hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # saida do frame em hsv
    salvaVideo.write(hsv)

    # mostra imagem original
    cv2.imshow('Original', frame)

    # mostra a imagem em hsv
    cv2.imshow('Vídeo hsv', hsv)

    # encerra o programa ao apertar a tecla a
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# libera a camera
capturaVideo.release()

# libera gravacao
salvaVideo.release()

# fecha tudo
cv2.destroyAllWindows()
