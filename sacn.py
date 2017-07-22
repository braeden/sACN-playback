import os
import time

#wireshark -D = interface list

interface = "eth0"

def capturePackets(fileName):
	time.sleep(.5)
	os.system("wireshark -i " + interface + "-R acn -a duration:5 -w " + fileName + ".pcap -Q")
	#https://www.wireshark.org/docs/wsug_html_chunked/ChCustCommandLine.html

def replayCapture(fileName):
	os.system("tcpreplay -i "interface + " " + fileName + ".pcap")

