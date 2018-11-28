import utime
from machine import Pin


def main():
    led = Pin(2, Pin.OUT)
    enabled = False
    while True:
        if enabled:
            led.off()
            print('LED Off')
        else:
            led.on()
            print('LED On')
        utime.sleep_ms(1000)
        enabled = not enabled


if __name__ == '__main__':
    main()
