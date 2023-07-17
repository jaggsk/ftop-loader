Formation Top Loader
--------------------

A tkinter GUI allowing users to create and update formation top data export files in a format suitable for import into standard geosicence software e.g. Petrel.

Project motivation: create standardised company/department-wide well top sets, stored in a format specific to selected geoscience software packages. Time saved loading multiple wells is significant in comparison to conventional hand loading procedures.


Author: K Jaggs 

Email: kevin.jaggs@ineos.com



Installation
------------

Installation can be directly from the file location or from a git repo.

Find the path of your main Python installation - the package will be installed to the site-packages directory in this location.

.. code:: bash

    which python

.. code:: bash

    C:\Users\kxj17699\AppData\Local\Programs\Python\Python311\Lib\site-packages

Install the package from a new cmd window (ensure not in the active venv) using the following command. python -m ensures that the main python installation is used and not an associated  virtual environment. 
Install directly from the git repo:


    pip install git+file:///https://github.com/jaggsk/ftop-loader



Version 0.1a1:
--------------

First pass alpha release.

Configured for Petrel export format only.

To do:
Bug in unconformity generator 
