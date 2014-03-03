#!/usr/bin/env python
# -*- coding: utf-8
'''
date: 2014-03-01
author: lijian <hustlijian@gmail.com>
description:
    input data to mysql database table
'''

import MySQLdb
import random
import time
import sys

HOST = 'localhost'
USER = 'root'
PASSWD = 'root'
DB = 'dbtest'
DBTABLE = 'testtable'

MAX = 10000  # random max number
TIME = 10000 # query times
QUERY = 1   # the key to query

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
    # insert data into table 
    for i in range(MAX):
        command = 'insert into %s (num) values (%d)' %(DBTABLE,random.randint(0,MAX))
        cursor.execute(command)
    conn.commit()
    
def show():
    # show result
    command = 'SELECT * FROM %s' %DBTABLE
    cursor.execute(command)
    result = cursor.fetchall()
    for record in result:
        print record[0] , "-->", record[1]
    
def query():
    # query the num in database
    command = 'SELECT * FROM %s WHERE id=%d'%(DBTABLE, QUERY)
    cursor.execute(command)
    #result = cursor.fetchall()

def main():
    #insert()

    start_time = int(round(time.time()*1000))
    for i in range(TIME):
        query()
    end_time  = int(round(time.time()*1000))
    #print 'query time: %d milliseconds' %(end_time-start_time)
    print '[------MySQL QPS Test------]'
    print 'QPS: %d query/seconds'%(TIME*1000/(end_time-start_time))

    # close connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()
