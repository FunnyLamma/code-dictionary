import json
import time
from datetime import datetime


def start():
    
    current_time = datetime.now()
    print("Welecome")
    print("It is currently", current_time)
    catagor_laung = input("What catagory do you want?")
    print("There is,")
    print("Python (py)")
    print("Javascript (js)")
    print("Ruby (rb)")
    print("Typescript (ts)")
    if catagor_laung == "py":
        print("Welecome to the python defenition directory!")
        print("Page 1")
        print("1. If Loops")
        print("2. While Loops")
        print("3. Classes")
        print("4. Booleans")
        print("5. Strings")
        print("6. The Time Module")
        print("7. The OS module")
        print("8. The JSON module")
        print("9. Modules")
        print("10. Next Page")
        num_check1 = input("Which definition do you want?")
        if num_check1 == 1:
            with open('data/python/ifloopdef.text') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 2:
            with open('data/python/whileloopdef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 3:
            with open('data/python/classdef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 4:
            with open('data/python/booleandef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 5:
            with open('data/python/stringdef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 6:
            with open('data/python/timemoddef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 7:
            with open('data/python/osmoddef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 8:
            with open('data/python/jsonmoddef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 9:
            with open('data/python/moduledef.txt') as example_file:
                example_text = example_file.read()
                print(example_text)
        if num_check1 == 10:
            def pypage2():
                print("Page 2")
                print("1. Format")
                print("2. With Statement")
                print("3. The Datetime Module")
                print("10. Next Page")
                num_check4 = input("Which definition do you want?")
                if num_check4 == 1:
                    with open('data/python/pyformat.txt') as example_file:
                        example_text = example_file.read()
                        print(example_text)
                if num_check4 == 2:
                    with open('data/python/withstate.txt') as example_file:
                        example_text = example_file.read()
                        print(example_text)
                if num_check4 == 3:
                    with open('data/python/datetimemod.txt') as example_file:
                        example_text = example_file.read()
                        print(example_text)                  
                if num_check4 == 4:
                    with open('data/python/discordbot.txt') as example_file:
                        example_text = example_file.read()
                        print(example_text)  
            pypage2()
            
                
    if catagor_laung == "js":
        print("Welecome to the javascript defenition directory!")
    if catagor_laung == "rb":
        print("Welecome to the ruby defenitiom directory!")
        print("Page 1")
        print("1. Format")
        num_check2 = input("What defenition do you want?")
        if num_check2 == 1:
            with open('data/ruby/rubyformatdef.text') as example_file:
                example_text = example_file.read()
                print(example_text)
    if catagor_laung == "ts":
        print("Welecome to the typecript defenition directory!")
    if catagor_laung == "ot":
        print("Welecome to the other defenition directory!")
        num_check3 = input("What defenition do you want?")
        if num_check3 == 1:
            with open('data/other/rubyvspython.text') as example_file:
                example_text = example_file.read()
                print(example_text)
    if catagor_laung == "qu":
        print("Welecome to the questions directory.")
start()