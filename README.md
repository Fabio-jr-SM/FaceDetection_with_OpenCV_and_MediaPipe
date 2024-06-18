# Face Detection with OpenCV and MediaPipe

Este projeto demonstra como usar OpenCV e MediaPipe para detectar rostos em tempo real usando a webcam do seu computador. O código captura vídeo da webcam, processa as imagens para detectar rostos e desenha caixas em torno dos rostos detectados.

## Requisitos

- Python 3.x
- OpenCV
- MediaPipe

## Instalação

Para instalar as bibliotecas necessárias, execute os seguintes comandos:

```sh
pip install opencv-python
pip install mediapipe
```

## Uso

Salve o seguinte código em um arquivo, por exemplo, `face_detection.py`:

```python
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
```

Execute o código com o seguinte comando:

```sh
python face_detection.py
```

## Como Funciona

1. **Captura de Vídeo**: O código usa OpenCV para capturar vídeo da webcam.
2. **Processamento de Imagem**: Cada quadro de vídeo é convertido de BGR para RGB.
3. **Detecção de Rosto**: MediaPipe é usado para detectar rostos no quadro de vídeo.
4. **Desenho nas Imagens**: Caixas são desenhadas em torno dos rostos detectados.
5. **Exibição de Vídeo**: O quadro de vídeo com as caixas desenhadas é exibido em uma janela.

Pressione `Esc` para encerrar o programa.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---