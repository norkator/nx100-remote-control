# noinspection SpellCheckingInspection
RALARM = "b'0,0,0,0,0,0,0,0,0,0\\r'"

# noinspection SpellCheckingInspection
RPOSJ = "b'45411,-59646,-55567,667,-1077,-1260,0,0,0,0,0,0\\r'"

# noinspection SpellCheckingInspection
RPOSC = "b'353.769,202.779,120.658,-1.34,35.78,27.84,0,0\\r'"
'''
Base coordinate:    b'353.769,202.779,120.658,-1.34,35.78,27.84,0,0\\r'
Robot coordinate:   b'353.769,202.779,120.658,-1.34,35.78,27.84,0,0\\r'
User coordinate:    b'640.625,274.481,353.192,-1.36,35.77,-107.58,0,0\\r'
'''

# noinspection SpellCheckingInspection
RSTATS = "b'194,0\\r'"

# noinspection SpellCheckingInspection
RJSEQ = "b'POYTA,10,9\\r'"

# noinspection SpellCheckingInspection
HOLD = "b'0000\\r\\n'"

# noinspection SpellCheckingInspection
RESET = "b'0000\\r\\n'"

# noinspection SpellCheckingInspection
CANCEL = "b'0000\\r\\n'"

# noinspection SpellCheckingInspection
SVON = "b'0000\\r\\n'"

# noinspection SpellCheckingInspection
START = "b'0000\\r\\n'"

# noinspection SpellCheckingInspection
MOVL = "b'0000\\r\\n'"


def get_mock_response(command):
    if command.name is 'RALARM':
        return RALARM
    elif command.name is 'RPOSJ':
        return RPOSJ
    elif command.name is 'RPOSC':
        return RPOSC
    elif command.name is 'RSTATS':
        return RSTATS
    elif command.name is 'RJSEQ':
        return RJSEQ
    elif command.name is 'HOLD':
        return HOLD
    elif command.name is 'RESET':
        return RESET
    elif command.name is 'CANCEL':
        return CANCEL
    elif command.name is 'SVON':
        return SVON
    elif command.name is 'START':
        return START
    elif command.name is 'MOVL':
        return MOVL
    else:
        return '[E] no mock response for given command ' + command.name
