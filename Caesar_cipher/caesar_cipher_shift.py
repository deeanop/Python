def codify(message, key, operation):
    result = []
    base_lower = ord('a')
    base_upper = ord('A')
    for element in message:
        if 'a' <= element <= 'z' or 'A' <= element <= 'Z':
            if operation == "encode":
                shift = key
            elif operation == "decode":
                shift = -key
            if element.islower():
                codified_char = chr((ord(element)-base_lower + shift) % 26 + base_lower)
            elif element.isupper():
                codified_char = chr((ord(element) - base_upper + shift) % 26 + base_upper)
            result.append(codified_char)
        else:
            result.append(element)

    result = "".join(result)
    return result