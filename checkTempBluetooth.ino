#define temperaturePin A0
float voltage, degreeC, degreeF;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  delay(10000);
  // Serial.println("started");
}

// Sends the degrees in Fahrenheit every 15 minutes
void loop() {
  for (int i = 0; i < 10; i++){
    voltage = getVoltage(temperaturePin);
    degreeC = (voltage - 0.5) * 100;
    degreeF = degreeC * (9.0/5.0) + 32.0;
    Serial.println(degreeF);
    delay(1000);
  }
  delay(890000);
}

float getVoltage(int pin) {
  return analogRead(pin) * 0.004882814;
}
