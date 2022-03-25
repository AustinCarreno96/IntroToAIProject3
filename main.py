from PyGUI import PyGUI
import os


def main():
    os.system("clasp ~/try1.cnf -n 4 > TEST.txt")
    myPyGUI = PyGUI()

if __name__ == "__main__":
    main()