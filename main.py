import json
import time
from datetime import datetime

current_time = datetime.now()

def start():
    print("Welecome")
    print(current_time)
    catagor_laung = input("What catagory do you want?")
    if catagor_laung == "py":
        print("Welecome to the python defenition directory!")
        num_check1 = input("Which definition do you want?")
        if num_check1 == 1:
            with open('data/python/ifloopdef.text') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 2:
            with open('data/python/whileloopdef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
    if catagor_laung == "js":
        print("Welecome to the javascript defenition directory!")
    if catagor_laung == "rb":
        print("Welecome to the ruby defenitiom directory!")
        num_check2 = input("What defenition do you want?")
        if num_check2 == 1:
            with open('data/ruby/rubyformatdef.text') as example_file:
                example_text = example_file.read()
                print(example_text)
    if catagor_laung == "ts":
        print("Welecome to the typecript defenition directory!")



start()