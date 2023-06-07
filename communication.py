import serial.tools.list_ports

# Trouver tous les ports série disponibles
ports = serial.tools.list_ports.comports()

# Chercher le port correspondant au Raspberry Pi Pico
for port in ports:
    if "Raspberry Pi Pico" in port.description:
        print(f"Port trouvé : {port.device}")
        break
else:
    print("Aucun port trouvé pour le Raspberry Pi Pico")