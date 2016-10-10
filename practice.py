"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    # single_words = []

    # for word in words:
    #     if word not in single_words:
    #         single_words.append(word)

    word_counter = {}
    single_words = []

    for word in words:
        if word not in word_counter:
            word_counter[word] = 0
        word_counter[word] += 1

    for word in word_counter:
        single_words.append(word)

    return single_words


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """

    # common_items = []

    # for item1 in items1:
    #     for item2 in items2:
    #         if item1 == item2:
    #             common_items.append(item1)

    # common_items = sorted(common_items)

    # for index in range(0, len(common_items)-2):
    #     if common_items[index] == common_items[index+1]:
    #         common_items.pop(index)

    # common_items = {}
    # list_o_common_items = []
    common_items = set()

    for item1 in items1:
        for item2 in items2:
            if item1 == item2:
                common_items.add(item1)
    #             if item1 not in common_items:
    #                 common_items[item1] = 0
    #             common_items[item1] += 1

    # for item in common_items:
    #     list_o_common_items.append(item)

    # return list_o_common_items
    return list(common_items)


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    sum_zero_pairs = []
    # sum_zero_pairs = {}
    # unique_zero_pairs = []

    for number in numbers:
        for index in range(0, len(numbers)-1):
            if number == 0:
                sum_zero_pairs.append([0,0])
            elif number + numbers[index] == 0:
                # pair = set([number, numbers[index]])
                sum_zero_pairs.append(sorted([number, numbers[index]]))
                # if pair not in sum_zero_pairs:
                #     sum_zero_pairs[pair] = 0
                # sum_zero_pairs[pair] += 1

    # sum_zero_pairs = sorted(sum_zero_pairs)

    # for index in range(0, len(sum_zero_pairs)-2):
    #     if sum_zero_pairs[index] == sum_zero_pairs[index+1]:
    #         sum_zero_pairs.pop(index)

    unique_zero_pairs = []

    for pair in sum_zero_pairs:
        if pair not in unique_zero_pairs:
            unique_zero_pairs.append(pair)

    # for pair in sum_zero_pairs:
    #     unique_zero_pairs.append(pair)

    return unique_zero_pairs


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    phrase = phrase.replace(" ", "")

    chars_counter = {}

    for letter in phrase:
        if letter not in chars_counter:
            chars_counter[letter] = 0
        chars_counter += 1

    # Not sure how to go about choosing the key that has the highest value.
    # How to compare the keys.

    return []

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
