# Smart Home Projekt

## Übersicht
Dieses Projekt verbindet einen Arduino mit einem Raspberry Pi, um Sensordaten und Steuerungsoptionen in einem Home Assistant Dashboard darzustellen. Die Kommunikation erfolgt über MQTT.

## Komponenten
- **Arduino**: Sensoren und Display
- **Raspberry Pi**: MQTT-Broker und Server
- **Home Assistant**: Dashboard

## Verzeichnisstruktur
- `arduino/`: Code für den Arduino
- `raspberry_pi/`: Code für den Raspberry Pi
- `home_assistant/`: Konfiguration für Home Assistant

## Schritte zur Einrichtung
1. Installiere MQTT-Broker auf dem Raspberry Pi.
2. Lade den Arduino-Code hoch.
3. Konfiguriere Home Assistant.

## Anforderungen
- Raspberry Pi mit installiertem Raspbian OS
- Arduino (z. B. Uno, Mega, ESP32)
- Home Assistant
- MQTT-Broker (z. B. Mosquitto)
