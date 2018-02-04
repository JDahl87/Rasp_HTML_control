#include <SoftwareSerial.h>

SoftwareSerial mySerial(10, 11); // RX, TX
static int messageSize = 9;
int counter = 0;

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  Serial.println("Goodnight moon!");
  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);
  //mySerial.println("Hello");
}

void loop() { // run over and over
  if (mySerial.available()) {
    Serial.write(mySerial.read());
    counter++;
  }
  if (counter >= 9){
    Serial.println();
    counter = 0;
  }
  
  if (Serial.available()) {
    mySerial.write(Serial.read());
  }
}

