#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {

  Serial.begin(9600);
  mySwitch.enableTransmit(10);
  pinMode(LED_BUILTIN, OUTPUT);
  mySwitch.setPulseLength(148);
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  while (Serial.available()){
    char leitor = (char)Serial.read();

    if(leitor == 'l'){
      mySwitch.sendTriState("0FFFFFFFFFFF");
      digitalWrite(LED_BUILTIN, HIGH);
      delay(2000);
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("luz");
    }
    if (leitor == 'v') {
      mySwitch.sendTriState("FFFFF0FFFFFF");
      digitalWrite(LED_BUILTIN, HIGH);
      delay(2000);
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("ventilador");
    }
  }
}
