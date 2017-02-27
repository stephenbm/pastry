.. module:: pastry.resources.groups

Groups
=====

The groups module adds support for the chef group resource.

Supported Operations
--------------------

    =============== ========================================
    `Index`_        Fetch a list of all of the groups
    `Get`_          Lookup group info
    `Create`_       Create a new group
    `Update`_       Update a group
    `Delete`_       Delete a group
    `Exists`_       Check if a group exists
    =============== ========================================

    .. _Index:      #pastry.resources.groups.Groups.index
    .. _Get:        #pastry.resources.groups.Groups.get
    .. _Create:     #pastry.resources.groups.Groups.create
    .. _Update:     #pastry.resources.groups.Groups.update
    .. _Delete:     #pastry.resources.groups.Groups.delete
    .. _Exists:     #pastry.resources.groups.Groups.exists

API Reference
-------------

.. autoclass:: Groups
   :members: index, get, create, update, delete, exists
