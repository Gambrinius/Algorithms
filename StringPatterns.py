import sys
__author__ = 'gambrinius'


def all_combinations(S, combinations):
    """
    The function find all combinations(string patterns)
    for input string.
    :param S:
    :param combinations:
    :return: modified input list (add combinations)
    """
    if len(S) < 1:
        return 0

    j = int()
    for j in range(len(S)):
        combinations.append(S[0: j + 1])

    all_combinations(S[1: j+1], combinations)


def count_overlapping_substrings(string, substring):
    """
    The function counts the number of occurrences
    of a substring in a string.
    :param string:
    :param substring:
    :return: count
    """
    count = 0
    i = -1
    while True:
        i = string.find(substring, i+1)
        if i == -1:
            return count
        count += 1


def sort_by_length(string):
    """
    The function sorts the list by string length.
    :param string:
    :return: length of string
    """
    return len(string)


def string_patterns(S):
    """
    The main function, finding string patterns.
    :param S:
    :return: list of unique combinations
    """
    array = list()  # list for storing all combinations
    all_combinations(S, array)  # find all combinations for string
    unique_combinations = list()    # list for storing result combinations

    for element in set(array):  # delete repeat combinations and single characters
        if len(element) != 1 and count_overlapping_substrings(S, element) >= 2:  # check conditions
            unique_combinations.append(element)
    unique_combinations.sort(key=sort_by_length, reverse=True)

    if len(unique_combinations) != 0:
        return unique_combinations
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
            try:
                input_file = open(sys.argv[1], 'r')
                test_cases = input_file.readlines()

                for test in test_cases:
                    print(string_patterns(test))
                    print("-----")
                input_file.close()
            except IOError:
                print('Can\'t open this file', sys.argv[1])
    else:
        print("Missed argument - name of text file")
