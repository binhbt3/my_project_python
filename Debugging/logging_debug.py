import logging
logging.basicConfig(filename = 'my_logging.txt',level =  logging.DEBUG, format = '%(asctime)s - %(levelname)s -%(message)s')

# We can disable any type of logging you want
#logging.disable(logging.CRITICAL)
#logging.disable(logging.WARNING)
logging.disable(logging.DEBUG)

# We have 5 type of logging: DEBUG, INFO, WARNING, ERROR, CRITICAL
logging.debug('Start of program')



def factorial(n):
        logging.debug('Start of factorial (%s)' %(n))
        total = 1
        for i in range(0, n + 1):
                total *=i
                logging.warning("i is %s, total is %s" %(i, total))
        logging.critical('Return value is %s' %(total))
        return total

	

print(factorial(4))

logging.debug('End of program')
