'''
Simple loggger
'''
import datetime


log_levels = {
    2: 'info',
    1: 'warning',
    0: 'error'
}

def log(message, level):
    '''
    Log a message with given log level
    '''
    print '[%s] [%s] %s' % (datetime.datetime.today().isoformat(), log_levels[level], message)


def info(message):
    '''
    Log an info message
    '''
    #TODO: we should select the log level from `log_levels`
    log(message, 2)
