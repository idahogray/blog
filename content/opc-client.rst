Writing a OPC Client
====================

:date: 2014-03-07
:modified: 2014-03-09
:tags: python programming work
:category: work
:summary: Short introduction to writing an OPC client


Introduction
------------

OPC is something I see quite often in my job as a SCADA engineer.
Up until recently, all I knew about OPC was that it relied on
Microsoft Windows' Object Linking and Embedding (OLE).
In fact OPC is short for **O**\ LE for **P**\ rocess Control.
Even though OPC was always a problem on projects,
I thought of it as a black box because of its relationship to
Windows.

However, on a recent project, I had the need to automate some tests.
I had two choices:

#. Develop or purchase a DNP3 communication library to communicate with
   the device being tested.
#. Use an OPC Server to speak DNP3 and then get the data out of the OPC
   server.

I had previously looked into what it would take to develop a DNP3
driver and it wasn't going to be cheap or easy. I needed this
application and I needed it yesterday. Therefore, I decided to
investigate what it would take to communicate with the OPC server.

Background
~~~~~~~~~~

I have quite a bit of Python programming experience and I knew
that the pywin32 library supported Windows COM. COM is what
OPC uses for communication on a Windows system.

I spent one weekend poking around on Google, playing with pywin32,
and using the demo mode of the Kepware OPC platform. I was able to
connect to the kepware server and get data out of it.

OPC Client
----------

The OPC client I am going to show here is by no means a complete
implementation. However, this simple application met the needs
of my project and is relatively simple to get set up.

Prerequisites
~~~~~~~~~~~~~

This application was written on a Windows 7 machine. I have started
using the Anaconda python distribution on Windows because it is
so easy to get the packages I need installed without having a full
C/C++ development environment. The pywin32 library is required and
can be installed via anaconda.

.. code-block:: bash

   $ conda install pywin32

It is also required to have the OPC Server configured. In this case,
I simply created a channel and device in the Kepware server. The channel
used the Simulator driver and I named it 'Simulator'. I also named the 
device 'Simulator'.

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
