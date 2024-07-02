""" A small demo of using Git submodules to bring in and clean the NSF Awards data, 
    while keeping the files versioned in XetHub. 
"""

import os
import shutil

# if the file is executed as a script
if __name__ == "__main__":

    # Loop over the files in the /raw directory
    directory = os.fsencode("nsf-awards/raw")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        # copy the files to the /clean directory
        shutil.copy("nsf-awards/raw/" + filename, "nsf-awards/clean/" + filename)
