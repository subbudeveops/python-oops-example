#LOGGING MODULE:
#---------------
# it is highly recommended to store complete application flow and exception information to afile. this process is called logging
#the main advangtages of logging are:
#1. we can use log files while performing debugging
#2. we can provide statistics like number of requests per day etc
#To implement logging,Python provides one inbuilt module logging

# logging levels:
# Depending on type of information ,logging data is divided according to the following 6 levels in python
#1.CRITICAL===>50==> Represents a very serious problems that needs high attention
#2.ERROR===>40==>Represents a serous error
#3.WARNNING==>==>Represents a warning message, some caution needed.it is alert to the programmer
#4.INFO==>20==>Represents that the level with some important information
#5.DEBUG==>10==>Represents a message with debugging information
#6.NOTSET==>0==> Represents that the level is not set
#By default while executing python program only warning and higher level message will be displayed.(WARRNING,ERROR,CRITICAL)
# NOTSET<DEBUG<INFO<WARNING<ERROR<CRITICAL

#HOW TO IMPLEMENT LOGGING:
#------------------------
#1.To perform logging,first WE HAVE TO require log file
# and we have to  specify which level message we have to store
# we can do this by using basicConfig() function of logging module
# logging.basicConfig(filename='log.txt',level=logging.WARNING) 
# If u want to write debug message we can use logging.debug(msg)
# same like same if u want to write info,warning,error,critical

import logging
logging.basicConfig(filename='log.txt',level=logging.INFO,filemode='w')# if use filemode='w' we can get present data in log file 
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('eror information')
logging.critical('critical information')

#output:

#INFO:root:info information
#WARNING:root:warning information
#ERROR:root:eror information
#CRITICAL:root:critical information

print()
# How to fromat  log messagesbased on my requirement:
# i want to print only level
import logging
logging.basicConfig(format='%(levelname)s')
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('eror information')
logging.critical('critical information')

#output

#logging module demo
#WARNING
#ERROR
#CRITICAL

print()

# If i want level name and messgae

import logging
logging.basicConfig(format='%(levelname)s:%(message)s')
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('eror information')
logging.critical('critical information')

#output

#logging module demo
#WARNING:warning information
#ERROR:eror information
#CRITICAL:critical information
 
print()

import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('eror information')
logging.critical('critical information')

#output:
#logging module demo
#2021-12-10 13:47:31,069:WARNING:warning information
#2021-12-10 13:47:31,084:ERROR:eror information
#2021-12-10 13:47:31,096:CRITICAL:critical information

print()

import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('eror information')
logging.critical('critical information')

#output:
#logging module demo
#2021-12-10 13:47:31,069:WARNING:warning information
#2021-12-10 13:47:31,084:ERROR:eror information
#2021-12-10 13:47:31,096:CRITICAL:critical information

print() 

import logging
logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',datefmt='%d/%m/%y %I:%M:%S %p')
print('logging module demo')
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

#output:
#logging module demo
#10/12/21 02:13:33 PM:WARNING:warning information
#10/12/21 02:13:33 PM:ERROR:eror information
#10/12/21 02:13:33 PM:CRITICAL:critical information


# How to write python program exception to the log file:
# By using the following we can write exception information to the log file
#logging.exception(msg)
#Python program to write exception information to the log file
import logging
logging.basicConfig(filename="explog.txt",level=logging.INFO)
logging.info('a new request come')
try:
    x=int(input('Enter the firstnumber:'))
    y=int(input('Enter the second number'))
    print(x/y)
except ZeroDivisionError as msg:
    print('cannot divide with Zero ')
    logging.exception(msg)
except ValueError as msg:
    print('Enter the digits')
    logging.exception(msg)
logging.info('Processing is completed')