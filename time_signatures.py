import colors_rgb
from time import sleep


def twoFourSignature():
    y = 1
    while y == 1:
        interval = int(input('Enter the number of bars: '))
        for x in range(interval):
            colors_rgb.red()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            colors_rgb.green()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            x += 1
        colors_rgb.turnOff
        stay = str(input('Continue? (y/n): '))
        if stay == 'y':
            y = 1
        elif stay == 'n':
            y = 0
    return


def threeFourSignature():
    y = 1
    while y == 1:
        interval = int(input('Enter the number of bars: '))
        for x in range(interval):
            colors_rgb.red()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            colors_rgb.blue()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            colors_rgb.blue()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            x += 1
        colors_rgb.turnOff
        stay = str(input('Continue? (y/n): '))
        if stay == 'y':
            y = 1
        elif stay == 'n':
            y = 0
    return


def fourFourSignature():
    y = 1
    while y == 1:
        interval = int(input('Enter the number of bars: '))
        for x in range(interval):
            colors_rgb.red()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            colors_rgb.yellow()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            colors_rgb.yellow()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            colors_rgb.yellow()
            sleep(0.5)
            colors_rgb.turnOff()
            sleep(0.5)
            x += 1
        colors_rgb.turnOff
        stay = str(input('Continue? (y/n): '))
        if stay == 'y':
            y = 1
        elif stay == 'n':
            y = 0
    return


def fourEightSignature():
    y = 1
    while y == 1:
        interval = int(input('Enter the number of bars: '))
        for x in range(interval):
            colors_rgb.red()
            sleep(0.255)
            colors_rgb.turnOff()
            sleep(0.255)
            colors_rgb.purple()
            sleep(0.255)
            colors_rgb.turnOff()
            sleep(0.255)
            colors_rgb.purple()
            sleep(0.255)
            colors_rgb.turnOff()
            sleep(0.25)
            colors_rgb.purple()
            sleep(0.25)
            colors_rgb.turnOff()
            sleep(0.25)
            colors_rgb.purple()
            sleep(0.25)
            colors_rgb.turnOff()
            sleep(0.25)
            colors_rgb.purple()
            sleep(0.25)
            colors_rgb.turnOff()
            sleep(0.25)
            colors_rgb.purple()
            sleep(0.25)
            colors_rgb.turnOff()
            sleep(0.25)
            colors_rgb.purple()
            sleep(0.25)
            colors_rgb.turnOff()
            sleep(0.25)
            x += 1
        colors_rgb.turnOff
        stay = str(input('Continue? (y/n): '))
        if stay == 'y':
            y = 1
        elif stay == 'n':
            y = 0
    return
