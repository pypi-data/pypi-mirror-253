# !/usr/bin/env python3

__version__="0.3.6"

def __main__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument("connector", help="choose a connector: c, cpp, g, gpp; or m (menu)")
    # parser.add_argument("cpp", help="cpp connector with GUI")
    # parser.add_argument("c", help="c connector with GUI")
    # parser.add_argument("gpp", help="gpp connector with CLI")
    # parser.add_argument("g", help="c connector with CLI")
    args = parser.parse_args()
    if args.connector=="m":
        from gguf_connector import menu
    if args.connector=="c":
        # from .c import *
        from gguf_connector import c
    elif args.connector=="cpp":
        # from .cpp import *
        from gguf_connector import cpp
    elif args.connector=="g":
        # from .g import *
        from gguf_connector import g
    elif args.connector=="gpp":
        # from .gpp import *
        from gguf_connector import gpp
    # print("in __main__ function")

# print("Please select a connector:\n1. llama.cpp\n2. ctransformers")
# choice = input("Enter your choice (1 to 2): ")

# if choice=="1":
#     from .cpp import *
# elif choice=="2":
#     from .c import *
# else:
#     print("Not a valid number.")