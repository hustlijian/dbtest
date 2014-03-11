#!/usr/bin/env python
# -*- coding: utf-8
'''
date: 2014-03-01
author: lijian <hustlijian@gmail.com>
description:
    input data to mongodb database 
    query the key, and count the QPS
'''

import random
import time
import sys
import getopt
import pymongo

HOST = 'localhost'
PORT = 27017
DB = 'dbtest' 
TABLE = 'testtable'
HELP = '''usage: mongo_test.py [-h] [-i count] [-q times]
desc.:
    [-h] --- get usage help
    [-i count] --- insert count of number into database
    [-q times] --- query the database the given times and get the QPS
'''

MAX = 10000 # inseart max number
TIME = 10000 # query times
QUERY = MAX/2   # the key to query,init here, random choosed in use place

# connect the database
conn = pymongo.Connection(HOST, PORT)
db = conn[DB]
# set the collection(table)
table = db[TABLE]

def insert():
    # insert data into database
    print 'insert count :%s'%MAX

    for i in range(MAX):
        key = str(i)
        value = str(random.randint(0,MAX)) 
        pairs = {"id": key,
                "num": value}
        table.insert(pairs)
    
def query():
    print 'query times: %d'%TIME
    start_time = int(round(time.time()*1000))
    for i in range(TIME):
        # query the num in database
        QUERY = random.randint(0, MAX)
        key = str(QUERY)
        key_pair = {"id":key}
        value = table.find_one()
        #print 'key:%s value:%s'%(key, value)
    end_time  = int(round(time.time()*1000))
    #print 'query time: %d milliseconds' %(end_time-start_time)
    print '[------MongoDB QPS Test------]'
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
