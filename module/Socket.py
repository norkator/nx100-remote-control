import socket

# https://drive.google.com/drive/folders/178NiGW2us9qwGYyyPQLYwU0fMyYPVp0x
# NX100 robot parameters
nx100_address = "192.168.2.28"
nx100_port = 80

CRLF = "\r\n"


def exec_commands(commands):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # connect the client
    client.connect((nx100_address, nx100_port))

    # send some data
    start_request = "CONNECT Robot_access" + CRLF
    client.send(start_request.encode())
    response = client.recv(4096)
    http_response = repr(response)
    http_response_len = len(http_response)
    print("Response length: %d" % http_response_len)
    print(http_response)

    # Close socket
    client.close()