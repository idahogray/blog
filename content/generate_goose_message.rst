Generating GOOSE Messages
=========================

:date: 2018-12-19 08:00
:tags: GOOSE, python, IEC 61850
:category: work
:summary: Generating GOOSE messages using Python


This is a continuation of a previous `post <{filename}2016-09-24-notes.rst>`_.
It that previous post, an implementation of the GOOSE |asn.1| encoder.
I have since update that repository to include an example showing how to created
a GOOSE message using that |asn.1| definition and the `scapy`_ library. The example
is explained below.

First, the IECGoosePDU ASN.1 type is created.

.. code-block:: python

   from pyasn1.type import tag

   from goose_pdu import IECGoosePDU

   g = IECGoosePDU().subtype(
       implicitTag=tag.Tag(
           tag.tagClassApplication,
           tag.tagFormatConstructed,
           1
        )
   )
   
Next, the static portion of the GOOSE message is created by setting each of the 
fields to an appropriate value. gocbRef, datSet, and goID are set to strings.
timeAllowedtoLive, stNum, sqNum, confRev, and numDatSetEntries are set to integers.
t is set to a valid timestamp. test and ndsCom are boolean values.

.. code-block:: python

   g.setComponentByName('gocbRef', 'PDC-2+11+700G_G1CFG/LLNO$GO$GooseDset_BF')
   g.setComponentByName('timeAllowedtoLive', 2000)
   g.setComponentByName('datSet', 'PDC02_11_700G_G1CFG/LLN0$Dset_BF')
   g.setComponentByName('goID, '11_700G_G1_Dset_BF')
   g.setComponentByName('t', b'\x55\x15\x1b\x9b\x69\x37\x40\x92')
   g.setComponentByName('stNum', 5)
   g.setComponentByName('sqNum', 1757)
   g.setComponentByName('test', False)
   g.setComponentByName('confRev', 3)
   g.setComponentByName('ndsCom', False)
   g.setComponentByName('numDatSetEntries', 6)

The dynamic data is then added. In this example, 2 boolean values are added to the message,
including their associated quality and timestamp. Each of the 6 data items are created and
added to the 'allData' field. The 'allData' field is then added to the GOOSE message.

.. code-block:: python

   from goose_pdu import AllData
   from goose_pdu import Data()

   d = AllData().subtype(
       implicitTag=tag.Tag(
           tag.tagClassContext,
           tag.tagFormatConstructed,
           11
        )
   )
   d1 = Data()
   d1.setComponentByName('boolean', False)
   d2 = Data()
   d2.setComponentByName('bit-string', "'0000000000000'B")
   d3 = Data()
   d3.setComponentByName'utc-time', b'\x55\x15\x14\xc0\xc8\xf5\xc0\x92')
   d4 = Data()
   d4.setComponentByName('boolean', False)
   d5 = Data()
   d5.setComponentByName('bit-string', "'0000000000000'B")
   d6 = Data()
   d6.setComponentByName'utc-time', b'\x55\x15\x14\xaa\x3a\x9f\x80\x92')
   d.setComponentByPosition(0, d1)
   d.setComponentByPosition(1, d2)
   d.setComponentByPosition(2, d3)
   d.setComponentByPosition(3, d4)
   d.setComponentByPosition(4, d5)
   d.setComponentByPosition(5, d6)
   g.setComponentByName('addData', d)

The last step is to create the `scapy`_ packet. The Ethernet frame is created with
the GOOSE multicast destination address. VLAN information is added to the packet placing
the message in VLAN 10 with priority 6, and GOOSE as the type. The GOOSE static data fields
are then added followed by the dynamic ASN.1 encoded fields.

.. code-block:: python

   from pyasn1.codec.ber import encoder
   from scapy.layers.l2 import Ether
   from scapy.layers.l2 import Dot1Q
   from scapy.utils import hexdump

   from goose import GOOSE

   hexdump(
       Ether(dst='01:0c:cd:01:00:14') /
       Dot1Q(vlan=10, type=0x88b8, prio=6) /
       GOOSE(appid=int(0x00b1)) /
       encoder.encode(g)
   )


Next Steps
----------

The next step in this experiment will be to use this GOOSE message in a network
packet created with scapy_ and transmit it on a network simulated using Linux
Network Namespaces, as described in earlier posts.

.. _scapy: http://www.secdev.org/projects/scapy/
.. _Wikipedia: https://en.wikipedia.org/wiki/Abstract_Syntax_Notation_One
.. _pyasn1: http://pyasn1.sourceforge.net/
.. |asn.1| replace:: :abbr:`ASN.1 (Abstract Syntax Notation One)`
.. |ber| replace:: :abbr:`BER (Basic Encoding Rules)`
.. _ber: https://en.wikipedia.org/wiki/X.690#BER_encoding
.. _goose_txt: https://github.com/keith-gray-powereng/goose-asn1/blob/master/goose.txt
.. _goose_asn: https://github.com/keith-gray-powereng/goose-asn1/blob/master/goose_asn.py
