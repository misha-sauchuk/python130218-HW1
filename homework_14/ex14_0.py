"""Программа для генерации и проверки контрольных сумм у файлов."""

from hashlib import sha256
import sys


# function to calculate hash of the file, received file name
def hash_file(file_name):
    line_hash = sha256(''.encode())
    with open(file_name) as file:
        for line in file:
            line_hash.update(line.encode())
    return line_hash.hexdigest()


# function to call function hash_file and to write hash information to the manifest file
def calc_hash(file_name, manifest_file):
    with open(manifest_file, 'a') as manifest:
        manifest.write(file_name + ' | ' + hash_file(file_name) + '\n')


# function to open manifest file and check the hash of the files
def manifest_read(manifest_file):
    with open(manifest_file) as manifest:
        for line in manifest:
            line = line.rstrip()
            file_name = line.split(' | ')[0]
            file_hash = line.split(' | ')[1]
            if hash_file(file_name) == file_hash:
                print('{} is ok'.format(file_name))
            else:
                print('{} is failed'.format(file_name))


# received command and file names from the command line in terminal
received_data = sys.argv
if len(received_data) < 2:  # check if user input file names
    print('ERROR you didn\'t enter the file names ')
    quit()
try:  # check if file names is correct
    for file in received_data[2:]:
        with open(file) as f:
            pass
except FileNotFoundError as er:
    print(er.__class__.__name__, er)
    quit()
to_do = received_data[1]  # define the the mode 1 or the mode 2
manifest_file = received_data[2]  # define the name of the manifest file
file_names = received_data[3:]  # define the name(s) of the working file(s)

if __name__ == '__main__':
    if to_do == '--calc':
        with open(manifest_file, 'w') as manifest:
            pass
        for file_name in file_names:
            calc_hash(file_name, manifest_file)
            print('checksum for {} calculated'.format(file_name))
    elif to_do == '--check':
        manifest_read(manifest_file)
    else:
        print('Invalid mode. Please try again')
