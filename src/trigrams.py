# -*- coding: utf-8 -*-
"""Trigrams.py generates pseudo random text outputgiven a large
text file input.
"""

import io
import re
import random
import sys


def pull_in_file(filename):
    """Read the text from the filename it's given."""
    file = io.open(filename)
    content = file.read()
    file.close()
    return content


# Slight Edit by Mike. Removed ? and ! from being subbed.
def find_and_replace_specials(content):
    """Function replaces special characters with whitespace."""
    return re.sub('[-\\()@#$%^&*;"<>|/1234567890_=+:]', ' ', content)


def create_tuples(t):
    """Function creates tuples from file data."""
    return zip(t, t[1:], t[2:])


def generate_dictionary(tuples):
    """Function generates a dictionary from our tuples."""
    d = {}
    for a, b, value in tuples:
        d.setdefault((a, b), []).append(value)
    return d


def process_file(filename):
    """Function calls above functions in order to process the file into a
    dictionary for use in following functions.
    """
    s = find_and_replace_specials(pull_in_file(filename))
    return generate_dictionary(create_tuples(s.split()))


# Edited by Mike
def pick_first_two_words(dictionary):
    """Function picks random starting word with cap if possible."""
    for key in dictionary:
        if key[0][0].istitle():
            return key
    else:
        return random.choice(list(dictionary))


def generate_sentence(dictionary, length):
    """Function generates a sentence of 'length' length and returns it."""
    result = ""
    word1, word2 = pick_first_two_words(dictionary)
    for i in range(length):
        result += '{} '.format(word1)
        possible_words = dictionary.get((word1, word2), False)
        if possible_words:
            word1, word2 = word2, random.choice(possible_words)
        else:
            word1, word2 = pick_first_two_words(dictionary)
    return result


def main():
    """Main function, calls all others."""
    if len(sys.argv) >= 3:
        try:
            arg1 = sys.argv[1]
            arg2 = int(sys.argv[2])
            print(generate_sentence(process_file(arg1), arg2))
        except ValueError:
            print('User supplied invalid length argument.')


if __name__ == '__main__':
    main()
