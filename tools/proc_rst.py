#!/usr/bin/env python
""" Process ipython notebook converted rst
"""

import sys
from os.path import split as psplit, join as pjoin


def line_indent(line):
    return len(line) - len(line.lstrip())


def is_empty(line):
    return line.strip() == ''


def proc_body(body, indent):
    spaces = ' ' * indent
    new_body = ['.. plot::\n', spaces + ':context:\n']
    plts = [line for line in body if line.strip().startswith('plt.')]
    if len(plts) == 0:
        new_body.append(spaces + ':nofigs:\n')
    new_body.append('\n')
    # Ignore trailing blank lines
    n_good = len(body)
    for line in body[::-1]:
        if not is_empty(line):
            break
        n_good -= 1

    for line in body[:n_good]:
        if is_empty(line):
            new_body.append(line)
            continue
        if line_indent(line) == indent:
            new_line = spaces + '>>> ' + line.lstrip()
            new_body.append(new_line)
            continue
        new_line = spaces + '... ' + line.lstrip()
        new_body.append(new_line)
    return new_body


def proc_notebook(contents):
    new_contents = []
    state = 'default'
    for line in contents:
        if state == 'default':
            if line.startswith('.. code:: python'):
                state = 'code-block-line0'
            else:
                new_contents.append(line)
            continue
        if state == 'code-block-line0':
            if line.strip() == '':
                continue
            block_indent = line_indent(line)
            block_body = []
            state = 'code-block-body'
        if state == 'code-block-body':
            if not is_empty(line) and line_indent(line) < block_indent:
                state = 'waiting-for-pl'
                new_contents += proc_body(block_body, block_indent)
            block_body.append(line)
        if state == 'waiting-for-pl':
            if line.startswith('.. parsed-literal::'):
                state = 'in-pl-line0'
                continue
            new_contents.append('\n')  # Restore trailing blank
            new_contents.append(line)
            state = 'default'
        if state == 'in-pl-line0':
            if is_empty(line):
                continue
            new_contents.append(line)
            state = 'default'

    return new_contents


def main():
    for rst_fname in sys.argv[1:]:
        with open(rst_fname, 'rt') as fobj:
            contents = fobj.readlines()
        better_contents = proc_notebook(contents)
        path, fname = psplit(rst_fname)
        new_fname = pjoin(path, 'p_' + fname)
        with open(new_fname, 'wt') as fobj:
            fobj.write(''.join(better_contents))


if __name__ == '__main__':
    main()
