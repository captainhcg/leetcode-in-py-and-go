class Logger(object):

    def __init__(self):
        self.cache = {}
        
    def shouldPrintMessage(self, timestamp, message):
        if timestamp - self.cache.get(message, -10) >= 10:
            self.cache[message] = timestamp
            return True
        return False
