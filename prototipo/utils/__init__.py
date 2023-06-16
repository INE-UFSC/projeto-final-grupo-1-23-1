import os
import inspect
def get_path(*args):
    # Get the address of the calling file
    calling_frame = inspect.stack()[1]
    calling_module = inspect.getmodule(calling_frame[0])
    calling_file_dir = os.path.dirname(os.path.abspath(calling_module.__file__))

    path = [calling_file_dir,*args]
    image_path = os.path.join(*path)

    return image_path