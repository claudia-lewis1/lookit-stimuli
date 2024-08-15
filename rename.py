# add 'exp1_' to the beginning of all the files in the directory that starts with 'fence' or 'mirror'
import os

def rename_images(directory):
    # for all the files in the directory
    for filename in os.listdir(directory):
        # if the file is a file
        if os.path.isfile(os.path.join(directory, filename)):
            # if the file starts with 'fence' or 'mirror'
            if filename.startswith('fence') or filename.startswith('mirror'):
                # rename the file
                os.rename(os.path.join(directory, filename), os.path.join(directory, 'exp1_' + filename))

if __name__ == '__main__':
    rename_images('mp4')