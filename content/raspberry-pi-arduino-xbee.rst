Connecting a Raspberry Pi and Arduino Using XBee
================================================

:date: 2013-06-19
:tags: arduino, raspberry-pi, xbee,
:category: make
:summary: Tutorial on how I connected my Raspberry Pi and Arduino Uno via XBee radios
:status: draft

------------
Introduction
------------
I am planning to build a parking system like the `Parking Spotter`_ in my garage
using my Arduino Uno, some ultrasonic sensors, and some LEDs. I would also 
like to use my Raspberry Pi to provide an interface where I can see if a car 
is in the garage or not. I need some way to connect the Arduino in the garage
to the Raspberry Pi in my office. I received some XBee radios for Christmas and
thought they would be perfect.

-----
Setup
-----
========================
XBee Radio Configuration
========================

I am going to skim over the hard part of setting up the radios and link to the
sources that I used. My first source was the O'Reilly book 
`Building Wireless Sensor Networks`_ by Robert Faludi. I used this book to do
the initial configuration of the pair of radios. There are places online
to get the same information, but I recommend buying the book from 
O'Reilly so it is DRM free and supporting the author.

===============================
Raspberry Pi to XBee Connection
===============================

The connection from the Raspberry Pi to the first XBee is really easy. I used
the `USB XBee Adapter`_ from Adafruit to connect it to one of the USB ports
of the Raspberry Pi.

==========================
Arduino to XBee Connection
==========================

The connection to the Arduino is only slightly more difficult. I again used the
`USB XBee Adapter`_ from Adafruit. This time I connected Arduino Uno pin 10
to the adapter's pin DOUT. Arduino pin 11 is connected to the adapter's pin DIN.
You will see below that I am using the SoftwareSerial library in the Arduino 
to communicate with the XBee.

.. image:: http://farm3.staticflickr.com/2867/9098495520_ce7dfe0e92.jpg

--------
Software
--------
I installed minicom on both my desktop and my Raspberry Pi. I am running Debian
and I have installed sudo. After minicom is installed, it needs to be configured.
See below for the steps required to install and configure minicom on both
computers.

.. code-block:: bash
	:linenos:

	sudo apt-get install minicom
	sudo minicom -s


.. _Screen Shot: http://farm6.staticflickr.com/5324/9096232891_bcb3bd6ac5.jpg

.. _Parking Spotter: http://www.instructables.com/id/Arduino-Ultrasonic-Parking-Spotter/

.. _Building Wireless Sensor Networks: http://shop.oreilly.com/product/9780596807740.do

.. _USB XBee Adapter: http://www.adafruit.com/products/247


