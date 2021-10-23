# blink-metronome

This metronome helps you when the sound distracts you training music.
Soon: You can turn on and off both LED and buzzer, you choose what to use.

It's set to 4/4 60bpm. Working on new features.

## Usage

The `GPIO.setmode(GPIO.BCM)` declared means that you need to use the port name, not its physical number.
To know both just execute `pinout` on your pi's terminal and use the `GPIO(x)` number.
If you want to use the physical, change this line to `GPIO.setmode(GPIO.BOARD)`.

I'm using RGB LED but you can use 1 simple LED or two to simulate the higher tempo.

## References

- [How to use RGB LED][rp]
- [Examples on pinout usage][pu]
- [Buzzer usage][bu]
- [Interrupts on raspi][ir]
- [Beats calculator][bc]
- [Python time's sleep][pt]
- [Using timer][ut]

* * *

> "Thanks for passing by."

  [rp]: https://www.instructables.com/Raspberry-Pi-Tutorial-How-to-Use-a-RGB-LED/
  [pu]: https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs
  [bu]: https://projects.raspberrypi.org/en/projects/rpi-connect-buzzer
  [ir]: https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
  [bc]: https://toolstud.io/music/bpm.php?bpm=100&bpm_unit=4%2F4
  [pt]: https://docs.python.org/3/library/time.html#time.sleep
  [ut]: https://stackoverflow.com/questions/377454/how-do-i-get-my-python-program-to-sleep-for-50-milliseconds