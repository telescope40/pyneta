Value INT_NAME (\S+)
Value STATUS ((up|down))
Value ADMIN ((up||down))
Value MAC_ADDRESS ([0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4})
Value MTU (\d+)
Value DUPLEX ((full|half)-duplex)
Value SPEED (\d+)

Start
  ^${INT_NAME} is ${STATUS}$$
  ^admin state is ${ADMIN},
  ^  Hardware:.*address: ${MAC_ADDRESS}\s
  ^  MTU ${MTU} bytes
  ^  ${DUPLEX}, ${SPEED} Mb/s -> Record







#Using the 'show interface Ethernet2/1' output from nxos1 (see link below), extract the interface name, line status, admin state, MAC address, MTU, duplex, and speed using TextFSM

#s1# show interface ethernet 2/1
#Ethernet2/1 is up
##admin state is up, Dedicated Interface
#  Hardware:  Ethernet, address: 000c.29d1.d56b (bia 2cc2.605e.5dba)
#  Internet Address is 10.66.66.1/24
#  MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec
#  reliability 255/255, txload 1/255, rxload 1/255
#  Encapsulation ARPA, medium is broadcast
#  Port mode is routed
#  full-duplex, 1000 Mb/s
#  Beacon is turned off
#  Auto-Negotiation is turned off
#  Input flow-control is off, output flow-control is off
#  Auto-mdix is turned off
#  Switchport monitor is off 
#  EtherType is 0x8100 
#  EEE (efficient-ethernet) : n/a
#  Last link flapped 5d17h
#  Last clearing of "show interface" counters never
#  3 interface resets
#  Load-Interval #1: 0 seconds
#    0 seconds input rate 0 bits/sec, 0 packets/sec
#    0 seconds output rate 0 bits/sec, 0 packets/sec
#    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
#  Load-Interval #2: 0 seconds
#    0 seconds input rate 0 bits/sec, 0 packets/sec
#    0 seconds output rate 0 bits/sec, 0 packets/sec
#    input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
#  RX
#    0 unicast packets  0 multicast packets  0 broadcast packets
#    0 input packets  0 bytes
#    0 jumbo packets  0 storm suppression packets
#    0 runts  0 giants  0 CRC/FCS  0 no buffer
#    0 input error  0 short frame  0 overrun   0 underrun  0 ignored
#    0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
#    0 input with dribble  0 input discard
#    0 Rx pause
#  TX
#    0 unicast packets  0 multicast packets  0 broadcast packets
#    0 output packets  0 bytes
#    0 jumbo packets
#    0 output error  0 collision  0 deferred  0 late collision
#    0 lost carrier  0 no carrier  0 babble  0 output discard
#    0 Tx pause
