#!/usr/bin/env python3
'''
For Functional Configurations Rotate, Translate, Sin, Cos and Atan the Data
Signals are represented using fixed-point 2’s complement numbers with an
integer width of 2 bits. Using the Q Numbers Format 1QN where
N = word width - 2. It can also be described as Fix(N+2)_N

The Phase Signals are: PHASE_IN and PHASE_OUT. The phase signals are always
represented using a fixed-point 2’s complement number with an integer width of
3 bits. As with the data signals the integer width is fixed and any remaining
bits are used for the fractional portion of the number. The Phase Signals
require an increased integer width to accommodate the increased range of
values they must represent when the Phase Format is set to Radians.
When Phase Format is set to Radians, PHASE_IN must be in the range:
-Pi <= (PHASE_IN) <= Pi. PHASE_IN outside this range produce undefined results.
In 2Q7, or Fix10_7, format values, +Pi and -Pi are represented as:
"01100100100" => 011.00100100 => +3.14
"10011011100" => 100.11011100 => - 3.14
'''

import click
import sys

# Representation parameters  
data_width = 16 
integer_width = 2

# Calculation of various paramters
sign_width = 1
fractional_width = data_width - integer_width - sign_width

# Definig some variables
expontent_msb = integer_width - 1
exponent_lsb = -fractional_width
exponent_lsb_range_max = exponent_lsb - 1

@click.command()
def convert():
    """Tool to convert floating point numbers to its XQN bit representation"""

    # Data input
    for input_value in map(float, sys.stdin.read().split()):
        bits = []
        if (input_value > 0):
            bits.append('0')
        else:
            bits.append('1')
            input_value = 2 ** integer_width + input_value
        
        approximation = 0
        for i in range(expontent_msb, exponent_lsb_range_max, -1):
            component = 2 ** i
            possible_approximation = approximation + component
            if (possible_approximation <= input_value):
                approximation = possible_approximation
                bits.append('1')
            else:
                bits.append('0')
        
        print(*bits, sep='')

if __name__ == '__main__':
    convert()
