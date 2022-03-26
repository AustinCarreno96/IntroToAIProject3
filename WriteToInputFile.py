


def writeToTheFile(attribute_dict, statement_count):
    test_file = open("try2.txt", "w")
    test_file.write('c\n' + 'c This is a test file for CLASP\n' + 'c\n' + 'p cnf ' + str(attribute_dict['count']) +
                    ' ' + str(statement_count) + ' \n' + str(attribute_dict['list'][0]) + ' ' +
                    str(attribute_dict['list'][1]) + ' 0\n')
    return test_file