import serial
from time import sleep
# Créer un objet de port série avec les paramètres de votre port
ser = serial.Serial('COM4', baudrate=9600)
# Envoi d'une phrase de test
message = "Test de communication série"

ser.write(message.encode('utf-8'))   # Convertissez la phrase en bytes
sleep(0.5)

# Fermeture de la connexion série
ser.close()
print("done")

# Attendre la réponse de votre carte MicroPython
#response = ser.readline()

# Afficher la réponse dans la console Python
#print(response)