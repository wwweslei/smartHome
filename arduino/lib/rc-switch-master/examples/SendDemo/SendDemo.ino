/*
  Example for different sending methods
  
  https://github.com/sui77/rc-switch/
  
*/

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {

  Serial.begin(9600);
  
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(10);

  // Optional set pulse length.
  mySwitch.setPulseLength(139);
  
  // Optional set protocol (default is 1, will work for most outlets)
   mySwitch.setProtocol(1);
  
  // Optional set number of transmission repetitions.
  // mySwitch.setRepeatTransmit(15);
  
}

void loop() {

  /* See Example: TypeA_WithDIPSwitches */
  mySwitch.switchOn("1398101", "00010");
  delay(1000);
  mySwitch.switchOff("1398101", "00010");
  delay(1000);

  /* Same switch as above, but using decimal code */
  mySwitch.send(1398101, 24);
  delay(1000);  
  mySwitch.send(1398101, 24);
  delay(1000);  

  /* Same switch as above, but using binary code */
  mySwitch.send("000101010101010101010101");
  delay(1000);  
  mySwitch.send("000101010101010101010101");
  delay(1000);

  /* Same switch as above, but tri-state code */ 
  mySwitch.sendTriState("0FFFFFFFFFFF");
  delay(1000);  
  mySwitch.sendTriState("0FFFFFFFFFFF");
  delay(1000);

  delay(20000);
}
