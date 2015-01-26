#!/usr/bin/env python
import logging
import os
import stat
import subprocess

import argh
import pypandoc
import requests
from blessings import Terminal
from bs4 import BeautifulSoup
from readability.readability import Document
from tabulate import tabulate


__version__ = '0.1'
logging.getLogger('requests').setLevel(logging.WARNING)


def test(problem_name):
    """
    Run the test input for a problem and compare it to the expected
    output.
    """
    t = Terminal()

    program = '{0}/program.py'.format(problem_name)
    test_input_filename = '{0}/input.txt'.format(problem_name)
    with open(test_input_filename, 'rU') as f:
        test_input = f.read()
    with open('{0}/output.txt'.format(problem_name), 'rU') as f:
        expected_output = f.read()

    result = subprocess.check_output(program, stdin=open(test_input_filename, 'rU'))

    if result.strip() != expected_output.strip():
        print t.bright_red('Test run failed!')
        print t.cyan('<== Input ==>')
        print test_input
        print t.cyan('<== Expected output ==>')
        print expected_output
        print t.cyan('<== Actual output ==>')
        print result
    else:
        print t.bright_green('Test run passed!')
        print t.cyan('<== Input ==>')
        print test_input
        print t.cyan('<== Output ==>')
        print expected_output


def info(problem_name):
    url = 'http://www.spoj.com/problems/{0}/'.format(problem_name.upper())
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text)
    problem_html = unicode(soup.findAll(**{'class': 'prob'})[0])
    readable_problem = Document(problem_html, negative_keywords=['ccontent'], positive_keywords=['prob'])
    problem_summary = readable_problem.summary(html_partial=True).strip()
    plain_problem = pypandoc.convert(problem_summary, 'plain', format='html')

    print plain_problem


@argh.decorators.named('list')
def list_problems(start=0):
    # TODO: List challenge, tutorial, etc. problems.
    url = 'http://www.spoj.com/problems/classical/sort=0,start={0}'.format(start)
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text)
    problems = []
    for row in soup.findAll(**{'class': 'problemrow'}):
        cells = row.findAll('td')
        problems.append([
            int(cells[0].text),  # ID
            cells[1].text,  # Name
            cells[2].text,  # Code
            int(cells[3].text),  # Users
            cells[4].text,  # Accuracy
        ])

    print tabulate(problems, headers=['ID', 'Name', 'Code', 'Users Solved', 'Accuracy %'],
                   tablefmt='fancy_grid')


problem_template = '''
#!/usr/bin/env python
"""
{title}

{url}
"""

if __name__ == '__main__':
    pass # Get to work!
'''.lstrip()


def create(problem_name):
    t = Terminal()
    problem_name = problem_name.lower()

    if os.path.isdir(problem_name):
        print t.bright_red('Directory for problem `{0}` already exists!'.format(problem_name))
        return

    url = 'http://www.spoj.com/problems/{0}/'.format(problem_name.upper())
    response = requests.get(url)
    response.raise_for_status()

    # TODO: Handle bad input.
    soup = BeautifulSoup(response.text)
    title = soup.find_all('h1')[1].text.strip()
    test_input, test_output = _find_sample_io(soup)

    # Create problem directory.
    os.makedirs(problem_name)

    # Write program template and chmod +x
    program = '{0}/program.py'.format(problem_name)
    with open(program, 'w') as f:
        f.write(problem_template.format(title=title, url=url))
    st = os.stat(program)
    os.chmod(program, st.st_mode | stat.S_IEXEC)

    with open('{0}/input.txt'.format(problem_name), 'w') as f:
        f.write(test_input)

    with open('{0}/output.txt'.format(problem_name), 'w') as f:
        f.write(test_output)

    print t.bright_green('Directory created for problem `{0}`.'.format(problem_name))


def _find_sample_io(soup):
    """
    Check for the various forms that sample input and output takes on a
    SPOJ page.
    """
    # Case 1: <p>Input: </p><pre>input</pre>
    #         <p>Output: </p><pre>output</pre>
    io = soup.find_all('pre')
    if len(io) == 2:
        test_input = io[0].text.strip()
        test_output = io[1].text.strip()
        return test_input, test_output

    io = soup.pre
    if len(io.contents) == 4:
        test_input = unicode(io.contents[1]).strip()
        test_output = unicode(io.contents[3]).strip()
        return test_input, test_output

    if 'Sample input:' in io.text and 'Sample output:' in io.text:
        test_input, test_output = io.text.split('Sample output:')
        test_input = test_input.replace('Sample input:', '')
        return test_input.strip(), test_output.strip()

    raise ValueError('Could not find sample input or output!')


def main():
    parser = argh.ArghParser()
    parser.add_commands([test, create, info, list_problems])
    parser.dispatch()


if __name__ == '__main__':
    main()
