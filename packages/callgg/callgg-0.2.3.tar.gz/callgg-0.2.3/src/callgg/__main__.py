#!/usr/bin/env python3

__version__="0.2.3"

def __main__():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument("connector", help="choose a connector: c, cpp, g, gpp; or menu")
    args = parser.parse_args()
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
    elif args.connector=="menu":
        # from .gpp import *
        from gguf_connector import menu
    # print("in __main__ sub-module/function")
