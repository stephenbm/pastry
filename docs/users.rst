.. module:: pastry.resources.users

Users
=====

Wraps the chef user account. In order to modify users in chef you will need server admin privledges.
Server admins are supported in chef 12.4.1 and above. If you are using an older version of chef server
you will have to use the pivotal user (not recommended) to be able to modify users. More info on 
chef server admins can be found in the chef `server admins documentation`_.

Supported Operations
--------------------

    =============== ========================================
    `Index`_        Fetch a list of all of the users
    `Get`_          Lookup user info
    `Create`_       Create a new user
    `Update`_       Update a group
    `Delete`_       Delete a group
    `Exists`_       Check if a user exists
    `Invite`_       Invite a user to an org
    =============== ========================================

    .. _Index:      #pastry.resources.users.Users.index
    .. _Get:        #pastry.resources.users.Users.get
    .. _Create:     #pastry.resources.users.Users.create
    .. _Update:     #pastry.resources.users.Users.update
    .. _Delete:     #pastry.resources.users.Users.delete
    .. _Exists:     #pastry.resources.users.Users.exists
    .. _Invite:     #pastry.resources.users.Users.invite

API Reference
-------------

.. _server admins documentation: https://docs.chef.io/ctl_chef_server.html#server-admins


.. autoclass:: Users
   :members: index, get, create, update, delete, exists, invite
