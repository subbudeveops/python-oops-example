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