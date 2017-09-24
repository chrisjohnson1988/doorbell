const int pulses[] = {1530, 433, 1530, 433, 1530, 433};
volatile int pulsesPos = 0;
int outPin = 13;
volatile boolean ringing = false;

void setup() {
  attachInterrupt(0, handleInterrupt, CHANGE);
  pinMode(outPin, OUTPUT);
}

void loop() {
  if(ringing) {
    digitalWrite(outPin, HIGH);
    delay(3000);
    digitalWrite(outPin, LOW);
    ringing = false;
  }  
}

unsigned int diff(int a, int b) {
  return abs(a - b);
}

void handleInterrupt() {
  static unsigned long lastTime = 0;
  const long time = micros();
  const unsigned int duration = time - lastTime;
  
  if(duration < 10) {
    return;
  }
  if(diff(duration, pulses[pulsesPos]) < 200) {
    pulsesPos++;
    if(pulsesPos == 6) {
     pulsesPos = 0;
     ringing = true;
    }
  }
  else {
    pulsesPos = 0;
  }
  lastTime = time;
}
