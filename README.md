![promo-image](doc/web_img.png) 

# Motoman NX100 - Remote Control

Yaskawa Motoman NX100 industrial robot remote control ability research.


Table of contents
=================
* [Documents](#documents)
* [Goals](#goals)
* [Install](#install)



Documents
============
Documents for development

* [Ethernet Server Function Manual](https://drive.google.com/file/d/11TY9v_Tb5k23DTz9VuEBmj-vJE5Fmc4R/view) 



Goals
============

* Simple web page for basic control and monitoring.
* Usable functions and response parsers to work as part of other Python apps.
* Key input functionality for moving robot with keyboard or controller.



Install
============

1. Go to `/module/Socket.py` and change `nx100_address` ip address to your network robot address.
2. Set `/module/Socket.py` MOCK_RESPONSE variable to False for real robot use or use Mock to test without robot.
3. Run app. Web interface opens from `http://localhost:8080/`

