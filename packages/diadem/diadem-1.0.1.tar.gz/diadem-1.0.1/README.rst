======
diadem
======

.. image:: https://img.shields.io/badge/made%20with-pop-teal
   :alt: Made with pop, a Python implementation of Plugin Oriented Programming
   :target: https://pop.readthedocs.io/

.. image:: https://img.shields.io/badge/made%20with-python-yellow
   :alt: Made with Python
   :target: https://www.python.org/

Diadem extends idem to streamline cloud resource management by organizing, parametrizing, and visualizing SLS data.

About
=====

Built on POP, diadem integrates with Idem, providing a user-friendly cli interface for handling complex cloud infrastructures.
It extends idem with the subcommands "compile" and "view", which grant idem the ability to do tasks based on complex
analysis of relationships between resources. Such as:

- Graphing the relationships between resources
- Identifying orphans
- Abstracting the similarities between resources into params
- Creating arg-bind relationships between resources

Each of these abilities enable you to easily get started with efficiently managing cloud resources with idem from ground zero.

What is POP?
------------

This project is built with `pop <https://pop.readthedocs.io/>`__, a Python-based
implementation of *Plugin Oriented Programming (POP)*. POP seeks to bring
together concepts and wisdom from the history of computing in new ways to solve
modern computing problems.

For more information:

* `Intro to Plugin Oriented Programming (POP) <https://pop-book.readthedocs.io/en/latest/>`__
* `pop-awesome <https://gitlab.com/vmware/pop/pop-awesome>`__
* `pop-create <https://gitlab.com/vmware/pop/pop-create/>`__

Getting Started
===============

Prerequisites
-------------

* Python 3.10+
* git *(if installing from source, or contributing to the project)*

Installation
------------

.. note::

   If wanting to contribute to the project, and setup your local development
   environment, see the ``CONTRIBUTING.rst`` document in the source repository
   for this project.

If wanting to use ``diadem``, you can do so by either
installing from PyPI or from source.

Install from PyPI
+++++++++++++++++

Install diadem with only the "compile" functionality:

.. code-block:: bash

   pip install diadem

Install diadem with matplotlib for data visualizations with matplotlib and networkx:

.. code-block:: bash

   pip install diadem[visualize]

Install from source
+++++++++++++++++++

.. code-block:: bash

   # clone repo
   git clone git@gitlab.com:Akm0d/diadem.git
   cd diadem

   # Setup venv
   python3 -m virtualenv .venv
   source .venv/bin/activate
   pip install -e .

Usage
=====

Diadem simplifies the management of cloud resources.
Use it to enumerate resources, organize SLS files, and visualize cloud infrastructure, ensuring efficient and secure cloud operations.

Examples
--------

Enumerate cloud resources with idem describe:

.. code-block:: bash

   idem describe "aws.*" > aws.sls
   idem describe "gitlab.*" > gitlab.sls

Create argbind relationships between resources only:

.. code-block:: bash

   idem compile aws.sls gitlab.sls --match-strategy=pass

Parametrize sls files by creating arg-bind relationships and abstract similarities between resources into params:

.. code-block:: bash

   idem compile aws.sls gitlab.sls

Parametrize sls files by creating arg-bind relationships, abstract similarities between resources into params, and organize the output into logical groups in a file tree:

.. code-block:: bash

   idem compile aws.sls gitlab.sls --tree=/srv/idem


Visualize relationships between resources using matplotlib:

.. code-block:: bash

   idem view /srv/idem/state --params /srv/idem/param

Run idem state on the newly crafted sls/param trees:

.. code-block:: bash

   idem state /srv/idem/state --params /srv/idem/param

Identify orphan resources and craft absent states for them:

.. code-block:: bash

   idem view /srv/idem/state  --params /srv/idem/param > orphans.sls

Show a graph of relationships between resources (requires having installed diadem with the "visualize" extras):

.. code-block:: bash

   idem view /srv/idem/state --params /srv/idem/param --show

Roadmap
=======

Reference the `open issues <https://gitlab.com/akm0d/diadem/issues>`__ for a list of
proposed features (and known issues).

Acknowledgements
================

* `Img Shields <https://shields.io>`__ for making repository badges easy.
