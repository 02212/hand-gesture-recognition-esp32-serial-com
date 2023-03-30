#include <Arduino.h>
String InBytes;
#define LED7 33
#define LED1 13
#define LED2 12
#define LED3 14
#define LED4 27
#define LED5 26
#define LED6 25

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
  pinMode(LED6, OUTPUT);
  pinMode(LED7, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    InBytes = Serial.readStringUntil('\n');
  if (InBytes == "0") {
      digitalWrite(LED4, LOW);
      digitalWrite(LED7, LOW);
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, LOW);
      digitalWrite(LED3, LOW);
      digitalWrite(LED5, LOW);
      digitalWrite(LED6, LOW);
      Serial.write("0");
      
    }
    if (InBytes == "1") {
      digitalWrite(LED4, LOW);
      digitalWrite(LED7, LOW);
      digitalWrite(LED1, HIGH);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, HIGH);
      digitalWrite(LED5, HIGH);
      digitalWrite(LED6, HIGH);
      Serial.write("1");
      
    }
    if (InBytes == "2") {
      digitalWrite(LED4, LOW);
      digitalWrite(LED7, HIGH);
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, LOW);
      digitalWrite(LED5, LOW);
      digitalWrite(LED6, LOW);
      Serial.write("2");
      
    }

      if (InBytes == "3") {
      digitalWrite(LED4, LOW);
      digitalWrite(LED7, LOW);
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, HIGH);
      digitalWrite(LED3, LOW);
      digitalWrite(LED5, LOW);
      digitalWrite(LED6, HIGH);
      Serial.write("3");
      
    }
        if (InBytes == "4") {
      digitalWrite(LED4, LOW);
      digitalWrite(LED7, LOW);
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, LOW);
      digitalWrite(LED3, HIGH);
      digitalWrite(LED5, HIGH);
      digitalWrite(LED6, HIGH);
      Serial.write("4");
      
    }
        if (InBytes == "5") {
      digitalWrite(LED4, HIGH);
      digitalWrite(LED7, LOW);
      digitalWrite(LED1, LOW);
      digitalWrite(LED2, LOW);
      digitalWrite(LED3, LOW);
      digitalWrite(LED5, HIGH);
      digitalWrite(LED6, LOW);
      Serial.write("5");
    }

    else {
      Serial.write("invalid information");
    }
  }
}
