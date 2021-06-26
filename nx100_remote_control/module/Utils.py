import logging

CR = "\r"


# return byte length of command
def utf8len(s):
    return len(s.encode('utf-8'))


# get byte length for command data
def command_data_length(command):
    if len(command.data) == 0:
        return 0
    else:
        return utf8len(command.data + CR)


# just print some response details
def print_response_details(command_response):
    command_response_len = len(command_response)
    logging.info("Command response length: %d" % command_response_len)
    logging.info("Command response: " + command_response)


# decimal to binary
def decimal_to_binary(num):
    return bin(num)


# binary to decimal
def binary_to_decimal(binary):
    decimal, i, n = 0, 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


# clean response
def clean_response(response):
    return response \
        .replace('b\'', '') \
        .replace('\\r\'', '') \
        .replace('\\r\\n\'', '')


# noinspection DuplicatedCode
def is_in_position(move_l, cp):
    return cp.get_x() == move_l.get_x() and cp.get_y() == move_l.get_y() \
           and cp.get_z() == move_l.get_z() and cp.get_tx() == move_l.get_tx() \
           and cp.get_ty() == move_l.get_ty() and cp.get_tz() == move_l.get_tz()
