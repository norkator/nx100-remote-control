# Raspberry Pi Notes

Some notes for Raspberry PI side.


Table of contents
=================
* [API](#api)
    * [Setup](#setup)
    * [Sonar](#sonar)
* [USBIP](#usbip)
* [OV9750 3D Camera](#ov9750-3d-camera)


API
============
Raspberry Pi hosts small Express api which is used to query i2c parameters from Arduino.

Setup
-----
NodeJS >12.x must be installed and after files has been transferred to PI must run:

```shell script
sudo npm install
sudo npm install -g pm2
sudo pm2 start index.js
sudo pm2 save
```


Sonar
-----
`http://<pi_address>:3000/sonar`
returns sonar distance value object with key `cm` which describes measured centimeters.



USBIP
============
USB/IP setups for Raspberry Pi and GPU server side. This is used to share 
3D stereo camera attached to Robot gripper. Rasp and GPU server has some distance.

PI
-----
(Raspberry Pi OS)
```shell script
sudo apt install usbip
sudo modprobe usbip_host
```

Ensure modules has `usbip_host` added to it: 
```shell script
sudo nano /etc/modules
```

Attach USB device if not attached yet. Run `lsusb` to list attached devices.

Get busid of device to be shared.
```shell script
usbip list -p -l
```

Bind device (share) with command:
```shell script
sudo usbip bind --busid=<bus_id> 
```
<bus_id> example could be 1-1.1


Run usbip daemon
```shell script
usbipd 
```


GPU Server
-----
(Ubuntu)

Install usbip tool if not installed
```shell script
sudo apt install linux-tools-generic
```

Enable vhci-hcd
```shell script
sudo modprobe vhci-hcd
```

To boot up with machine start.
```shell script
sudo nano /etc/modules
```
has line `vhci-hcd`

Attach remote usb device
```shell script
sudo usbip attach -r <host_ip_address> -b <host_bus_id>
```


OV9750 3D Camera
============
Camera works out of the box with Windows and Mac but not in Linux (Ubuntu).

Getting camera to work with Linux is in progress. Using following command:
```shell script
hwinfo --usb
```

Got following output:
```shell script
03: USB 00.0: 0000 Unclassified device                          
  [Created at usb.122]
  Unique ID: cLrx.LvB8fpuxKC6
  Parent ID: k4bc.orx_URqq2_3
  SysFS ID: /devices/pci0000:00/0000:00:06.0/usb1/1-2/1-2:1.0
  SysFS BusID: 1-2:1.0
  Hardware Class: unknown
  Model: "ARC International 3D USB Camera"
  Hotplug: USB
  Vendor: usb 0x05a3 "ARC International"
  Device: usb 0x9750 "3D USB Camera"
  Revision: "21.03"
  Driver: "uvcvideo"
  Driver Modules: "uvcvideo"
  Device File: /dev/input/event7
  Device Files: /dev/input/event7, /dev/input/by-path/pci-0000:00:06.0-usb-0:2:1.0-event, /dev/input/by-id/usb-3D_USB_Camera_3D_USB_Camera-event-if00
  Device Number: char 13:71
  Speed: 12 Mbps
  Module Alias: "usb:v05A3p9750d2103dcEFdsc02dp01ic0Eisc01ip00in00"
  Driver Info #0:
    Driver Status: uvcvideo is active
    Driver Activation Cmd: "modprobe uvcvideo"
  Config Status: cfg=new, avail=yes, need=no, active=unknown
  Attached to: #5 (Hub)
```

in progress...
