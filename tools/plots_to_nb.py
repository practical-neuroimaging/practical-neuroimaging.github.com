""" Convert code in plot directives to notebook for debugging
"""
import sys
from os.path import splitext, basename

try:
    import IPython.nbformat.v3 as nbf
except ImportError:
    import IPython.nbformat.current as nbf


def get_plot_directives(rst_fobj):
    """ Return code blocks from rst directives """
    code_blocks = []
    current_block = []
    state = 'outside'
    for line in rst_fobj:
        if state == 'outside':
            if line.strip().startswith('.. plot::'):
                state = 'inside0'
            continue
        if state == 'inside0':
            indentation = line.replace(line.lstrip(), '')
            n_indent = len(indentation)
            state = 'inside-params'
        if state == 'inside-params':
            if line.strip().startswith(':'):
                continue
            if line.strip() != '':
                raise ValueError('Invalid syntax')
            state = 'code-block'
            continue
        if state == 'code-block':
            if line == '\n':
                current_block.append(line)
                continue
            if line.startswith(indentation):
                current_block.append(line[n_indent:])
                continue
            state = 'outside'
            while len(current_block) and current_block[-1] == '\n':
                current_block.pop()
            code_blocks.append(''.join(current_block).rstrip())
            current_block = []
    return code_blocks


def blocks_to_nb(code_blocks, nb_name=''):
    nb = nbf.new_notebook(name=nb_name)
    ws = nbf.new_worksheet()
    ws['cells'] = [nbf.new_code_cell('%matplotlib inline')]
    for block in code_blocks:
        ws['cells'].append(nbf.new_code_cell(block))
    nb['worksheets'].append(ws)
    return nb


def main():
    fname = sys.argv[1]
    froot, _ = splitext(fname)
    nb_fname = froot + '.ipynb'
    with open(fname, 'rt') as fobj:
        code_blocks = get_plot_directives(fobj)
    nb = blocks_to_nb(code_blocks, basename(froot))
    with open(nb_fname, 'wt') as fobj:
        fobj.write(nbf.writes_json(nb))


if __name__ == '__main__':
    main()
