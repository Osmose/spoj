Sphere Online Judge Utility
===========================

Just a small utility I've made for solving problems on the
`Sphere Online Judge <http://www.spoj.com>`_ using Python. It was fun to
automate making the directories for each problem, possibly more fun than
solving the problems themselves.

Install
-------

.. code-block:: sh
   pip install https://github.com/Osmose/spoj.git

Solving a Problem
-----------------

To start solving a problem, create a new directory for it using the ``create``
command along with the code for the problem:

.. code-block:: sh
   $ ./spoj.py create test
   Directory created for problem `test`.
   $ cd test
   $ ls
   input.txt  output.txt  program.py

``program.py`` contains the code for the program, and ``input.txt`` and
``output.txt`` contain the test input and output scraped from the problem page.

## Testing a solution

To test a solution, use the `test` command:

.. code-block:: sh
   $ ./spoj.py test test
   Test run failed!
   <== Input ==>
   1
   2
   88
   42
   99

   <== Expected output ==>
   1
   2
   88

   <== Actual output ==>

   # After fixing the code...
   $ ./spoj.py test test
   Test run passed!
   <== Input ==>
   1
   2
   88
   42
   99

   <== Output ==>
   1
   2
   88

## Developer Setup

1. Use a `virtualenv <https://virtualenv.pypa.io/en/latest/>`_!
2. Install the package in development mode:

.. code-block:: sh
   $ ./setup.py develop

## License
This software is licensed under the
`MIT License <http://opensource.org/licenses/MIT>`_. For more information, see
the ``LICENSE`` file.
