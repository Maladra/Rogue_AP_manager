from tempfile import mkstemp
from shutil import move, copymode
from os import fdopen, remove

def replace(file_path, pattern, subst):
    #Create temp file
    fh, abs_path = mkstemp()
    with fdopen(fh,'w') as new_file:
        with open(file_path) as old_file:
            for line in old_file:
                if pattern in line:
                    new_file.write('interface='+subst+'\n')
                else:
                    new_file.write(line)
    #Copy the file permissions from the old file to the new file
    copymode(file_path, abs_path)
    #Remove original file
    remove(file_path)
    #Move new file
    move(abs_path, file_path)


replace('./test32.txt','interface=', 'BONJOUR')