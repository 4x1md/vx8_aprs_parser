'''
Created on June 01, 2016

@author: 4x5dm
'''

import sys
from data_types.beacon_packet import BeaconPacket
from data_types.metadata import Metadata

FILE_NAME = "vx8.img"

class MEM_PARAMS:
    """Yaesu VX-8DR/DE memory parameters."""
    RADIO_ID = "AH29D" # Radio id at the beginning of memory dump. 
    METADATA_ADDR = 0xC24A  # APRS beacons metadata address.
    METADATA_SIZE = 24  # APRS beacons metadata address.
    BEACONS_CONTENT_ADDR = 0xC6FA  # APRS beacons content address.
    BEACON_DATA_SIZE = 146     # Length of beacon data stored.
    BEACONS = 50      # Number of beacons stored.
    
class Parser(object):
    
    def __init__(self):
        pass
    
    def parse(self, file_name):
        print "Parsing %s..." % file_name
        
        print 'Reading file...'
        
        f = open(file_name, 'rb')
        raw_data = f.read()
        f.close()
        
        # If the memory dump is not from VX-8DR/DE, display warning message.
        if not raw_data.startswith(MEM_PARAMS.RADIO_ID):
            print "The file doesn't seem to be a valid VX-8DR memory dump."
        
        print 'Extracting inbox messages...'
        
        metadata_start_addr = MEM_PARAMS.METADATA_ADDR
        beacons_start_addr = MEM_PARAMS.BEACONS_CONTENT_ADDR
        beacon_packets = []
        
        for i in range(0, MEM_PARAMS.BEACONS):
            # Metadata start and end addresses for beacon number i
            metadata_addr = metadata_start_addr + MEM_PARAMS.METADATA_SIZE * i
            metadata_addr_end = metadata_addr + MEM_PARAMS.METADATA_SIZE
            raw_metadata = raw_data[metadata_addr:metadata_addr_end]
            
            # Process metadata
            metadata = Metadata(raw_metadata)
            
            # If metadata does not point to a used memory slot, ignore it
            if not metadata.in_use:
                continue
                
            # Beacon address for beacon number i
            msg_addr = beacons_start_addr + (MEM_PARAMS.BEACON_DATA_SIZE + 14) * i
            raw_message = raw_data[msg_addr:msg_addr+metadata.pkt_len]
            beacon_packet = BeaconPacket(raw_message, metadata)
            beacon_packets.append(beacon_packet)
            
        print 'Found %s messages.' % (len(beacon_packets))
        
        return beacon_packets

if __name__ == '__main__':
    print 'Starting parser...'
    
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = FILE_NAME
    
    parser = Parser()
    beacons = parser.parse(file_name)
    
    for beacon in beacons:
        print beacon
    
    print 'Displayed %s messages.' % (len(beacons))

    print 'End.'
