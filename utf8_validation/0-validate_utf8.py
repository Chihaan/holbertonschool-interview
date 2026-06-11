#!/usr/bin/python3
"""UTF-8 Validator"""

def validUTF8(data):
    """Checks if data sent is UTF8 validated"""

    cpt = 0
    for nb in data:
        if cpt == 0 and nb >> 7 == 0b0:
            cpt = 0
        elif cpt == 0 and nb >> 5 == 0b110:
            cpt = 1
        elif cpt == 0 and nb >> 4 == 0b1110:
            cpt = 2
        elif cpt == 0 and nb >> 3 == 0b11110:
            cpt = 3
        elif cpt > 0 and nb >> 6 == 0b10:
            cpt -= 1
        else:
            return False
        
    return cpt == 0