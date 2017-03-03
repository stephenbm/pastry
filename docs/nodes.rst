.. module:: pastry.resources.nodes

Nodes
=====

The groups module adds support for chef nodes.

Supported Operations
--------------------

    =================== ========================================
    `Exists`_           Check if a node exists
    `Get Acl`_          Fetch a node's acl
    `Set Permission`_   Set a permission for a node
    =================== ========================================

    .. _Exists:             #pastry.resources.nodes.Nodes.exists
    .. _Get Acl:            #pastry.resources.nodes.Nodes.exists
    .. _Set Permission:     #pastry.resources.nodes.Nodes.exists

API Reference
-------------

.. autoclass:: Nodes
   :members: exists, get_acl, set_permission
