import os
import shutil

class FileMover:
    def __init__(self, parent_dir):
        self.parent_dir = parent_dir

    def make_directories(self):
        if os.path.exists(self.parent_dir):
            L = os.listdir(self.parent_dir)
            directories = []

            for file in L:
                if "." in file:
                    directory = file[file.index(".")+1:]
                    directories.append(directory)
                    path = os.path.join(self.parent_dir, directory)

                    try:
                        os.mkdir(path)
                    except:
                        pass

            return list(set(directories))

    def move_files(self):
        directories = self.make_directories()

        if os.path.exists(self.parent_dir):
            L = os.listdir(self.parent_dir)

            for i in L:
                if '.' in i:
                    for directory in directories:
                        if directory in i[len(i)-5:]:
                            shutil.move(os.path.join(self.parent_dir, i), os.path.join(self.parent_dir, directory))
                            break

# Example
#parent_dir = r'C:\Users\hp\Documents\TEST2'
#file_mover = FileMover(parent_dir)
#file_mover.move_files()
