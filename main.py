# Author: Ethan Cox
# Group: HPU Code Club
# Date: 8/23/2022
# Program: Morse Code translator

from morse_code import MorseCode

def main():
    print(MorseCode.ToMorse('hello, world!'))
    print(MorseCode.ToMorse('a test of translation'))

    print(MorseCode.FromMorse('.- / .... .- .-. .--. ... .. -.-. --- .-. -.. --..-- / -- -.-- / -.. . .- .-. -.-.--'))
    print(MorseCode.FromMorse('...-- / -..- / .---- ..--- / -...- / ...-- -....'))

if __name__ == "__main__":
    main()