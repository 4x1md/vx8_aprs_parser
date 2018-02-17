'''
Created on Feb 10, 2018

@author: 4X1MD
'''

class BeaconPacket:
    
    def __init__(self, raw_data, metadata):
        self._metadata = metadata # Metadata(raw_data)
        
        # Destination call sign
        self.dst_callsign = self.to_8_bit(raw_data[0:6])
        self.dst_ssid = (ord(raw_data[6]) >> 1) - 0x30
        
        # Source call sign
        self.src_callsign = self.to_8_bit(raw_data[7:13])
        self.src_ssid = (ord(raw_data[13]) >> 1) - 0x30
        
        # Path: DIGI(F) and DIGI(L)
        """If byte which stores SSID, has bit 7 set, VX-8 will mark the call sign
        with a star."""
        # DIGI(F)
        self.digi_f = self.to_8_bit(raw_data[14:20])
        self.digi_f_ssid = (ord(raw_data[20]) >> 1) - 0x30
        self.digi_f_ssid = self.digi_f_ssid & 0b111111
        # DIGI(L)
        if ord(raw_data[21]) != 0xFF:
            self.digi_l = self.to_8_bit(raw_data[21:27])
            self.digi_l_ssid = (ord(raw_data[27]) >> 1) - 0x30
            self.digi_l_ssid = self.digi_l_ssid & 0b111111
        else:
            self.digi_l = ""
            self.digi_l_ssid = 0
        
        # Body
        self.body = raw_data[30:30+metadata.pkt_len].strip()
        self.path = None

    def to_8_bit(self, data):
        res = ""
        for c in data:
            res += chr(ord(c) / 2)
        return res
    
    def __repr__(self):
        # Source
        source = self.src_callsign
        if self.src_ssid > 0:
            source += "-%s" % self.src_ssid
        
        # Destination
        dest = self.dst_callsign
        if self.dst_ssid > 0:
            dest += "-%s" % self.dst_ssid
        
        # Path
        path = self.digi_f.strip()
        if self.digi_f_ssid > 0:
            path += "-%s" % self.digi_f_ssid
        if self.digi_l != "":
            path += "; %s" % self.digi_l.strip()
            if self.digi_l_ssid > 0:
                path += "-%s" % self.digi_l_ssid
        
        return '<BeaconPacket from=%s to=%s path="%s" body="%s">' % \
            (source, dest, path, self.body)
