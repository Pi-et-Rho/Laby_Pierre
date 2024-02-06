import configparser
from labyrinthe import Labyrinthe

def load_config(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    data = {}

    for section in config.sections():
        if section == 'general':
            general_data = {}
            for key, value in config.items(section):
                if key.startswith('size_'):
                    general_data[key] = int(value)
                else:
                    general_data[key] = value
            data[section] = general_data
        elif section == 'map':
            map_data = [int(cell) if cell.isdigit() or (cell[0] == '-' and cell[1:].isdigit()) else cell for line in config.get(section, 'data').split('\n') for cell in line.split(',')]
            data[section] = map_data
        else:
            section_data = [tuple(map(int, config.get(section, key).split(','))) for key in config.options(section)]
            data[section] = section_data

    return data

def load_labyrinthe(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)

    size_x = int(config['general']['size_x'])
    size_y = int(config['general']['size_y'])
    
    map_data = [line for line in config['map']['data'].split('\n') if line.strip()]

    laby = Labyrinthe(size_x, size_y)
    laby.load_from_file(map_data)

    return laby


file_path = 'data/laby-03.ini'
config_data = load_config(file_path)

size_x = config_data['general']['size_x']
size_y = config_data['general']['size_y']
map_data = config_data['map']