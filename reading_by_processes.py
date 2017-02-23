# -*- coding: utf-8 -*-
from multiprocessing import Pool, current_process
# import os

__author__ = "Ilya Konon"
__email__ = "ilya.konon.95@gmail.com"

"""
Create two process and organize them to share data from the data.txt file.
Your task is to output the line of data.txt using two processes without disturbing the order of the lines.
"""

filename = "data.txt"


def process_wrapper(lineByte):
    with open(filename, 'rb') as file:
        file.seek(lineByte)
        # print("Current process - %s\n" % os.getpid())
        # print("Current process - %s\n" % current_process().name)
        output_line = file.readline()
        return output_line


if __name__ == '__main__':
    # init objects
    pool = Pool(processes=2)  # create 2 processes
    jobs = []

    # create jobs
    with open(filename, 'rb') as f:
        nextLineByte = f.tell()
        for line in f:
            jobs.append(pool.apply_async(process_wrapper, (nextLineByte,)))
            nextLineByte = f.tell()

    # wait for all jobs to finish
    for job in jobs:
        print(job.get().decode('utf-8').rstrip())

    # clean up
    pool.close()
