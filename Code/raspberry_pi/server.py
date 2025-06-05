# Raspberry Pi Server Code for Smart Home Project

import serial
import paho.mqtt.client as mqtt

# Serial port configuration
SERIAL_PORT = '/dev/ttyUSB0'  # Adjust as needed
BAUD_RATE = 9600

# MQTT configuration
MQTT_BROKER = 'localhost'
MQTT_TOPIC = 'home/sensors'
MQTT_DISPLAY_TOPIC = 'home/display'
MQTT_CLEAR_TOPIC = 'home/display/clear'

# Initialize serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# Initialize MQTT client
client = mqtt.Client()
client.connect(MQTT_BROKER)

# Callback for MQTT messages
def on_message(client, userdata, msg):
    if msg.topic == MQTT_DISPLAY_TOPIC:
        text = msg.payload.decode('utf-8')
        ser.write(f"DISPLAY:{text}\n".encode('utf-8'))
    elif msg.topic == MQTT_CLEAR_TOPIC:
        ser.write("CLEAR\n".encode('utf-8'))

client.on_message = on_message
client.subscribe([(MQTT_DISPLAY_TOPIC, 0), (MQTT_CLEAR_TOPIC, 0)])

print("Server is running...")

try:
    while True:
        if ser.in_waiting > 0:
            # Read data from Arduino
            data = ser.readline().decode('utf-8').strip()
            print(f"Received: {data}")

            # Publish data to MQTT broker
            client.publish(MQTT_TOPIC, data)

except KeyboardInterrupt:
    print("Server stopped.")
    ser.close()
    client.disconnect()
