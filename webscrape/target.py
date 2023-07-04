import os

def getTarget() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(dir_path + "\\target.txt", "r") as fh:
            return fh.readline()
    except FileNotFoundError:
        return input("No target file found write your search target: ")