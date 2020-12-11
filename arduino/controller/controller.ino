

#define px 2
#define py 3


void setup() {
    Serial.begin(9600);
  
}

void loop() {
  int y = digitalRead(py);
  int x = digitalRead(px);
  
  if (x == 0) {
    Serial.print(0);
  } else if( y == 0) {
    Serial.print(1);
  }
  
  delay(100);

}
