from PyGUI import PyGUI
import os
import platform
import WriteToInputFile

# TODO: Things Needed to Be Done
#       - Update where the file we're opening to be a selected file from the GUI rather than my test file
#       - Possibly take the file path given rather than just file name
#       - Update CLASP for Windows devices
#       - Convert numbers back to attributes after CLASP solves problem
#       - Create feasible objects from hard constraints

# TODO: Notes
#       - We do not convert penalty and possibilistic logic to CNF
#       - Take hard constraint and make feasible objects, from there apply penalty and possibilistic logic on those
#         objects

def main():
    statement_count = 0
    with open('testInput.txt', 'r') as test_file:
        for line in test_file:
            attributes = line.split(' OR ')
            statement_count += 1

    attribute_dict = convertAttributesToNumbers(attributes)
    WriteToInputFile.writeToTheFile(attribute_dict, statement_count)
    test_file = 'try2.txt'

    if platform.system() == "Darwin":
        os.system("clasp " + test_file + " -n 2 > TEST.txt")
    else:
        os.system("clasp " + test_file + " -n 2 > TEST.txt")

    myPyGUI = PyGUI()


def convertAttributesToNumbers(attributes):
    attribute_number_list = []
    attribute_count = 0


    for attribute in attributes:
        match attribute:
            case "salad":
                attribute_number_list.append(1)
            case "soup":
                attribute_number_list.append(-1)
            case "fish":
                attribute_number_list.append(2)
            case "beef":
                attribute_number_list.append(-2)
            case "wine":
                attribute_number_list.append(3)
            case "beer":
                attribute_number_list.append(-3)
            case "cake":
                attribute_number_list.append(4)
            case "ice-cream":
                attribute_number_list.append(-4)
        attribute_count += 1

    attribute_dict = {
        'count': attribute_count,
        'list': attribute_number_list
    }

    return attribute_dict



if __name__ == "__main__":
    main()