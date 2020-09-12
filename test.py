from bluepy.btle import Scanner, DefaultDelegate

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
        elif isNewData:
            print("Received new data from", dev.addr)

scan_secs = 5
print("Scanning for %s seconds" % scan_secs)
scanner = Scanner().withDelegate(ScanDelegate())

try:
    devices = scanner.scan(scan_secs)
except btle.BTLEException as err:
    print("Unable to scan for devices, did you set-up permissions for bluepy-helper correctly? ex: %s" % err)

for dev in devices:
    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi) )
    for (adtype, desc, value) in dev.getScanData():
        print("  %s = %s" % (desc, value) )

# print("Devices found:")
# for dev in devices:
#     localname = dev.getValueText(9)

#     if not localname: continue

#     if localname.startswith("XMCTD_"):
#         print("Bedlight lamp v1  %s (%s), rssi=%d" % (dev.addr, localname, dev.rssi))
#     elif localname.startswith("yeelight_ms"):
#         print("Candela %s (%s), rssi=%d" % (dev.addr, localname, dev.rssi))
