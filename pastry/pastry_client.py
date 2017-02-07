import requests

from pastry.utils.auth import signed_headers


class PastryClient(object):
    _server = None
    _organization = None
    _client = None
    _keypath = None

    @classmethod
    def initialize(cls, server, organization, client, keypath):
        cls._server = server
        cls._organization = organization
        cls._client = client
        cls._keypath = keypath

    @classmethod
    def get_url(cls, endpoint):
        if not cls._server:
            cls.initialize(
                'https://pchfsvr1v.standardbank.co.za',
                'chopchop',
                'skynet',
                '/Users/cudaza/.chef/skynet.pem')
        return cls._server, (endpoint % {'org': cls._organization})

    @classmethod
    def call(cls, endpoint, method='GET', data=None):
        server, path  = cls.get_url(endpoint)
        headers = signed_headers(cls._client, cls._keypath, server, path, method=method, data=data)
        resp = requests.get('%s%s' % (server, path), headers=headers, verify=False)
        print resp.text
