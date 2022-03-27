from PyGUI import PyGUI
import os
import platform
import WriteToInputFile
import re
import pandas as pandas
import Objects

# TODO: Things Needed to Be Done
#       - Update where the file we're opening to be a selected file from the GUI rather than my test file
#       - Possibly take the file path given rather than just file name
#       - Update CLASP for Windows devices
#       - Convert numbers back to attributes after CLASP solves problem
#       - Create feasible objects from hard constraints
#       - This will take a file for hard constraints, another for attributes and another for logic
#       -

# TODO: Notes
#       - We do not convert penalty and possibilistic logic to CNF
#       - Take hard constraint and make feasible objects, from there apply penalty and possibilistic logic on those
#         objects

def main():

    statement_count = 0
    input_dict = {
        'attributes': [],
        'hard_constraints': [],
        'penalty_logic': [],
        'possibilistic_logic': [],
        'qualitative_choice_logic': []
    }

    # Open Files
    attr = Objects.Attributes('Attributes.txt')
    input_dict['attributes'] = attr.readAttributes()

    hard_constraint_file = open('HardConstraintInput.txt', 'r')
    hard_constraint = hard_constraint_file.read()
    input_dict['hard_constraints'] = hard_constraint.split('\n')


    # attributes_text_file = open('Attributes.txt', 'r')
    # attributes_listed = attributes_text_file.read()
    # attributes_split_by_type = attributes_listed.split('\n')
    #
    # for index in attributes_split_by_type:
    #     attributes_split_from_type.append(index.split(': '))
    #
    # for index in range(len(attributes_split_from_type)):
    #     input_dict['attributes']['Type'].append(attributes_split_from_type[index][0])
    #     input_dict['attributes']['Attribute_List'].append(attributes_split_from_type[index][1])


    # input_dict['attributes']['Attribute_List'][0].split(', ')



    # for index in range(attr.numberOfAttributeTypes()):
    #     input_dict['attributes'].append()



    attribute_dict = convertAttributesToNumbers(input_dict['attributes'])
    WriteToInputFile.writeToTheFile(attribute_dict, statement_count)
    test2_file = 'CNF.txt'

    if platform.system() == "Darwin":
        os.system("clasp " + test2_file + " -n 2 > TEST.txt")
    else:
        os.system("clasp " + test2_file + " -n 2 > TEST.txt")

    myPyGUI = PyGUI()


def convertAttributesToNumbers(attributes):
    attribute_number_list = []
    attribute_list = []
    attribute_count = 0

    # Converting attributes to one list without their types
    for index in range(len(attributes)):
        attribute_list.append(attributes[index][1])
        attribute_list.append(attributes[index][2])

    # Converting attributes to their digit form for CLASP
    for index in range(len(attribute_list)):

        match attribute_list[index]:
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



main()