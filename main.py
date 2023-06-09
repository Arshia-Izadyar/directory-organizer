import os
from approach1 import organize
from approach2 import organize2

import sys


def scan_dir():
    input_pwd = str(input("Enter a (FULL) Path or Leave empty for executing script on PWD : "))
    if input_pwd == "":
        input_pwd = os.getcwd()
        list = os.listdir(input_pwd)
    else:
        list = os.listdir(input_pwd)
    return list, input_pwd




if __name__ == "__main__":
    file_list, path = scan_dir()
    if sys.argv[1] == "method1":
        organize(file_list, path)
    if sys.argv[1] == "method2":
        organize2(file_list, path)

    else:
        print('no argv')
