class HttpRequestException(Exception):
    def __init__(self, exception, message):
        self.inner = exception
        self.message = message

    def __str__(self):
        return '%s\n%s' % (self.inner, self.message)