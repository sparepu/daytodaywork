import socket
import time
import argparse

parser=argparse.ArgumentParser("prog=DNSResponseTime")
parser.add_argument("host", help="Enter the hostname you want to lookup")
args = parser.parse_args()
counter = [0] * 10

while True:
   try:
      dns_start=time.time()
      ip=socket.gethostbyname(args.host)
      dns_end=time.time()
      x=(dns_end - dns_start) * 1000
      if x < 1:
         counter[0] += 1
      elif x < 2:
         counter[1] += 1
      elif x < 3:
         counter[2] += 1
      time.sleep (0.05)
   except KeyboardInterrupt:
      break 
print 'Requests less than 1ms are %d' %counter[0]
print 'Requests less than 2ms are %d' %counter[1]
print 'Requests less than 3ms are %d' %counter[2]

