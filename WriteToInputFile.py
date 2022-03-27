def writeToTheFile(attribute_dict, statement_count):
    test_file = open("CNF.txt", "w")
    test_file.write('c\n' + 'c This is a test file for CLASP\n' + 'c\n' + 'p cnf ' + str(attribute_dict['count']) +
                    ' ' + str(statement_count) + ' \n1 0\n3 0\n')
    return test_file