from machine import Pin, UART
from time import sleep
import utime

# Initializing pins for devices and UART communication
fan = Pin(15, Pin.OUT)
fan1 = Pin(14, Pin.OUT)
led = Pin(16, Pin.OUT)
led1 = Pin(18, Pin.OUT)
uart = UART(0, 9600)

# USS configuration
signal_pin = Pin(0, Pin.IN)

# Initial states of devices
fan_state = 0
fan1_state = 0
bedroom_led_state = 0
hall_led_state = 0

# Flag to enable/disable distance measurement
distance_enabled = False  

# Function to control the state of a device
def control_device(pin, state):
    pin.value(state)

# Function to measure distance using ultrasonic sensor
def get_distance():
    # Trigger measurement by briefly pulling the signal pin low
    signal_pin.init(Pin.OUT)
    signal_pin.value(0)
    utime.sleep_us(2)
    signal_pin.value(1)
    utime.sleep_us(5)
    signal_pin.value(0)
    
    # Wait for the echo response
    signal_pin.init(Pin.IN)
    while signal_pin.value() == 0:
        pulse_start = utime.ticks_us()

    while signal_pin.value() == 1:
        pulse_end = utime.ticks_us()

    pulse_duration = utime.ticks_diff(pulse_end, pulse_start)
    
    # Speed of sound is approximately 343 meters per second at sea level
    # Convert the time to distance (cm)
    distance = (pulse_duration * 34300) / (2 * 10**6)
    
    return distance

# Main loop
while True:
    if uart.any():
        data = str(uart.read())
        print(data)

        # Command to activate distance measurement
        if 'activate' in data:
            distance_enabled = True
        # Command to deactivate distance measurement
        elif 'deactivate' in data:
            distance_enabled = False

        # Control commands for bedroom fan
        if 'bedroom fan on' in data:
            fan_state = 1
        elif 'bedroom fan off' in data:
            fan_state = 0

        # Control commands for hall fan
        if 'hall fan on' in data:
            fan1_state = 1
        elif 'hall fan off' in data:
            fan1_state = 0

        # Control commands for bedroom light
        if 'bedroom light on' in data:
            bedroom_led_state = 1
            hall_led_state = 0  # Turn off hall light when bedroom light is on
        elif 'bedroom light off' in data:
            bedroom_led_state = 0

        # Control commands for hall light
        if 'hall light on' in data:
            hall_led_state = 1
            bedroom_led_state = 0  # Turn off bedroom light when hall light is on
        elif 'hall light off' in data:
            hall_led_state = 0

        # Control commands for all lights
        if 'lights on' in data:
            bedroom_led_state = 1
            hall_led_state = 1
        elif 'lights off' in data:
            bedroom_led_state = 0
            hall_led_state = 0

        # Control commands for all fans
        if 'fans on' in data:
            fan_state = 1
            fan1_state = 1
        elif 'fans off' in data:
            fan_state = 0
            fan1_state = 0

        # Control commands for all devices
        if 'all devices' in data:
            bedroom_led_state = 1
            hall_led_state = 1
            fan_state = 1
            fan1_state = 1
        # Command to turn off all devices
        elif 'turn off' in data:
            bedroom_led_state = 0
            hall_led_state = 0
            fan_state = 0
            fan1_state = 0

    if distance_enabled:
        # USS functionality
        distance = get_distance()
        print("Distance: {:.2f} cm".format(distance))

        if distance < 10:
            # If distance is less than 10cm, turn on bedroom fan and light
            fan_state = 1
            bedroom_led_state = 1
        else:
            # If distance is greater than or equal to 10cm, turn off bedroom fan and light
            fan_state = 0
            bedroom_led_state = 0

    # Control devices based on states
    control_device(fan, fan_state)
    control_device(fan1, fan1_state)
    control_device(led, bedroom_led_state)
    control_device(led1, hall_led_state)

    sleep(3)  # Sleep for 3 seconds before the next iteration
