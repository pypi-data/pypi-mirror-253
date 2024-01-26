=====
Cutci
=====


.. image:: https://img.shields.io/pypi/v/cutci.svg
        :target: https://pypi.python.org/pypi/cutci

.. image:: https://img.shields.io/travis/jianhongdeng/cutci.svg
        :target: https://travis-ci.com/jianhongdeng/cutci

.. image:: https://readthedocs.org/projects/cutci/badge/?version=latest
        :target: https://cutci.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Cutci is a library to calculate Human Thermal Comfort Index (UTCI) by GPU-accelerated computing with CuPy.

The original (CPU version) code for calculating MRT and UTCI referenced the `CalcHiTiSea_pkg`_.


* Free software: Apache Software License 2.0
* Documentation: https://cutci.readthedocs.io.




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

build: python setup.py sdist bdist_wheel

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`CalcHiTiSea_pkg`: https://doi.org/10.6084/m9.figshare.14661198.v2
