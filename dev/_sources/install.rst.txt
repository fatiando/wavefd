.. _install:

Installing
==========

.. note::

    **This package is in early stages of development.**

    We welcome any feedback and ideas!
    Let us know by submitting
    `issues on Github <https://github.com/fatiando/wavefd/issues>`__
    or send us a message on our
    `Gitter chatroom <https://gitter.im/fatiando/fatiando>`__.


Which Python?
-------------

You'll need **Python 3.5 or greater**.

We recommend using the `Anaconda <http://continuum.io/downloads#all>`__ Python
distribution to ensure you have all dependencies installed and the ``conda``
package manager available.
Installing Anaconda does not require administrative rights to your computer and
doesn't interfere with any other Python installations in your system.


Dependencies
------------

* numpy
* numba
* matplotlib
* h5py


Installing
----------

Use ``pip`` to install the latest source from Github::

    pip install https://github.com/fatiando/wavefd/archive/master.zip

Alternatively, you can clone the git repository and install using ``pip``::

    git clone https://github.com/fatiando/wavefd.git
    cd wavefd
    pip install .

