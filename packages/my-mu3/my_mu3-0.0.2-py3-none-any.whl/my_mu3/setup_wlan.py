import serial
import sys
import time

EXAMPLE_RUN = "setup-wlan MY_WIFI_NAME MY_PASSWORD /dev/ttyS0"

HELP_MSG = f"Invalid args, example: {EXAMPLE_RUN}"

BAUDRATE = 9600
TIMEOUT = 7

WIFISET_CMD_UNFORMATTED = "AT+WIFISET={},{},STA "
WIFICON_CMD = "AT+WIFICON=1 "
IP_CHECK_CMD = "AT+WIFISIP "

def main():
    if len(sys.argv) != 4:
        print(HELP_MSG)
        sys.exit(1)

    ssid_name = sys.argv[1]
    ssid_pass = sys.argv[2]
    serial_port = sys.argv[3]
    wifiset_cmd = WIFISET_CMD_UNFORMATTED.format(ssid_name, ssid_pass)
    with serial.Serial() as ser:
        ser.baudrate = BAUDRATE
        ser.port = serial_port
        ser.timeout = TIMEOUT
        ser.open()

        def wait_for_ok():
            line = ser.readline()
            while "OK" not in line.decode():
                print(f"waiting for ok, received {line.decode()}")
                time.sleep(0.01)
                line = ser.readline()

        print("setting wifi details")
        ser.write(wifiset_cmd.encode())
        wait_for_ok()
        print("connecting to wifi")
        ser.write(WIFICON_CMD.encode())
        wait_for_ok()
        print("checking ip")
        ser.write(IP_CHECK_CMD.encode())

        output_lines = []
        line = ser.readline()
        while line:
            output_lines.append(line)
            line = ser.readline()
        print(f"ip is {output_lines}")

if __name__ == "__main__":
    main()