# Pico-Wake-Word
TinyML Wake Word project on the Raspberry Pi Pico
The application works by listening to the microphone and processing the data before sending it the model to be analyzed. The application takes advantage of Pico's ADC and DMA to listen for samples, saving the CPU to perform the complex analysis.
The Pico does not come with an onboard microphone. For this application, we use the Adafruit Electret Microphone Amplifier breakout.
A demo is available at https://youtu.be/V0KXZGhHUQY?si=RL6ra9ZWRKMzhr-C
