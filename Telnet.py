import sys
import telnetlib

tn_ip = "192.168.2.28"
tn_port = "23"

CRLF = "\r\n"


def telnet():
    try:
        tn = telnetlib.Telnet(tn_ip, tn_port, 15)
    except:
        print('Unable to connect to Telnet server: ' + tn_ip)
        return
    tn.set_debuglevel(100)

    write_command(tn, "CONNECT" + CRLF)

    tn_read = tn.read_all()
    print(repr(tn_read))

def write_command(tn, command):
    tn.write(command.encode("ascii"))
    print('Send command: ' + command)


telnet()
