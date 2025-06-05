// Arduino Code for Smart Home Project

#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Initialize the LCD (I2C address 0x27, 16 column, 2 rows)
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  Serial.begin(9600); // Start serial communication
  lcd.begin(16, 2);   // Initialize the LCD (16 columns, 2 rows)
  lcd.backlight();    // Turn on the backlight
  lcd.setCursor(0, 0);
  lcd.print("Smart Home");
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');

    if (command.startsWith("DISPLAY:")) {
      String text = command.substring(8);
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print(text);
    } else if (command == "CLEAR") {
      lcd.clear();
    }
  }

  // Example: Send dummy sensor data to Raspberry Pi
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);

  // Display sensor value on LCD
  lcd.setCursor(0, 1);
  lcd.print("Sensor: ");
  lcd.print(sensorValue);

  delay(1000); // Wait for 1 second
}
