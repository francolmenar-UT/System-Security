import os
import time

def test_handle(test_list):
    """
    Receives the list with the tests to execute from the cli
    Calls the switch which calls to the methods of each test

    :param test_list: List with all the tests to run
    :return:
    """

    for test in test_list:
        switch(test)


def switch(x):
    """
    Switch implementation
    Calls to the methods for each test

    :param x: Element to consider
    :return: Case in x
    """
    return {
        '1': test_1(),
        '2': "",
    }[x]


def test_1():
    os.system("./assess 50")
    os.system("0")
