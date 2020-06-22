import os
import re
import shutil

class Organize():
    def __init__(self, path):
        self.path = str(path)
        self.files = []
        self.file_types = []
        self.new_folders = []


    def get_files(self):
        for item in os.listdir(self.path):
            if os.path.isfile(self.path + r"\\" + item):
                self.files.append(item)


    def get_file_types(self):
        for file in self.files:
            type = self.get_item_type(file)
            if type not in self.file_types:
                self.file_types.append(type)


    def make_dir(self):
        for dir in self.file_types:
            if not os.path.exists(self.path + r"\\" + dir):
                os.makedirs(self.path + r"\\" + dir)
                self.new_folders.append(dir)


    def move_files(self):
        for file in self.files:
            type = self.get_item_type(file)
            if os.path.exists(self.path + r"\\" + type):
                shutil.move(self.path + r"\\" + file,
                            self.path + r"\\" + type)


    def get_item_type(self, item):
        file_extension = re.split("\.", item)
        file_type = file_extension[-1]
        return file_type
