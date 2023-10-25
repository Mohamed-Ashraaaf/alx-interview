#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    # Initialize the number of remaining bytes for the current char
    remaining_bytes = 0

    # Iterate through the data
    for byte in data:
        # Check if this is the start of a new character
        if remaining_bytes == 0:
            # Count the number of leading '1's in the binary rep
            mask = 1 << 7
            while mask & byte:
                remaining_bytes += 1
                mask >>= 1

            # Validate the number of bytes for the character
            if remaining_bytes == 0:
                continue
            if remaining_bytes == 1 or remaining_bytes > 4:
                return False
        else:
            # Check if the byte is a valid continuation byte
            if byte >> 6 != 0b10:
                return False

        # Reduce the count of remaining bytes
        remaining_bytes -= 1

    # If there are remaining bytes, return False
    return remaining_bytes == 0
