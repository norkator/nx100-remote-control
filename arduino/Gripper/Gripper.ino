/*
 * NX100 Robot gripper controller (Nano) ATmega328p
 */

// ## Libraries ##
#include <Stepper.h>
#include <Wire.h>

// ########################
// ## PIN CONFIGURATIONS ##
// ########################
int motorA1       = 2;  // stepper A1
int motorA2       = 3;  // stepper A2
int motorB1       = 4;  // stepper B1
int motorB2       = 5;  // stepper B2
int endStop       = 6;  // homing endstop
int robotInput    = 7;  // close|open signal (PC817)
int robotOutput   = 8;  // acknowledge signal (using relay)
int holdOutput    = 9;  // gripper hit something (using relay)
int hitSensor     = 10; // hit signal trigger
int sonarTrigPin  = 11; // Trigger|enable pin
int sonarEchoPin  = 12; // Output signal | Echo pin
int I2C_SDA_PIN   = A4; // SDA for i2C
int I2C_SCL_PIN   = A5; // SCL for i2C


// Variables
int I2C_ADDRESS = 8; // randomly chosen address
boolean homingDone = false;
const int stepsPerRevolution = 200;   // steps per revolution
const int stepperMotorSpeed = 150;    // stepper motor speed
const int gripperStepsFullyOpen = -1500; // how many steps needed to reverse when gripper is fully open
Stepper myStepper(stepsPerRevolution, motorA1, motorA2, motorB1, motorB2);
int currentStepPosition = 0;
boolean holdOn = false;
long duration = 0, cm = 0;


// SETUP
void setup() {
  // Init serial
  Serial.begin(9600);
  // EStop
  pinMode(endStop, INPUT_PULLUP);
  // NX100 input
  pinMode(robotInput, INPUT_PULLUP);
  // NX100 output
  pinMode(robotOutput, OUTPUT);
  digitalWrite(robotOutput, HIGH); // off
  // Robot hold output
  pinMode(holdOutput, OUTPUT);
  digitalWrite(holdOutput, HIGH); // off
  // Hit sensor (switch)
  pinMode(hitSensor, INPUT_PULLUP);
  // Init stepper
  myStepper.setSpeed(stepperMotorSpeed);
  Serial.println("Setup ok");
  // Sonar
  pinMode(sonarTrigPin, OUTPUT);
  pinMode(sonarEchoPin, INPUT);
  // Join i2c bus with address
  Wire.setClock(10000);
  Wire.begin(I2C_ADDRESS); 
  Wire.onReceive(receiveCommand);
}


// LOOP
void loop() {
  if (!homingDone) {
    homing();
  }

  // Sonar distance
  readSonar();

  // Robot gives gripper close position value command, finally acknowledge with output signal
  int rInputVal = digitalRead(robotInput);
  if (rInputVal == LOW) {
    // closing gripper
    int newPos = abs(gripperStepsFullyOpen);
    if (currentStepPosition < newPos) {
      Serial.println("Closing gripper");
      myStepper.step(newPos);
      currentStepPosition = newPos;
      digitalWrite(robotOutput, LOW); // acknowledge closed
    }
  } else {
    // opening gripper
    if (currentStepPosition > gripperStepsFullyOpen) {
      Serial.println("Opening gripper");
      myStepper.step(gripperStepsFullyOpen);
      currentStepPosition = gripperStepsFullyOpen;
      digitalWrite(robotOutput, HIGH); // acknowledge open
    }
  }


  // Gripper hit switch trigger action
  // will turn robot hold on, hold can be manualle released from robot pendant
  int hInputVal = digitalRead(hitSensor);
  if (hInputVal == LOW) {
    if (holdOn == false) {
      Serial.println("Gipper hit -> turning hold on!");
      digitalWrite(holdOutput, LOW); // hold on
      holdOn = true;
    }
  } else {
    if (holdOn == true) {
      Serial.println("Gipper ok -> turning hold off!");
      digitalWrite(holdOutput, HIGH); // hold off
      holdOn = false;
    }
  }


  turnOffStepper();
}


/**
 * Homing procedure
 * 1. close gripper more till hit estop
 * 2. open gripper fully
 * 3. set homing done
 */
void homing() {
  Serial.println("Homing gripper...");
  int steps = 0;
  int eStopVal = HIGH;
  while (eStopVal == HIGH) {
    eStopVal = digitalRead(endStop);
    myStepper.step(1);
    steps++;
  }
  Serial.print("Gripper endstop hit at ");
  Serial.print(steps);
  Serial.println(" steps.. gripper is fully closed");
  myStepper.step(gripperStepsFullyOpen); // open fully
  currentStepPosition = gripperStepsFullyOpen;
  Serial.println("Gripper fully open, saving current position");
  homingDone = true;
}


/**
 * Turn off stepper driver
 * solves stepper driver overheating problem
 */
void turnOffStepper() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, LOW);
}


/**
 * Meassure sonar distance
 * sonar is installed next to camera pointing directly same direction
 * code taken from: https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/
 */
void readSonar() {
  digitalWrite(sonarTrigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(sonarTrigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(sonarTrigPin, LOW);
  duration = pulseIn(sonarEchoPin, HIGH);
  cm = (duration/2) / 29.1;     // Divide by 29.1 or multiply by 0.0343
  // inches = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135
}


/**
 * i2c receive command
 * Raspberry Pi will command nano to do something
 */
void receiveCommand(int byteCount) {
  String cmd = "";
  while (1 < Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    cmd += c;
    Serial.print(c);         // print the character
  }
  Serial.println("");
  Wire.read();    // receive byte as an integer
  if (cmd == "sonar_distance") {
    Wire.write(cm);
  }
}
