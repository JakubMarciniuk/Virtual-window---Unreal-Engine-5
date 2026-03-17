import socket
import struct
from pythonosc import udp_client

# Ustawienia
OPENTRACK_IP = "127.0.0.1"
OPENTRACK_PORT = 4242
UE5_IP = "127.0.0.1"
UE5_PORT = 9000  # Użyjemy portu 9000, żeby było czysto

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((OPENTRACK_IP, OPENTRACK_PORT))
client = udp_client.SimpleUDPClient(UE5_IP, UE5_PORT)

print("MOST DZIALA. Przesyłam dane do Unreal Engine...")

while True:
    data, addr = sock.recvfrom(1024)
    # OpenTrack UDP wysyła 6 liczb (double): X, Y, Z, Yaw, Pitch, Roll
    if len(data) >= 48:
        d = struct.unpack('<6d', data[0:48])

        # Przypisujemy do zmiennych dla jasności
        x, y, z = d[0], d[1], d[2]
        yaw, pitch, roll = d[3], d[4], d[5]

        # Wysyłamy JEDNĄ paczkę do UE5: [Yaw, Pitch, Roll, X, Y, Z]
        # Adres wiadomości to "/dane", ale w UE5 będziemy to ignorować i brać wszystko jak leci
        client.send_message("/dane", [yaw, pitch, roll, x, y, z])