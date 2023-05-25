#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    swapped_case_words = [word.swapcase() for word in reversed_words]
    reversed_sentence = ' '.join(swapped_case_words)
    return reversed_sentence
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = raw_input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
