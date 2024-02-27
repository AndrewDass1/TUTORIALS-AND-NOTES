import configparser

config = configparser.ConfigParser()
config.read('file.ini')

get_a_variable = config.get('HEADER', 'species')
print(get_a_variable)