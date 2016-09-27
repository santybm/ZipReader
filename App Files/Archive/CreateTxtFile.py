import os.path


def CreateFile(name_of_file,toFile):

    save_path = 'C:/Documents/example/'
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    completeName = os.path.join(save_path, name_of_file+".txt")
    file1 = open(completeName , "w")
    
    file1.write(toFile)
    file1.close()
