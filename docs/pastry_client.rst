.. module:: pastry.pastry_client

PastryClient
============


Supported Operations
--------------------

    ============== =================================================
    `Initialize`_  Initialize the client with the chef server info
    `Load Config`_ Load server config from a yaml file
    `Get Url`_     Get the server and endpoint for the request
    `Call`_        Call a resource on the chef server
    ============== =================================================

    .. _Initialize: #pastry.pastry_client.PastryClient.initialize
    .. _Load Config: #pastry.pastry_client.PastryClient.load_config
    .. _Get Url: #pastry.pastry_client.PastryClient.get_url
    .. _Call: #pastry.pastry_client.PastryClient.call

API Reference
-------------

.. autoclass:: PastryClient
   :members: initialize, load_config, get_url, call
