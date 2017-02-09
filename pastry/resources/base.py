'''base is a class that resources inherit from to provide common http
methods'''

from pastry.pastry_client import PastryClient


class Base(object):
    '''
    Base class for chef resources to inherit from
    '''
    _base_url = None

    @classmethod
    def base_url(cls):
        '''
        Get the base url for this resaource - raise a ValueError if the
        child class has not set it's url
        '''
        if not cls._base_url:
            raise ValueError('Base url has not been set of this resource')
        return cls._base_url

    @classmethod
    def index(cls):
        '''
        Fetch all instances of this resource
        '''
        return PastryClient.call(cls.base_url())

    @classmethod
    def get(cls, instanceid):
        '''
        Fetch a specific instance of a resource
        '''
        return PastryClient.call('%s/%s' % (cls.base_url(), instanceid))

    @classmethod
    def create(cls, instance):
        '''
        Create a new instance
        '''
        return PastryClient.call(
            '%s' % cls.base_url(), method='POST', data=instance)
