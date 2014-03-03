#!/usr/bin/env python
# -*- coding: utf-8
'''
date: 2014-03-01
author: lijian <hustlijian@gmail.com>
description:
    input data to mysql database table
'''

import redis
import random
import time
import sys

HOST = 'localhost'
PORT = 6379
DB = 0

MAX = 10000 # inseart max number
TIME = 1000000 # query times
QUERY = MAX/2   # the key to query

# connect the database

r = redis.StrictRedis(host=HOST, port=PORT, db=DB)

def insert():
    # insert data into database
    for i in range(MAX):
        key = str(i)
        value = str(random.randint(0,MAX)) 
        #print key , value
        r.set(key, value)
    
def query():
    # query the num in database
    key = str(QUERY)
    value = r.get(key)
    #print 'key:%s value:%s'%(key, value)

def main():
    #insert()

    start_time = int(round(time.time()*1000))
    for i in range(TIME):
        query()
    end_time  = int(round(time.time()*1000))
    #print 'query time: %d milliseconds' %(end_time-start_time)
    print '[------Redis QPS Test------]'
    print 'QPS: %d query/seconds'%(TIME*1000/(end_time-start_time))

if __name__ == '__main__':
    main()
