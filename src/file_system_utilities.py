import os
import shutil

def copy_static_dir(source_dir: str, destination_dir: str):
    """copy directory tree of a given directory to a given destination directory.
    does not preserve destination data.

    Args:
        source_dir (str): source path to static directory string
        destination_dir (str): destination path directory string
    """    
    if(os.path.exists(destination_dir)):
        shutil.rmtree(destination_dir)
    os.makedirs(destination_dir)
    
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        #print(source_path)
        destination_path = os.path.join(destination_dir, item)
        #print(destination_path)
        
        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
        elif os.path.isdir(source_path):
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            copy_static_dir(source_path, destination_path)
    
def read_file(path: str) -> str:
    """pass a valid path string into this function 
    and get the contents of that file returned.
    
    Args:
        path (str): a path string ex: ("\path\file")
        
    Raises:
        ValueError: given path not found

    Returns:
        str: contents of a file
    """    
    if not os.path.exists(path):
        raise ValueError(f"Given path {path} does not exist.")
    with open(path) as file:
        content = file.read()
    return content
        
def write_file(content: str, dest_path: str) -> None:
    """write given content to a file, at the given path.
    overwrite file content if the file exists.
    if the path and file does not exist create it.

    Args:
        content (str): a string of content to be writen to a file.
        dest_path (str): destination path with filename.
    """    
    path = os.path.dirname(dest_path)
    
    if os.path.exists(dest_path):
        # file exists in destination already.
        # overwrite the file
        with open(dest_path, 'w') as file:
            file.write(content)
    else:
        # file does not exist in destination path,
        # or path does not exist
        os.makedirs(path, 511 ,True)
        with open(dest_path, 'w') as file:
            file.write(content)
