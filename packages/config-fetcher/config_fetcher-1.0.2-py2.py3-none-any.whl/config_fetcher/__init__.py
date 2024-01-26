import os.path

__author__ = "Alexandre Collin-Betheuil"
__copyright__ = "Copyright 2024 / Inetum / CD 13"
__credits__ = ["Alexandre Collin-Betheuil"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alexandre Collin-Betheuil"
__email__ = "alexandre.et.collin@gmail.com"
__status__ = "Production"

class _ConfigValue:
    __value = None
    __rawValue = None

    def __init__(self, rawValue):
        self.__value = rawValue
        self.__rawValue = rawValue

    def get_raw_value(self):
        if self.__rawValue == None:
            return self.__value
        return self.__rawValue

    def get_value(self):
        return self.__value

    def get_variables(self):
        variables = []
        i = self.__value.find('{{')
        while i != -1:
            variables.append(self.__value[i + 2:self.__value.find('}}', i + 2)])
            i = self.__value.find('{{', i + 1)
        return variables

    def has_variable(self):
        return self.__value.find('{{') != -1
    
    def replace_variable(self, variable, value):
        self.__value = self.__value.replace('{{' + variable + '}}', value)
    
    
class ConfigFetcher:
    __values = {}
    __defaultSection = 'global'

    def __init__(self, filePath, defaultSectionName = 'global'):
        if not os.path.isfile(filePath):
            raise IOError('File not found: ' + filePath)
        self.__defaultSection = defaultSectionName
        content = self._read_file(filePath)
        self._parse_file(content)
        self._replace_variables()

    def _replace_variables(self):
        for sectionName in self.__values:
            self._replace_variable_in_section(self.__values[sectionName])
        if self._is_there_variable() == True:
            self._replace_variables()
    
    def _is_there_variable(self):
        for sectionName in self.__values:
            section = self.__values[sectionName]
            for key in section:
                if section[key].has_variable() == True:
                    return True
        return False

    def _replace_variable_in_section(self, section):
        for key in section:
            variables = section[key].get_variables()
            for variable in variables:
                self._replaceVariable(section, key, variable)

    def _replaceVariable(self, section, key, variable):
        stripedVariable = variable.strip()
        if stripedVariable in section:
            self._replace_variableByValue(section, key, variable, section, stripedVariable)
        elif stripedVariable in self.__values[self.__defaultSection]:
            self._replace_variableByValue(section, key, variable, self.__values[self.__defaultSection], stripedVariable)
        elif '.' in stripedVariable:
            splited = stripedVariable.split('.', 1)
            if splited[0] not in self.__values or splited[1] not in self.__values[splited[0]]:
                raise IOError('Variable not found: ' + stripedVariable)
            self._replace_variableByValue(section, key, variable, self.__values[splited[0]], splited[1])
        else:
            raise IOError('Variable not found: ' + variable)

    def _replace_variableByValue(self, destSection, destKey, variable, sourceSection, sourceKey):
        destSection[destKey].replace_variable(variable, sourceSection[sourceKey].get_value())

    def _parse_file(self, content):
        sectionName = self.__defaultSection
        lines = content.split('\n')
        for line in lines:
            line = line.strip()
            if line == '':
                continue
            if line[0] == '#':
                continue
            if line[0] == '[' and line[-1] == ']':
                sectionName = line[1:-1].strip()
                continue
            if '=' not in line:
                continue
            key, value = line.split('=', 1)
            if sectionName not in self.__values:
                self.__values[sectionName] = {}
            self.__values[sectionName][key.strip()] = _ConfigValue(value.strip())

    def _read_file(self, filePath):
        f = open(filePath, 'r')
        content = f.read()
        f.close()
        return content
    
    def get_formated_values(self):
        values = ''
        for section in self.__values:
            values += '[' + section + ']' + '\n'
            for key in self.__values[section]:
                values += key + '=' + self.__values[section][key].get_value() + '\n'
            values += '\n'
        values = values[:-2]
        return values

    def print_values(self):
        print(self.get_formated_values())

    def get_value(self, section, key):
        return self.__values[section][key].get_value()
    
    def get_raw_value(self, section, key):
        return self.__values[section][key].get_raw_value()

    def has_option(self, section, key):
        return section in self.__values and key in self.__values[section]
    
    def save(self, filePath):
        f = open(filePath, 'w')
        f.write(self.get_formated_values())
        f.close()
