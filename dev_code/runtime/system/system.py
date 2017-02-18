import os


class System():

    def __init__(self):
        pass


    @staticmethod
    def create_file(filename, path):
        norm_file = os.path.normpath(path+"/"+filename)
        norm_path = os.path.normpath(path)
        if os.path.isdir(norm_path) and not os.path.isfile(norm_file):
            file_object = open(norm_file, "w")
            file_object.write("This is the " + filename + " file.")
            file_object.close()



    @staticmethod
    def create_dir(dirname, path):
        norm_dir = os.path.normpath(path+"/"+dirname)
        norm_path = os.path.normpath(path)
        if os.path.isdir(norm_path) and not os.path.isdir(norm_dir):
            os.mkdir(norm_dir)