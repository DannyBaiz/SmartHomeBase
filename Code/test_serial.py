# Testskript für serielle Kommunikation mit Arduino (Display)
import serial
import time

# Passe den Port ggf. an (z.B. /dev/tty.usbmodemXXXX oder /dev/ttyUSB0)
SERIAL_PORT = '/dev/tty.usbmodem11301'  # Ersetze durch deinen Port
BAUD_RATE = 9600

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
time.sleep(2)  # Warten, bis Verbindung steht

print('1: Text anzeigen')
print('2: Display löschen')
print('3: Beenden')

while True:
    cmd = input('Befehl wählen (1/2/3): ')
    if cmd == '1':
        text = input('Text für Display: ')
        ser.write(f'DISPLAY:{text}\n'.encode('utf-8'))
    elif cmd == '2':
        ser.write(b'CLEAR\n')
    elif cmd == '3':
        break
    else:
        print('Ungültige Eingabe!')

ser.close()
print('Verbindung geschlossen.')
