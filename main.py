from PyGUI import PyGUI
import os
import platform
import Objects
import re as regular_expression

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
    # Holding all necessary words and logic for output to user
    input_dict = {
        'attributes': {
            'words': [],
            'numbers': []
        },
        'hard_constraints': {
            'stmts': [],
            'numbers': [],
            'clasp_ready_stmts': [],
            'constraint_statement': ''
        },
        'penalty_logic': {
            'logic_stmts': [],
            'penalty': [],
            'stmts_as_numbers': [],
            'clasp_ready_stmts': []
        },
        'possibilistic_logic': {
            'logic_stmts': [],
            'tolerance': [],
            'stmts_as_numbers': [],
            'clasp_ready_stmts': []
        },
        'qualitative_choice_logic': [],
        'clasp_ready_stmts': []
    }

    # Will hold same values as input_dict, but as numbers for clasp
    number_dict = {
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
    input_dict['attributes']['words'] = attr.readAttributes()


    # Opening hard constraints file and manipulating string inside
    hard_constraint_file = open('HardConstraintInput.txt', 'r')
    hard_constraint = hard_constraint_file.read()
    input_dict['hard_constraints']['stmts'] = hard_constraint.split('\n')
    ConvertConstraintsToNumbers(input_dict)

    for index in range(len(input_dict['hard_constraints']['numbers'])):
        for logic in input_dict['hard_constraints']['numbers'][index]:
            if logic == 'NOT':
                input_dict['hard_constraints']['numbers'][index].remove(logic)

    for outer_index in range(len(input_dict['hard_constraints']['numbers'])):
        string = ''
        for index in range(len(input_dict['hard_constraints']['numbers'][outer_index])):
            string += str(input_dict['hard_constraints']['numbers'][outer_index][index])
        string += ' 0'
        input_dict['hard_constraints']['clasp_ready_stmts'].append(string)
        input_dict['hard_constraints']['constraint_statement'] += \
            input_dict['hard_constraints']['clasp_ready_stmts'][outer_index] + '\n'
    input_dict['hard_constraints']['clasp_ready_stmts'].remove(input_dict['hard_constraints']['clasp_ready_stmts']
                                                               [len(input_dict['hard_constraints']
                                                                    ['clasp_ready_stmts']) - 1])


    # Breaking down logic files to get input ready for clasp
    breakDownLogicFile('Logic.txt', input_dict)

    # Converting words to numbers for clasp
    statement_count = logicStatementConvertToNumbers(input_dict)

    # Removing 'NOT' from logic statements
    for index in range(len(input_dict['penalty_logic']['stmts_as_numbers'])):
        for logic in input_dict['penalty_logic']['stmts_as_numbers'][index]:
            if logic == 'NOT':
                input_dict['penalty_logic']['stmts_as_numbers'][index].remove(logic)


    for outer_index in range(len(input_dict['penalty_logic']['stmts_as_numbers'])):
        string = ''
        for index in range(len(input_dict['penalty_logic']['stmts_as_numbers'][outer_index])):
            string += str(input_dict['penalty_logic']['stmts_as_numbers'][outer_index][index])
        string += ' 0'
        input_dict['penalty_logic']['clasp_ready_stmts'].append(string)

    # TODO: Remove when ready
# ----------------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------

    # input_dict['attributes']['Attribute_List'][0].split(', ')



    # for index in range(attr.numberOfAttributeTypes()):
    #     input_dict['attributes'].append()


    # Converting attributes to numbers as needed
    input_dict['attributes']['numbers'] = convertAttributesToNumbers(input_dict['attributes']['words'])

    # Writing to file that will be sent to clasp
    writeToTheFile(input_dict)

    # Naming file that will be sent to clasp
    test2_file = 'CNF.txt'

    if platform.system() == "Darwin":
        os.system("clasp " + test2_file + " -n 0 > CLASPOutput.txt")
    else:
        os.system("clasp " + test2_file + " -n 0 > CLASPOutput.txt")

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

    return attribute_number_list
# ----------------------------------------------------------------------------------------------------------------------

def logicStatementConvertToNumbers(input_dict):
    statement_split_list = []
    for index in range(len(input_dict['penalty_logic']['logic_stmts'])):
        statement_split_list.append(input_dict['penalty_logic']['logic_stmts'][index].split(' '))

    for outer_index in range(len(input_dict['penalty_logic']['logic_stmts'])):

        for inner_index in range(len(statement_split_list[outer_index])):
            match statement_split_list[outer_index][inner_index]:
                case "salad":
                    salad = 1
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -salad
                    else:
                        statement_split_list[outer_index][inner_index] = salad
                case "soup":
                    soup = -1
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -soup
                    else:
                        statement_split_list[outer_index][inner_index] = soup
                case "fish":
                    fish = 2
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -fish
                    else:
                        statement_split_list[outer_index][inner_index] = fish
                case "beef":
                    beef = -2
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -beef
                    else:
                        statement_split_list[outer_index][inner_index] = beef
                case "wine":
                    wine = 3
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -wine
                    else:
                        statement_split_list[outer_index][inner_index] = wine
                case "beer":
                    beer = -3
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -beer
                    else:
                        statement_split_list[outer_index][inner_index] = beer
                case "cake":
                    cake = 4
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -cake
                    else:
                        statement_split_list[outer_index][inner_index] = cake
                case "ice-cream":
                    ice_cream = -4
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -ice_cream
                    else:
                        statement_split_list[outer_index][inner_index] = ice_cream
                case "OR":
                    statement_split_list[outer_index][inner_index] = ' '
                case "AND":
                    statement_split_list[outer_index][inner_index] = ' 0\n'
    input_dict['penalty_logic']['stmts_as_numbers'] = statement_split_list

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


def writeToTheFile(input_dict):
    test_file = open("CNF.txt", "w")
    test_file.write('c\n' + 'c This is a test file for CLASP\n' + 'c\n' + 'p cnf '
                    + str(len(input_dict['attributes']['words'])) +
                    ' ' + str(len(input_dict['hard_constraints']['numbers'])) + ' \n' +
                    input_dict['hard_constraints']['constraint_statement'])
    return test_file
# ---------------------------------------------------------------------------------------------------------------------


def ConvertConstraintsToNumbers(input_dict):
    statement_split_list = []
    for index in range(len(input_dict['hard_constraints']['stmts'])):
        statement_split_list.append(input_dict['hard_constraints']['stmts'][index].split(' '))
    # print(statement_split_list)

    for outer_index in range(len(statement_split_list)):

        for inner_index in range(len(statement_split_list[outer_index])):
            match statement_split_list[outer_index][inner_index]:
                case "salad":
                    salad = 1
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -salad
                    else:
                        statement_split_list[outer_index][inner_index] = salad
                case "soup":
                    soup = -1
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -soup
                    else:
                        statement_split_list[outer_index][inner_index] = soup
                case "fish":
                    fish = 2
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -fish
                    else:
                        statement_split_list[outer_index][inner_index] = fish
                case "beef":
                    beef = -2
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -beef
                    else:
                        statement_split_list[outer_index][inner_index] = beef
                case "wine":
                    wine = 3
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -wine
                    else:
                        statement_split_list[outer_index][inner_index] = wine
                case "beer":
                    beer = -3
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -beer
                    else:
                        statement_split_list[outer_index][inner_index] = beer
                case "cake":
                    cake = 4
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -cake
                    else:
                        statement_split_list[outer_index][inner_index] = cake
                case "ice-cream":
                    ice_cream = -4
                    if statement_split_list[outer_index][inner_index - 1] == 'NOT':
                        statement_split_list[outer_index][inner_index] = -ice_cream
                    else:
                        statement_split_list[outer_index][inner_index] = ice_cream
                case "OR":
                    # statement_count += 1
                    statement_split_list[outer_index][inner_index] = ' '
                case "AND":
                    # statement_count += 1
                    statement_split_list[outer_index][inner_index] = ' 0\n'
    input_dict['hard_constraints']['numbers'] = statement_split_list
    # return statement_count
# ---------------------------------------------------------------------------------------------------------------------

main()

