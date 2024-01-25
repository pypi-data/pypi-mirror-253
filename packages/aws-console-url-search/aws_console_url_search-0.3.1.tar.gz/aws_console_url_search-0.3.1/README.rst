
.. .. image:: https://readthedocs.org/projects/aws_console_url_search/badge/?version=latest
    :target: https://aws_console_url_search.readthedocs.io/index.html
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/aws_console_url_search-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/aws_console_url_search-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/aws_console_url_search-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/aws_console_url_search-project

.. image:: https://img.shields.io/pypi/v/aws_console_url_search.svg
    :target: https://pypi.python.org/pypi/aws_console_url_search

.. image:: https://img.shields.io/pypi/l/aws_console_url_search.svg
    :target: https://pypi.python.org/pypi/aws_console_url_search

.. image:: https://img.shields.io/pypi/pyversions/aws_console_url_search.svg
    :target: https://pypi.python.org/pypi/aws_console_url_search

.. image:: https://img.shields.io/badge/Release_History!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/aws_console_url_search-project/blob/main/release-history.rst

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/aws_console_url_search-project

------

.. .. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://aws_console_url_search.readthedocs.io/index.html

.. .. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://aws_console_url_search.readthedocs.io/py-modindex.html

.. .. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://aws_console_url_search.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/aws_console_url_search-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/aws_console_url_search-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/aws_console_url_search-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/aws_console_url_search#files


Welcome to ``aws_console_url_search`` Documentation
==============================================================================
``aws_console_url_search (acs)`` is a cross-platform CLI tool for lightning-fast AWS Console URL opener. Say goodbye to hunting through tabs or bookmarks—acs instantly locates and opens your desired AWS Console URL in your default browser. It's not just fast; it's blazingly fast! With pinpoint accuracy and interactive features, acs redefines your AWS Console experience.


Demo
------------------------------------------------------------------------------
.. image:: https://asciinema.org/a/633187.svg
    :target: https://asciinema.org/a/633187


.. _install:

Install
------------------------------------------------------------------------------
``aws_console_url_search`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install aws_console_url_search

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade aws_console_url_search

Then you can type ``acs`` CLI command to enter the interactive UI:

.. code-block::

    $ acs


Usage - Search AWS Service or Menu URL
------------------------------------------------------------------------------
.. code-block::

    $ acs
    [Query (region = None)]: <--- type your query here
    [x] 🌟 🪣 s3 (None)
          Store and retrieve any amount of data from anywhere
    [ ] 🌟 👤 iam (None)
          Manage User Access and Encryption Keys
    [ ] 🌟 🖥 ec2 (None)
          Virtual Servers in the Cloud
    [ ] 🌟 🌐 vpc (None)
          Isolated Cloud Resources
    [ ] 🌟 dynamodb (None)
          Managed NoSQL Database


Usage - Switch AWS Region
------------------------------------------------------------------------------
.. code-block::

    $ acs
    (AWS Region Query): !@ <--- type your aws region query here
    [x] no region | Auto decide based on your AWS Console history
          Hit Enter set region and return to search
    [ ] us-east-1 | US East (N. Virginia)
          Hit Enter set region and return to search
    [ ] us-east-2 | US East (Ohio)
          Hit Enter set region and return to search
    [ ] us-west-1 | US West (N. California)
          Hit Enter set region and return to search
    [ ] us-west-2 | US West (Oregon)
          Hit Enter set region and return to search
