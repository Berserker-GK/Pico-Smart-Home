# Raspberry Pi Pico Smart Home Automation System

## Overview
This repository contains the Python script for a smart home automation system implemented on a Raspberry Pi Pico board. The system utilizes GPIO pins for controlling devices such as fans and LEDs, and it communicates with other devices via UART.

### Hardware Requirements

- 1x [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/)
- 1x Micro USB cable
- 1x HC 05 Bluetooth module
- 2x LED
- 2x Fans
- 1x Ultrasonic Sensor
- Jumper wires
- 2x 1x20 male header pins (for the Pico)

### Features

- Ultrasonic Sensor (USS): Measures distance and controls bedroom fan and light based on proximity.
- UART Communication: Listens for commands through UART to control various devices.
- Device Control: Controls bedroom fan, hall fan, bedroom LED, and hall LED based on received commands.
- Automation Logic: Implements basic automation logic for turning on/off devices based on conditions.

## Getting Started

### Prerequisites

- Raspberry Pi Pico board
- Micro USB cable
- MicroPython firmware installed on the Raspberry Pi Pico

### How to run

- Upload the Python script to your Raspberry Pi Pico board.
- Connect the required devices (fans, LEDs, ultrasonic sensor) to the corresponding GPIO pins based on the script.
- Power up the Raspberry Pi Pico.
- Customize the script or UART commands based on your specific setup and requirements.

### Usage

- Ensure that the Raspberry Pi Pico is powered and the script is running.
- Send commands through UART to control devices. Example commands:
      - To turn on the bedroom fan: bedroom fan on
      - To turn off all devices: turn off
- Monitor the console output for distance measurements from the ultrasonic sensor.

### Acknowledgments
- The script is based on the Raspberry Pi Pico MicroPython documentation.
- Thanks to the open-source community for providing resources and inspiration.
