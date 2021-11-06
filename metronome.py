# libraries
import os
import colors_rgb
import time_signatures


# INITIAL MESSAGE
os.system('clear')
print('\n Welcome to the blinking metronome project!')
print('''\
                                _                          
                  __      _____| | ___ ___  _ __ ___   ___ 
                  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ |
                   \ V  V /  __/ | (_| (_) | | | | | |  __/
                    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                                            

                ''')
print('\n Press ctrl+C to exit...\n')


def main():
    while True:
        choose = int(input('''
                                Choose the time signature:
                                1 - [2 / 4]    2- [3 / 4]
                                3 - [4 / 4]    4 - [4 / 8]
                                ctrl+C to exit
                                \n'''))
        if choose == 1:
            time_signatures.twoFourSignature()
        elif choose == 2:
            time_signatures.threeFourSignature()
        elif choose == 3:
            time_signatures.fourFourSignature()
        elif choose == 4:
            time_signatures.fourEightSignature()
        else:
            print('Choose a valid option\n')


try:
    main()
except KeyboardInterrupt:
    colors_rgb.turnOff()
    print('Thanks!\n')
