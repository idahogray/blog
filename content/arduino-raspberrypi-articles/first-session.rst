Arduino and Raspberry Pi
========================

:date: 2014-01-04
:tags: arduino
:category: personal
:summary: The first post in a series of introducing the Arduino and Raspberry Pi to my father and brother

My father, brother, and I are starting to have weekly or bi-weekly sessions so I can teach them
about the arduino and raspberry pi. It will also give us a scheduled time to work on a project.
Finally, it will be good time spent together for the three of us.

Session 1 Agenda and Links
---------------------------

#. Introduction to the Arduino_ boards and software

    * Uno
    * Leonardo
    * Others

#. Install the `Arduino Software`_ in Windows or Linux
#. Connect the Arduino to the PC and make sure the software can communicate with it

    #. Choose the Leonardo from the list of boards
    #. Choose the correct serial port
    #. Choose the blink example from the menus, compile it, and send it to the Arduino
    #. Make sure there are no errors
    #. Make sure the onboard LED connected to pin 13 is blinking

#. Visually insped the code and describe how it works

    * Declaring constants (different than what is in the examples)
    * setup function
    * loop function
    * Built in function: `pinMode`_
    * Built in function: `digitalWrite`_
    * Built in function: `delay`_

#. Use an external LED

    #. Wire up and external LED with the correct resistor value
    #. Alter the Arduino code to choose the correct pin
    #. Compile and send to the Arduino
    #. Verify the LED blinks

#. Play with the code a little bit
    
    #. Make the LED stay on longer
    #. Make the LED stay off longer
    #. Make the LED blink faster with equal on/off times (duty cycle)

#. Talk about Pulse Width Modulation (PWM) (A form of analog output)

    * Built in function: `analogWrite`_

#. Use PWM to fade an LED

    #. Open the Fade example from the Arduino IDE menu
    #. Inspect the code to see what it does
    #. Set the led pin correctly in the code for how the LED is connected
    #. Compile and send the code to the Arduino
    #. Verify the LED fades in and out

#. Play with the code a little bit

    #. Make it take longer to fade in and out
    #. Make it fade faster
    #. Make it so it only fades out and then goes immediately to full brightness again

References
----------

.. _Arduino: http://arduino.cc
.. _Arduino Software: http://arduino.cc/en/Main/Software
.. _pinMode: http://arduino.cc/en/Reference/PinMode
.. _digitalWrite: http://arduino.cc/en/Reference/DigitalWrite
.. _delay: http://arduino.cc/en/Reference/Delay
.. _analogWrite: http://arduino.cc/en/Reference/AnalogWrite
