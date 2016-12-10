import sys
__author__ = 'gambrinius'


def next_number(number):
    """
    This function find the next number greater than N using the same digits.
    If no permutation is greater, print 0.
    :param number:
    :return: next_biggest_number
    """
    digits_list = [int(i) for i in str(number)]
    for i in reversed(range(len(digits_list))):
        if i == 0:  # when 1 digit or this is the biggest number, which may be composed of these digits
            return 0
        if digits_list[i] > digits_list[i-1]:  # finding index required for separation source number
            break
    left, right = digits_list[:i], digits_list[i:]  # separate to left and right parts
    for k in reversed(range(len(right))):
        if right[k] > left[-1]:  # find the smallest digit from right part larger than last digit of left part
            right[k], left[-1] = left[-1], right[k]  # swap them
            break
    return int("".join(map(str, (left+sorted(right)))))  # formed final number


if __name__ == "__main__":
    if len(sys.argv) > 1:
            try:
                input_file = open(sys.argv[1], 'r')
                test_cases = input_file.readlines()
                for test in test_cases:
                    print(next_number(int(test)))
                    print("-----")
                input_file.close()
            except IOError:
                print('Can\'t open this file', sys.argv[1])
    else:
        print("Missed argument - name of text file")
