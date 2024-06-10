import os
import random

choice = [1, 2, 3]

def random_file_maker(path: str, n: int):
    if n > 0:
        num_folders = random.choice(choice)
        
        for i in range(num_folders):
            folder_name = f"Folder_{i}"
            folder_path = os.path.join(path, folder_name)
            os.makedirs(folder_path)

            num_files = random.choice(choice)
            
            for j in range(num_files):
                with open(os.path.join(folder_path, f"File_{j}.txt"), 'w') as f:
                    f.write(f"Plik probny {j}")

            random_file_maker(folder_path, n - 1)

start_directory = "C:\\Users\\kacpu\\Programowanie\\Semestr3\\Lista2\\Folder_Start"
random_file_maker(start_directory, 3)

File_Paths = []
def find(path,filename):
        if os.path.isdir(path):
            for file in os.listdir(path):
                childpath = os.path.join(path,file)

                if os.path.isdir(childpath):
                    find(childpath,filename)
                elif file == filename:
                    File_Paths.append(childpath)
find(start_directory,'File_2.txt')          
print(File_Paths,len(File_Paths))