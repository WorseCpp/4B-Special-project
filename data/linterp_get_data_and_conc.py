import numpy as np

import sys

def main(file):
    data = open(file, "r").read().split("\n")

if __name__ == "__main__":
    if (sys.argc != 2):
        print("Please give one argument!")
    else:
        main(sys.argv[1])
    