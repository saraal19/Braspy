from tkinter import *
import cv2
from PIL import Image, ImageTk
import mediapipe as mp
import time
import math
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
# Initialisation de l'objet de détection de main de mediapipe
mp_hands = mp.solutions.hands
handds=mp_hands.Hands()
#previous time
pTime = 0
#current time
cTime = 0
x1,y1,x2,y2=0,0,0,0

# Fonction pour afficher la caméra
def show_camera():
    # Afficher la caméra
    cap = cv2.VideoCapture(0)
    mp_hands = mp.solutions.hands
    handds = mp_hands.Hands()
    while True:
        # Capturer une image depuis la caméra
        ret, img = cap.read()
        # Inverser l'image horizontalement pour afficher comme un miroir
        img = cv2.flip(img, 1)
        # Convertir l'image depuis le format BGR (couleurs) à RGB (blanc et noir)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Convertir l'image en objet ImageTk
        img = ImageTk.PhotoImage(Image.fromarray(img))
        # Afficher l'image dans la Frame
        L1['image'] = img
        window.update()

    # Affichage des landmarks de la main détectée
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            ## eeemethode 1 pour afficher les circle sur la min et
            mpDraw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            #pour trouver id de chaque point de la main (chaque cercle)
            for id, lm in enumerate(hand_landmarks.landmark):
                #pour convert les point en pixel
                h, w, c = img.shape
                #pour trouver une position pour tous la main
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id,cx,cy)
                if id == 4:
                    x1,y1=cx,cy
                    cv2.circle(img, (cx,cy),15,(255, 0, 255), cv2.FILLED)
                if id ==8:
                    cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                    x2, y2 = cx, cy
                #faire une line entre 4 et 8
                cv2.line(img,(x1,y1),(x2,y2),(255,0,255),3)
                #trouver la destance entre 4 et8
                destance=math.hypot(x2-x1,y2-y1)
                print(destance)
                #ona max of destance 210 et min 30 et dans volume max 0 et min -65.25
                #convert destance on volume
                vol= np.interp(destance,[30,210],[-65.25,0])

window = Tk()
window.title("Commande bras manipulateur")
window.geometry("1200x900")
window.config(background="#C7E9B0")
message = Label(window, text="Vous pouvez commander le bras en suivant les gestes suivants :", font=("Century Gothic", 18), bg="#C7E9B0", fg="#454545")
message.pack()

#image poing=stop
imageStop = PhotoImage(file="poing.png")
# Créer un bouton avec une image
bouton1 = Button(window, image=imageStop)
# Positionner le bouton à l'aide de la méthode .place(x, y)
bouton1.place(x=70, y=70)
message1 = Label(window, text="Stop", font=("Century Gothic", 14), bg="#C7E9B0", fg="#454545")
message1.place(x=105, y=190)


#image pouce=rotation 360° base
imagePouce = PhotoImage(file="pouce.png")
bouton2 = Button(window, image=imagePouce)
bouton2.place(x=300, y=70)
message2 = Label(window, text="Rotation 360°", font=("Century Gothic", 14), bg="#C7E9B0", fg="#454545")
message2.place(x=300, y=190)

#image index=rotation 1ère articulation
imageIndex = PhotoImage(file="index.png")
bouton3 = Button(window, image=imageIndex)
bouton3.place(x=70, y=270)
message3 = Label(window, text="Rotation articulation 1", font=("Century Gothic", 14), bg="#C7E9B0", fg="#454545")
message3.place(x=30, y=390)

#image index+pouce=rotation 2ère articulation
imageIndexPouce = PhotoImage(file="indexPouce.png")
bouton4 = Button(window, image=imageIndexPouce)
bouton4.place(x=300, y=270)
message4 = Label(window, text="Rotation articulation 2", font=("Century Gothic", 14), bg="#C7E9B0", fg="#454545")
message4.place(x=260, y=390)

# Créer une Frame pour afficher la caméra
f1 = LabelFrame(window, bg="#BBD6B8")
f1.place(x=530, y=70)

# Créer un Label pour afficher l'image de la caméra
L1 = Label(f1, bg="#BBD6B8")
L1.pack()

# Créer un bouton pour démarrer la caméra
boutonCamera = Button(window, text="Démarrer la caméra", command=show_camera, font=("Century Gothic", 14), bg="white", fg="#454545")
boutonCamera.place(x=140, y='500')

window.mainloop()
