
class Attributes:
    def __init__(self, file_name):
        self.file_name = file_name
        self.attribute_number = 0
        self.attribute_type = ''
        self.option_1 = ''
        self.option_2 = ''


    def openFile(self):
        return open(self.file_name, 'r')


    def numberOfAttributeTypes(self):
        return len(self.openFile().read().split('\n'))


    def readAttributes(self):
        attributes_split_from_type = []
        individual_attributes = []
        attribute_objects = []
        attribute_type = []

        attributes_split_by_type = self.openFile().read().split('\n')
        # attributes_split_by_type = attributes_listed.split('\n')

        for index in range(len(attributes_split_by_type)):
            attributes_split_from_type.append(attributes_split_by_type[index].split(': '))
            attribute_type.append(attributes_split_from_type[index][0])

            individual_attributes.append(attributes_split_from_type[index][1].split(', '))

            attribute_objects.append([attribute_type[index],
                                      individual_attributes[index][0], individual_attributes[index][1]])

        return attribute_objects






