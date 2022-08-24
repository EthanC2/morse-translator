# 'MorseCode: a static class that translates ASCII strings to and from Morse code.
# Based on excerpts from the Radiocommunication Sector of ITU's International Morse Code Specifications:
# - https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf
# - https://morsecode.world/international/morse2.html

class MorseCode:
    __morse_code = {
        # Alphabet
        'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'	-..', 'e':'.', 'f':'..-.', 'g':'--.',
        'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.',
        'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-',
        'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..'
    
        # Numbers

        # Punctuation
    }
    
    def ToMorse(msg: str):
        pass

    def FromMorse(msg: str):
        pass