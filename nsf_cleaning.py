""" A small demo of using Git submodules to bring in and clean the NSF Awards data, 
    while keeping the files versioned in XetHub. 
"""

import os
import shutil
import pandas as pd

# if the file is executed as a script
if __name__ == "__main__":

    # Loop over the files in the /raw directory
    directory = os.fsencode("nsf-awards/raw")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        # load the parquet file into a pandas dataframe
        df = pd.read_parquet("nsf-awards/raw/" + filename)

        # Drop the AGENCY column in place
        df.drop(columns="AGENCY", inplace=True)

        # copy the files to the /clean directory
        # shutil.copy("nsf-awards/raw/" + filename, "nsf-awards/clean/" + filename)

        # save the dataframe as a parquet file in the /clean directory
        df.to_parquet("nsf-awards/clean/" + filename)
