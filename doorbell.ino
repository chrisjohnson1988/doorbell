const int PULSES[] = {1530, 433};
const int PULSE_LENGTH = sizeof(PULSES)/2;
const int RANGE = 200;
const int PULSE_COUNT = 6;

volatile int pulsesPos = 0;

void setup() {
  Serial.begin(9600);
  Serial.println("\nRESET");
  attachInterrupt(0, handleInterrupt, CHANGE);
}

void loop() {
}

unsigned int diff(int a, int b) {
  return abs(a - b);
}

void handleInterrupt() {
  static unsigned long lastTime = 0;
  const long time = micros();
  const unsigned int duration = time - lastTime;
  
  if(duration < 50) {
    return;
  }
  
  if(diff(duration, PULSES[pulsesPos % PULSE_LENGTH]) < RANGE) {  
    if(++pulsesPos == PULSE_COUNT) {
      Serial.print("x");
      pulsesPos = 0;
    }
  } else {
    pulsesPos = 0;
  }
  lastTime = time;
}
