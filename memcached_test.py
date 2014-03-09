#!/usr/bin/env python
# -*- coding: utf-8
'''
date: 2014-03-01
author: lijian <hustlijian@gmail.com>
description:
    input data to memcached database 
    query the key, and count the QPS
'''

import random
import time
import sys
import getopt
import memcache

HOST = '127.0.0.1'
PORT = 11211
HELP = '''usage: memcached_test.py [-h] [-i count] [-q times]
desc.:
    [-h] --- get usage help
    [-i count] --- insert count of number into database
    [-q times] --- query the database the given times and get the QPS
'''

MAX = 10000 # inseart max number
TIME = 10000 # query times
QUERY = MAX/2   # the key to query,init here, random choosed in use place

# connect the database
server = '%s:%s'%(HOST, PORT)
mc = memcache.Client([server], debug=0)

def insert():
    # insert data into database
    print 'insert count :%s'%MAX
    for i in range(MAX):
        key = str(i)
        value = random.randint(0,MAX)
        #print key , value
        mc.set(key, value)
    
def query():
    print 'query times: %d'%TIME
    start_time = int(round(time.time()*1000))
    for i in range(TIME):
        # query the num in database
        QUERY = random.randint(0, MAX)
        key = str(QUERY)
        value = mc.get(key)
        #print 'key:%s value:%s'%(key, value)
    end_time  = int(round(time.time()*1000))
    #print 'query time: %d milliseconds' %(end_time-start_time)
    print '[------Memcached QPS Test------]'
    print 'QPS: %d query/seconds'%(TIME*1000/(end_time-start_time))

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hq:i:")
    except getopt.GetoptError:
        print(HELP)
        sys.exit(1)
    if not opts:
        print HELP

    for opt, arg in opts:
        if opt == '-h':
            print HELP
            sys.exit()
        elif opt == '-i':
            global MAX
            MAX = int(arg)
            insert()
        elif opt == '-q':
            global TIME 
            TIME = int(arg)
            query()

if __name__ == '__main__':
    main(sys.argv[1:])
