#!/usr/bin/env python
# -*- coding: utf-8
'''
date: 2014-03-01
author: lijian <hustlijian@gmail.com>
description:
    input data to Berkeley DB
    query the key, and count the QPS
'''

import random
import time
import sys
import getopt
import bsddb

DB = "bsddb.db"
MODE = "c"
HELP = '''usage: bdb_test.py [-h] [-i count] [-q times]
desc.:
    [-h] --- get usage help
    [-i count] --- insert count of number into database
    [-q times] --- query the database the given times and get the QPS
'''

MAX = 10000 # inseart max number
TIME = 10000 # query times
QUERY = MAX/2   # the key to query,init here, random choosed in use place

# open the database
db = bsddb.hashopen(DB, MODE)

def insert():
    # insert data into database
    print 'insert count :%s'%MAX
    for i in range(MAX):
        key = str(i)
        value = str(random.randint(0,MAX)) 
        #print key , value
        db[key] = value
    
def query():
    print 'query times: %d'%TIME
    start_time = int(round(time.time()*1000))
    for i in range(TIME):
        # query the num in database
        QUERY = random.randint(0, MAX)
        key = str(QUERY)
        if db.has_key(key):
            pass
        #print 'key:%s value:%s'%(key, value)
    end_time  = int(round(time.time()*1000))
    #print 'query time: %d milliseconds' %(end_time-start_time)
    print '[------Berkeley QPS Test------]'
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
