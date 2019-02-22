import os
import numpy as np
import pylas


def write(las, path):

    if os.path.exists(path):
        # Raise most specific subclass of FileExistsError (3.6) and IOError (2.7).
        raise Exception('Cannot write because path {} already exists.'.format(path))
    
    las.write_to_file(path,do_compress=True)
































    
