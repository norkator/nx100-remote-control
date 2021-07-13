# Motoman NX100 - Remote Control

Yaskawa Motoman NX100 industrial robot remote control ability research for machine vision control development. 
See [Youtube demo video](https://youtu.be/9swshogfL1c).

Actual tasks will be here [Uenian33 - nx100_robotic_tasks](https://github.com/uenian33/nx100_robotic_tasks).


Table of contents
=================
* [Documents](#documents)
    * [Youtube videos](#youtube-videos)
* [Infrastructure](#infrastructure)
* [NX100 Configs](#nx100-configs)
* [Install](#install)
* [Lint, Test, Build](#lint-test-build)
* [Programs](#programs)
* [MoveL](#movel)
* [MoveJ](#movej)
* [Arduino gripper](#arduino-gripper)
    * [Ladder changes](#ladder-changes)
    * [Python sample](#python-sample)
    * [Arduino code](#arduino-code)
    * [Sketch](#sketch)
* [Releasing](#releasing)



Documents
============
Documents for development

* [Uenian33 - nx100_robotic_tasks](https://github.com/uenian33/nx100_robotic_tasks)
    * End goal. This repository will be control origin for this robot in the future.
* [Ethernet Server Function Manual](https://drive.google.com/file/d/11TY9v_Tb5k23DTz9VuEBmj-vJE5Fmc4R/view) 
    * This document has information about http socket working.
* [Concurrent I/O Manual](https://drive.google.com/file/d/1Dhij10r6Mk60-kloPwJcXpPA7n-u2KN2/view?usp=sharing)
    * Remote IO signal outputs, inputs, all other IO signals and ladder programming information.


Youtube videos
-----
These videos are part of documentation.
* [First demo promo](https://youtu.be/9swshogfL1c) related to remote control software side.
* [Custom hardware gripper](https://youtu.be/Cx4sLZeZK_E) related to first test of working gripper.
* [Calibrating and testing ML pipeline](https://youtu.be/NBE9e7AJw6I) related to first tests with machine learning based control.
* [Grasping demo](https://youtu.be/nW2mAJsRXbo) Grasping demo. Using MOVL and MOVJ commands.


Infrastructure
============
This is planned infrastructure for robot project with computing server.<br>
![infra-image](doc/hardware_network.png) 


NX100 Configs
============
```diff
- Do changes with your own risk! in case you brick your robot or your setup is different and it doesn't work. I cannot help.
```
1. Log into NX100 with Yaskawa emperor password from security menu. Same menu as you use to login to maintenance mode.
   ```
   System info -> Security -> Select Management Mode ->
   But do not enter Management Mode password but instead Yaskawa emperor password.
   ```
   Do your own research to find required password.
2. Enable following FD parameters  
   All supported parameters list: [NX100 / NXC100 PARAMETER LIST](https://drive.google.com/file/d/1YA_C3Vg_eh7pp0q-liEpeXLgl6D-lV0I/view?usp=sharing)
   ```
   FD078 => bit set to 1 (Ethernet WWW)
   ```
3. Connect ethernet cable.
   ```
   LAN0 (next to serial COM port) 
   ```
   LAN1 should be occupied by default, that wire goes to pendant.
   ![pc-cards](doc/nx100_cards.jpg)
4. Specify ethernet configuration ip, mask, default gateway.
   ```
   1. Power off NX100 -> press down pendant "MAIN MENU" button while powering on NX100
   2. Release "MAIN MENU" after seeing Motoman screen on pendant.
   3. Login with Yaskawa emperor password from System -> Security.
   4. SYSTEM -> SETUP -> OPTION FUNCTION -> TCP -> "USED"
   5. SYSTEM -> SETUP -> OPTION FUNCTION -> NETWORK -> Give details.
   6. Under network also find HOST SETUP -> Provide address details.
   7. See that your changes have been saved.
   8. Reboot NX100 and ping your NX100 ip address.
   9. Test out this library.
   ```


Install
============

1. Install or upgrade existing package
   ```shell script
   pip install nx100-remote-control
   pip install --upgrade nx100-remote-control
   ```
2. You can change robot parameters via importing nx100_remote_control.
   ```python
   import nx100_remote_control
   
   nx100_remote_control.NX100_IP_ADDRESS = '192.168.2.28'
   nx100_remote_control.NX100_TCP_PORT = 80
   
   nx100_remote_control.MOCK_RESPONSE = False  
   ```
3. Import available contents like below examples or run web server. 
    * Web interface opens from `http://localhost:8080/` which looks something like this in below image.
   ```python
   import nx100_remote_control
   from nx100_remote_control.module import WebServer
   
   nx100_remote_control.MOCK_RESPONSE = True 
   
   WebServer.run(addr="localhost", port=8080)
   ```
   * Use MOCK_RESPONSE = True to run without attached robot.
   * Replace "localhost" with "0.0.0.0" to make web server available to local network devices.

![web-interface-image](doc/web_img.png) 


Lint, Test, Build
============
Must have installed: `pip install flake8 pytest`  
Lint: `flake8 ./nx100_remote_control --count --select=E9,F63,F7,F82 --show-source --statistics`  
Test: `pytest`  
Build: `python -m build`  


Programs
============

`Testing.py` => Used for development and testing individual commands.   
`XboxController.py` => As name says, can use controller to control robot, just demo.  


MoveL
============
Quick sample for MovL command to do linear movement with robot. 
See MoveL object for more details or read `Ethernet Server Function Manual`.

```python
from nx100_remote_control.module import Commands, Utils
from nx100_remote_control.objects import MoveL

Commands.write_linear_move(MoveL.MoveL(
    MoveL.MoveL.motion_speed_selection_posture_speed,
    5,
    MoveL.MoveL.coordinate_specification_base_coordinate,
    353.769, 202.779, 120.658,
    -1.34, 35.78, 27.84,
    Utils.binary_to_decimal(0x00000001),
    0, 0, 0, 0, 0, 0, 0
))
```
Use MoveL.MoveL object to see options for `motion_speed_selection_` and for `coordinate_specification_`

Then to wait for move to be completed you can use callback function as example:

```python
from nx100_remote_control.module import Commands, Utils
from nx100_remote_control.objects import MoveL

def callback_success():
    print('MoveL position has been reached')

def callback_failed():
    print('MoveL error or position not reached on given timeout')

move_l = MoveL.MoveL(
    MoveL.MoveL.motion_speed_selection_posture_speed,
    5,
    MoveL.MoveL.coordinate_specification_base_coordinate,
    353.769, 202.779, 120.658,
    -1.34, 35.78, 27.84,
    Utils.binary_to_decimal(0x00000001),
    0, 0, 0, 0, 0, 0, 0
)
    
Commands.robot_in_target_point_callback(
    move_l=move_l, timeout=10, _callback_success=callback_success, _callback_failed=callback_failed
)
```

So this will exec `_callback_success` if position reached in given timeout or run `_callback_failed` if not.

Another commander class way

```python
from nx100_remote_control.module import LinearMove, Utils
from nx100_remote_control.objects import MoveL
    
move_l = MoveL.MoveL(
    MoveL.MoveL.motion_speed_selection_posture_speed,
    5,
    MoveL.MoveL.coordinate_specification_base_coordinate,
    352.769, 202.779, 120.658,
    -1.34, 35.78, 27.84,
    Utils.binary_to_decimal(0x00000001),
    0, 0, 0, 0, 0, 0, 0
)

linear_move = LinearMove.LinearMove()
linear_move.go(move_l=move_l, wait=True, poll_limit_seconds=10)
print('finished')
```


MoveJ
============
Quick sample for MovJ command to do joint motion movement with robot. 
Read `Ethernet Server Function Manual` for more details about MOVJ

```diff
- !!! BE CAREFUL WITH MOVJ COMMAND AND IT'S SPEED SETTING !!!
```
* Speed is given as percentage from 1 to 100.
* Start running it with lower speed. 

```python
from nx100_remote_control.module import JointMove, Utils
from nx100_remote_control.objects import MoveJ
    
move_j = MoveJ.MoveJ(
    25,  # speed %
    MoveJ.MoveJ.coordinate_specification_base_coordinate,
    352.769, 202.779, 120.658,
    -1.34, 35.78, 27.84,
    Utils.binary_to_decimal(0x00000001),
    0, 0, 0, 0, 0, 0, 0
)
linear_move = JointMove.JointMove()
linear_move.go(move_j=move_j, wait=True, poll_limit_seconds=10)
print('finished')
```


Arduino gripper
============
Arduino folder contains code and sketch for custom Gripper integrated for NX100 Motoman.


Ladder changes
-------
NX100 ladder config had by default GRP meaning grouped signals so had to ungroup them
to gain access to output relay #30052
![ladder-config](arduino/ladder_config.jpg) 

Idea here was that I needed to be able to control relay #30052
with stock #10022 universal output signal but also with network input #22012 signal
and this needed STR + NOT handling for both cases (see image ladder line 0359)


Python sample
-------
Work in progress with gripper.

```python
from nx100_remote_control.module import Gripper

Gripper.write_gripper_close()
Gripper.write_gripper_open()
Gripper.read_gripper_closed_command_register()
Gripper.read_gripper_acknowledge()
Gripper.read_gripper_hit()
```


Arduino code
-------
Obvious bits are one input and two outputs. Hardware 
decisions don't matter, code can be changed accordingly.

* PC817 is used to bring NX100 IO card UNIVERSAL OUTPUT signal as input for Arduino.
* Two relays are used to short circuit NX100 input signal line's to switch on/off 
UNIVERSAL INPUT signal.



Sketch
-------

![Electrical-drawing](./arduino/GripperSketch_bb.png)

Custom part sources
* [L298 Stepper Driver](https://forum.fritzing.org/uploads/short-url/cOmtO5zuLdoAiea5hppdo0YsU1N.fzpz)
* [LM2596 Step Down Module](https://forum.fritzing.org/uploads/default/original/2X/8/876018ce35bcc333dd7083f3bbbc5dcc86a9fb20.fzpz)
* [PC817 Opto-isolator](https://github.com/RafaGS/Fritzing/blob/master/Sharp%20PC817.fzpz)
* [HC-SR04 Sonar](https://fritzing-data.s3.eu-central-1.amazonaws.com/0ec82cd976950bb5439acdd825c9c8c1.fzpz?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA2HCNQME5J5JNR5LX%2F20210612%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20210612T133948Z&X-Amz-Expires=900&X-Amz-SignedHeaders=host&X-Amz-Signature=368c32cdbce2a5ce10266e8599b724db47e37fa24c7fefffe923d4e05937c0f1)


Releasing
============
```diff
- Remember to increment setup.cfg version before release tag!
```
