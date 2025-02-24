import os
from pathlib import Path

class Folder:
    def getFileNames(self, name):
        filenames = []
        p = ""

        for root, dirs, files in os.walk("/home"):
            for dir in dirs:
                if dir.endswith(name):
                    p = os.path.join(root, name)
                    break
        filenames = next(os.walk(p), (None, None, []))[2]
        print(os.path.isdir(p))
        return filenames
    
    def __init__(self, name):
        self.name = name
        self.filenames = self.getFileNames(self.name)

    def __str__(self):
        format = f"{self.name} contains {len(self.filenames)} files:\n"
        i = 1
        for file in self.filenames:
            format += '\t' + str(i) + ". \t" + file + '\n'
            i += 1
        return format

def get_folder_version(DIRNAME):
    """ Will try to read a number from the foldername that contains this file.
    Minus signs are ignored and if there are multiple numbers within the foldername
    it will return them as a single integer. """
    try:
        version = int(''.join(filter(str.isdigit, DIRNAME)))
        return version
    except:
        raise NameError("Folder name doesn't contain a number.")

# def create_new_folder(VERSION):

# ## move one folder up
# ## 

def main():
    print("Note if any of the files contain numbers that do not represent the version, this program won't work as expected!!!\n")
    foldername = input("Type the name of your folder: ")
    
    folder = Folder(name=foldername)
    print(folder)
    # os.mkdir(full_path_to_grandparent)
    # VERSION = get_folder_version(folder.name)
    # os.open(str(full_path_to_dir.parent.resolve()))
    ##

if __name__ == "__main__":
    main()