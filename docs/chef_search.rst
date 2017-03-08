.. module:: pastry.resources.search

Search
======

The search resource provides access to chef search. It supports filtering out only
required fields instead of returning the entire objects from the chef server.

Supported Operations
--------------------

    =============== =================================================
    `Index`_        Fetch a list of available search indexes
    `Run`_          Run a search against an index on the chef server
    =============== =================================================

    .. _Index:      #pastry.resources.search.Search.index
    .. _Run:        #pastry.resources.search.Search.run

API Reference
-------------

.. autoclass:: Search
   :members: index, run
