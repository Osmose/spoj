Sphere Online Judge Utility
===========================

Just a small utility I've made for solving problems on the
`Sphere Online Judge <http://www.spoj.com>`_ using Python. It was fun to
automate making the directories for each problem, possibly more fun than
solving the problems themselves.


Install
-------

::

    pip install https://github.com/Osmose/spoj.git


Finding Problems
----------------
You can view a list of problems with the ``list`` command, optionally passing
a problem ID to start the list on (it shows 50 problems at a time)::

    $ spoj list --start=50
      ID  Name                            Code        Users Solved    Accuracy %
    ----  ------------------------------  --------  --------------  ------------
      55  Jasiek                          JASIEK               291         25.06
      56  Dyzio                           DYZIO                804         30.76
      57  Supernumbers in a permutation   SUPPER               526         30.45
    # ... etc ...

You can view the info about a particular problem by passing the problem code to
the ``info`` command::

    $ spoj info test
    +--------------------------------------------------------------------------+
    |                                                                          |
    | SPOJ Problem Set (classical)                                             |
    |                                                                          |
    |                                                                          |
    |                                                                          |
    | 1. LIFE, THE UNIVERSE, AND EVERYTHING                                    |
    |                                                                          |
    |                                                                          |
    | Problem code: TEST                                                       |
    +--------------------------------------------------------------------------+

    Your program is to use the brute-force approach in order to _find the
    Answer to Life, the Universe, and Everything._ More precisely...


Solving a Problem
-----------------

To start solving a problem, create a new directory for it using the ``create``
command along with the code for the problem::

    $ spoj create test
    Directory created for problem `test`.
    $ cd test
    $ ls
    input.txt  output.txt  program.py

``program.py`` contains the code for the program, and ``input.txt`` and
``output.txt`` contain the test input and output scraped from the problem page.


Testing a solution
------------------

To test a solution, use the `test` command::

    $ spoj test test
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
    $ spoj test test
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


Developer Setup
---------------

1. Use a `virtualenv <https://virtualenv.pypa.io/en/latest/>`_!
2. Install the package in development mode::

    $ ./setup.py develop


License
-------
This software is licensed under the
`MIT License <http://opensource.org/licenses/MIT>`_. For more information, see
the ``LICENSE`` file.
