#make functions for each task
#create a project directory function
#Import os functions : os.path.exists(path), os.makedirs(path), os.path.isfile(filename), os.path.join(dir, file)

import os
def create_project_dir(directory):
    #check if the directory already exists
    if not os.path.exists(directory):
        #we want to create new directory
        print("Creating the directory" + directory)
        #function to create a directory is makedirs
        os.makedirs(directory)

def write_file(path_file, data):
    with open(path_file, 'w') as f:
        f.write(data)



#function to create two text files queue.txt and crawled.txt
#base_url is the URL we need to visit
#now these text files are stored on hard drives which will take time to access, read and write, so we will convert
# it into data structure, set. Set Variables are faster to read/write stored on RAM
def create_text_files(directory, baseurl):
    #have file paths before creating the files
    queue = os.path.join(directory, 'queue.txt')
    crawled = os.path.join(directory, 'crawled.txt')
    #check if the file already exists
    if not os.path.isfile(queue):
        write_file(queue, baseurl)
    else:
        append_to_file(queue, baseurl)
    if not os.path.isfile(crawled):
        write_file(crawled, '')
    else:
        delete_file_contents(crawled)


#Append to file function
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data+'\n') # to ensure that next data is written on next line


#delete file function
def delete_file_contents(path):
    open(path, 'w').close() # do not write anything in opened file, -> removal of data

#function which takes contents of file and put it in a set
def file_to_set(path):
    results = set()
    with open(path, 'rt') as f: # t is for text file
        for line in f:
            results.add(line.replace('\n','')) # replace \n with nothing in the line
    return results

def set_to_file(set1, path):
    with open(path, 'wt') as f:
        for each in sorted(set1): # to ensure links are in sorted order
            f.write(each+'\n') # so that each link is in a new line



