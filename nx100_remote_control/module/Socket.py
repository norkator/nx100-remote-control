import nx100_remote_control
from nx100_remote_control.module import Utils, MockResponse
import logging
import socket

CR = "\r"
CRLF = "\r\n"


# exec single command object
def exec_single_command(command):
    if nx100_remote_control.MOCK_RESPONSE:
        return Utils.clean_response(MockResponse.get_mock_response(command))

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.settimeout(5)

    # connect the client
    client.connect((nx100_remote_control.NX100_IP_ADDRESS, nx100_remote_control.NX100_TCP_PORT))

    # start request
    start_request = "CONNECT Robot_access" + CRLF
    client.send(start_request.encode())
    response = client.recv(4096)
    start_response = repr(response)
    if 'OK: NX Information Server' not in start_response:
        client.close()
        logging.error('[E] Command start request response not ok!')
        return

    # command request
    cmd_data_length = Utils.command_data_length(command)
    command_request = "HOSTCTRL_REQUEST " + command.name + " " + str(cmd_data_length) + CRLF
    logging.info('Sending command: ' + command_request)
    client.send(command_request.encode())
    response = client.recv(4096)
    command_response = repr(response)
    if ('OK: ' + command.name) not in command_response:
        client.close()
        logging.error('[E] Command request response not ok!')
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
    logging.info('No implementation')
