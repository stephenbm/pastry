.. module:: pastry.resources.cookbooks

Cookbooks
=========

The cookbooks resource adds support for querying chef cookbooks.

Supported Operations
--------------------

    =================== ===========================================
    `Index`_            Fetch a list of all of the groups
    `Exists`_           Check if a group exists
    `Contents`_         Get the list of files in a cookbook
    `Parse Filename`_   Splits up the path to a file in a cookbook
    `File Content`_     Read the contents of a file
    =================== ===========================================

    .. _Index:          #pastry.resources.cookbooks.Cookbooks.index
    .. _Exists:         #pastry.resources.cookbooks.Cookbooks.exists
    .. _Contents:       #pastry.resources.cookbooks.Cookbooks.contents
    .. _Parse Filename: #pastry.resources.cookbooks.Cookbooks.parse_filename
    .. _File Content:   #pastry.resources.cookbooks.Cookbooks.file_content

API Reference
-------------

.. autoclass:: Cookbooks
   :members: index, exists, contents, parse_filename, file_content
