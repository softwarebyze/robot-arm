
#include <Servo.h>
// buttons get 10k resistors

Servo servo[4]; // create an array of servos
const byte servoPins[] = {5,6,9,10};
const int angles[] = {5, 10, 90, 40};

void go(int servo_num, int to, int speed) {
  int servo_pos;
  int angle;
  while(servo_pos != to) {
    servo_pos = servo[servoPins[servo_num]].read();
    if (servo_pos > to) {
      angle = servo_pos-1;
    }
    else if (servo_pos < to) {
      angle = servo_pos+1;
    }
    servo[servoPins[servo_num]].write(angle);
    delay(speed);
  }
}

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
  Serial.println("Connecting to Robot Arm Servos");
  for (int n = 0; n < 4; n++) {
    Serial.print("Connecting to Servo");
    servo[n].attach(servoPins[n]);
    Serial.println(n);
  }
}

void loop() {
  int angle;
  int test_servo = 1;
  int speed = 10;
  if (Serial.available()) {
    Serial.println("Serial Available");
    angle = Serial.parseInt(); //which angle
    Serial.print("Setting angle to ");
    Serial.println(angle);
    go(test_servo, angle, speed);
  }
  
}
