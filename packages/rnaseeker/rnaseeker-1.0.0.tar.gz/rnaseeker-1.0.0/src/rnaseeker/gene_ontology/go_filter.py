#! /usr/bin/env python3
"""Filter gProfiler output and format for Revigo"""
# go_filter
# author: Josh Tompkin
# contact: jtompkindev@gmail.com
# github: https://github.com/jtompkin/RNAseq
from __future__ import annotations

import sys
import csv
import argparse
from typing import TextIO

from rnaseeker.version import __version__

_VERSION = __version__


def filter_terms(
    in_file: TextIO,
    delimiter: str = ',',
    term_column: int = 1,
    to_filter: str = '',
    filter_path: str | None = None,
) -> list[list[str]]:
    """Filter gene ontology terms from input file"""
    if filter_path:
        with open(filter_path, 'r', encoding='UTF-8') as filter_file:
            terms_to_filter = [i.rstrip() for i in filter_file.readlines()]
    else:
        terms_to_filter = [i.lstrip() for i in to_filter.split(';')]
    with in_file:
        in_reader = csv.reader(in_file, delimiter=delimiter)
        return [row for row in in_reader if row[term_column] not in terms_to_filter]


def write_terms(
    out_file: TextIO,
    terms: list[list[str]],
    delimiter: str = '\t',
    format_out: bool = True,
    header: bool = False,
    id_column: int = 2,
    pval_column: int = 4,
) -> None:
    """Write gene ontology terms. Optionally format output for Revigo"""
    with out_file:
        if format_out:
            out_writer = csv.writer(
                out_file, delimiter=delimiter, quoting=csv.QUOTE_MINIMAL
            )
            out_writer.writerows(
                [[row[id_column], row[pval_column]] for row in terms[1:]]
            )
        else:
            out_writer = csv.writer(
                out_file, delimiter=delimiter, quoting=csv.QUOTE_ALL
            )
            if header:
                out_writer.writerow(terms[0])
            out_writer.writerows(terms[1:])


def main(arguments: list[str] | None = None):
    """Parse arguments and call functions."""
    parser = argparse.ArgumentParser(
        prog='go_filter', description='Filter gProfiler output and format for revigo'
    )
    parser.add_argument(
        '-v', '--version', action='version', version=f'rnaseq: {parser.prog} {_VERSION}'
    )

    input_options = parser.add_argument_group('input options')
    input_options.add_argument(
        'gProfiler_file',
        type=argparse.FileType('r', encoding='UTF-8'),
        help='Path to gProfiler file to filter. ' + "Reads from standard in if `-'.",
    )
    input_options.add_argument(
        '-c',
        '--term-column',
        dest='term_column',
        type=int,
        default=1,
        help='Integer of column index containing gene ontology terms. '
        + 'Index starts at 0. Defaults to 1.',
    )
    input_options.add_argument(
        '-d',
        '--in-delimiter',
        dest='in_delimiter',
        default=',',
        help="Delimiter character for input. Defaults to `,'.",
    )

    output_options = parser.add_argument_group('output options')
    output_options.add_argument(
        '-o',
        '--out',
        dest='out_file',
        type=argparse.FileType('w', encoding='UTF-8'),
        default=sys.stdout,
        help="Path to output file. Writes to standard out if `-'. "
        + 'Defaults to standard out.',
    )
    output_options.add_argument(
        '-p',
        '--pval-column',
        dest='pval_column',
        type=int,
        default=4,
        help='Integer index of column containing result P-value. '
        + 'Index starts at 0. Defaults to 4. Only used if formatting output.',
    )
    output_options.add_argument(
        '-i',
        '--id-column',
        dest='id_column',
        type=int,
        default=2,
        help='Integer index of column containing gene ontology ids. '
        + 'Index starts at 0. Defaults to 2. Only used if formatting output.',
    )
    output_options.add_argument(
        '-s',
        '--out-delimieter',
        dest='out_delimiter',
        default='\t',
        help='Delimiter character for output. Defaults to tab.',
    )
    output_options.add_argument(
        '--no-format',
        dest='format_out',
        action='store_false',
        help='Do not format output for Revigo. Output will be '
        + 'formatted like gProfiler.',
    )
    output_options.add_argument(
        '--header',
        dest='write_header',
        action='store_true',
        help='Write header of input file to output. Only writes if '
        + '--no-format is specified.',
    )

    filter_options = parser.add_argument_group('filter options')
    filter_options.add_argument(
        '-f',
        '--filter',
        dest='filter_terms',
        default='biological_process;molecular_function;cellular_component',
        help='String containing gene ontology terms to filter from input '
        + 'file. Separate terms with a semicolon (;).',
    )
    filter_options.add_argument(
        '--filter-file',
        dest='filter_path',
        help='Path to file containing gene ontology terms to filter. '
        + 'One gene ontology term per line. Not compatible with -f.',
    )

    args = parser.parse_args(arguments)

    filtered_terms = filter_terms(
        args.gProfiler_file,
        delimiter=args.in_delimiter,
        to_filter=args.filter_terms,
        filter_path=args.filter_path,
    )
    write_terms(
        args.out_file,
        terms=filtered_terms,
        delimiter=args.out_delimiter,
        format_out=args.format_out,
        header=args.write_header,
        id_column=args.id_column,
        pval_column=args.pval_column,
    )


if __name__ == '__main__':
    main()
