import configparser
from labyrinthe import Labyrinthe
from utils import convert_data

class Loader:

    def __init__(self, file_path):
        self.sizex = 0
        self.sizey = 0
        self.map = []
        self.author = ""
        self.version = ""
        self.monsters = []
        self.file_path = file_path
        self.tilesize = 0

        self.load_config()

    def load_config(self):
        config = configparser.ConfigParser()
        config.read(self.file_path)
        data = {}

        for section in config.sections():
            if section == 'general':
                general_data = {}
                for key, value in config.items(section):
                    if key.startswith('size_') or key.startswith("tile"):
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
        self.set_values(data)
        
    def set_values(self, data):
        self.sizex = data["general"]["size_x"]
        self.sizey = data["general"]["size_y"]
        

        new_list = []
        line = []
        counter = 0
        for element in data["map"]:
            line.append(convert_data(element))
            counter += 1
            if counter >= self.sizex:
                counter = 0
                new_list.append(line)
                line = []
        self.map = new_list


        self.author = data["general"]["author"]
        self.version = data["general"]["version"]
        self.tilesize = data["general"]["tilesize"]
        for i in range(len(data["monsters"])):
            self.monsters.append(data["monsters"][i])
        
    def load_labyrinthe(self):
        config = configparser.ConfigParser()
        config.read(self.file_path)

        size_x = int(config['general']['size_x'])
        size_y = int(config['general']['size_y'])
        
        map_data = [line for line in config['map']['data'].split('\n') if line.strip()]

        laby = Labyrinthe(size_x, size_y)
        laby.load_from_file(map_data)

        return laby



if __name__ == "__main__":
    file_path = 'data/laby-03.ini'
    data = Loader(file_path)
    print(data.monsters)