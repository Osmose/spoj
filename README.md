# Sphere Online Judge Solutions

Just a collection of solutions I've made for problems on the
[Sphere Online Judge](http://www.spoj.com). It was fun to automate making the
directories for each problem, possibly more fun than solving the problems
themselves.

## Setup

1. Use a [virtualenv](https://virtualenv.pypa.io/en/latest/)!
2. Install the requirements:

```sh
$ pip install -r requirements.txt
```

## Solving a Problem

To start solving a problem, create a new directory for it using the `create`
command along with the code for the problem:

```sh
$ ./spoj.py create test
Directory created for problem `test`.
$ cd test
$ ls
input.txt  output.txt  program.py
```

`program.py` contains the code for the program, and `input.txt` and `output.txt`
contain the test input and output scraped from the problem page.

## Testing a solution

To test a solution, use the `test` command:

```sh
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
```


## License
This software is licensed under the
[MIT License](http://opensource.org/licenses/MIT). For more information, see the
`LICENSE` file.
