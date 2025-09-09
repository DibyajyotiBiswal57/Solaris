#include <Servo.h>
Servo plantServo;

const int ldrPin = A0;      // LDR sensor analog pin
const int servoPin = 9;     // Servo signal pin
int maxLight = 0;
int bestPos = 90;

void setup() {
  plantServo.attach(servoPin);
  Serial.begin(9600);
}

void loop() {
  maxLight = 0;
  bestPos = 90;

  // Sweep the servo from 0 to 180 degrees
  for (int pos = 0; pos <= 180; pos += 10) {
    plantServo.write(pos);
    delay(300);  // Wait for LDR to stabilize

    int lightVal = analogRead(ldrPin);
    Serial.print("Position: "); Serial.print(pos);
    Serial.print(" | Light Level: "); Serial.println(lightVal);

    if (lightVal > maxLight) {
      maxLight = lightVal;
      bestPos = pos;
    }
  }

  // Move to the brightest position
  plantServo.write(bestPos);
  Serial.print("Best Position: "); Serial.println(bestPos);

  delay(60000);  // Wait 1 minute before next scan
}
