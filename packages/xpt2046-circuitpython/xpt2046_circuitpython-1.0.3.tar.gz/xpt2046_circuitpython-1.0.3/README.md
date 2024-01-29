## [skip to docs](https://github.com/humeman/xpt2046-circuitpython/blob/main/docs/README.md)

# xpt2046-circuitpython
A CircuitPython (or Adafruit-Blinka) library which reads values from an XPT2046 chip, commonly found on cheap microcontroller TFT displays.

## installation
This project is available on PyPi:
```sh
pip3 install xpt2046-circuitpython
```

Or, to install it manually:
```sh
git clone https://github.com/humeman/xpt2046-circuitpython
cd xpt2046-circuitpython
pip3 install .
```

If you're using this on regular Linux rather than CircuitPython, make sure you also [install Adafruit Blinka](https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi).

## usage
Be sure to enable SPI in `sudo raspi-config` before proceeding.

### sample wiring

| TFT   | Board     | GPIO   | Pin # |
| ----- | --------- | ------ | ----- |
| T_CLK | SPI0 SCLK | GPIO11 | 23    |
| T_CS  |           | GPIO6  | 31    |
| T_DIN | SPI0 MOSI | GPIO10 | 19    |
| T_DO  | SPI0 MISO | GPIO9  | 21    |
| T_IRQ |           | GPIO22 | 15    |

### examples
The most basic read example is:
```py
import xpt2046_circuitpython
import time
import busio
import digitalio
from board import SCK, MOSI, MISO, D6, D22

# Pin config
T_CS_PIN = D6
T_IRQ_PIN = D22

# Set up SPI bus using hardware SPI
spi = busio.SPI(clock=SCK, MOSI=MOSI, MISO=MISO)
# Create touch controller
touch = xpt2046.Touch(
    spi, 
    cs = digitalio.DigitalInOut(T_CS_PIN),
    interrupt = digitalio.DigitalInOut(T_IRQ_PIN)
)

# Check if we have an interrupt signal
if touch.is_pressed():
    # Get the coordinates for this touch
    print(touch.get_coordinates())
```

Some more examples:
* [read.py](https://github.com/humeman/xpt2046-circuitpython/blob/main/samples/read.py): A simple program which continuously prints coordinates when the screen is pressed
* [adafruit-ili.py](https://github.com/humeman/xpt2046-circuitpython/blob/main/samples/adafruit-ili.py): A simple drawing program for an ILI9341 display controlled by the Adafruit display library