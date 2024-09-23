import os
import shutil


def copy_dir(source_dir: str, destination_dir: str):
    """copy directory tree of a given directory to a given destination directory.
    does not preserve destination data.

    Args:
        source_dir (str): source path directory string
        destination_dir (str): destination path directory string
    """    
    if(os.path.exists(destination_dir)):
        shutil.rmtree(destination_dir)
    os.makedirs(destination_dir)
    
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        print(source_path)
        destination_path = os.path.join(destination_dir, item)
        print(destination_path)
        
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        elif os.path.isdir(source_path):
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            copy_dir(source_path, destination_path)
    

