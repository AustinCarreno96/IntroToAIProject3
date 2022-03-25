from PyGUI import PyGUI
import os
import platform


def main():
    if platform.system() == "Darwin":
        os.system("clasp ~/try1.cnf -n 4 > TEST.txt")
    else:
        print("Need file path for CLASP")

    myPyGUI = PyGUI()

if __name__ == "__main__":
    main()