# -*- coding: utf-8 -*-
"""Here we test our functions from trigrams.py."""
import pytest

GENERATE_SENTENCE_TEST_TABLE = [
    7,
    4,
    12
]

FAKE_DICT = {
    ('A', 'b'): ['y', 'z'],
    ('Gar', 'bar'): [],
    ('something', 'Germ'): [],
    ('Monty', 'python'): []}

FAKE_DICT2 = {
    ('a', 'b'): ['y', 'z'],
    ('gar', 'bar'): [],
    ('something', 'germ'): [],
    ('monty', 'python'): []}


def test_pull_in_file():
    """Function tests pull_in_file function with test file."""
    from trigrams import pull_in_file
    assert pull_in_file('filetest.txt') == 'this is a test file'


def test_find_and_replace_specials():
    """Test find_and_replace_specials with special characters and text."""
    from trigrams import find_and_replace_specials
    result = find_and_replace_specials('this *-# has *(#$ special @)# chars')
    out = 'this     has      special     chars'
    assert result == out


def test_create_tuples_1():
    """Function tests create_tuples with test data."""
    from trigrams import create_tuples
    input_list = ['hello', 'world', 'test']
    out = [('hello', 'world', 'test')]
    assert list(create_tuples(input_list)) == out


def test_create_tuples_2():
    """Function tests create_tuples with alternative test data."""
    from trigrams import create_tuples
    input_list = ['hello', 'world', 'test', 'tttest']
    out = [('hello', 'world', 'test'), ('world', 'test', 'tttest')]
    assert list(create_tuples(input_list)) == out


def test_generate_dictionary_1():
    """Function tests generate_dictionary with test data."""
    from trigrams import generate_dictionary
    tuples = [('hello', 'world', 'test'), ('world', 'test', 'tttest')]
    assert generate_dictionary(tuples) == {
        ('hello', 'world'): ['test'],
        ('world', 'test'): ['tttest']
    }


def test_generate_dictionary_2():
    """Function tests generate_dictionary with test data."""
    from trigrams import generate_dictionary
    tuples = [
        ('I', 'wish', 'I'),
        ('wish', 'I', 'may'),
        ('I', 'may', 'I'),
        ('may', 'I', 'wish'),
        ('I', 'wish', 'I'),
        ('wish', 'I', 'might')
    ]
    assert generate_dictionary(tuples) == {
        ('I', 'wish'): ['I', 'I'],
        ('wish', 'I'): ['may', 'might'],
        ('may', 'I'): ['wish'],
        ('I', 'may'): ['I']
    }


def test_process_file():
    """Function tests process_file with test data."""
    from trigrams import process_file
    assert process_file('filetest.txt') == {
        ('a', 'test'): ['file'],
        ('is', 'a'): ['test'],
        ('this', 'is'): ['a']
    }


def test_pick_first_two_words():
    """Function tests pick_first_two_words with test data."""
    from trigrams import pick_first_two_words
    assert pick_first_two_words({('word', 'b'): 3}) == ('word', 'b')


@pytest.mark.parametrize('n', GENERATE_SENTENCE_TEST_TABLE)
def test_generate_sentence(n):
    """Function tests generate_sentence with test data."""
    from trigrams import generate_sentence
    d = {
        ('a', 'test'): ['file'],
        ('is', 'a'): ['test'],
        ('this', 'is'): ['a']
    }
    assert len(generate_sentence(d, n).split()) == n
# This area is where Mike is doing some testing.


def test_find_and_replace_specials2():
    """Test find_and_replace_specials with keeping ! ? and periods."""
    from trigrams import find_and_replace_specials
    result = find_and_replace_specials('this$has!special?charas.')
    out = 'this has!special?charas.'
    assert result == out


def test_pick_first_two_words2():
    """Function tests pick_first_two_words with test data."""
    from trigrams import pick_first_two_words
    assert pick_first_two_words({('Word', 'blah'): []}) == ('Word', 'blah')


def test_pick_first_two_words3():
    """Function tests pick_first_two_words correctly gets cap word."""
    from trigrams import pick_first_two_words
    test = pick_first_two_words(FAKE_DICT)
    assert test[0][0].istitle()


def test_pick_first_two_words4():
    """Function tests pick_first_two_words gets words if dict has no caps."""
    from trigrams import pick_first_two_words
    assert pick_first_two_words({('word', 'blah'): []}) == ('word', 'blah')
