#!/usr/bin/env python

import argparse
import FM15_transform.data2bufr as data2bufr
import os

THISDIR = os.path.dirname(os.path.realpath(__file__))

def main():
    parser = argparse.ArgumentParser(
        description='Utility to take as input a TAC or other text file containing a ' +
        'single FM15 METAR record or METAR bulletin and convert to geojson records')
    parser.add_argument(
        'metar', metavar='metar', type=str, nargs=1,
        help='Filename of TAC or METAR bulletin'
    )
    parser.add_argument(
        'month', metavar='month', type=int, nargs=1,
        help='Numeric value (1-12) of the month of the observation'
    )
    parser.add_argument(
        'year', metavar='year', type=int, nargs=1,
        help='Year of the observation in YYYY format'
    )
    args = parser.parse_args()
    metar_filename = args.metar[0]
    month = args.month[0]
    year = args.year[0]

    data2bufr.transform_file(metar_filename, month, year)

