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
int endStop = 6;
int robotInput = 7;
int robotOutput = 8;

// Variables
boolean homingDone = false;
const int stepsPerRevolution = 200;   // steps per revolution
const int stepperMotorSpeed = 300;    // stepper motor speed
Stepper myStepper(stepsPerRevolution, motorA1, motorA2, motorB1, motorB2);
int currentStepPosition = 0;


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
  // Init stepper
  myStepper.setSpeed(stepperMotorSpeed);
  Serial.println("Setup ok");
}


// LOOP
void loop() {
  if (!homingDone) {
    // homing();
  }

  int rInputVal = digitalRead(robotInput);
  if (rInputVal == LOW) {
    // delay(1000);
    myStepper.step(2500);
  }

  // Todo, robot gives gripper close position value command, 
  // move gripper to wanted position and set output HIGH to acknowledge
  /*
  int commandPositionValue = digitalRead(robotInput);
  ...
  digitalWrite(robotOutput, HIGH);
  */

  // Todo, robot gives gripper open position value command,
  // move gripper to wanted position and set output LOW to acknowledge
  /*
  int commandPositionValue = digitalRead(robotInput);
  ...
  digitalWrite(robotOutput, LOW);
  */
  
  turnOffStepper();
}


/**
 * Homing procedure
 * 1. close gripper more till hit estop
 * 2. open gripper fully
 * 3. set homing done
 */
void homing() {
  int eStopVal = digitalRead(endStop);
  while (eStopVal == LOW) {
    myStepper.step(1);
  }
  myStepper.step(-100); // open fully
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
