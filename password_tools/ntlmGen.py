#!/usr/bin/env python
import sys
#hashlib required
#pip install hashlib
import hashlib,binascii

hashValue = sys.argv[1]
#print "Creating NTLM Hash of ", sys.argv[1]

def is_ascii(text):
    if isinstance(text, unicode):
        try:
            text.encode('ascii')
        except UnicodeEncodeError:
            return False
    else:
        try:
            text.decode('ascii')
        except UnicodeDecodeError:
            return False
    return True



if len(sys.argv) == 3:  
    #Read from file
    f = open(sys.argv[1], "r")
    fo = open(sys.argv[2], "a")
    words = f.readlines()
    for x in words:
        if is_ascii(x):
            word = x.strip(' \t\n\r')
            #TrustedSec script for NTLM hash gen
            hash = hashlib.new('md4', word.encode('utf-16le')).digest()
            fo.write(binascii.hexlify(hash).upper() + '\n')
        else:
            print 'ignoring non-ascii character', word

    f.close()
    fo.close()

else:
    print "[!] Error you must specify file to read form and write too!"
    print "[-] Example: ./ntlmGen.py words.txt hash.txt"
    exit()

