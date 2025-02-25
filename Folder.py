import os, platform
from pathlib import Path
SYSTEM = platform.system()

class Folder:
    def upgradeName(name):
        """ Will try to read a number from the foldername that contains this file.
        Minus signs are ignored and if there are multiple numbers within the foldername
        it will return them as a single integer. """
        try:
            next_version = int(''.join(filter(str.isdigit, name))) + 1
            new = list(name)
            x = 0
            for i in new:
                if str(i).isdigit():
                    new.pop(x)
                    break
                x += 1
            new.insert(x, str(next_version))
            return ''.join(new)      
        except:
            raise NameError("Folder name doesn't contain a number.")
    
    def getFileNames(self, name):
        p = ""

        for root, dirs, files in os.walk("/home"):
            for dir in dirs:
                if dir.endswith(name):
                    p = os.path.join(root, name)
                    break
        self.PATH = p
        
        return next(os.walk(p), (None, None, []))[2]
    
    def __init__(self, name):
        self.name = name
        self.filenames = self.getFileNames(name)
        self.PARENT_PATH = self.PATH[:len(self.PATH)-len("/"+name)]

    def __str__(self):
        format = f"{self.name} contains {len(self.filenames)} files:\n"
        i = 1
        for file in self.filenames:
            format += '\t' + str(i) + ". \t" + file + '\n'
            i += 1
        return format
    
    def renameFolder(self, new_name):
        os.rename(self.name, new_name)
        self.name = new_name

    def CreateNewDirVersion(self):
        next = Folder.upgradeName(self.name)
        os.mkdir(self.PARENT_PATH+"/"+next)

        ## Copy files to new dir and rename files.
        
        # if SYSTEM == "Windows":
        #     os.popen(f'copy {self.PATH} destination.txt')
        # else:
        #     os.popen('cp source.txt destination.txt') 