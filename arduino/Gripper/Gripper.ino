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

// Variables
const int stepsPerRevolution = 200;   // steps per revolution
const int stepperMotorSpeed = 300;    // stepper motor speed
Stepper myStepper(stepsPerRevolution, motorA1, motorA2, motorB1, motorB2);


// SETUP
void setup() {
  // Init serial
  Serial.begin(9600);
  // Init stepper
  myStepper.setSpeed(stepperMotorSpeed);
  Serial.println("Setup ok");
}


// LOOP
void loop() {
  delay(1 * 1000);

  myStepper.step(2500);

  /*
  if (getValue(commandToProcess,';',0) == "forward") {
    myStepper.step( getValue(commandToProcess,';',1).toInt() );
  } else if (getValue(commandToProcess,';',0) == "backward") {
    myStepper.step(-getValue(commandToProcess,';',1).toInt() );
  }
  */
  
  turnOffStepper();
}


// Solves stepper driver overheating problem
void turnOffStepper() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, LOW);
}
