def decode_morse(morse_code):
    final = ""
    morse = morse_code.strip().replace('   ', ' 0 ')
    print(morse)
    for i in morse.split():
        if i in MORSE_CODE:
            final += MORSE_CODE[i]
        elif i == '0':
            final += ' '
    return final
