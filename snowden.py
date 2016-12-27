import sys
import re
__author__ = 'gambrinius'

"""
Edward Snowden knows that NSA agents use the following algorithm to cypher their messages.

1) They delete all spaces and punctuation marks.
2) They replace all successive identical letters by one such letter.
3) They insert two identical letters at an arbitrary place many times.

Snowden has intercepted some messages which are "meaningless" sequences of letters that NSA agent Bob has sent to other NSA agent Alice about possible Snowden's location. He wants to be able to restore the message as it was after step 2). Help Snowden write a program in Python that removes all pairs of identical letters from the message inserted at the third step.

The program should be executed by calling 'python snowden.py cipheredmessage.txt' where "cipheredmessage.txt" is a file with a ciphered message sent by Bob. The message consists of lowercase English letters and its length is at most 100 000. Output the message after step 2). The program should produce an answer in less than a few seconds.

Example
Execute: python snowden.py somefile.txt
somefile.txt: wwsndaadowffdennn
Output: snowden
"""


def replacer(process_line, r):
    result = process_line.replace(r+r, '')
    return result


def decrypt(line):
    """
    This function decrypt messages for Snowden
    :param line:
    :return: message
    """
    pattern = re.compile(r'([a-z])\1')
    find_results = pattern.findall(line)
    for result in find_results:
        line = replacer(line, result)

    if not find_results:
        return line
    else:
        return decrypt(line)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'r') as input_file:
            ciphered_message = input_file.readlines()
            decrypt_line = str()
            result_message = list()
            for input_line in ciphered_message:
                decrypt_line = (decrypt(input_line))
                result_message.append(decrypt_line)
                print(decrypt_line)
    else:
        print("Missed argument - name of text file")
