from PyGUI import PyGUI
import os
import platform
import WriteToInputFile
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
        'penalty_logic': {
            'logic_stmts': [],
            'penalty': []
        },
        'possibilistic_logic': {
            'logic_stmts': [],
            'tolerance': []
        },
        'qualitative_choice_logic': []
    }

    # Open Files
    attr = Objects.Attributes('Attributes.txt')
    input_dict['attributes'] = attr.readAttributes()

    hard_constraint_file = open('HardConstraintInput.txt', 'r')
    hard_constraint = hard_constraint_file.read()
    input_dict['hard_constraints'] = hard_constraint.split('\n')

    breakDownLogicFile('Logic.txt', input_dict)
    logicStatementConvertToNumbers(input_dict)

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
    WriteToInputFile.writeToTheFile(attribute_dict, len(input_dict['hard_constraints']))
    test2_file = 'CNF.txt'

    if platform.system() == "Darwin":
        os.system("clasp " + test2_file + " -n 10 > ClaspOutput.txt")
    else:
        os.system("clasp " + test2_file + " -n 10 > ClaspOutput.txt")

    PyGUI(input_dict)
# ----------------------------------------------------------------------------------------------------------------------


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
# ----------------------------------------------------------------------------------------------------------------------

def logicStatementConvertToNumbers(input_dict):
    test = []
    test2 = []
    for index in range(len(input_dict['penalty_logic']['logic_stmts'])):
        test.append(input_dict['penalty_logic']['logic_stmts'][index].split(' '))
# ----------------------------------------------------------------------------------------------------------------------


def breakDownLogicFile(file_name, input_dict):
    p_logic_statements = []
    poss_logic_statements = []
    qual_logic_statements = []

    plogic_plit_from_p = []
    poss_logic_plit_from_t = []


    file = open(file_name, 'r')
    file = file.read()
    file = file.replace('\n', ';')
    broken_by_logic_type = file.split(';;')

    penalty_logic = broken_by_logic_type[0]
    possibilistic_logic = broken_by_logic_type[1]
    qualitative_choice_logic = broken_by_logic_type[2]


    penalty_logic = penalty_logic.split(':')

    for index in range(len(penalty_logic)):
        p_logic_statements = penalty_logic[index].split(';')

    p_logic_statements.remove(p_logic_statements[0])

    for index in range(len(p_logic_statements)):
        plogic_plit_from_p.append(p_logic_statements[index].split(','))
        input_dict['penalty_logic']['logic_stmts'].append(plogic_plit_from_p[index][0])
        input_dict['penalty_logic']['penalty'].append(int(plogic_plit_from_p[index][1]))


    poss_logic = possibilistic_logic.split(':')

    for index in range(len(poss_logic)):
        poss_logic_statements = poss_logic[index].split(';')

    poss_logic_statements.remove(poss_logic_statements[0])

    for index in range(len(poss_logic_statements)):
        poss_logic_plit_from_t.append(poss_logic_statements[index].split(','))
        input_dict['possibilistic_logic']['logic_stmts'].append(poss_logic_plit_from_t[index][0])
        input_dict['possibilistic_logic']['tolerance'].append(float(poss_logic_plit_from_t[index][1]))


    qual_statements = qualitative_choice_logic.split(':')

    for index in range(len(qual_statements)):
        qual_logic_statements = (qual_statements[index].split(';'))

    qual_logic_statements.remove(qual_logic_statements[0])
    input_dict['qualitative_choice_logic'] = qual_logic_statements
# ----------------------------------------------------------------------------------------------------------------------


main()