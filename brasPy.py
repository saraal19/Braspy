from tkinter import *
import cv2
from PIL import Image,ImageTk
window=Tk()
window.title("Commande bras manipulateur")
window.geometry("1200x500")
window.config(background="#C7E9B0")
message=Label(window,text="Vous pouvez commander le bras en suivant les gestes suivants :",font=("Century Gothic",18),bg="#C7E9B0",fg="#454545")
message.pack()

#image poing=stop
imageStop= PhotoImage(file="poing.png")
# Créer un bouton avec une image
bouton1 = Button(window, image=imageStop)
# Positionner le bouton à l'aide de la méthode .place(x, y)
bouton1.place(x=70, y=70)
message1=Label(window,text="Stop",font=("Century Gothic",14),bg="#C7E9B0",fg="#454545")
message1.place(x=105, y=190)


#image pouce=rotation 360° base
imagePouce=PhotoImage(file="pouce.png")
bouton2 = Button(window, image=imagePouce)
bouton2.place(x=300, y=70)
message2=Label(window,text="Rotation 360°",font=("Century Gothic",14),bg="#C7E9B0",fg="#454545")
message2.place(x=300, y=190)

#image index=rotation 1ère articulation
imageIndex=PhotoImage(file="index.png")
bouton3 =Button(window, image=imageIndex)
bouton3.place(x=70, y=270)
message3=Label(window,text="Rotation articulation 1",font=("Century Gothic",14),bg="#C7E9B0",fg="#454545")
message3.place(x=30, y=390)

#image index+pouce=rotation 2ère articulation
imageIndexPouce=PhotoImage(file="indexPouce.png")
bouton4=Button(window, image=imageIndexPouce)
bouton4.place(x=300, y=270)
message4=Label(window,text="Rotation articulation 2",font=("Century Gothic",14),bg="#C7E9B0",fg="#454545")
message4.place(x=260, y=390)

window.mainloop()