from bidict import bidict

# 'MorseCode: a static class that translates ASCII strings to and from Morse code.
# Based on excerpts from the Radiocommunication Sector of ITU's International Morse Code Specifications:
# - https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf
# - https://morsecode.world/international/morse2.html

class MorseCode:
    __morse_code = bidict({
        # Alphabet
        'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'	-..', 'e':'.', 'f':'..-.', 'g':'--.',
        'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.',
        'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-',
        'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
    
        # Numbers
        '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-', 
        '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',

        # Punctuation & Symbols
        '&':'.-...', '\'':'.----.', '@':'.--.-.', ')':'-.--.-', '(':'-.--.',
        ':':'---...', ',':'--..--', '=':'-...-', '!':'-.-.--', '.':'.-.-.-',
        '-':'-....-', '%':'------..-.-----', '+':'.-.-.', '\"':'.-..-.',
        '?':'..--..', '/':'-..-.'
    })
    
    def ToMorse(text: str) -> str:
        translation = ""

        for i, char in enumerate(text):
            char = char.lower()

            if char in MorseCode.__morse_code:
                translation += MorseCode.__morse_code[char]
            else:
                translation += char

            if i < len(text)-1:
                translation += ' '

        return translation

    def FromMorse(msg: str) -> str:
        translation = ""
        chars = msg.split()

        for i, char in enumerate(chars):
            if char in MorseCode.__morse_code:
                translation += MorseCode.__morse_code[char]
            else:
                translation += char

            if i < len(chars)-1:
                translation += ' '

        return translation