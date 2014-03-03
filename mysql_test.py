#!/usr/bin/env python
# -*- coding: utf-8
'''
date: 2014-03-01
author: lijian <hustlijian@gmail.com>
description:
    input data to mysql database table
    query the key, and count the QPS
'''
import random
import time
import sys
import getopt
import MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWD = 'root'
DB = 'dbtest'
DBTABLE = 'testtable'
HELP = '''usage: mysql_test.py [-h] [-i count] [-q times]
desc.:
    [-h] --- get usage help
    [-i count] --- insert count of number into database
    [-q times] --- query the database the given times and get the QPS
'''

MAX = 10000  # random max number
TIME = 10000 # query times
QUERY = 1   # the key to query, init here, and random in use place

# connect the database
try:
    conn = MySQLdb.connect(host=HOST,user=USER,
        passwd=PASSWD,db=DB)
except MySQLdb.ERROR, e:
    print 'Error %d:%s'%(e.args[0], e.args[1])
    exit(1)

# create cursor
cursor = conn.cursor()

def insert():
    print 'insert count :%s'%MAX
    # insert data into table 
    for i in range(MAX):
        command = 'insert into %s (num) values (%d)' %(DBTABLE,random.randint(0,MAX))
        cursor.execute(command)
    conn.commit()
    
def query():
    print 'query times: %d'%TIME
    start_time = int(round(time.time()*1000))
    for i in range(TIME):
        # query the num in database
        QUERY = random.randint(0,MAX)
        command = 'SELECT * FROM %s WHERE id=%d'%(DBTABLE, QUERY)
        cursor.execute(command)
        #result = cursor.fetchall()
        
    end_time  = int(round(time.time()*1000))
    #print 'query time: %d milliseconds' %(end_time-start_time)
    print '[------MySQL QPS Test------]'
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

    # close connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main(sys.argv[1:])
