# Marvellous Infosyste...

# Automation using Python

# Automation script which accept directory name from user and display all names & checksum of files from that directory.

from sys import *
import os
import hashlib



def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()

def printDuplicate(dict1):
   results = list(filter(lambda x: len(x) > 1, dict1.values()))
#    print("results",len(results))
   
   if(len(results)>0):
        print("Duplicate found:")
        count =0
        if(len(results) > 0):
            for result in results:
                for subresult in result:
                    count += 1
                    if(count >= 2):
                        os.remove(subresult)
                count = 0
   else:
        print("No duplicates found")


def DisplayChecksum(path):
    flag = os.path.isabs (path)

    dups = {}
   
    if flag== False:
        path = os.path.abspath(path)
        exists = os.path.isdir(path)
    if exists:

        for dirName, subdirs, filelist in os.walk(path): 
            # print("Current folder is: "+dirName)
            for filen in filelist:
                path = os.path.join(dirName, filen)
                file_hash = hashfile(path)
                # arr = {}
                # arr = FindDuplicate(file_hash,path)
                # print("arr",arr)
                if(file_hash in dups):
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
                # print("File name : ",path)
                # print("Checksum : ",file_hash)
                # print()
        # print("::dups",dups)   
        return dups
   
    else:
        print("Invalid Path")


def main():
    print("----  Marvellous Infosystems by Shreya Mulay ----")

    print("Application name: "+argv[0])

    if (len(argv) != 2):
        print("Error: Invalid number of arguments")
        exit()

    if (argv[1] == "h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display checksum of files")
        exit()
    
    if (argv[1]=="u") or (argv[1]=="-U"):
        print("usage: ApplicationName AbsolutePath_of_Directory Extention")
        exit()

    try:
        arr = {}
        arr = DisplayChecksum(argv[1])
        printDuplicate(arr)

    except ValueError:

        print("Error: Invalid datatype of input")

    except Exception as E:

        print("Error: Invalid input",E)

if __name__ == "__main__":

    main()

    # run as python main.py Test >> output.txt