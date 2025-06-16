void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);  // LED integrado en pin 13
  digitalWrite(13, LOW);
}

void loop() {
  if (Serial.available() > 0) {
    char data = Serial.read();
    if (data == '1') {
      digitalWrite(13, HIGH);  // Enciende LED si detecta teléfono
    } else if (data == '0') {
      digitalWrite(13, LOW);   // Apaga LED si no detecta teléfono
    }
  }
}
