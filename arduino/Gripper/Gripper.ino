/*
 * NX100 Robot gripper controller (Nano) ATmega328p
 */

// ## Libraries ##
#include <Stepper.h>
#include <Wire.h>

// ########################
// ## PIN CONFIGURATIONS ##
// ########################
int motorA1 = 2;
int motorA2 = 3;
int motorB1 = 4;
int motorB2 = 5;
int endStop = 6; // homing endstop
int robotInput = 7; // close|open signal (PC817)
int robotOutput = 8; // acknowledge signal (using relay)
int holdOutput = 9; // gripper hit something (using relay)
int hitSensor = 10; // hit signal trigger

// Variables
boolean homingDone = false;
const int stepsPerRevolution = 200;   // steps per revolution
const int stepperMotorSpeed = 150;    // stepper motor speed
const int gripperStepsFullyOpen = -1500; // how many steps needed to reverse when gripper is fully open
Stepper myStepper(stepsPerRevolution, motorA1, motorA2, motorB1, motorB2);
int currentStepPosition = 0;
boolean holdOn = false;


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
}


// LOOP
void loop() {
  if (!homingDone) {
    homing();
  }


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
