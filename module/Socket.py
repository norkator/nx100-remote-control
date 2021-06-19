from module import Utils, MockResponse
import socket

# NX100 robot parameters
nx100_address = "192.168.2.28"
nx100_port = 80

MOCK_RESPONSE = False

CR = "\r"
CRLF = "\r\n"


# exec single command object
def exec_single_command(command):
    if MOCK_RESPONSE:
        return Utils.clean_response(MockResponse.get_mock_response(command))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)

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

    # command request
    cmd_data_length = Utils.command_data_length(command)
    command_request = "HOSTCTRL_REQUEST " + command.name + " " + str(cmd_data_length) + CRLF
    # print('Sending command: ' + command_request)
    client.send(command_request.encode())
    response = client.recv(4096)
    command_response = repr(response)
    if ('OK: ' + command.name) not in command_response:
        client.close()
        print('[E] Command request response not ok!')
        return

    # command data request
    command_data_request = command.data + (CR if len(command.data) > 0 else '')
    client.send(command_data_request.encode())
    response = client.recv(4096)
    command_data_response = repr(response)

    # close socket
    client.close()

    return Utils.clean_response(command_data_response)


# exec array of command objects
def exec_multiple_commands(commands):
    print('No implementation')
