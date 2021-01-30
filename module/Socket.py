import socket

# https://drive.google.com/drive/folders/178NiGW2us9qwGYyyPQLYwU0fMyYPVp0x
# NX100 robot parameters
nx100_address = "192.168.2.28"
nx100_port = 80

CR = "\r"
CRLF = "\r\n"


# exec single command object
def exec_single_command(command):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((nx100_address, nx100_port))

    # start request
    start_request = "CONNECT Robot_access" + CRLF
    client.send(start_request.encode())
    response = client.recv(4096)
    start_response = repr(response)
    if 'OK: NX Information Server' not in start_response:
        client.close()
        print('[E] Command start request response not ok!')
        return

    # command
    command_request = "HOSTCTRL_REQUEST " + command.name + " " + str(utf8len(command.name + CR)) + CRLF
    client.send(command_request.encode())
    response = client.recv(4096)
    command_response = repr(response)

    # close socket
    client.close()

    return command_response


# exec array of command objects
def exec_multiple_commands(commands):
    print('No implementation')


# --------------------------------------------------------------------------------
# Helpers

# return byte length of command
def utf8len(s):
    return len(s.encode('utf-8'))


# just print some response details
def print_response_details(command_response):
    command_response_len = len(command_response)
    print("Command response length: %d" % command_response_len)
    print("Command response: " + command_response)
