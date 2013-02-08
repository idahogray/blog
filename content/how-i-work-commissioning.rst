How I Work - Commissioning
==========================

:date: 2013-02-06 8:22
:tags: how-i-work, commissioning, open-source
:category: how-i-work
:slug: how-i-work-commissioning
:summary: A description of How I Work when commissioning a SCADA project
:status: draft

I would like to describe how I work when commissioning a substation SCADA project. 
This post describes the software that I use during commissioning.

NovaTech OrionLX Communications Processor
-----------------------------------------

Most of my commissioning work over the last few years has involved the NovaTech Orion family of communications processors.
Therefore, this post will describe my work with that equipment.  Some of the 
content could be applied to other processors, but not all of it.

One of the Orion features that I really like is the ASCII text configuration file format.  This allows for doing things like

* Editing the configuration outside of the NovaTech Communications Director software in any text editor
* Comparing revisions using common diff tools
* Managing revisions of a configuration using commonly available revision control software
* Automating creation of the configuration file using common programming languages (Python being my favorite)
* Automating checking/verification of the configuration file

Software Applications
---------------------
During commissioning I use many software applications, most of which are 
freely available open source tools.  These tools
assist me in ensuring commissioning goes smoothly. I will describe each of
the tools listed here and how I employ them.

* Open Source

    * Mercurial
    * Subversion
    * Notepad++
    * Firefox

        * Firebug

    * putty
    * Inkscape
    * Teraterm
    * Wireshark
    * Winscp

* Closed Source
