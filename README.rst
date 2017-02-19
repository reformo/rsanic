rsanic
==========

Micro framework built on top of sanic.py written in Python 3.

Installing rsanic
=====================

.. code-block:: bash

    pip3 install rsanic

Example app:

* Local Redis service must be installed and running at port 6397

* Shows how to use html or json responses

.. code-block:: bash

    git clone https://github.com/reformo/rsanic.git
    cd rsanic/example
    python3 server.py

or if you have `pm2 <http://pm2.keymetrics.io>`_ installed

.. code-block:: bash

    git clone https://github.com/reformo/rsanic.git
    cd rsanic/example
    pm2 start process.yml

Then use any web browser to open address: http://127.0.0.1:8000/

Credits
=======

* `Mehmet Korkmaz <http://github.com/mkorkmaz>`_
