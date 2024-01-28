# my_mu3
A small project to grab and parse images from the MU3 Vision Sensor in a seperate process (to free up CPU).

## Installation
```
pip install my-mu3
```

## API Usage

Note the below relies on the camera being connected to the same WLAN (WIFI) network as the computer. Also note that
 it also relies on the ip address being known. See the section Connecting WLAN for help. It also relies on the camera
 being configured into image transmission mode, where both switches on the camera are in the up position. In this mode,
 the camera will show it is connected to a wifi network (and not broadcasting one) if both front lights are off. 
however, by default in this mode the camera will broadcast a network, this could be used though I haven't tested it. 

One point to note is that the below relies on `cv2.waitKey(1)` to exit, so if you are running headless it won't exit 
cleanly. Sorry.  

```python
import time

import cv2

from my_mu3.mu3_image_grabber import Mu3ImageGrabber

IP_ADDRESS = "192.168.1.183"

def main():

    my_mu3 = Mu3ImageGrabber(ip_address=IP_ADDRESS)

    exit_flag = False
    my_mu3.start()

    while not exit_flag:

        image = my_mu3.get_image()
        if image is not None:
            cv2.imshow('mu3 camera', image)

        if cv2.waitKey(1) == ord("q"):
            exit_flag = True
        time.sleep(0.01)

    my_mu3.stop()

if __name__ == "__main__":
    main()
```

## Connecting WLAN
The library relies on being connected to the same WLAN as the camera. To do so, AT commands can be sent to the camera
 via UDP or via Serial. A convenience script is included in this repository that sends AT commands to connect the
 camera to a WLAN network, that relies on having a serial port connected. One example of a repo that provides
 a "soft" serial port for the raspberry pi, ie you can use non-serial pins at a much lower speed,
 is [here](https://github.com/adrianomarto/soft_uart). I used this with 9600 baud rate, the default for the camera.  

```
setup-wlan MY_WIFI_NAME MY_PASSWORD /dev/ttyS0
```

## Using AT Commands/Chatting with the Camera

You can also use AT commands yourself. The camera will print AT commands if you send the below via serial. Note the 
space after the command, this is vital (or a combo of carriage return and new line).  
```
AT+HELP 
```

The output of this AT_HELP is included in this repo as the 'output_at_help.txt' file. Additionally, a program to
 chat via serial with the camera is included where it will let you type and send input in examples/serial_chat.py.