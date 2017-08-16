.. module:: pastry.resources.environmnets

Environments
============

The environments resource adds support for managing chef environments.

Supported Operations
--------------------

    =============== ========================================
    `Index`_        Fetch a list of all of the users
    `Get`_          Lookup user info
    `Create`_       Create a new environment
    `Update`_       Update an environment
    `Delete`_       Delete an environment
    `Exists`_       Check if an environment exists
    =============== ========================================

    .. _Index:      #pastry.resources.environments.Environments.index
    .. _Get:        #pastry.resources.environments.Environments.get
    .. _Create:     #pastry.resources.environments.Environments.create
    .. _Update:     #pastry.resources.environments.Environments.update
    .. _Delete:     #pastry.resources.environments.Environments.delete
    .. _Exists:     #pastry.resources.environments.Environments.exists

API Reference
-------------

.. autoclass:: Environments
   :members: index, get, create, update, delete, exists
