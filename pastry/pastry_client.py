import os
import yaml
import requests

from pastry.utils.auth import signed_headers


class PastryClient(object):
    '''
    PastryClient is used by the resources to send requests to chef.
    You can use the PastryClient to initialize the config to use for the
    chef server.
    '''
    _server = None
    _organization = None
    _client = None
    _keypath = None
    initialized = False
    verify = True

    @classmethod
    def initialize(cls, server, organization, client, keypath):
        '''
        Initializes the server connection info

        :param server: The url for the chef server e.g. https://my.chef.server
        :param organization: The name of the cheff org to use
        :param client: The client/username to use
        :param keypath: The path to the pem for the client/user
        :type server: string
        :type organization: string
        :type client: string
        :type keypath: string
        '''
        cls._server = server
        cls._organization = organization
        cls._client = client
        cls._keypath = keypath
        cls.initialized = True

    @classmethod
    def load_config(cls, config_path=None):
        '''
        Load server config from a yaml file

        If no config_path is specified it will try to load config from
        ``$HOME/.chef/pastry.yaml``

        .. note::

            This method is automatically called if an http requests is made and
            the client has not yet been initialised

        :param config_path: The path to the config file on the local filesystem
        :type config_path: string
        '''
        if not config_path:
            config_path = os.path.join(
                os.environ['HOME'], '.chef', 'pastry.yaml')
        if not os.path.exists(config_path):
            raise ValueError(
                'PastryClient not initialized and %s does not exist' %
                config_path
            )
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file.read())
        cls.initialize(
            config['server'],
            config['organization'],
            config['client'],
            config['keypath']
        )

    @classmethod
    def get_url(cls, endpoint):
        '''
        Fetches the server and updates the endpoint with the organization
        
        :param endpoint: The endpoint being called on the chef server
        :type endpoint: string
        :return: The server url and updated endpoint
        :rtype: tuple
        '''
        if not cls.initialized:
            cls.load_config()
        return cls._server, (endpoint % {'org': cls._organization})

    @classmethod
    def call(cls, endpoint, method='GET', data=None):
        '''
        Send an http request to the chef server api

        :param endpoint: The endpoint for the resource being called
        :param method: The HTTP method
        :param data: The body of the request
        :type endpoint: string
        :type method: string
        :type data: hash
        :return: The json response from the server
        :rtype: hash
        '''
        server, path = cls.get_url(endpoint)
        headers = signed_headers(
            cls._client, cls._keypath, path, method=method, data=data)
        resp = requests.get(
            '%s%s' % (server, path), headers=headers, verify=cls.verify)
        return resp.json
