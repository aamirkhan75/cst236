Source Example
==============

Source2 provides functions for describing a rectangle.

Determining rectangle Type
^^^^^^^^^^^^^^^^^^^^^^^^^

The function :func:`source.source2.get_rectangle` provides users with a way to provide a set of four sides
of a rectangle and returns the type of rectangle ("invalid", "square", "rectangle" or "neither")

rectangle Example
^^^^^^^^^^^^^^^

>>> from source.source2 import get_rectangle
>>> get_rectangle(1, 2, 1, 2)
'rectangle'



Module Reference
^^^^^^^^^^^^^^^^

.. automodule:: source.source2
    :members: