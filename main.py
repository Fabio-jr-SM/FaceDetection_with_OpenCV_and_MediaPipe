import cv2
import mediapipe as mp

# Iniciar o OpenCV e o MediaPipe
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhecedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # Ler as informações da webcam
    verificador, frame = webcam.read() 

    '''
    Verificador -> verificar se conseguiu ler as informações da webcam
    Frame -> imagem caso o verificador for verdadeiro
    '''

    if not verificador:
        break

    # Converter a imagem de BGR para RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Reconhecer os rostos na imagem
    lista_rostos = reconhecedor_rostos.process(frame_rgb)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # Desenhar os rostos na imagem
            desenho.draw_detection(frame, rosto)

    # Mostrar a imagem resultante
    cv2.imshow("Rostos na webcam", frame)

    # Quando apertar Esc parar o loop
    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()
