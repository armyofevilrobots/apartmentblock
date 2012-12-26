
import sys
import daemon
import time
import os
from configobj import ConfigObj
from optparse import OptionParser
import logging
import socket
from ..dhcpd import DHCPD



def daemon_main():
    dhcpd = DHCPD()
    print "Listening."
    dhcpd.listen()




def main():
    logging.warn("Starting up.")
    daemon_main()
