# !/usr/bin/env python3

__version__="0.3.8"

def __init__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument("connector", help="choose a connector: c, cpp, g, gpp; or m (menu)")
    args = parser.parse_args()
    if args.connector=="m":
        from gguf_connector import menu
    if args.connector=="c":
        from gguf_connector import c
    elif args.connector=="cpp":
        from gguf_connector import cpp
    elif args.connector=="g":
        from gguf_connector import g
    elif args.connector=="gpp":
        from gguf_connector import gpp
    # print("in __init__ function")