# Raspberry Pi Notes

Some notes for Raspberry PI side.


Table of contents
=================
* [USBIP](#usbip)


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