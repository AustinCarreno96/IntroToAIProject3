from PyGUI import PyGUI
import os
import platform
import WriteToInputFile



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
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
        os.system("clasp " + test_file + " -n 2 > TEST.txt")
    else:
        print("Need file path for CLASP")

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