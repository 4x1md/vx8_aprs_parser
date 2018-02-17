'''
Created on Feb 10, 2018

@author: 4X1MD
'''

class Metadata:
    
    def __init__(self, raw_data):
        # Date and time
        self.date = raw_data[0:2]
        self.time = raw_data[4:5]
        
        # Packet sender
        self.sender_callsign = raw_data[8:15]
        self.sender_ssid = raw_data[17] + raw_data[19]
        self.ascii_callsign = True if (ord(raw_data[18]) & 0b00010000) else False
        
        # Data length
        # If packet length is 0xFFFF, it is actually 0
        self.pkt_len = ord(raw_data[20]) * 0x100 + ord(raw_data[21])
        self.pkt_len = 0 if self.pkt_len == 0xFFFF else self.pkt_len
        
        # Memory cell stores packet (1 if true, 0 if false)
        # If in use value is 0xFFFF, it is actually 0
        self.in_use = ord(raw_data[22]) * 0x100 + ord(raw_data[23])
        self.in_use = True if self.in_use == 1 else False
        
    def __repr__(self):
        return '<Metadata callsign=%s-%s, ascii=%s, pkt_len=%s, in_use=%s>' % \
            (self.sender_callsign, self.sender_ssid, self.ascii_callsign, self.pkt_len, self.in_use)
