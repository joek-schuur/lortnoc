import Folder

def main():
    print("Note if any of the files contain numbers that do not represent the version, this program won't work as expected!!!\n")
    
    foldername = input("Type the name of your folder: ")   
    folder = Folder(name=foldername)
    print(folder)

    print("Creating new directory in parent folder.")
    folder.CreateNewDirVersion()

if __name__ == "__main__":
    main()