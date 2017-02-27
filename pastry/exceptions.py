class HttpError(Exception):
    def __init__(self, message, statuscode, *args, **kwargs):
        self.statuscode = statuscode
        super(HttpError, self).__init__(message, *args, **kwargs)

    def __str__(self):
        return '(%s) %s' % (self.statuscode, self.message)
