# TinyML Wake-Word Detection on Raspberry Pi Pico

This application implements the wake word example from
[Tensorflow Lite for Microcontrollers](https://www.tensorflow.org/lite/microcontrollers)
on the Raspberry Pi Pico.

The wake word example shows how to run a 20 kB neural network that can detect 2
keywords, "yes" and "no". More information about this example is available on
the [Tensorflow Lite Micro examples folder](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro/examples/micro_speech).

We use as input an electret microphone to detect the words "yes" or "no" and
turn the on-device LED on and off in response.

### Pico Microphone

This project is dependant on the `pico-microphone` library by
[Sandeep Mistry](https://github.com/sandeepmistry).
Take a look [here](https://github.com/sandeepmistry/pico-microphone) for more
information about the library.

## Contents

- [Overview](#overview)
- [Before You Begin](#before-you-begin)
    - [Hardware Requirements](#hardware-requirements)
    - [Hardware Setup](#hardware-setup)
        - [Assembly](#assembly)
        - [Wiring](#wiring)
    - [Software Setup](#software-setup)
- [Wake-Word uf2 file](#wake-word-uf2-file)
- [Build Yourself](#build-yourself)
- [Making Your Own Changes](#making-your-own-changes)
- [Contributions](#contributions)
- [License](#license)

## Overview


### Hardware Requirements

- 1x [Raspberry Pi Pico](https://www.raspberrypi.org/products/raspberry-pi-pico/)
- 1x Micro USB cable
- 1x HC 05 Bluetooth module
- 2x LED
- 2x Fans
- 1x Ultrasonic Sensor
- Jumper wires
- 2x 1x20 male header pins (for the Pico)
- 1x 1x5 male header pins (for the microphone)

#### Assembly

1. Solder headers onto your Raspberry Pi Pico
2. Solder headers onto your Adafruit Electret Microphone

#### Wiring

The electret microphone breakout is an analog input, meaning we can connect it
to one of the ADC pins on the Raspberry Pi Pico. Make the following connections:

##### Analog Microphone

| __Adafruit Electret Microphone__ | __Raspberry Pi Pico__ |
|------------------------------|-------------------|
| OUT                          | ADC0 - Pin31      |
| GND                          | Any ground pin    |
| VDD                          | 3V3(OUT) - Pin36  |


### Software Setup

The final step before using this application is to set up the software stack
(CMake and compilers). The easiest way to do this is to follow the steps on the
Raspberry Pi Pico SDK [repository](https://github.com/raspberrypi/pico-sdk).
Once done you can test your tolchain setup by running some of the examples
found in the Pico examples
[repository](https://github.com/raspberrypi/pico-examples).


## Making Changes

If you would like to use a different microphone, different LED, use other pins
on Pico or change the audio quality, you will need to know how to make these
changes to the application.

### Changing the LED

The LED settings can be found in `micro_speech/rp2/command_responder.cc`. To
change the LED to a different pin (instead of the onboard LED), change the line:

```cpp
#define LED_PIN 25
```

To change the functionality of the LED, edit the `if-else` section:

```cpp
if (found_command == "yes"){
  //turn led on
  gpio_put(LED_PIN, 1);
}
else if (found_command == "no"){
  //turn led off
  gpio_put(LED_PIN, 0);
}
```

### Changing the ADC

The ADC pin is defined in the `src/audio_provider.cc` script. To
change the pin used in the application, change the lines:

```cpp
#define ADC_PIN 26
#define CAPTURE_CHANNEL 0
```

### Changing the Audio Quality

You can change the audio quality captured in the application. By default, the
Tensorflow model expects a `16kHz` quality. `16kHz` means `16000` samples every
second. Below you can see the analog config in the `src/audio_provider.cc`
file.

```cpp
const struct analog_microphone_config config = {
    // GPIO to use for input, must be ADC compatible (GPIO 26 - 28)
    .gpio = ADC_PIN + CAPTURE_CHANNEL,

    // bias voltage of microphone in volts
    .bias_voltage = 1.25,

    // sample rate in Hz
    .sample_rate = 16000,

    // number of samples to buffer
    .sample_buffer_size = ADC_BUFFER_SIZE,
};
```

You can change the different settings to best suit your need.



