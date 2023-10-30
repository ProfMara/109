import cv2 
import numpy
import mediapipe as mp
#importando o controlador do teclado



#captura o vídeo
video = cv2.VideoCapture(0)

#pegando as medidas do video
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

#detecção de mãos
mp_hands = mp.solutions.hands
#ferramentas de desenho
mp_draw = mp.solutions.drawing_utils

#robozinho detector de maos
hands = mp_hands.Hands(min_detection_confidence=0.01, min_tracking_confidence=0.05)

tipIds = [4,8,12,16,20]

def contarDedos(img, hand_landmarks, handNo=0):
    fingers = []
    global state

    if hand_landmarks:
        landmarks = hand_landmarks[handNo].landmark

        for i in tipIds:
            finger_tip_y = landmarks[i].y
            finger_bottom_y = landmarks[i-2].y

            #se o dedo não for dedão
            if i != 4:
                if finger_tip_y < finger_bottom_y:
                    fingers.append(1)
                else:
                    fingers.append(0)
        
        total = fingers.count(1)

        

        

        texto = f"Dedos: {total}"
        
        cv2.putText(img, texto, (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (200,0,0),2  )

#desenha a mão
def desenharMarcas(img, marcas):
    if marcas:
        for marca in marcas:
            mp_draw.draw_landmarks(img, marca, mp_hands.HAND_CONNECTIONS)

while True:

    success, frame = video.read()
    if success:
        #manda identificar se há mãos na imagem
        results = hands.process(frame)
        
        desenharMarcas(frame, results.multi_hand_landmarks)
        contarDedos(frame, results.multi_hand_landmarks)
        cv2.imshow("WEBCAM", frame)
    
    if cv2.waitKey(2)==27:
        break