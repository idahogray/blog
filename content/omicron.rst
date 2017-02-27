Automating the Omicron CMC using Python
======================================= 

:date: 2015-03-20
:tags: python programming work
:category: work
:summary: Short introduction to automating the CMC using Python.
:status: draft


Introduction
------------

A recent project of mine included a controller that performed
logic and made decisions on what breakers should be tripped for
a given event. This controller had approximately 300 inputs.

We typically try to test as many states of the system as possible.
The only way to test an acceptable amount of system states was to
automate the process. Even with automation, it would be impossible
to test 2^300 states. Automation was needed to bring the number
of tested states to an acceptable number.

My company owns a Omicron CMC256Plus three-phase test set. Our
version supports publishing and subscribing to GOOSE messages.
The plan was to use this feature to help automate some of our tests.

The CMC software, called Test Universe, supports a Windows COM
interface. We could automate the software, and therefore, the CMC 
itself, using COM. This is one of the features of the Python Pywin32
library.

This blog post describes the COM interface of the Test Universe
and provides examples of how to use it to accomplish automated testing.


Background
~~~~~~~~~~

I have quite a bit of Python programming experience and I knew
that the pywin32 library supported Windows COM. COM is what
OPC uses for communication on a Windows system.

I spent one weekend poking around on Google, playing with pywin32,
and using the Omicron Testu Universe CMEngine user's manual. I also
received some help from Omicron Technical Support. I was able to
connect to the CMC, load GOOSE settings, and automate the value of
binary points inside of the simulated datasets.

Prerequisites
~~~~~~~~~~~~~

This application was written on a Windows 7 machine. I have started
using the Anaconda python distribution on Windows because it is
so easy to get the packages I need installed without having a full
C/C++ development environment. The pywin32 library is required and
can be installed via anaconda.

.. code-block:: bash

   $ conda install pywin32

It is also required to have Omicron Test Universe installed. I am using
Test Universe 3.00 SR2 with the 2014-10 service pack.

The Code
~~~~~~~~

The code below is really simple. It connects to the Kepware OPC client,
creates a group, adds one binary tag to the group, retrieves the value,
quality, and timestamp of the tag (which should be False), writes a value
of True to the tag, then rereads the value, quality, and timestamp. Finally
it disconnects from the OPC Server.

.. code-block:: python
   :linenos:

   from win32com import client
   opc = client.Dispatch('OPC.Automation.1')
   opc.Connect('KEPware.KEPServerEX.V5')
   group = opc.OPCGroups.Add('Test Group')
   group.IsActive = True
   item = group.OPCItems.AddItem('Simulator.Simulator.K0000.00', 1)
   value, quality, time = item.Read(client.constants.OPCDevice)
   print("Value: {}; Quality: {}; Time: {}".format(value, quality, time))
   item.Write(True)
   value, quality, time = item.Read(client.constants.OPCDevice)
   print("Value: {}; Quality: {}; Time: {}".format(value, quality, time))
   opc.Disconnect()

What's Next
-----------

OPC has a lot more options than just reading or writing to a single point
at a time. Your client can subscribe to events and get notified when a
point value changes. I didn't make use of that functionality in my
project but I probably will in the future.
