import os
import shutil

# if the file is executed as a script
if __name__ == "__main__":
    print("hello world")

    # define the fully qualified path to a directory

    # read the parquet data from the /raw/ directory in the /nsf-awards/ folder
    # there are four files in that directory, so we need to read them all
    # and concatenate them into a single dataframe

    directory = os.fsencode("nsf-awards/raw")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        # copy the file to the /clean directory
        shutil.copy("nsf-awards/raw/" + filename, "nsf-awards/clean/" + filename)
