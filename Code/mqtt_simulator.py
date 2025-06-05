# MQTT Sensor Data Simulator
# Sendet Testdaten an das Topic 'home/test' für Home Assistant

import time
import paho.mqtt.client as mqtt

MQTT_BROKER = 'localhost'
MQTT_PORT = 1883
MQTT_TOPIC = 'home/test'

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT)

try:
    value = 0
    while True:
        value += 1
        payload = str(value)
        print(f"Sende {payload} an {MQTT_TOPIC}")
        client.publish(MQTT_TOPIC, payload)
        time.sleep(5)
except KeyboardInterrupt:
    print("Simulator gestoppt.")
    client.disconnect()
