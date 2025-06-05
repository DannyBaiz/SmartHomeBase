# Serial-to-MQTT bridge for Arduino <-> MQTT (for Home Assistant)
import serial
import paho.mqtt.client as mqtt
import time
import threading
import sys
import glob

BAUD_RATE = 9600
MQTT_BROKER = 'localhost'
MQTT_SENSOR_TOPIC = 'home/sensors'
MQTT_DISPLAY_TOPIC = 'home/display'
MQTT_CLEAR_TOPIC = 'home/display/clear'

def find_arduino_port():
    # Sucht nach typischen Arduino-Ports auf macOS
    ports = glob.glob('/dev/tty.usbmodem*') + glob.glob('/dev/tty.usbserial*')
    if not ports:
        print('Kein Arduino-Port gefunden! Bitte Arduino anschließen.')
        sys.exit(1)
    print(f'Gefundene Ports: {ports}')
    return ports[0]  # Nimmt den ersten gefundenen Port

SERIAL_PORT = find_arduino_port()

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
time.sleep(2)

client = mqtt.Client()
client.connect(MQTT_BROKER)

# Empfange MQTT-Befehle und leite an Arduino weiter
def on_message(client, userdata, msg):
    if msg.topic == MQTT_DISPLAY_TOPIC:
        text = msg.payload.decode('utf-8')
        ser.write(f'DISPLAY:{text}\n'.encode('utf-8'))
    elif msg.topic == MQTT_CLEAR_TOPIC:
        ser.write(b'CLEAR\n')

client.subscribe([(MQTT_DISPLAY_TOPIC, 0), (MQTT_CLEAR_TOPIC, 0)])
client.on_message = on_message

def serial_to_mqtt():
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').strip()
            if data.isdigit():
                client.publish(MQTT_SENSOR_TOPIC, data)

threading.Thread(target=serial_to_mqtt, daemon=True).start()
client.loop_forever()
