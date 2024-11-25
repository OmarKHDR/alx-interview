#!/usr/bin/python3
'''Module should be documented
'''


def validUTF8(data):
    '''Func is Documented
    '''
    if data == []:
        return True
    control_byte = data[0]
    check = 0b10000000
    bit_limit = control_byte & check
    byte_count = 1
    while (bit_limit != 0) and byte_count <= 6:
        check = check >> 1
        bit_limit = control_byte & check
        byte_count += 1
    if byte_count == 6 or byte_count == 2:
        return False
    if byte_count == 1:
        return validUTF8(data[1:])
    for i in range(1, byte_count-1):
        if data[i] & 0b11000000 != 0b10000000:
            return False
    return validUTF8(data[byte_count - 1:])
