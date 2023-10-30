import cv2
import mediapipe as mp
import math


cap = cv2.VideoCapture(0)



#mãos
mp_hands = mp.solutions.hands
#ferramentas de desenho
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(min_detection_confidence=0.6, min_tracking_confidence=0.5 )
tipIds = [4,8,12,16,20]

def contarDedos(img, hand_landmarks, handNo=0):
   
   

    if hand_landmarks:
        
        landmarks = hand_landmarks[handNo].landmark
        
       
        #PINÇA
        
        
        

       

      
        
def desenharMarcas(image, marcas):
    if marcas:
        for marca in marcas:
            mp_draw.draw_landmarks(image, marca, mp_hands.HAND_CONNECTIONS)


while True:
    success, image = cap.read()
    if success:
        results = hands.process(image)
        desenharMarcas(image, results.multi_hand_landmarks )
        contarDedos(image,results.multi_hand_landmarks )
        cv2.imshow("", image)

    if cv2.waitKey(1)==27:
        break


