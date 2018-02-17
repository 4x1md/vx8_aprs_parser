# Yaesu VX-8DR/DE incoming APRS beacons parser

Incoming APRS messages parser for Yaesu VX-8DR/DE.

## Overview

This project was used to explore memory contents of my Yaesu VX-8DE transceiver. I was looking for incoming APRS messages for [APRS beacons map](https://github.com/4x1md/yaesu_aprs_maps) project.

The project parses memory dumps saved by Chirp and displays incoming APRS messages. It consists of three main classes:

```Parser``` - the parser which reads data from memory dump file parses incoming messages and prints them.

```Metadata``` - class that maps metadata of each incoming APRS packet.

```BeaconPacket``` - class that maps incoming APRS packets. It stores source and destination call signs, path and message body.

## Running the parser

The ```parser.py``` script can be run from command line using the following command:

```python parser.py [file_name]```

where ```[file_name]``` is name and full path of the file containing VX-8DR/DE memory dump.

## Output examples

![APRS beacon messages](https://raw.githubusercontent.com/4x1md/vx8_aprs_parser/master/images/output_1.png)

![APRS beacon messages](https://raw.githubusercontent.com/4x1md/vx8_aprs_parser/master/images/output_1.png)

## Links
1. [Yaesu VX-8DR/DE APRS Beacons Map](https://4x1md.github.io/yaesu_aprs_maps/)
2. [Chirp repository](https://github.com/tylert/chirp.hg): [Yaesu VX-8 driver](https://github.com/tylert/chirp.hg/blob/master/chirp/drivers/vx8.py) - memory maps for bot VX-8R and VX-8DR.
3. [Chirp repository](https://github.com/tylert/chirp.hg): [Yaesu VX-8R Image](https://github.com/tylert/chirp.hg/blob/master/tests/images/Yaesu_VX-8_R.img) used for testing the VX-8R parser.

## Questions? Suggestions? Bug reports?

You are more than welcome to contact me with any questions, suggestions or propositions regarding this project. You can:

1. Visit [my QRZ.COM page](https://www.qrz.com/db/4X1MD)
2. Visit [my Facebook profile](https://www.facebook.com/Dima.Meln)
3. Write me an email to iosaaris =at= gmail dot com

73 de 4X1MD
