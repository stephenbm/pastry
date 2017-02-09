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
    `Delete`_       Delete a group
    =============== ========================================

    .. _Index:      #pastry.resources.groups.Groups.index
    .. _Get:        #pastry.resources.groups.Groups.get
    .. _Create:     #pastry.resources.groups.Groups.create
    .. _Delete:     #pastry.resources.groups.Groups.delete

API Reference
-------------

.. autoclass:: Groups
   :members: index, get, create, delete
