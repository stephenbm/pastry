.. module:: pastry.resources.pushy

Pushy
=====

Provides a wrapper to the chef pushy endpoints. node_states (status) is the only supported endpoint at
this time.

Supported Operations
--------------------

    =============== ========================================
    `Status`_        Check the push jobs status on a node
    =============== ========================================

    .. _Status:      #pastry.resources.pushy.Pushy.status

API Reference
-------------

.. autoclass:: Pushy
   :members: status
