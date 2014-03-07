#!/usr/bin/env python
# -*- coding: utf-8
'''
date: 2014-03-01
author: lijian <hustlijian@gmail.com>
description:
    input data to postgresql database table
    query the key, and count the QPS
'''
import random
import time
import sys
import getopt
import psycopg2

DB = 'dbtest'
USER = 'lijian'
DBTABLE = 'testtable'
HELP = '''usage: postgresql_test.py [-h] [-i count] [-q times]
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
    conn = psycopg2.connect(database=DB,user=USER)
# create cursor
    cursor = conn.cursor()
except psycopg2.DataError, e:
    print 'Error %s'%e
    exit(1)


def insert():
    print 'insert count :%s'%MAX


    # create a table
    try:
        command = 'CREATE TABLE %s(id serial primary key, num integer );'%DBTABLE
        cursor.execute(command)
    except :
        print 'create table error'

    # insert data into table 
    for i in range(MAX):
        command = 'insert into %s(num)  values (%d)' %(DBTABLE,random.randint(0,MAX))
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
    print '[------PostgreSQL QPS Test------]'
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
    conn.close()

if __name__ == '__main__':
    main(sys.argv[1:])
