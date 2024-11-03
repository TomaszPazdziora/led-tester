import serial

ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    timeout=1
)

if ser.is_open:
    print(f"Connected with: {ser.name}")

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline(ser.in_waiting or 1)
            if data:
                print(data.decode('utf-8'))


except KeyboardInterrupt:
    print("Closing connection.")

finally:
    ser.close()
